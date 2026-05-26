---
title: Technical documentation for developers
description: Advanced technical documentation for contributing to BSD Router Project
---

This page explains how to build a BSDRP image and how to customize
the build for your own appliance. The build is driven by
[poudriere image](technical-docs/poudriere.md); the page below
focuses on the BSDRP-side workflow.

## How to build BSDRP images

All these steps run on a FreeBSD host.

### Prerequisites

- FreeBSD 15.0 or higher
- `ports-mgmt/poudriere` (or `poudriere-devel`)
- `devel/git`

You also need enough free space for a FreeBSD source tree, a ports
tree, the poudriere jail, the packages, and the final images. Plan
for at least 20 GB on the build host.

### Getting the BSDRP source code

Clone the repository:

```
pkg install git sudo poudriere-devel
git clone https://github.com/ocochard/BSDRP.git BSDRP
```

### Running the build

The top-level `Makefile` is the single entry point. To build the
default images:

```
cd BSDRP
make
```

Useful targets:

| Target              | Description |
|:--------------------|:------------|
| `all` (default)     | Build the firmware images |
| `clean`             | Remove generated images |
| `clean-packages`    | Remove built packages |
| `clean-jail`        | Remove the poudriere jail and its object directories |
| `clean-src`         | Remove patched source trees (useful when an old FreeBSD obj tree blocks an upgrade) |
| `clean-all`         | Remove everything |
| `upstream-sync`     | Fetch the latest FreeBSD and ports sources and update the hashes in `Makefile.vars` |
| `compress-images`   | Compress the generated images |
| `checksum-images`   | Compute checksums of the generated images |
| `release`           | Build, compress, and checksum (used to cut a release) |

Run `make help` for the complete list.

The FreeBSD source tree supports multiple architectures with limited
cross-compilation; for example you can generate an i386 BSDRP image
from a FreeBSD amd64 host, but not the other way around.

## How to generate customized BSDRP images

If you want to ship your own appliance based on the BSDRP build
system, the simplest approach is to first build a stock BSDRP image
end-to-end, then customize the parts you care about. The build is a
chain of poudriere steps, so customization is mostly a matter of
swapping configuration files.

The interesting locations in the BSDRP repository are:

- `poudriere.etc/poudriere.d/` - jail, port-tree, and image configuration files
- `BSDRP/kernels/` - kernel configuration files used by the build
- `BSDRP/Files/` - overlay directory copied onto the image
- `Makefile` and `Makefile.vars` - high-level build orchestration and source-tree pins

### Main configuration files

The build pulls together several files; see the [poudriere image
page](technical-docs/poudriere.md#how-bsdrp-customizes-the-poudriere-image-build)
for the full list. The most useful starting points when customizing:

- `poudriere.d/BSDRPj-src.conf` - `src.conf` knobs for the buildworld
  step (controls which parts of the base system get compiled)
- `poudriere.d/image-BSDRPj-src.conf` - extra knobs applied during
  installworld into the final image (typically `WITHOUT_` toggles
  that strip the final image)
- `poudriere.d/BSDRPj-make.conf` - port build options shared across
  every port in the bulk build
- `poudriere.d/BSDRP-pkglist*` - list of packages to build and install
  on the image
- `poudriere.d/excluded.files` - paths to exclude during installworld
- `BSDRP/Files/usr/local/etc/pkg.conf` - `FILES_IGNORE_GLOB` rules
  that prevent specific files from being extracted from packages
- `BSDRP/kernels/<arch>` - kernel configuration files

### Customizing the package list

To add `vim` and `tmux` to the image, append them to the package
list:

```
echo "editors/vim@console" >> poudriere.etc/poudriere.d/BSDRP-pkglist.common
echo "sysutils/tmux"       >> poudriere.etc/poudriere.d/BSDRP-pkglist.common
```

Then rebuild. The `Makefile` re-runs the poudriere bulk and image
steps as needed.

### Customizing the kernel

Edit (or replace) the kernel configuration file under
`BSDRP/kernels/` for the architecture you are building. The file is
copied into the patched FreeBSD source tree by `make patch-sources`
and picked up by the jail's `buildkernel`.

### Customizing the overlay

Anything placed under `BSDRP/Files/` is copied onto the image during
the `poudriere image` step (the `-c` flag in the image command).
Watch ownership and permissions; they are preserved verbatim.

### Stripping more of the base system from the image

Add `WITHOUT_` knobs to
`poudriere.etc/poudriere.d/image-BSDRPj-src.conf`. They are applied
during the installworld into the image only, so they will not
prevent ports from finding the headers and libraries they need at
build time.

If a file you want gone is not covered by a `WITHOUT_` knob, add it
to `poudriere.etc/poudriere.d/excluded.files` instead.

## How to modify an existing image

All of these steps are run on a FreeBSD system, using a decompressed
BSDRP full image.

### Partition layout of a BSDRP image

A BSDRP full image is a GPT disk with these partitions:

- EFI system partition (10 M) with the boot loader
- First system partition, labelled `gpt/${IMAGENAME}1`
- Second system partition, labelled `gpt/${IMAGENAME}2` (used by the
  upgrade process to receive the new image)
- Configuration partition (32 M), labelled `gpt/cfg`
- Data partition (32 M), labelled `gpt/data`

See the [poudriere image page](technical-docs/poudriere.md#partition-scheme)
for an annotated `gpart show` output.

### Mounting a BSDRP image as a memory disk

#### Automated way

Use the script shipped with the BSDRP sources: `./image_tool.sh
mount <filename>` and `./image_tool.sh umount`.

#### Manual way

Attach the image to a memory disk:

```
mdconfig -a -t vnode -f BSDRP-amd64.img
```

The system prints the md name created (for example `md0`). List the
partitions:

```
gpart show -l md0
```

Mount the first system partition (replace `BSDRP1` with the image's
partition label if you named it differently):

```
mount /dev/gpt/BSDRP1 /mnt
```

When you are done, unmount and detach:

```
umount /mnt
mdconfig -d -u 0
```

### Increasing /etc and /var RAM disk size

On a running BSDRP system, remount the root filesystem read-write:

```
[root@BSDRP]/# mount -uw /
```

Change the size values in these files:

- `/conf/base/etc/md_size`
- `/conf/base/var/md_size`

Then remount read-only and reboot (answer "no" if it detects
configuration changes):

```
[root@BSDRP]/# mount -ur /
[root@BSDRP]/# reboot
```

## How to debug

Some tips for debugging.

### Performance optimization

See the [FreeBSD forwarding performance](technical-docs/performance.md)
page for more information.

### Shell scripts

Run your script with `sh -x`:

```
[root@router]~#sh -x /usr/local/sbin/system
```

### RC scripts

If you want to write rc scripts, start by reading [Practical rc.d
scripting in BSD](http://www.freebsd.org/doc/en_US.ISO8859-1/articles/rc-scripting/).
