---
title: Technical documentation for developers
description: Advanced technical documentation for contributing to BSD Router Project
---
# poudriere-image

Note that work-in-progess to migrate from the old NanoBSD to the [new poudriere image framework](technical-docs/poudriere.md).

# How to build BSDRP images

All theses steps are done from a FreeBSD system.

## Prerequisite

You need 21G of free space (1G for FreeBSD installation, 3G for FreeBSD sources, 3G for ports sources and 8G for the working dir).

### Getting BSDRP source code

git clone:

```
pkg install git sudo poudriere-devel
git clone https://github.com/ocochard/BSDRP.git BSDRP
```

## Running the build script

Display the options proposed by the make.sh script :

```
make
```

The FreeBSD code include all architecture and limited cross-compiling tools: You can generate an i386 BSDRP image from a FreeBSD amd64, but you can’t generate a sparc64 image from an i386/amd64 host.

Once you download the code, you can kept your BSDRP sources up-to-date with these commands:

```
make upstream-sync
```

# How to generate customized BSDRP images

If you want to generate your customized BSDRP image, first try to build one generic BSDRP image from source.

You can check the files of the project “BSDRP” and its child project “BSDRPcur”. A child project overwrite the MASTER_PROJECT files/kernels settings.

If this step works for you, then you can begin to customize it.

## Customizing BSDRP in few slides

[Short presentation of NanoBSD and BSD Router Project](https://docs.google.com/presentation/pubid=1d-CqdLljaCcO-sdyfqOn4pLR-wzWaIGC9JeetcU97ks&start=false&loop=false&delayms=5000).

## main files

### make.conf

This file include the main global information for building the image:

- NAME: Name of the Project
- MASTER_PROJECT: For a child project, name of the parent project
- SVN_SRC_PATH: SVN URL for the source tree
- SVN_PORTS_PATH: SVN URL for the port source tree
- FREEBSD_SRC: directory for locally stored FreeBSD source tree
- SRC_PATCH_DIR: Directory for FreeBSD patches
- PORTS_SRC: Directory for locally stored ports source tree
- PORT_PATCH_DIR: Directory for port patches
- DISK_SIZE : Size in MB of the destination disk
- NANOBSD_DIR: Where the nanobsd tree lives
- NANO_MODULES_ARCH: List of kernel modules to build for ARCH

### \$PROJECT/\$PROJECT.nano

This file include all the customization steps:

You can change the:

- Size of configuration partition (NANO_CONFSIZE)
- Size of data partition (NANO_DATASIZE)
- Size of the /etc RAM disk (NANO_RAM_ETCSIZE)
- Size of the /tmp, /var RAM disk (NANO_RAM_TMPVARSIZE)
- and so one…

<!-- -->

    * 

You can declare new package (and their dependency, but only if they use special option) to be installed: For example, if you want to add vim-lite, you add theses lines:

```
add_port "converters/libiconv" "-DNO_INSTALL_MANPAGES -DFORCE_PKG_REGISTER -DNOPORTDOCS"
add_port "editors/vim-lite" "-DWITHOUT_X11 -DNO_INSTALL_MANPAGES -DNOPORTDOCS"
```

If you need to set special permission on some file after their installation, you need to add these steps on the bsdrp_custom () function.

### \$PROJECT/kernels/\$ARCH

This directory include the kernel configuration files. You need to edit these files and the NANO_MODULES_\$ARCH variable in the make.conf for customizing your own kernel and modules.

### \$PROJECT/Files directory

All files put in the Files/ directory will be copied to the BSDRP image. Pay attention to the owner, group, and permissions.

## Little child project example

Here is a little example (minimum modification) for building a new project based on BSDRP, but for a web server appliance: This project will be a child project of BSDRP.

Start by downloading BSDRP source code (refers to getting BSDRP source code chapter) and go in the BSDRP directory.

Then create a new directory using your project name:

```
mkdir WEBSRV
```

#### make.conf

Now we need to configure a minimum project configuration file:

```
echo 'NAME="WEBSRV"' > WEBSRV/make.conf
echo 'MASTER_PROJECT="BSDRP"' >> WEBSRV/make.conf
```

#### Listing all run-dependency of your ports

We want to add the port www/mohawk.

The first step is to list all run-deps of this port.

You need to have downloaded the FreeBSD port-tree first (automatically done if you’ve already generated one BSDRP image).

If you’ve installed BSDRP on /usr/local/BSDRP, here is an example for displaying the run-deps:

```
setenv PORTSDIR /usr/local/BSDRP/BSDRP/FreeBSD/ports
cd $PORTSDIR/www/mohawk
make run-depends-list
devel/libevent
```

Here we need devel/libevent is a running dependency for www/mohawk.

#### project.nano

Now we will copy the nanobsd configuration file from BSDRP:

```
cp BSDRP/BSDRP.nano WEBSRV/WEBSRV.nano
```

Edit the file WEBSRV/WEBSRV.nano and delete all lines related to routing ports like that:

```
add_port "category/port_name" "build options"
```

And add (in the \#### Ports list section \#####) all the running dependency and your port:

```
add_port "devel/libevent"
add_port "www/mohawk"
```

Remove theses lines that compile and install extra small tools too:

```
customize_cmd add_netrate
```

Then modify the bsdrp_custom () function in this file too for removing the quagga chown hack.

#### Files/etc/version

Now set-up the version number:

```
mkdir -p WEBSRV/Files/etc
echo '1' > WEBSRV/Files/etc/version 
```

#### Generating image

Now you should generate a full new image:

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

# How to modify an existing image

All theses step are done from a FreeBSD system using a unziped BSDRP full-image.

## Partition layout of a BSDRP image

Here are all partition found in a BSDRP-full image:

- s1a: first system partition (UFS labeled as BSDRPs1a)
- s2a: Second system partition, didn’t exist if the system was never upgraded (UFS labeled as BSDRPs2a)
- s3: cfg partition (UFS labeled as BSDRPs3)
- s4: data partition (UFS labeled as BSDRPs4)

FreeBSD call “slide” (s) an MBR partition.

## Mounting a BSDRP image as a memory disk

### Automated way

Use the script include with BSDRP sources: ./image_tool.sh mount \<filename\> ./image_tool.sh umount

### Manual way

Using the BSDRP image file, create a memory disk (md):

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

You should found the s1a (system) and s3 (cfg) partition. Mount the system partition for example:

```
mount /dev/md0s1a /mnt
```

Now you can do all your changes on the image.

And the end, umount and close the memory disk:

```
umount /mnt
mdconfig -d -u 0
```

### Increasing /etc and /var RAM disk size

Mount the filesystem in read-write mode:

```
[root@BSDRP]/# mount -uw /
```

And change the value in these files:

- /conf/base/etc/md_size
- /conf/base/var/md_size

The remount the filesystem in read-only and reboot (answer “no” if it detect configuration changes)

```
[root@BSDRP]/conf/base/var# mount -ur /
[root@BSDRP]/conf/base/var# reboot
```

# How to debug

Here are some advice for debugging.

## Performance optimization

You can found more information about FreeBSD on the [FreeBSD forwarding Performance](technical-docs/performance.md) page.

## Shell script

Start your script with “sh -x”:

```
[root@router]~#sh -x /usr/local/sbin/system
```

## RC script

If you want to create some RC scripts, you need to start by reading [Practical rc.d scripting in BSD](http://www.freebsd.org/doc/en_US.ISO8859-1/articles/rc-scripting/).
