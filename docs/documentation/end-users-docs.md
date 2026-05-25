---
title: User Guide
description: BSD Router Project User Guide
---
## Hardware Compatibility List

To run BSDRP, you will need:

- A 4GB flash disk (such as Compact Flash, USB stick, or mSATA module).
- At least 1GB of RAM.

All hardware supported by the latest FreeBSD release is compatible with BSDRP, except for some drivers that have been removed (e.g., wireless, PCMCIA, SCSI, USB printer, and FireWire).

## Filename convention

BSDRP image filenames follow this pattern:

BSDRP_*release*_*image type*_*arch*.img.xz

The value *image type* can be:

- full : For full installation, includes the bootloader, system, and data partitions.
- upgrade : For system upgrades, includes only one system partition

The value *arch* can be:

- amd64 : For modern x86 64-bit CPUs (Intel and AMD)
- aarch64 : For ARM 64-bit CPUs.

Examples:

- BSDRP_2.0_full_amd64.img: Full image for x86_64.
- BSDRP_2.0_upgrade_aarch64.img: Upgrade image for ARM.

The *.mtree.xz files are used for system integrity check.

## Installation

#### To a flash media (CF/USB)

##### Windows users

Here are the 2 steps for writing the image to a CF/flasg/USB removable media:

1.  Decompress the BSDRP image using [7-Zip](http://www.7-zip.org/) to get a .img file.
2.  Use [Image Writer for Windows](http://win32diskimager.sourceforge.net/) to write the .img file to your CF/flash/USB device.

##### *BSD or Linux users

Connect your flash or USB drive and note its device name. Decompress the image and copy it to your drive using a byte copy command. Then unzip the file and byte copy it to your drive (**Warning: Be sure to double-check the destination disk!**):

```
xzcat BSDRP_full_amd64_vga.1.0.img.xz | dd of=/dev/sd4 bs=256k
```

You can boot from this media now.

##### Mac OS X users

Insert the USB key, and display list of external devices:

```
% diskutil list | grep external
/dev/disk3 (external, physical):
```

Check if it is already mounted

```
% mount | grep '/dev/disk3'
/dev/disk0s2 on / (hfs, local, journaled)
devfs on /dev (devfs, local)
fdesc on /dev (fdesc, union)
map -hosts on /net (autofs, automounted)
map auto_home on /home (autofs, automounted)
/dev/disk3s1 on /Volumes/UNTITLED (msdos, local, nodev, nosuid, noowners)
```

The last line is your USB device. Unmount it and write the BSDRP image to the device adding the ‘r’ letter:

```
sudo umount -f /dev/disk3s1
xzcat BSDRP_full_amd64_vga.1.0.img.xz | sudo dd of=/dev/rdisk3 bs=1m
```

If successful, OSX will pop up an error dialog telling you it doesn‘t recognise the disk. Click ’Eject’, remove the USB key, and you’re done.

#### To an hard drive

Boot BSDRP from the previously generated usb key, then from BSDRP, display the BSDRP system diskname:

```
[root@router]~# glabel status | grep BSDRP
 ufs/BSDRPs3     N/A  da1s3
 ufs/BSDRPs4     N/A  da1s4
ufs/BSDRPs1a     N/A  da1s1a
```

=\> On this example BSDRP is on disk da1 (USB key)

Display all the system disks:

```
[root@router]# sysctl kern.disks
kern.disks: da1 da0 ada0
```

=\> On this example, because da1 is the BSDRP disk, ada0 is the hard-drive where we want install BSDRP.

Then copy the BSDRP disk to the hard-drive:

```
[root@router]# system install ada0
Copying 487MB from da1 to ada0...
487+0 records in
487+0 records out
510656512 bytes transferred in 30.351293 secs (16824868 bytes/sec)
```

Reboot your system (and don’t forget to remove the USB key).

Once rebooted from your hard drive, you can expand the /data slice for using all the free space:

```
system expand-data-slice
```

#### Special notes for PC-Engines

##### Alix platform

You need to use [BIOS revision 0.99h](http://www.pcengines.ch/alix2.htm) minimum. You can use the [pfSense Alix BIOS update FreeDOS image disk](https://doc.pfsense.org/index.php/ALIX_BIOS_Update_Procedure) for an easy upgrade.

## Quick start

Login as root with no password.

If you are using the serial version, serial port parameters are: 115200,8,N,1,MODEM.

Start by using the help:

```
help
```

Create a password for root (mandatory for SSH):

```
passwd
```

For a routing protocol daemons, you have choice between bird or FRRouting (Quaga fork).

As an example, for starting FRR and enter into its cli mode:

```
sysrc frr_enable=yes
service frr start
cli
```

Do your frr configuration, and save frr config and exit cli:

```
wr
exit
```

Then save all changes (you can avoid this by enabling autosave feature):

```
config save
```

## Configuration files

All modifications done in configuration files (/etc/*, /usr/local/etc/*) need to be saved before a reboot.

Use the config command for saving configuration:

```
[root@R1]~#config
BSD Router Project configuration tool
Usage: /usr/local/sbin/config option
  - diff     : Show diff between current and saved config
  - save     : Save current config
  - apply    : Apply current config
  - rollback : Revert to previous config
  - put      : Put the saved config to a remote server
  - get      : Get config from remote server
  - reset    : Return to default configuration
  - help (h) [option]  : Display this help message.
                        If [option] given, display more detail about the option
```


!!! note
    Don’t modify /boot/loader.conf: Your changes will be lost after an upgrade. In place, create a new file /boot/loader.conf.local and put your modifications on this file.


## Upgrading examples

### From BSDRP directly

#### HTTP/FTP fetch without checking SHA256

Directly download and send output to xzcat+upgrade:

```
fetch 'http://URL/BSDRP-upgrade.image.xz' -o - | xzcat | upgrade
```

Real example to upgrade to 1.96:

```
fetch 'https://sourceforge.net/projects/bsdrp/files/BSD_Router_Project/1.96/amd64/BSDRP-1.96-upgrade-amd64-serial.img.xz/download' -o - | xzcat | upgrade
```

#### SSH fetch without checking SHA256

Same than previously, but using SSH:

```
ssh my-user@my-ssh-server cat /path-to/BSDRP-upgrade.image.xz | xzcat | upgrade
```

#### Using a SCP Client or fetching upgrade file from BSDRP

This method required:

- A minimum of 60MB of free RAM on your BSDRP (mem_avail value in the “show mem” output)
- One of this:
  - Sending the upgrade file + sha256 with a SCP client ([FileZilla](http://filezilla-project.org/) or [WinSCP](http://winscp.net) as example)
  - Or downloading upgrade file directly from BSDRP

Resume:

1.  Create a TMPFS (RAM disk) directory
2.  Transfer BSDRP image upgrade file + sha256 on the ram disk using the SCP client or download the image directly
3.  Check SHA256
4.  Upgrade the system

Step 1: Creating the ram disk

On BSDRP, enter theses commands for creating a RAM drive:

```
mount -t tmpfs tmpfs /mnt/
```

Step 2: Transferring image file + sha256 in the temporary RAM drive

Using your SCP client, send the BSDRP upgrade image to the router’s **/mnt** folder.

Or download them from BSDRP:

```
cd /mnt
fetch URL/BSDRP-upgrade.image.xz
fetch URL/BSDRP-upgrade.image.sha256
```

Step 3: After transfer complete, On BSDRP, enter this command:

```
sha256 -c `cat BSDRP-upgrade.image.sha256 | cut -d ' ' -f 4` BSDRP-upgrade.image.xz && echo "good" || echo "bad"
xzcat /mnt/BSDRP-upgrade.image.xz | upgrade
umount /mnt
```

### From a *nix server

This method required a SSH client (all Linux/Unix should include it).

From the client, enter this command:

```
cat BSDRP_1.2_upgrade_amd64_vga.img.xz | ssh root@a.b.c.d "xzcat | upgrade"
```

## Security

### SSH access

SSH access with the root user is not available by default: You need to set-up a password for the root account before with the **passwd** command.

Example:

```
[root@R1]~# passwd
Changing local password for root
New Password: XXXXXXXX
Retype New Password: XXXXXXXX
```

### System integrity check

[Reference mtree file are provided](../downloads.md) for checking the integrity of all your files on your router.

You can check your BSDRP system integrity using these references files by downloading the corresponding file into your router and using “system integrity” command.

As example, if you are using 0.35 amd64-serial release, from your BSDRP router (if it had DNS resolution and Internet access configured):

```
cd /tmp
fetch http://downloads.sourceforge.net/project/bsdrp/BSD_Router_Project/0.35/BSDRP_0.35_amd64_serial.mtree.xz
system integrity BSDRP_0.35_amd64_serial.mtree.xz
```

## System Management

### autosave configuration

All modifications in configuration files done into /etc and /usr/local/etc needs to be saved with “config save” command. (/etc and /usr/local/etc is a ram disk).

You can enable service autosave for automatically issue command “config save” each time a modification is detected into /etc or /usr/local/etc.

```
sysrc autosave_enable=yes
service autosave start
```

### Serial port

#### Enabling dual console vga/serial

If you are using the vga release of BSDRP, you can enable the serial access (COM1) with the command

```
system dual-console
```

#### baud rate

Serial port baud rate need to be modified in 2 different files:

- /boot.config
- /etc/ttys

For modifying the /boot.config file you need to mount RW the /:

```
mount -uw /
```

Change the speeed value just after the “-S” option (don’t remove the other -D or/and -h options!) in the /boot.config file.

Check that you didn’t have legacy values (boot_serial, comconsole_speed, console) configured on your /boot/loader.conf.local: There are useless with the use of /boot.config.

Once done, mount RO /:

```
mount -ur /
```

Then edit etc/ttys and change the baud rate in line ttyu0 (if you need to change the first serial port).

#### Changing the default serial port used for console

If you need to change the default serial port to use for console (like Supermicro that use COM2 for sol):

- Start by displaying the list of available serial ports
- Then change the value in /boot/loader.conf.local

<!-- -->

```
root@bsdrp# grep uart /var/run/dmesg.boot
uart0: <16550 or compatible> port 0x3f8-0x3ff irq 4 flags 0x10 on acpi0
uart0: console (38400,n,8,1)
uart1: <16550 or compatible> port 0x2f8-0x2ff irq 3 on acpi0
root@bsdrp# mount -uw /
root@bsdrp# echo 'comconsole_port="0x2f8"' >> /boot/loader.conf.local
root@bsdrp# mount -ur /
```

### IPMI

If you need to configure the local IPMI board, you have to load the IPMI drivers.

Edit /etc/rc.conf and check that module “ipmi” is declared on the kld_list variable:

```
kld_list='ipmi'
```

You can load it from the shell too:

```
kldload ipmi
```

Then you can use [ipmitool](http://ipmitool.sourceforge.net/) for configuring it.

For connecting with IPMI to serial port with IPMI SOL (Serial over lAN) from a remote machine, change the baud-rate of the serial line to 115200 and to connect to it (example with default password for IBM x3550):

```
ipmitool -H 192.168.1.11 -U USERID -P PASSW0RD sol set non-volatile-bit-rate 115.2
ipmitool -H 192.168.1.11 -U USERID -P PASSW0RD sol set volatile-bit-rate 115.2
ipmitool -H 192.168.1.11 -U USERID -P PASSW0RD -I lanplus -a sol activate
```

### Watchdog

Add to /etc/rc.conf:

```
# Load Intel ICH watchdog interrupt timer driver
kld_list='ichwd'
# Start watchdogd dameon
watchdogd_enable="yes"
```

And start it:

```
kldload ichwd
service watchdogd start
```

If you already load ipmi module, watchdogd can use IPMI in place of ichwd.

### SNMP

Enable bsdnmpd:

```
sysrc bsnmpd_enable=YES
```

Edit /etc/snmpd.config according to your needs and start the daemon:

```
service bsnmpd start
```

Then you can check it locally (it uses public as default snmp community):

```
[root@BSDRP]~# bsnmpget sysDescr.0
sysDescr.0 = router.bsdrp.net 2059309898 FreeBSD 9.1-RELEASE-p1
```

### Syslog

For generating syslog message, just edit /etc/syslog.conf and check the example:

```
# uncomment this to enable logging to a remote loghost named loghost
#*.*                                            @loghost
```

Then restart syslogd:

```
service syslogd restart
```


!!! note
    BSDRP v1.4 and earlier have a default configuration that prevent remote syslog. This behavior can be changed by editing /etc/rc.conf.misc and replacing syslogd_flags=“-ss” by syslogd_falgs=“-s”


### Firmware Upgrade

#### Mellanox

Stat by identifying your NIC ID:

```
# mstfwmanager
Querying Mellanox devices firmware ...

Device #1:
----------

  Device Type:      ConnectX4
  Part Number:      MCX416A-CCA_Ax
  Description:      ConnectX-4 EN network interface card; 100GbE dual-port QSFP28; PCIe3.0 x16; ROHS R6
  PSID:             MT_2150110033
  PCI Device Name:  pci0:2:0:0
  Base GUID:        e41d2d0300fdbd90
  Base MAC:         e41d2dfdbd90
  Versions:         Current        Available
     FW             12.26.1040     N/A
     PXE            3.5.0803       N/A
     UEFI           14.19.0014     N/A

  Status:           No matching image found
```

Then go to the [Mellanox firmware web site](https://www.mellanox.com/page/firmware_download) in section “Device Type” -\> “Part Number” -\> “PSID”, then fetch it into your BSDRP and upgrade it:

```
# mount /data
# cd /data
# fetch http://www.mellanox.com/downloads/firmware/fw-ConnectX4-rel-12_26_4012-MCX416A-CCA_Ax-UEFI-14.19.17-FlexBoot-3.5.805.bin.zip
# unzip fw-ConnectX4-rel-12_26_4012-MCX416A-CCA_Ax-UEFI-14.19.17-FlexBoot-3.5.805.bin.zip
# mstfwmanager -u -i fw-ConnectX4-rel-12_26_4012-MCX416A-CCA_Ax-UEFI-14.19.17-FlexBoot-3.5.805.bin
Querying Mellanox devices firmware ...

Device #1:
----------

  Device Type:      ConnectX4
  Part Number:      MCX416A-CCA_Ax
  Description:      ConnectX-4 EN network interface card; 100GbE dual-port QSFP28; PCIe3.0 x16; ROHS R6
  PSID:             MT_2150110033
  PCI Device Name:  pci0:2:0:0
  Base GUID:        e41d2d0300fdbd90
  Base MAC:         e41d2dfdbd90
  Versions:         Current        Available
     FW             12.26.1040     12.26.4012
     PXE            3.5.0803       3.5.0805
     UEFI           14.19.0014     14.19.0017

  Status:           Update required

---------
Found 1 device(s) requiring firmware update...

Perform FW update? [y/N]: y
Device #1: Updating FW ...
Initializing image partition -   OK
Writing Boot image component -   OK
Done

Restart needed for updates to take effect.
```

## Debugging

### Enabling crash dump

#### Local swap dump device

For saving and extracting a crash dump you need:

- A swap partition with same size as your RAM size (will store the raw RAM dump)
- A data partition with same size as your RAM size (for storing the extracted dump)

For enabling crash dump, the steps are:

1.  Configure a dump device that will be used for storing memory dump (can be an external USB key)
2.  Increase size of /data for being able to store the memory dump
3.  Configure to mount /data automatically (because next step needs it)
4.  Configure to store dump into /data

Here is an an example when we split data partition 4 in 2 BSD partitions:

- One as swap
- One as /data

But if you can plug an USB key with a size=RAM size, you can avoid to expand your partition 4 and just using this device.

Step to follows:

1.  Delete partition 4 (/data)
2.  Recreate partition 4 using full disk space
3.  Create 2 BSD partitions in this new large partition 4:
    - partition s4a (4.2BSD) with a size= RAM size
    - partition s4b (swap) with a size= RAM size
4.  Format s4a in UFS and enable dumpon on the swap

Then we destroy the default small partition 4, and re-create a new one that will use the full disk size, and create BSD-partition inside it (MBR partition scheme allow only 4 partitions, then we’re using sub-partition in BSD mode):

```
gpart delete -i 4 da0
gpart add -t freebsd da0
bsdlabel -w /dev/da0s4
```

Now start the BSD partition editor:

```
bsdlabel -e /dev/da0s4
```

and replace these lines:

```
# /dev/da0s4:
8 partitions:
#          size     offset    fstype   [fsize bsize bps/cpg]
  a:  284191428          16   unused        0     0     0
  c:  284191428          0    unused        0     0     # "raw" part, don't edit
```

by this one (size and fstype of line a: and b: modified, ‘*’ mean automatic size):

```
# /dev/da0s4:
8 partitions:
#          size     offset    fstype   [fsize bsize bps/cpg]
  a:   16G          16        4.2BSD        0     0     0
  b:   *          *         swap
  c:  284191428          0    unused        0     0     # "raw" part, don't edit
```

Then quit the editor (:x) and format partition a (/data):

```
newfs -UjL BSDRPs4 /dev/da0s4a
sysrc dumpdev="/dev/da0s4b"
sysrc dumpdir="/data/crash"
sysrc dumpon_flags="-Z"
sysrc savecore_enable=YES
sed -i "" -e "/data/s/noauto/noatime/" /etc/fstab
mount /data
mkdir /data/crash
chmod 700 /data/crash
config save
service dumpon start
```

Now, during a crash it will wrote the core dump to :

```
#14 0xffffffff8096c34a at taskqueue_run_locked+0x14a
#15 0xffffffff8096d258 at taskqueue_thread_loop+0xe8
#16 0xffffffff808d4495 at fork_exit+0x85
#17 0xffffffff80d1b30e at fork_trampoline+0xe
Uptime: 3m10s
Dumping 1112 out of 16325 MB:..2%..11%..21%..31%..41%..51%..61%..71%..81%..91%
Dump complete
```

And after a reboot it will automatically extract the dump from dumpdevice and store it to /data/crash:

```
[root@router]~# ll -h /data/crash/
total 100456
-rw-r--r--  1 root  wheel     2B Aug 30 14:57 bounds
-rw-------  1 root  wheel   487B Aug 30 14:57 info.0
lrwxr-xr-x  1 root  wheel     6B Aug 30 14:57 info.last@ -> info.0
-rw-------  1 root  wheel   115M Aug 30 14:57 vmcore.0
lrwxr-xr-x  1 root  wheel     8B Aug 30 14:57 vmcore.last@ -> vmcore.0
```

#### netdump

In case where you didn’t have enough disk space to localy store dump, you can use netdump(4).

On the receiving FreeBSD server (not your router):

```
pkg install netdumpd
service netdumpd enable
service netdumpd start
```

Then on your router, declare source interface to use, source IP address, gateway

```
sysrc dumpdev=igb1
sysrc dumpon_flags="-s 198.19.0.24 -c 192.168.1.10 -g 192.168.1.254
```

and enable it:

```
# service dumpon restart
kernel dumps on priority: device
0: /dev/null
server address: 198.19.0.24
client address: 192.168.1.10
gateway address: 192.168.1.254
```

### Installing debug symbols

Symbol files of kernel and binary are available in the separate DEBUG archive file. It needs:

1.  Either 1Gbs of Free RAM for creating a large tmpfs or 1Gbs of free space in /data (use “system expand-data-slice”)
2.  The debug tar file needs to being extracted in /data/ (there is already a symlink from /usr/lib/debug pointing to /data/debug)

Here in an example, by starting expanding the data slice:

```
[root@router]~# system expand-data-slice
There is (1.0G) available on your disk that can be use for /data
Are you sure to repartition your disk ? (y/n)y
(etc.)
Done
[root@router]~# mount /data
[root@router]~# df -h /data/
Filesystem          Size    Used   Avail Capacity  Mounted on
/dev/ufs/BSDRPs4    1G     16M     974M     1%    /data
[root@router]~# fetch "URL/BSDRP-1.60-debug-amd64.tar.xz" -o - | tar -C /data -xvf -
```

### Analysing core dump

You need to install debug symbols first, then:

```
kgdb /usr/lib/debug/boot/kernel/kernel.debug /data/crash/vmcore.0

GNU gdb 6.1.1 [FreeBSD]
Copyright 2004 Free Software Foundation, Inc.
GDB is free software, covered by the GNU General Public License, and you are
welcome to change it and/or distribute copies of it under certain conditions.
Type "show copying" to see the conditions.
There is absolutely no warranty for GDB.  Type "show warranty" for details.
This GDB was configured as "amd64-marcel-freebsd"...

Unread portion of the kernel message buffer:

Fatal trap 12: page fault while in kernel mode
cpuid = 7; apic id = 0e
fault virtual address   = 0x0
fault code              = supervisor write data, page not present
instruction pointer     = 0x20:0xffffffff80d5480e
stack pointer           = 0x28:0xfffffe0466ba61e0
frame pointer           = 0x28:0xfffffe0466ba61e0
code segment            = base 0x0, limit 0xfffff, type 0x1b
                        = DPL 0, pres 1, long 1, def32 0, gran 1
processor eflags        = interrupt enabled, resume, IOPL = 0
current process         = 1900 (pkt-gen)
trap number             = 12
panic: page fault
cpuid = 7
KDB: stack backtrace:
#0 0xffffffff80971167 at kdb_backtrace+0x67
#1 0xffffffff80929b72 at vpanic+0x182
#2 0xffffffff809299e3 at panic+0x43
#3 0xffffffff80d56e84 at trap_fatal+0x324
#4 0xffffffff80d57083 at trap_pfault+0x1e3
#5 0xffffffff80d56683 at trap+0x273
#6 0xffffffff80d39261 at calltrap+0x8
#7 0xffffffff8047c664 at cxgbe_netmap_reg+0x2f4
#8 0xffffffff8063d48c at netmap_hw_reg+0x2c
#9 0xffffffff8063a93b at netmap_do_regif+0x2ab
#10 0xffffffff8063b564 at netmap_ioctl+0xba4
#11 0xffffffff8063f14e at freebsd_netmap_ioctl+0x3e
#12 0xffffffff8085e47c at devfs_ioctl+0xac
#13 0xffffffff80eee78d at VOP_IOCTL_APV+0x8d
#14 0xffffffff80a08901 at vn_ioctl+0x131
#15 0xffffffff8085ecdf at devfs_ioctl_f+0x1f
#16 0xffffffff8098ed7b at kern_ioctl+0x29b
#17 0xffffffff8098ea71 at sys_ioctl+0x171
Uptime: 4m41s
Dumping 1112 out of 16325 MB:..2%..11%..21%..31%..41%..51%..61%..71%..81%..91%

#0  doadump (textdump=<value optimized out>) at pcpu.h:222
222     pcpu.h: No such file or directory.
        in pcpu.h

(kgdb) backtrace
#0  doadump (textdump=<value optimized out>) at pcpu.h:222
#1  0xffffffff809295f9 in kern_reboot (howto=260) at /usr/local/BSDRP/BSDRPcur/FreeBSD/src/sys/kern/kern_shutdown.c:366
#2  0xffffffff80929bab in vpanic (fmt=<value optimized out>, ap=<value optimized out>) at /usr/local/BSDRP/BSDRPcur/FreeBSD/src/sys/kern/kern_shutdown.c:759
#3  0xffffffff809299e3 in panic (fmt=0x0) at /usr/local/BSDRP/BSDRPcur/FreeBSD/src/sys/kern/kern_shutdown.c:690
#4  0xffffffff80d56e84 in trap_fatal (frame=0xfffffe0466ba6120, eva=0) at /usr/local/BSDRP/BSDRPcur/FreeBSD/src/sys/amd64/amd64/trap.c:801
#5  0xffffffff80d57083 in trap_pfault (frame=0xfffffe0466ba6120, usermode=0) at /usr/local/BSDRP/BSDRPcur/FreeBSD/src/sys/amd64/amd64/trap.c:658
#6  0xffffffff80d56683 in trap (frame=0xfffffe0466ba6120) at /usr/local/BSDRP/BSDRPcur/FreeBSD/src/sys/amd64/amd64/trap.c:421
#7  0xffffffff80d39261 in calltrap () at /usr/local/BSDRP/BSDRPcur/FreeBSD/src/sys/amd64/amd64/exception.S:236
#8  0xffffffff80d5480e in bzero () at /usr/local/BSDRP/BSDRPcur/FreeBSD/src/sys/amd64/amd64/support.S:53
#9  0xffffffff8047c664 in cxgbe_netmap_reg (na=<value optimized out>, on=<value optimized out>) at /usr/local/BSDRP/BSDRPcur/FreeBSD/src/sys/dev/cxgbe/t4_netmap.c:102
#10 0xffffffff8063d48c in netmap_hw_reg (na=0xfffff800055ba400, onoff=1) at /usr/local/BSDRP/BSDRPcur/FreeBSD/src/sys/dev/netmap/netmap.c:2788
#11 0xffffffff8063a93b in netmap_do_regif (priv=<value optimized out>, na=<value optimized out>, ringid=<value optimized out>, flags=<value optimized out>)
    at /usr/local/BSDRP/BSDRPcur/FreeBSD/src/sys/dev/netmap/netmap.c:2050
#12 0xffffffff8063b564 in netmap_ioctl (priv=<value optimized out>, cmd=<value optimized out>, data=0xfffffe0466ba69b0 "vcxl0", td=0xfffff8001509a500)
    at /usr/local/BSDRP/BSDRPcur/FreeBSD/src/sys/dev/netmap/netmap.c:2257
#13 0xffffffff8063f14e in freebsd_netmap_ioctl (dev=<value optimized out>, cmd=3225184658, data=0xfffffe0466ba69b0 "vcxl0", ffla=<value optimized out>,
    td=0xfffff8001509a500) at /usr/local/BSDRP/BSDRPcur/FreeBSD/src/sys/dev/netmap/netmap_freebsd.c:1389
#14 0xffffffff8085e47c in devfs_ioctl (ap=<value optimized out>) at /usr/local/BSDRP/BSDRPcur/FreeBSD/src/sys/fs/devfs/devfs_vnops.c:831
#15 0xffffffff80eee78d in VOP_IOCTL_APV (vop=<value optimized out>, a=<value optimized out>) at vnode_if.c:1067
#16 0xffffffff80a08901 in vn_ioctl (fp=0xfffff80015191f00, com=<value optimized out>, data=0xfffffe0466ba69b0, active_cred=0xfffff8019928bd00, td=0x1) at vnode_if.h:448
#17 0xffffffff8085ecdf in devfs_ioctl_f (fp=0x0, com=131072, data=0x0, cred=0x4000, td=0xfffff8001509a500)
    at /usr/local/BSDRP/BSDRPcur/FreeBSD/src/sys/fs/devfs/devfs_vnops.c:789
#18 0xffffffff8098ed7b in kern_ioctl (td=<value optimized out>, fd=<value optimized out>, com=3225184658, data=0xfffffe0466ba69b0 "vcxl0") at file.h:327
#19 0xffffffff8098ea71 in sys_ioctl (td=0xfffff8001509a500, uap=0xfffffe0466ba6b10) at /usr/local/BSDRP/BSDRPcur/FreeBSD/src/sys/kern/sys_generic.c:746
#20 0xffffffff80d57825 in amd64_syscall (td=<value optimized out>, traced=0) at subr_syscall.c:135
#21 0xffffffff80d3954b in Xfast_syscall () at /usr/local/BSDRP/BSDRPcur/FreeBSD/src/sys/amd64/amd64/exception.S:396
#22 0x000000080100e5ca in ?? ()
Previous frame inner to this frame (corrupt stack?)
Current language:  auto; currently minimal
```

### Generate a panic on a hang/freeze system

If your system didn’t panic but freeze, you can generate a panic by sending a Non Maskable Interupt (NMI) by IPMI (chassis power diag).

```
ipmitool -I lanplus -H SERVER -U USER -P PASSWORD chassis power diag
```

### Kernel live debugging

You need to install debug symbols first, then:

```
[root@router]~# kgdb /boot/kernel/kernel /dev/mem
GNU gdb 6.1.1 [FreeBSD]
Copyright 2004 Free Software Foundation, Inc.
GDB is free software, covered by the GNU General Public License, and you are
welcome to change it and/or distribute copies of it under certain conditions.
Type "show copying" to see the conditions.
There is absolutely no warranty for GDB.  Type "show warranty" for details.
This GDB was configured as "amd64-marcel-freebsd"...
Reading symbols from /boot/kernel/if_lagg.ko...Reading symbols from /usr/lib/debug//boot/kernel/if_lagg.ko.symbols...done.
done.
Loaded symbols for /boot/kernel/if_lagg.ko
#0  sched_switch (td=0xffffffff8156b140, newtd=<value optimized out>,
    flags=<value optimized out>)
    at /usr/local/BSDRP/BSDRP/FreeBSD/src/sys/kern/sched_ule.c:1945
1945    /usr/local/BSDRP/BSDRP/FreeBSD/src/sys/kern/sched_ule.c: No such file or directory.
        in /usr/local/BSDRP/BSDRP/FreeBSD/src/sys/kern/sched_ule.c
(kgdb) ptype ifindex_table[5]->ife_ifnet
type = struct ifnet {
    void *if_softc;
    void *if_l2com;
    struct vnet *if_vnet;
    struct {
        struct ifnet *tqe_next;
        struct ifnet **tqe_prev;
    } if_link;
    char if_xname[16];
    const char *if_dname;
    int if_dunit;
    u_int if_refcount;
    struct ifaddrhead if_addrhead;
    int if_pcount;
    struct carp_if *if_carp;
    struct bpf_if *if_bpf;
    u_short if_index;
    short if_index_reserved;
    struct ifvlantrunk *if_vlantrunk;
    int if_flags;
    int if_capabilities;
    int if_capenable;
    void *if_linkmib;
---Type <return> to continue, or q <return> to quit---q
Quit
(kgdb)
```

## Going further

BSDRP is a FreeBSD, then you need to read how to configure a FreeBSD for using it.

Here is a list of useful documentations:

- [BSDRP Examples](examples.md)
- [FreeBSD Handbook](http://www.freebsd.org/doc/en_US.ISO8859-1/books/handbook/):
  - [Bridging](http://www.freebsd.org/doc/en_US.ISO8859-1/books/handbook/network-bridging.html)
  - [Link Aggregation and Failover](http://www.freebsd.org/doc/en_US.ISO8859-1/books/handbook/network-aggregation.html)
  - [Alternate Queuing](http://www.freebsd.org/doc/en_US.ISO8859-1/books/handbook/firewalls-pf.html)
  - [IPv6](http://www.freebsd.org/doc/en_US.ISO8859-1/books/handbook/network-ipv6.html)
- [FreeBSD Man Pages](http://www.freebsd.org/cgi/man.cgi)
- [Introduction to NETGRAPH on FreeBSD Systems](http://www.netbsd.org/gallery/presentations/ast/2012_AsiaBSDCon/Tutorial_NETGRAPH.pdf)
- [FRRouting user guide](https://frrouting.org/user-guide/)
- [Bird user manual](http://bird.network.cz/get_doc&f=bird.html)

## Advanced customization

### Scripts

The root filesystem is in read-only mode, then you can’t modify or create your own script on it.

For modify the existing script (don’t forget to send us your improvement), use the “data” partition. Here is an example for customizing the config script:

```
mount /data
cp /usr/local/bin/config /data
vi /data/config
```

Now you can add your great patches to config script. And test it:

```
sh /data/config
```

Then, don’t forget to umount the /data partition:

```
umount /data
```

### System

You can modify the full filesystem by re-mount the active slice in read-write mode:

```
mount -uw /
```

Now you can modify all files or removing/installing package.

Here is how to remove ucarp as example:

```
[root@router]~# pkg info | grep ucarp
ucarp-1.5.2.20171201           Userlevel Common Address Redundancy Protocol
[root@router]~# pkg remove ucarp
Checking integrity... done (0 conflicting)
Deinstallation has been requested for the following 1 packages (of 0 packages in the universe):

Installed packages to be REMOVED:
        ucarp-1.5.2.20171201

Number of packages to be removed: 1

Proceed with deinstalling packages? [y/N]: y
[1/1] Deinstalling ucarp-1.5.2.20171201...
[1/1] Deleting files for ucarp-1.5.2.20171201:   0%
pkg: /usr/local/etc/rc.d/ucarp different from original checksum, not removing
[1/1] Deleting files for ucarp-1.5.2.20171201: 100%
```

After your changes, re-mount it in read-only mode:

```
mount -ur /
```


!!! warning
    But warning: All your changes (with the exception of /boot/loader.conf.local) will be lost after an upgrade!


## Improving forwarding speed

Check the [FreeBSD forwarding Performance](technical-docs/performance.md) page for more information.
