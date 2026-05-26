---
title: User Guide
description: BSD Router Project User Guide
---
## Hardware compatibility list

To run BSDRP, you need:

- A 4 GB flash disk (such as a CompactFlash card, USB stick, or mSATA module).
- At least 1 GB of RAM.

All hardware supported by the latest FreeBSD release is compatible with BSDRP, except for some drivers that have been removed (e.g., wireless, PCMCIA, SCSI, USB printer, and FireWire).

## Filename convention

BSDRP image filenames follow this pattern:

BSDRP_*release*_*image type*_*arch*.img.xz

The *image type* can be:

- full: for a full installation; includes the bootloader, system, and data partitions
- upgrade: for system upgrades; includes only one system partition

The *arch* can be:

- amd64: for modern x86 64-bit CPUs (Intel and AMD)
- aarch64: for ARM 64-bit CPUs

Examples:

- BSDRP_2.0_full_amd64.img: full image for x86_64
- BSDRP_2.0_upgrade_aarch64.img: upgrade image for ARM

The `*.mtree.xz` files are used for system integrity checks.

## Installation

### To flash media (CF/USB)

#### Windows users

The two steps for writing the image to a CF/flash/USB removable medium:

1.  Decompress the BSDRP image using [7-Zip](http://www.7-zip.org/) to get a `.img` file.
2.  Use [Image Writer for Windows](http://win32diskimager.sourceforge.net/) to write the `.img` file to your CF/flash/USB device.

#### *BSD or Linux users

Connect your flash or USB drive and note its device name. Decompress the image and copy it to the drive using a byte-copy command (**Warning: be sure to double-check the destination disk!**):

```
xzcat BSDRP_full_amd64_vga.1.0.img.xz | dd of=/dev/sd4 bs=256k
```

You can boot from this media now.

#### macOS users

Insert the USB key and list the external devices:

```
% diskutil list | grep external
/dev/disk3 (external, physical):
```

Check whether it is already mounted:

```
% mount | grep '/dev/disk3'
/dev/disk0s2 on / (hfs, local, journaled)
devfs on /dev (devfs, local)
fdesc on /dev (fdesc, union)
map -hosts on /net (autofs, automounted)
map auto_home on /home (autofs, automounted)
/dev/disk3s1 on /Volumes/UNTITLED (msdos, local, nodev, nosuid, noowners)
```

The last line is your USB device. Unmount it and write the BSDRP image to the device, prefixing the device name with `r`:

```
sudo umount -f /dev/disk3s1
xzcat BSDRP_full_amd64_vga.1.0.img.xz | sudo dd of=/dev/rdisk3 bs=1m
```

If successful, macOS will show an error dialog saying it doesn’t recognize the disk. Click “Eject”, remove the USB key, and you’re done.

### To a hard drive

Boot BSDRP from the USB key you just created. From BSDRP, display the BSDRP system disk name:

```
[root@router]~# glabel status | grep BSDRP
 ufs/BSDRPs3     N/A  da1s3
 ufs/BSDRPs4     N/A  da1s4
ufs/BSDRPs1a     N/A  da1s1a
```

In this example, BSDRP is on disk `da1` (the USB key).

Display all the system disks:

```
[root@router]# sysctl kern.disks
kern.disks: da1 da0 ada0
```

In this example, since `da1` is the BSDRP disk, `ada0` is the hard drive where we want to install BSDRP.

Copy the BSDRP disk to the hard drive:

```
[root@router]# system install ada0
Copying 487MB from da1 to ada0...
487+0 records in
487+0 records out
510656512 bytes transferred in 30.351293 secs (16824868 bytes/sec)
```

Reboot your system (and don’t forget to remove the USB key).

Once rebooted from your hard drive, you can expand the `/data` slice to use all the free space:

```
system expand-data-slice
```

### Special notes for PC Engines

#### Alix platform

You need at least [BIOS revision 0.99h](http://www.pcengines.ch/alix2.htm). You can use the [pfSense Alix BIOS update FreeDOS image disk](https://doc.pfsense.org/index.php/ALIX_BIOS_Update_Procedure) for an easy upgrade.

## Quick start

Log in as `root` with no password.

If you are using the serial version, the serial port parameters are: 115200, 8, N, 1, MODEM.

Start with the built-in help:

```
help
```

Set a password for root (mandatory for SSH):

```
passwd
```

For a routing protocol daemon, you can choose between Bird and FRRouting (a Quagga fork).

As an example, to start FRR and enter its CLI mode:

```
sysrc frr_enable=yes
service frr start
cli
```

Configure FRR, then save its config and exit the CLI:

```
wr
exit
```

Then save all changes (you can skip this step by enabling the autosave feature):

```
config save
```

## Configuration files

Any changes to configuration files (`/etc/*`, `/usr/local/etc/*`) must be saved before a reboot.

Use the `config` command to save the configuration:

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
    Don’t modify `/boot/loader.conf`: your changes will be lost after an upgrade. Instead, create a new file `/boot/loader.conf.local` and put your modifications there.


## Upgrading examples

### From BSDRP directly

#### HTTP/FTP fetch without checking SHA256

Download the image directly and pipe the output through xzcat into upgrade:

```
fetch 'http://URL/BSDRP-upgrade.image.xz' -o - | xzcat | upgrade
```

Real example to upgrade to 1.96:

```
fetch 'https://sourceforge.net/projects/bsdrp/files/BSD_Router_Project/1.96/amd64/BSDRP-1.96-upgrade-amd64-serial.img.xz/download' -o - | xzcat | upgrade
```

#### SSH fetch without checking SHA256

Same as above, but over SSH:

```
ssh my-user@my-ssh-server cat /path-to/BSDRP-upgrade.image.xz | xzcat | upgrade
```

#### Using an SCP client, or fetching the upgrade file from BSDRP

This method requires:

- At least 60 MB of free RAM on your BSDRP (the `mem_avail` value in the `show mem` output)
- One of the following:
  - Sending the upgrade file and its sha256 with an SCP client (for example [FileZilla](http://filezilla-project.org/) or [WinSCP](http://winscp.net))
  - Or downloading the upgrade file directly from BSDRP

Summary:

1.  Create a TMPFS (RAM disk) directory
2.  Transfer the BSDRP upgrade image and its sha256 onto the RAM disk using the SCP client, or download them directly
3.  Check the SHA256
4.  Upgrade the system

Step 1: create the RAM disk

On BSDRP, run the following command to create a RAM drive:

```
mount -t tmpfs tmpfs /mnt/
```

Step 2: transfer the image file and sha256 onto the temporary RAM drive

Using your SCP client, send the BSDRP upgrade image to the router's **/mnt** folder.

Or download them directly from BSDRP:

```
cd /mnt
fetch URL/BSDRP-upgrade.image.xz
fetch URL/BSDRP-upgrade.image.sha256
```

Step 3: once the transfer is complete, run on BSDRP:

```
sha256 -c `cat BSDRP-upgrade.image.sha256 | cut -d ' ' -f 4` BSDRP-upgrade.image.xz && echo "good" || echo "bad"
xzcat /mnt/BSDRP-upgrade.image.xz | upgrade
umount /mnt
```

### From a *nix server

This method requires an SSH client (Linux and Unix systems include one by default).

From the client, run:

```
cat BSDRP_1.2_upgrade_amd64_vga.img.xz | ssh root@a.b.c.d "xzcat | upgrade"
```

## Security

### SSH access

SSH access for the root user is not available by default. You first need to set a password for the root account with the **passwd** command.

Example:

```
[root@R1]~# passwd
Changing local password for root
New Password: XXXXXXXX
Retype New Password: XXXXXXXX
```

### System integrity check

[Reference mtree files are provided](../downloads.md) so you can check the integrity of all files on your router.

To check the integrity of your BSDRP system, download the corresponding reference file onto your router and run the `system integrity` command.

For example, on a 0.35 amd64-serial release (assuming the router has DNS resolution and internet access):

```
cd /tmp
fetch http://downloads.sourceforge.net/project/bsdrp/BSD_Router_Project/0.35/BSDRP_0.35_amd64_serial.mtree.xz
system integrity BSDRP_0.35_amd64_serial.mtree.xz
```

## System management

### Autosave configuration

Any changes to configuration files under /etc and /usr/local/etc must be persisted with the `config save` command (both directories live on a RAM disk).

You can enable the autosave service to automatically run `config save` whenever a change is detected under /etc or /usr/local/etc:

```
sysrc autosave_enable=yes
service autosave start
```

### Serial port

#### Enabling dual VGA/serial console

If you are using the VGA release of BSDRP, you can enable serial access (COM1) with:

```
system dual-console
```

#### Baud rate

The serial port baud rate must be changed in two files:

- /boot.config
- /etc/ttys

To edit /boot.config, first remount / read-write:

```
mount -uw /
```

Change the speed value just after the `-S` option in /boot.config (do not remove the other `-D` or `-h` options).

Check that there are no legacy values (`boot_serial`, `comconsole_speed`, `console`) in /boot/loader.conf.local. They are unnecessary when /boot.config is in use.

Once done, remount / read-only:

```
mount -ur /
```

Then edit /etc/ttys and change the baud rate on the `ttyu0` line (for the first serial port).

#### Changing the default serial port used for the console

If you need to change which serial port is used for the console (Supermicro boards, for example, use COM2 for SOL):

- First list the available serial ports
- Then update the value in /boot/loader.conf.local

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

To configure the local IPMI board, you first need to load the IPMI driver.

Edit /etc/rc.conf and make sure the `ipmi` module is listed in the `kld_list` variable:

```
kld_list='ipmi'
```

You can also load it from the shell:

```
kldload ipmi
```

Then you can use [ipmitool](http://ipmitool.sourceforge.net/) to configure it.

To connect to the serial port over IPMI SOL (Serial Over LAN) from a remote machine, set the baud rate of the serial line to 115200 and then activate the session (example uses the default password for an IBM x3550):

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
# Start watchdogd daemon
watchdogd_enable="yes"
```

And start it:

```
kldload ichwd
service watchdogd start
```

If the `ipmi` module is already loaded, `watchdogd` can use IPMI instead of `ichwd`.

### SNMP

Enable bsnmpd:

```
sysrc bsnmpd_enable=YES
```

Edit /etc/snmpd.config to suit your needs and start the daemon:

```
service bsnmpd start
```

You can then check it locally (the default SNMP community is `public`):

```
[root@BSDRP]~# bsnmpget sysDescr.0
sysDescr.0 = router.bsdrp.net 2059309898 FreeBSD 9.1-RELEASE-p1
```

### Syslog

To send syslog messages to a remote host, edit /etc/syslog.conf. The file already includes a commented example:

```
# uncomment this to enable logging to a remote loghost named loghost
#*.*                                            @loghost
```

Then restart syslogd:

```
service syslogd restart
```


!!! note
    BSDRP v1.4 and earlier ship with a default configuration that blocks remote syslog. To change this, edit /etc/rc.conf.misc and replace `syslogd_flags="-ss"` with `syslogd_flags="-s"`.


### Firmware upgrade

#### Mellanox

Start by identifying your NIC:

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

Go to the [Mellanox firmware download site](https://www.mellanox.com/page/firmware_download), navigate to "Device Type" -> "Part Number" -> "PSID", then fetch the firmware on your BSDRP router and apply the upgrade:

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

To save and extract a crash dump you need:

- A swap partition the same size as your RAM (to store the raw memory dump)
- A data partition the same size as your RAM (to store the extracted dump)

The steps to enable crash dumps are:

1.  Configure a dump device for storing the memory dump (this can be an external USB key)
2.  Increase the size of /data so it can hold the memory dump
3.  Configure /data to mount automatically (the next step needs it)
4.  Configure the system to save dumps under /data

Here is an example that splits data partition 4 into two BSD partitions:

- One as swap
- One as /data

If you can plug in a USB key the same size as your RAM, you can skip expanding partition 4 and just use that device.

Steps:

1.  Delete partition 4 (/data)
2.  Recreate partition 4 using the full available disk space
3.  Create two BSD partitions inside this new partition 4:
    - partition s4a (4.2BSD) the size of your RAM
    - partition s4b (swap) the size of your RAM
4.  Format s4a as UFS and enable dumpon on the swap partition

Now destroy the default small partition 4, recreate it using the full disk size, and create BSD partitions inside it (the MBR scheme allows only four partitions, so we use BSD sub-partitions):

```
gpart delete -i 4 da0
gpart add -t freebsd da0
bsdlabel -w /dev/da0s4
```

Now start the BSD partition editor:

```
bsdlabel -e /dev/da0s4
```

Replace these lines:

```
# /dev/da0s4:
8 partitions:
#          size     offset    fstype   [fsize bsize bps/cpg]
  a:  284191428          16   unused        0     0     0
  c:  284191428          0    unused        0     0     # "raw" part, don't edit
```

with these (the size and fstype of the `a:` and `b:` lines are updated; `*` means "automatic size"):

```
# /dev/da0s4:
8 partitions:
#          size     offset    fstype   [fsize bsize bps/cpg]
  a:   16G          16        4.2BSD        0     0     0
  b:   *          *         swap
  c:  284191428          0    unused        0     0     # "raw" part, don't edit
```

Then quit the editor (`:x`) and format partition a (/data):

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

When a crash occurs, the core dump is written to the dump device:

```
#14 0xffffffff8096c34a at taskqueue_run_locked+0x14a
#15 0xffffffff8096d258 at taskqueue_thread_loop+0xe8
#16 0xffffffff808d4495 at fork_exit+0x85
#17 0xffffffff80d1b30e at fork_trampoline+0xe
Uptime: 3m10s
Dumping 1112 out of 16325 MB:..2%..11%..21%..31%..41%..51%..61%..71%..81%..91%
Dump complete
```

After the next reboot the dump is automatically extracted from the dump device and stored in /data/crash:

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

If you do not have enough local disk space to store a dump, you can use netdump(4).

On the receiving FreeBSD server (not your router):

```
pkg install netdumpd
service netdumpd enable
service netdumpd start
```

Then on your router, set the source interface, source IP address, and gateway:

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

Kernel and binary symbol files are shipped in a separate DEBUG archive. To install them you need:

1.  Either 1 GB of free RAM (to create a large tmpfs) or 1 GB of free space in /data (use `system expand-data-slice`)
2.  The debug tarball extracted under /data/ (a symlink from /usr/lib/debug already points to /data/debug)

Here is an example that begins by expanding the data slice:

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

### Analysing a core dump

Install debug symbols first, then:

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

### Generate a panic on a hung or frozen system

If your system has frozen rather than panicked, you can force a panic by sending a Non-Maskable Interrupt (NMI) via IPMI (`chassis power diag`):

```
ipmitool -I lanplus -H SERVER -U USER -P PASSWORD chassis power diag
```

### Live kernel debugging

Install debug symbols first, then:

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

BSDRP is a FreeBSD-based system, so the standard FreeBSD documentation applies.

Useful references:

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

The root filesystem is mounted read-only, so you cannot modify or create scripts directly on it.

To customize an existing script (and please send your improvements back upstream), use the `/data` partition. Here is an example for the `config` script:

```
mount /data
cp /usr/local/bin/config /data
vi /data/config
```

Apply your changes to the script, then test it:

```
sh /data/config
```

When you are done, unmount the /data partition:

```
umount /data
```

### System

You can modify the whole filesystem by remounting the active slice read-write:

```
mount -uw /
```

You can now modify any file, or install and remove packages.

For example, to remove ucarp:

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

After your changes, remount it read-only:

```
mount -ur /
```


!!! warning
    All your changes (with the exception of /boot/loader.conf.local) will be lost after an upgrade.


## Improving forwarding speed

See the [FreeBSD forwarding performance](technical-docs/performance.md) page for more information.
