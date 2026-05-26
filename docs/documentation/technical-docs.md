---
title: Technical documentation for developers
description: Advanced technical documentation for contributing to BSD Router Project
---
## poudriere-image

A migration from the old NanoBSD build to the [new poudriere image framework](technical-docs/poudriere.md) is in progress.

## How to build BSDRP images

All these steps are run on a FreeBSD system.

### Prerequisites

You need 21 GB of free space (1 GB for the FreeBSD installation, 3 GB for the FreeBSD sources, 3 GB for the ports tree, and 8 GB for the working directory).

#### Getting the BSDRP source code

Clone the repository:

```
pkg install git sudo poudriere-devel
git clone https://github.com/ocochard/BSDRP.git BSDRP
```

### Running the build script

Display the options offered by the `make.sh` script:

```
make
```

The FreeBSD source tree supports multiple architectures with limited cross-compilation. You can generate an i386 BSDRP image from a FreeBSD amd64 host, but you cannot generate a sparc64 image from an i386 or amd64 host.

Once you have the source, you can keep your BSDRP tree up to date with:

```
make upstream-sync
```

## How to generate customized BSDRP images

If you want to build a customized BSDRP image, first build a generic BSDRP image from source.

Look at the files in the `BSDRP` project and its child project `BSDRPcur`. A child project overrides the parent's files and kernel settings.

Once you can build the generic image, you can start customizing.

### Customizing BSDRP in a few slides

[Short presentation of NanoBSD and BSD Router Project](https://docs.google.com/presentation/pubid=1d-CqdLljaCcO-sdyfqOn4pLR-wzWaIGC9JeetcU97ks&start=false&loop=false&delayms=5000).

### Main files

#### make.conf

This file holds the main global settings for the image build:

- NAME: name of the project
- MASTER_PROJECT: for a child project, the name of the parent project
- SVN_SRC_PATH: SVN URL for the source tree
- SVN_PORTS_PATH: SVN URL for the ports source tree
- FREEBSD_SRC: directory for the locally stored FreeBSD source tree
- SRC_PATCH_DIR: directory for FreeBSD patches
- PORTS_SRC: directory for the locally stored ports tree
- PORT_PATCH_DIR: directory for port patches
- DISK_SIZE: size in MB of the destination disk
- NANOBSD_DIR: where the NanoBSD tree lives
- NANO_MODULES_ARCH: list of kernel modules to build for ARCH

#### \$PROJECT/\$PROJECT.nano

This file holds all of the customization steps.

You can change:

- the size of the configuration partition (NANO_CONFSIZE)
- the size of the data partition (NANO_DATASIZE)
- the size of the /etc RAM disk (NANO_RAM_ETCSIZE)
- the size of the /tmp and /var RAM disk (NANO_RAM_TMPVARSIZE)
- and so on...

<!-- -->

    * 

You can declare new packages to install (and their dependencies, but only if they need special build options). For example, to add `vim-lite`, add these lines:

```
add_port "converters/libiconv" "-DNO_INSTALL_MANPAGES -DFORCE_PKG_REGISTER -DNOPORTDOCS"
add_port "editors/vim-lite" "-DWITHOUT_X11 -DNO_INSTALL_MANPAGES -DNOPORTDOCS"
```

If you need to set special permissions on some files after installation, add those steps to the `bsdrp_custom ()` function.

#### \$PROJECT/kernels/\$ARCH

This directory holds the kernel configuration files. Edit these files and the `NANO_MODULES_$ARCH` variable in `make.conf` to customize your kernel and modules.

#### \$PROJECT/Files directory

All files placed in the Files/ directory will be copied into the BSDRP image. Pay attention to the owner, group, and permissions.

### Small child project example

Here is a minimal example for building a new project based on BSDRP, this time for a web server appliance. The new project will be a child project of BSDRP.

Start by downloading the BSDRP source code (see the "Getting the BSDRP source code" section) and change into the BSDRP directory.

Then create a new directory using your project name:

```
mkdir WEBSRV
```

#### make.conf

Configure a minimal project configuration file:

```
echo 'NAME="WEBSRV"' > WEBSRV/make.conf
echo 'MASTER_PROJECT="BSDRP"' >> WEBSRV/make.conf
```

#### Listing all run-dependencies of your ports

We want to add the port `www/mohawk`.

The first step is to list all of its run-time dependencies.

The FreeBSD ports tree must already be downloaded (which is done automatically if you have already built a BSDRP image).

Assuming BSDRP is installed in /usr/local/BSDRP, here is how to list the run-time dependencies:

```
setenv PORTSDIR /usr/local/BSDRP/BSDRP/FreeBSD/ports
cd $PORTSDIR/www/mohawk
make run-depends-list
devel/libevent
```

So `devel/libevent` is a run-time dependency of `www/mohawk`.

#### project.nano

Copy the NanoBSD configuration file from BSDRP:

```
cp BSDRP/BSDRP.nano WEBSRV/WEBSRV.nano
```

Edit `WEBSRV/WEBSRV.nano` and delete all lines that add routing-related ports, of the form:

```
add_port "category/port_name" "build options"
```

Then, in the `#### Ports list section #####`, add all run-time dependencies along with your port:

```
add_port "devel/libevent"
add_port "www/mohawk"
```

Also remove these lines that compile and install extra small tools:

```
customize_cmd add_netrate
```

And edit the `bsdrp_custom ()` function in the same file to remove the Quagga chown hack.

#### Files/etc/version

Set the version number:

```
mkdir -p WEBSRV/Files/etc
echo '1' > WEBSRV/Files/etc/version 
```

#### Generating the image

You can now generate a full image:

```
root@laptop:/usr/local/BSDRP # ./make.sh -p WEBSRV
BSD Router Project image build script

Will generate an WEBSRV image with theses values:
- Target architecture: amd64
- Console : -vga
- Source Updating/installing: NO
- Build the full world (take about 1 hour): YES
- FAST mode (skip compression and checksumming): NO
- TMPFS: NO
- Debug image type: NO
Copying amd64 Kernel configuration file
Launching NanoBSD build process...
00:00:00 # NanoBSD image WEBSRV build starting
00:00:00 ## Clean and create object directory (/usr/obj/WEBSRV.amd64)
00:00:00 ## Construct build make.conf (/usr/obj/WEBSRV.amd64/make.conf.build)
00:00:00 ## run buildworld
00:00:00 ### log: /usr/obj/WEBSRV.amd64/_.bw
00:15:03 ## build kernel (amd64)
00:15:03 ### log: /usr/obj/WEBSRV.amd64/_.bk
00:17:50 ## Clean and create world directory (/usr/obj/WEBSRV.amd64/_.w)
00:17:50 ## Construct install make.conf (/usr/obj/WEBSRV.amd64/make.conf.install)
00:17:50 ## installworld
00:17:50 ### log: /usr/obj/WEBSRV.amd64/_.iw
00:18:29 ## install /etc
00:18:29 ### log: /usr/obj/WEBSRV.amd64/_.etc
00:18:30 ## configure nanobsd /etc
00:18:30 ## install kernel (amd64)
00:18:30 ### log: /usr/obj/WEBSRV.amd64/_.ik
00:18:33 ## run customize scripts
00:18:33 ## customize "add_port_devel_libevent2"
00:18:33 ### log: /usr/obj/WEBSRV.amd64/_.cust.add_port_devel_libevent2
00:18:33 ## customize "add_port_www_mohawk"
00:18:33 ### log: /usr/obj/WEBSRV.amd64/_.cust.add_port_www_mohawk
00:18:34 ## customize "cleanup_ports"
00:18:34 ### log: /usr/obj/WEBSRV.amd64/_.cust.cleanup_ports
00:18:34 ## customize "shrink_md_fbsize"
00:18:34 ### log: /usr/obj/WEBSRV.amd64/_.cust.shrink_md_fbsize
00:18:34 ## customize "cust_install_files"
00:18:34 ### log: /usr/obj/WEBSRV.amd64/_.cust.cust_install_files
00:18:34 ## customize "bsdrp_custom"
00:18:34 ### log: /usr/obj/WEBSRV.amd64/_.cust.bsdrp_custom
00:18:38 ## customize "cust_allow_ssh_root"
00:18:38 ### log: /usr/obj/WEBSRV.amd64/_.cust.cust_allow_ssh_root
00:18:38 ## customize "bsdrp_console_vga"
00:18:38 ### log: /usr/obj/WEBSRV.amd64/_.cust.bsdrp_console_vga
00:18:38 ## configure nanobsd setup
00:18:38 ### log: /usr/obj/WEBSRV.amd64/_.dl
00:18:39 ## run late customize scripts
00:18:39 ## build diskimage
00:18:39 ### log: /usr/obj/WEBSRV.amd64/_.di
00:19:02 # NanoBSD image WEBSRV completed
unmounting  /usr/local/BSDRP/WEBSRV/kernels
 /usr/local/BSDRP/WEBSRV/Files
NanoBSD build seems finish successfully.
Compressing WEBSRV upgrade image...
/usr/obj/WEBSRV.amd64/WEBSRV-1-upgrade-amd64-vga.img (1/1)
  100 %        26.2 MiB / 101.9 MiB = 0.257   3.0 MiB/s       0:34             
Generating checksum for WEBSRV upgrade image...
WEBSRV upgrade image file here:
/usr/obj/WEBSRV.amd64/WEBSRV-1-upgrade-amd64-vga.img.xz
Compressing WEBSRV full image...
/usr/obj/WEBSRV.amd64/WEBSRV-1-full-amd64-vga.img (1/1)
  100 %        26.2 MiB / 244.1 MiB = 0.107   5.3 MiB/s       0:45             
Generating checksum for WEBSRV full image...
Zipped WEBSRV full image file here:
/usr/obj/WEBSRV.amd64/WEBSRV-1-full-amd64-vga.img.xz
Zipping and renaming mtree...
/usr/obj/WEBSRV.amd64/WEBSRV-1-amd64-vga.mtree (1/1)
  100 %      262.3 KiB / 1753.4 KiB = 0.150                                    
HIDS reference file here:
/usr/obj/WEBSRV.amd64/WEBSRV-1-amd64-vga.mtree.xz
Done !
```

## How to modify an existing image

All of these steps are run on a FreeBSD system, using a decompressed BSDRP full image.

### Partition layout of a BSDRP image

A BSDRP full image contains:

- s1a: first system partition (UFS labeled `BSDRPs1a`)
- s2a: second system partition; does not exist if the system has never been upgraded (UFS labeled `BSDRPs2a`)
- s3: cfg partition (UFS labeled `BSDRPs3`)
- s4: data partition (UFS labeled `BSDRPs4`)

FreeBSD calls an MBR partition a "slice" (s).

### Mounting a BSDRP image as a memory disk

#### Automated way

Use the script shipped with the BSDRP sources: `./image_tool.sh mount <filename>` and `./image_tool.sh umount`.

#### Manual way

Create a memory disk (md) from the BSDRP image file:

```
mdconfig -a -t vnode -f BSDRP_0.35_full_i386_serial.img -x 63 -y 16
```

The system will display the md name created:

```
md0
```

Now list all partitions on this md:

```
# ls /dev/md0*
# /dev/md0    /dev/md0s1  /dev/md0s1a /dev/md0s2  /dev/md0s3
```

You should see the s1a (system) and s3 (cfg) partitions. Mount the system partition, for example:

```
mount /dev/md0s1a /mnt
```

You can now make changes to the image.

When you are done, unmount and detach the memory disk:

```
umount /mnt
mdconfig -d -u 0
```

#### Increasing /etc and /var RAM disk size

Remount the filesystem read-write:

```
[root@BSDRP]/# mount -uw /
```

Change the value in these files:

- /conf/base/etc/md_size
- /conf/base/var/md_size

Then remount the filesystem read-only and reboot (answer "no" if it detects configuration changes):

```
[root@BSDRP]/conf/base/var# mount -ur /
[root@BSDRP]/conf/base/var# reboot
```

## How to debug

Some tips for debugging.

### Performance optimization

See the [FreeBSD forwarding performance](technical-docs/performance.md) page for more information.

### Shell scripts

Run your script with `sh -x`:

```
[root@router]~#sh -x /usr/local/sbin/system
```

### RC scripts

If you want to write rc scripts, start by reading [Practical rc.d scripting in BSD](http://www.freebsd.org/doc/en_US.ISO8859-1/articles/rc-scripting/).
