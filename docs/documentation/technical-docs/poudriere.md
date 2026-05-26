---
title: Poudriere image
description: How BSDRP firmware images are built with poudriere image
---

BSDRP firmware images are built with the `poudriere image` feature.
This page describes how it works and how the BSDRP build is wired on
top of it.

!!! info "Historical note"

    BSDRP previously shipped a heavily customized NanoBSD script that
    bundled package generation. It was replaced by poudriere image to
    avoid maintaining build code that duplicated the FreeBSD ports
    infrastructure. The old NanoBSD reference material is kept on the
    [NanoBSD page](nanobsd.md).

## External links about Poudriere

Documentation and tutorials about Poudriere:

-  [Poudriere wiki](https://github.com/freebsd/poudriere/wiki): official wiki
-  [Building Packages with Poudriere](https://www.freebsd.org/doc/handbook/ports-poudriere.html): presentation page in the FreeBSD Handbook
-  [poudriere man page](https://github.com/freebsd/poudriere/wiki/poudriere.8): the man page

## Understanding poudriere image

### What is Poudriere?

Poudriere is a shell script that builds packages in a clean jail
environment. The `poudriere image` subcommand combines that clean jail
with the freshly built packages to produce a bootable firmware image.

### Image types

Poudriere can generate multiple image types (the default is `iso+zmfs`):

- `iso`: ISO 9660 format image
  - `iso+mfs`: ISO 9660 variant where the root filesystem is MFS mounted
  - `iso+zmfs` (default): ISO 9660 variant where the root filesystem is LZ77 compressed and MFS mounted
- `usb`: GPT-layout UFS2 image with a UEFI boot loader
  - `usb+mfs`: variant where the root filesystem is MFS mounted
  - `usb+zmfs`: variant where the root filesystem is LZ77 compressed and MFS mounted
- `rawdisk`: raw UFS2, softupdates-enabled disk image
- `zrawdisk`: raw ZFS disk image
- `tar`: XZ-compressed tarball
- `firmware`: dual-system-partition image with GPT partitions and a UEFI boot loader (the type used by BSDRP)
- `rawfirmware`: raw disk image (a single system partition, suitable for upgrades)
- `embedded`: u-boot-ready embedded image
- `zsnapshot`: full and incremental ZFS snapshots to be used in a jail

BSDRP uses the `firmware` type.

### Minimal example: a router image from scratch

The fastest way to see poudriere image in action, without any
BSDRP-specific tooling, is to build a small router image by hand.
Using Poudriere on ZFS is not mandatory but strongly advised.

1.  Install Poudriere and configure it:

        sudo pkg install poudriere-devel
        echo "ZPOOL=$(zpool list -H | cut -f1)" | sudo tee -a /usr/local/etc/poudriere.conf

2.  Create a Poudriere jail with a GENERIC kernel (by default, the
    kernel is not built or installed), here named "router":

        sudo poudriere jail -c -j router -v 15.0-RELEASE -K GENERIC

3.  Create a ports tree using `poudriere ports`:

        sudo poudriere ports -c -p router_ports

4.  Generate the list of ports to be built and added to the firmware
    image:

        cat > ~/router-pkglist <<EOF
        sysutils/tmux
        net/frr10
        net/bird2
        net/mpd5
        EOF

5.  Build the ports (that is, generate binary packages) from the
    corresponding jail using `poudriere bulk`:

        sudo poudriere bulk -j router -p router_ports -f ~/router-pkglist

6.  Generate the disk image (4 GB total: two system partitions of 2 GB
    each) using `poudriere image`:

        sudo poudriere image -t firmware -j router -s 4g -p router_ports -h router -n router -f ~/router-pkglist
        (...)
        [00:00:15] Creating ESP image
        [00:00:15] ESP Image created
        [00:00:21] Image available at: /usr/local/poudriere/data/images/router.img

### Resulting image layout

#### Final firmware file size

The example above produces a single image file:

```
# ls -alh /usr/local/poudriere/data/images/router.img
-rw-r--r--  1 root  wheel   3.8G Jul 22 19:24 /usr/local/poudriere/data/images/router.img
```

The 3.8 GiB disk image fits on a [marketed-size 4 GB flash disk](https://github.com/freebsd/poudriere/pull/638).

#### Partition scheme

A `firmware` image has the following GPT layout:

- 10 M GPT partition with the EFI bootloader
- First system partition, called `gpt/${IMAGENAME}1`
- Second system partition, called `gpt/${IMAGENAME}2` (used by the upgrade process)
- Configuration partition (hard-coded to 32 M), called `gpt/cfg`
- Data partition (hard-coded to 32 M), called `gpt/data`

```
# mdconfig -a -t vnode -f /usr/local/poudriere/data/images/router.img
md0
# gpart show -l md0
=>      4  7995515  md0  GPT  (3.8G)
        4    20480    1  (null)  (10M)
    20484      123    2  (null)  (62K)
    20607  3921920    3  router1  (1.9G)
  3942527  3921920    4  router2  (1.9G)
  7864447    65536    5  cfg  (32M)
  7929983    65536    6  data  (32M)

# mount /dev/gpt/router1 /mnt/
# df -h /mnt
Filesystem          Size    Used   Avail Capacity  Mounted on
/dev/gpt/router1    1.8G    1.5G    103M    94%    /mnt
```

#### /etc RAM disk

The root filesystem is mounted read-only, and `/etc` and `/var` are
backed by RAM disks so the system can run on read-only media:

```
root@router:~ # mount
/dev/gpt/router1 on / (ufs, local, read-only)
devfs on /dev (devfs, local, multilabel)
/dev/md0 on /etc (ufs, local)
/dev/md1 on /var (ufs, local)
```

#### fstab

The generated `fstab` uses GPT labels:

```
root@router:~ # cat /etc/fstab
/dev/gpt/router1 / ufs ro 1 1
/dev/gpt/cfg  /cfg  ufs rw,noatime,noauto        2 2
/dev/gpt/data /data ufs rw,noatime,noauto,failok 2 2
```

System upgrades work by setting the `bootonce` GPT attribute on the
inactive system partition: the new image is written there, the
attribute tells the boot loader to use it once, and the new partition
becomes the active one only after a successful boot.

## How BSDRP customizes the poudriere image build

To reproduce the BSDRP firmware image, several configuration files
are needed.

Poudriere requires both a jail and a port tree. To avoid confusion,
the BSDRP names are prefixed with `j` and `p`:

- `BSDRPj` for the jail name
- `BSDRPp` for the port tree name

The configuration files (in the BSDRP repository under
`poudriere.etc/poudriere.d/`) are prefixed with `BSDRP-`:

- `BSDRPj-src.conf`: all `src.conf` parameters used for the reference jail buildworld/installworld
- `BSDRPj-make.conf`: all common port parameters and port build options
- `image-BSDRPj-src.conf`: parameters added for installworld (followed by a `delete-old`)

The build also uses:

- `BSDRP-pkglist`: list of packages to be built and included in the final image
- A kernel configuration file: the [BSDRP amd64 configuration](https://github.com/ocochard/BSDRP/blob/master/BSDRP/kernels/amd64)
- `excluded.files`: list of files to exclude during installworld
- [`overlaydir/usr/local/etc/pkg.conf`](https://github.com/ocochard/BSDRP/blob/master/BSDRP/Files/usr/local/etc/pkg.conf): includes a `FILES_IGNORE_GLOB` list that prevents specific files from being extracted during package installation

### Configuration files

#### poudriere.d/BSDRPj-src.conf

Holds the `src.conf` parameters used to build the jail (buildworld
and installworld). This jail also builds the ports, so the compiler
must remain available here.

The [BSDRPj-src.conf](https://github.com/ocochard/BSDRP/blob/master/poudriere.etc/poudriere.d/BSDRPj-src.conf) is on GitHub.

#### poudriere.d/image-BSDRPj-src.conf

Adds `WITHOUT_` knobs that are applied during the installworld step
into the final image. This is where the compiler and other components
that are no longer needed get removed from the firmware.

The [image-BSDRPj-src.conf](https://github.com/ocochard/BSDRP/blob/master/poudriere.etc/poudriere.d/image-BSDRPj-src.conf) is on GitHub.

#### poudriere.d/BSDRPj-make.conf

Build parameters for the ports.

The [BSDRPj-make.conf](https://github.com/ocochard/BSDRP/blob/master/poudriere.etc/poudriere.d/BSDRPj-make.conf) is on GitHub.

#### BSDRP-pkglist

Lists the packages to be built and added to the final image.

The [BSDRP-pkglist](https://github.com/ocochard/BSDRP/blob/master/poudriere.etc/poudriere.d/BSDRP-pkglist.common) is on GitHub.

#### excluded.files

List of files and directories that `WITHOUT_` knobs were not able to
keep out of the final image.

The [excluded.files](https://github.com/ocochard/BSDRP/blob/master/poudriere.etc/poudriere.d/excluded.files) is on GitHub.

#### Files excluded from packages

When customizing port options, some files cannot be disabled. `pkg`
can be configured to skip extracting specific files from packages
during installation.

The [customized pkg.conf](https://github.com/ocochard/BSDRP/blob/master/BSDRP/Files/usr/local/etc/pkg.conf) is on GitHub.

### Building the jail

The BSDRP `Makefile` drives the whole flow; if you just want a
BSDRP image, `make` is enough. The sections below describe what it
does under the hood so you can reproduce or customize the steps by
hand.

Start by patching the BSDRP sources (system sources and ports) using
the [BSDRP Makefile](https://github.com/ocochard/BSDRP/blob/master/Makefile):

```
make patch-sources
```

Two patched source trees are now ready:

- `obj/FreeBSD` (includes the BSDRP-specific kernel configuration file)
- `obj/ports`

Then create the jail from the patched source tree:

```
poudriere jail -e poudriere.etc -c -j BSDRPj -b -m src=obj/FreeBSD -K amd64
```

Command-line details:

- `-b`: build from source
- `-c`: create a jail
- `-j`: short name for the jail (long names later produce long directory names that are not well supported)
- `-e`: load all configuration files from `./poudriere.etc`
- `-m src=`: path to the patched source branch to use
- `-K`: the kernel configuration file (copied here while patching the BSDRP source tree)

### Creating the port tree

Create a port tree using the existing patched port tree:

```
poudriere ports -e poudriere.etc -c -p BSDRPp -m null -M obj/ports
```

### Building packages

This is Poudriere's native role: give it the jail name, the port
tree name, and the list of packages.

```
poudriere bulk -e poudriere.etc -j BSDRPj -p BSDRPp -f /usr/local/etc/poudriere.d/BSDRP-pkglist.common
```

### Generating the firmware image

Build a 2 GB image using the previous sets, jail, and port tree:

```
poudriere image -t firmware -s 2g \
    -j BSDRPj -p BSDRPp -n BSDRP -h router.bsdrp.net \
    -c BSDRP/Files/ \
    -f poudriere.etc/poudriere.d/BSDRP-pkglist \
    -X poudriere.etc/poudriere.d/excluded.files \
    -A poudriere.etc/poudriere.d/post-script.sh
```

Command-line explanation:

- `-s`: size of the full image (matching the flash media)
- `-j`: the jail just generated
- `-p`: the Poudriere port tree whose packages we just built
- `-n`: image name, also used as the partition name
- `-h`: hostname configured on the image
- `-c`: directory tree to be copied onto the image (should include a `pkg.conf` with the `FILES_IGNORE_GLOB`)
- `-f`: list of packages to install on the image
- `-X`: list of files to exclude from installworld
- `-A`: post-script executed at the end for final image tuning (such as generating an mtree)
