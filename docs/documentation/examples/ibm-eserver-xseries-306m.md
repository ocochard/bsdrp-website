---
title: IBM eServer xSeries 306m
---
### dmesg

```
Copyright (c) 1992-2013 The FreeBSD Project.
Copyright (c) 1979, 1980, 1983, 1986, 1988, 1989, 1991, 1992, 1993, 1994
        The Regents of the University of California. All rights reserved.
FreeBSD is a registered trademark of The FreeBSD Foundation.
FreeBSD 10.0-CURRENT #0 r249330: Wed Apr 10 11:35:11 CEST 2013
    root@orange.bsdrp.net:/usr/obj/BSDRPcur.amd64/usr/local/BSDRP/BSDRPcur/FreeBSD/src/sys/amd64 amd64
FreeBSD clang version 3.2 (tags/RELEASE_32/final 170710) 20121221
CPU: Intel(R) Pentium(R) 4 CPU 3.00GHz (3000.18-MHz K8-class CPU)
  Origin = "GenuineIntel"  Id = 0xf49  Family = 0xf  Model = 0x4  Stepping = 9
  Features=0xbfebfbff<FPU,VME,DE,PSE,TSC,MSR,PAE,MCE,CX8,APIC,SEP,MTRR,PGE,MCA,CMOV,PAT,PSE36,CLFLUSH,DTS,ACPI,MMX,FXSR,SSE,SSE2,SS,HTT,TM,PBE>
  Features2=0x641d<SSE3,DTES64,MON,DS_CPL,CNXT-ID,CX16,xTPR>
  AMD Features=0x20100800<SYSCALL,NX,LM>
  AMD Features2=0x1<LAHF>
  TSC: P-state invariant
real memory  = 1073741824 (1024 MB)
avail memory = 977702912 (932 MB)
Event timer "LAPIC" quality 400
ACPI APIC Table: <PTLTD          APIC  >
ioapic0 <Version 2.0> irqs 0-23 on motherboard
netmap: loaded module
cryptosoft0: <software crypto> on motherboard
acpi0: <PTLTD   RSDT> on motherboard
acpi0: Power Button (fixed)
cpu0: <ACPI CPU> on acpi0
atrtc0: <AT realtime clock> port 0x70-0x71 irq 8 on acpi0
Event timer "RTC" frequency 32768 Hz quality 0
attimer0: <AT timer> port 0x40-0x43,0x50-0x53 irq 0 on acpi0
Timecounter "i8254" frequency 1193182 Hz quality 0
Event timer "i8254" frequency 1193182 Hz quality 100
Timecounter "ACPI-fast" frequency 3579545 Hz quality 900
acpi_timer0: <24-bit timer at 3.579545MHz> port 0x1008-0x100b on acpi0
pcib0: <ACPI Host-PCI bridge> port 0xcf8-0xcff on acpi0
pci0: <ACPI PCI bus> on pcib0
pcib1: <ACPI PCI-PCI bridge> irq 16 at device 1.0 on pci0
pcib1: failed to allocate initial I/O port window: 0-0xfff
pcib1: failed to allocate initial memory window: 0-0xfffff
pcib1: failed to allocate initial prefetch window: 0-0xfffff
pci1: <ACPI PCI bus> on pcib1
pcib2: <ACPI PCI-PCI bridge> irq 17 at device 28.0 on pci0
pci2: <ACPI PCI bus> on pcib2
pcib3: <ACPI PCI-PCI bridge> at device 0.0 on pci2
pci3: <ACPI PCI bus> on pcib3
em0: <Intel(R) PRO/1000 Legacy Network Connection 1.0.6> port 0x4000-0x403f mem 0xc0280000-0xc029ffff,0xc0240000-0xc027ffff irq 17 at device 3.0 on pci3
em0: Ethernet address: 00:0e:0c:de:45:de
001.000007 netmap_attach [1680] success for em0
em1: <Intel(R) PRO/1000 Legacy Network Connection 1.0.6> port 0x4040-0x407f mem 0xc02a0000-0xc02bffff irq 18 at device 3.1 on pci3
em1: Ethernet address: 00:0e:0c:de:45:df
001.000008 netmap_attach [1680] success for em1
pcib4: <ACPI PCI-PCI bridge> irq 17 at device 28.4 on pci0
pci4: <ACPI PCI bus> on pcib4
bge0: <Broadcom NetXtreme Gigabit Ethernet Controller, ASIC rev. 0x004101> mem 0xc0300000-0xc030ffff irq 16 at device 0.0 on pci4
bge0: CHIP ID 0x00004101; ASIC REV 0x04; CHIP REV 0x41; PCI-E
miibus0: <MII bus> on bge0
brgphy0: <BCM5750 1000BASE-T media interface> PHY 1 on miibus0
brgphy0:  10baseT, 10baseT-FDX, 100baseTX, 100baseTX-FDX, 1000baseT, 1000baseT-master, 1000baseT-FDX, 1000baseT-FDX-master, auto, auto-flow
bge0: Ethernet address: 00:14:5e:84:79:40
pcib5: <ACPI PCI-PCI bridge> irq 16 at device 28.5 on pci0
pci5: <ACPI PCI bus> on pcib5
bge1: <Broadcom NetXtreme Gigabit Ethernet Controller, ASIC rev. 0x004101> mem 0xc0400000-0xc040ffff irq 17 at device 0.0 on pci5
bge1: CHIP ID 0x00004101; ASIC REV 0x04; CHIP REV 0x41; PCI-E
miibus1: <MII bus> on bge1
brgphy1: <BCM5750 1000BASE-T media interface> PHY 1 on miibus1
brgphy1:  10baseT, 10baseT-FDX, 100baseTX, 100baseTX-FDX, 1000baseT, 1000baseT-master, 1000baseT-FDX, 1000baseT-FDX-master, auto, auto-flow
bge1: Ethernet address: 00:14:5e:84:79:41
uhci0: <Intel 82801G (ICH7) USB controller USB-A> port 0x3000-0x301f irq 23 at device 29.0 on pci0
usbus0 on uhci0
uhci1: <Intel 82801G (ICH7) USB controller USB-B> port 0x3020-0x303f irq 19 at device 29.1 on pci0
usbus1 on uhci1
uhci2: <Intel 82801G (ICH7) USB controller USB-C> port 0x3040-0x305f irq 18 at device 29.2 on pci0
usbus2 on uhci2
ehci0: <Intel 82801GB/R (ICH7) USB 2.0 controller> mem 0xc0000000-0xc00003ff irq 23 at device 29.7 on pci0
usbus3: EHCI version 1.0
usbus3 on ehci0
pcib6: <ACPI PCI-PCI bridge> at device 30.0 on pci0
pci10: <ACPI PCI bus> on pcib6
vgapci0: <VGA-compatible display> port 0x5000-0x50ff mem 0xc8000000-0xcfffffff,0xc0500000-0xc050ffff irq 16 at device 4.0 on pci10
isab0: <PCI-ISA bridge> at device 31.0 on pci0
isa0: <ISA bus> on isab0
atapci0: <Intel ICH7 UDMA100 controller> port 0x1f0-0x1f7,0x3f6,0x170-0x177,0x376,0x30a0-0x30af at device 31.1 on pci0
ata0: <ATA channel> at channel 0 on atapci0
ahci0: <Intel ICH7 AHCI SATA controller> port 0x30d8-0x30df,0x30cc-0x30cf,0x30d0-0x30d7,0x30c8-0x30cb,0x3060-0x307f mem 0xc0000400-0xc00007ff irq 19 at device 31.2 on pc
i0
ahci0: AHCI v1.10 with 4 3Gbps ports, Port Multiplier not supported
ahcich0: <AHCI channel> at channel 0 on ahci0
pci0: <serial bus, SMBus> at device 31.3 (no driver attached)
acpi_button0: <Power Button> on acpi0
uart0: <16550 or compatible> port 0x3f8-0x3ff irq 4 flags 0x10 on acpi0
uart0: console (38400,n,8,1)
atkbdc0: <Keyboard controller (i8042)> port 0x60,0x64 irq 1 on acpi0
atkbd0: <AT Keyboard> irq 1 on atkbdc0
atkbd0: [GIANT-LOCKED]
orm0: <ISA Option ROMs> at iomem 0xc0000-0xcafff,0xcb000-0xcbfff,0xe0000-0xe17ff on isa0
sc0: <System console> at flags 0x100 on isa0
sc0: VGA <16 virtual consoles, flags=0x300>
vga0: <Generic ISA VGA> at port 0x3c0-0x3df iomem 0xa0000-0xbffff on isa0
p4tcc0: <CPU Frequency Thermal Control> on cpu0
Timecounters tick every 1.000 msec
IPsec: Initialized Security Association Processing.
usbus0: 12Mbps Full Speed USB v1.0
usbus1: 12Mbps Full Speed USB v1.0
usbus2: 12Mbps Full Speed USB v1.0
ugen0.1: <Intel> at usbus0
uhub0: <Intel UHCI root HUB, class 9/0, rev 1.00/1.00, addr 1> on usbus0
ugen1.1: <Intel> at usbus1
uhub1: <Intel UHCI root HUB, class 9/0, rev 1.00/1.00, addr 1> on usbus1
ugen2.1: <Intel> at usbus2
uhub2: <Intel UHCI root HUB, class 9/0, rev 1.00/1.00, addr 1> on usbus2
usbus3: 480Mbps High Speed USB v2.0
ugen3.1: <Intel> at usbus3
uhub3: <Intel EHCI root HUB, class 9/0, rev 2.00/1.00, addr 1> on usbus3
ada0 at ahcich0 bus 0 scbus1 target 0 lun 0
ada0: <WDC WD800ABJS-23TEA0 01.00A02> ATA-7 SATA 2.x device
ada0: 300.000MB/s transfers (SATA 2.x, UDMA6, PIO 8192bytes)
ada0: Command Queueing enabled
ada0: 76324MB (156312576 512 byte sectors: 16H 63S/T 16383C)
ada0: Previously was known as ad4
pass0 at ata0 bus 0 scbus0 target 0 lun 0
pass0: <HL-DT-ST RW/DVD GCC-T10N 1.00> Removable CD-ROM SCSI-0 device
pass0: 33.300MB/s transfers (UDMA2, ATAPI 12bytes, uhub0: 2 ports with 2 removable, self powered
PIO 65534bytes)
Timecounter "TSC-low" frequency 1500088211 Hz quality 1000
uhub1: 2 ports with 2 removable, self powered
uhub2: 2 ports with 2 removable, self powered
Root mount waiting for: usbus3
Root mount waiting for: usbus3
Root mount waiting for: usbus3
uhub3: 6 ports with 6 removable, self powered
Trying to mount root from ufs:/dev/ufs/BSDRPs1a [ro]...
ichwd0 on isa0
```

### pciconf

```
hostb0@pci0:0:0:0:      class=0x060000 card=0x02fd1014 chip=0x27788086 rev=0x81 hdr=0x00                                                                         [79/744]
    vendor     = 'Intel Corporation'
    device     = 'E7230/3000/3010 Memory Controller Hub'
    class      = bridge
    subclass   = HOST-PCI
pcib1@pci0:0:1:0:       class=0x060400 card=0x02fd1014 chip=0x27798086 rev=0x81 hdr=0x01
    vendor     = 'Intel Corporation'
    device     = 'E7230/3000/3010 PCI Express Root Port'
    class      = bridge
    subclass   = PCI-PCI
pcib2@pci0:0:28:0:      class=0x060400 card=0x02fd1014 chip=0x27d08086 rev=0x01 hdr=0x01
    vendor     = 'Intel Corporation'
    device     = 'NM10/ICH7 Family PCI Express Port 1'
    class      = bridge
    subclass   = PCI-PCI
pcib4@pci0:0:28:4:      class=0x060400 card=0x02fd1014 chip=0x27e08086 rev=0x01 hdr=0x01
    vendor     = 'Intel Corporation'
    device     = '82801GR/GH/GHM (ICH7 Family) PCI Express Port 5'
    class      = bridge
    subclass   = PCI-PCI
pcib5@pci0:0:28:5:      class=0x060400 card=0x02fd1014 chip=0x27e28086 rev=0x01 hdr=0x01
    vendor     = 'Intel Corporation'
    device     = '82801GR/GH/GHM (ICH7 Family) PCI Express Port 6'
    class      = bridge
    subclass   = PCI-PCI
uhci0@pci0:0:29:0:      class=0x0c0300 card=0x02fd1014 chip=0x27c88086 rev=0x01 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = 'NM10/ICH7 Family USB UHCI Controller'
    class      = serial bus
    subclass   = USB
    bar   [20] = type I/O Port, range 32, base 0x3000, size 32, enabled
uhci1@pci0:0:29:1:      class=0x0c0300 card=0x02fd1014 chip=0x27c98086 rev=0x01 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = 'NM10/ICH7 Family USB UHCI Controller'
    class      = serial bus
    subclass   = USB
    bar   [20] = type I/O Port, range 32, base 0x3020, size 32, enabled
uhci2@pci0:0:29:2:      class=0x0c0300 card=0x02fd1014 chip=0x27ca8086 rev=0x01 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = 'NM10/ICH7 Family USB UHCI Controller'
    class      = serial bus
    subclass   = USB
    bar   [20] = type I/O Port, range 32, base 0x3040, size 32, enabled
ehci0@pci0:0:29:7:      class=0x0c0320 card=0x02fd1014 chip=0x27cc8086 rev=0x01 hdr=0x00                                                                         [36/744]
    vendor     = 'Intel Corporation'
    device     = 'NM10/ICH7 Family USB2 EHCI Controller'
    class      = serial bus
    subclass   = USB
    bar   [10] = type Memory, range 32, base 0xc0000000, size 1024, enabled
pcib6@pci0:0:30:0:      class=0x060401 card=0x02fd1014 chip=0x244e8086 rev=0xe1 hdr=0x01
    vendor     = 'Intel Corporation'
    device     = '82801 PCI Bridge'
    class      = bridge
    subclass   = PCI-PCI
isab0@pci0:0:31:0:      class=0x060100 card=0x02fd1014 chip=0x27b88086 rev=0x01 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '82801GB/GR (ICH7 Family) LPC Interface Bridge'
    class      = bridge
    subclass   = PCI-ISA
atapci0@pci0:0:31:1:    class=0x01018a card=0x02fd1014 chip=0x27df8086 rev=0x01 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '82801G (ICH7 Family) IDE Controller'
    class      = mass storage
    subclass   = ATA
    bar   [20] = type I/O Port, range 32, base 0x30a0, size 16, enabled
ahci0@pci0:0:31:2:      class=0x010601 card=0x02fd1014 chip=0x27c18086 rev=0x01 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = 'NM10/ICH7 Family SATA Controller [AHCI mode]'
    class      = mass storage
    subclass   = SATA
    bar   [10] = type I/O Port, range 32, base 0x30d8, size 8, enabled
    bar   [14] = type I/O Port, range 32, base 0x30cc, size 4, enabled
    bar   [18] = type I/O Port, range 32, base 0x30d0, size 8, enabled
    bar   [1c] = type I/O Port, range 32, base 0x30c8, size 4, enabled
    bar   [20] = type I/O Port, range 32, base 0x3060, size 32, enabled
    bar   [24] = type Memory, range 32, base 0xc0000400, size 1024, enabled
none0@pci0:0:31:3:      class=0x0c0500 card=0x02fd1014 chip=0x27da8086 rev=0x01 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = 'NM10/ICH7 Family SMBus Controller'
    class      = serial bus
    subclass   = SMBus
    bar   [20] = type I/O Port, range 32, base 0x3080, size 32, enabled
pcib3@pci0:2:0:0:       class=0x060400 card=0x00000000 chip=0x032c8086 rev=0x09 hdr=0x01
    vendor     = 'Intel Corporation'
    device     = '6702PXH PCI Express-to-PCI Bridge A'
    class      = bridge
    subclass   = PCI-PCI
ioapic0@pci0:2:0:1:     class=0x080020 card=0x00000000 chip=0x03268086 rev=0x09 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '6700/6702PXH I/OxAPIC Interrupt Controller A'
    class      = base peripheral
    subclass   = interrupt controller
    bar   [10] = type Memory, range 32, base 0xc0100000, size 4096, enabled
em0@pci0:3:3:0: class=0x020000 card=0x118a8086 chip=0x10798086 rev=0x03 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '82546GB Gigabit Ethernet Controller'
    class      = network
    subclass   = ethernet
    bar   [10] = type Memory, range 64, base 0xc0280000, size 131072, enabled
    bar   [18] = type Memory, range 64, base 0xc0240000, size 262144, enabled
    bar   [20] = type I/O Port, range 32, base 0x4000, size 64, enabled
em1@pci0:3:3:1: class=0x020000 card=0x118a8086 chip=0x10798086 rev=0x03 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '82546GB Gigabit Ethernet Controller'
    class      = network
    subclass   = ethernet
    bar   [10] = type Memory, range 64, base 0xc02a0000, size 131072, enabled
    bar   [20] = type I/O Port, range 32, base 0x4040, size 64, enabled
bge0@pci0:4:0:0:        class=0x020000 card=0x02c61014 chip=0x165914e4 rev=0x11 hdr=0x00
    vendor     = 'Broadcom Corporation'
    device     = 'NetXtreme BCM5721 Gigabit Ethernet PCI Express'
    class      = network
    subclass   = ethernet
    bar   [10] = type Memory, range 64, base 0xc0300000, size 65536, enabled
bge1@pci0:5:0:0:        class=0x020000 card=0x02c61014 chip=0x165914e4 rev=0x11 hdr=0x00
    vendor     = 'Broadcom Corporation'
    device     = 'NetXtreme BCM5721 Gigabit Ethernet PCI Express'
    class      = network
    subclass   = ethernet
    bar   [10] = type Memory, range 64, base 0xc0400000, size 65536, enabled
vgapci0@pci0:10:4:0:    class=0x030000 card=0x03251014 chip=0x515e1002 rev=0x02 hdr=0x00
    vendor     = 'Advanced Micro Devices [AMD] nee ATI'
    device     = 'ES1000'
    class      = display
    subclass   = VGA
    bar   [10] = type Prefetchable Memory, range 32, base 0xc8000000, size 134217728, enabled
    bar   [14] = type I/O Port, range 32, base 0x5000, size 256, enabled
    bar   [18] = type Memory, range 32, base 0xc0500000, size 65536, enabled
```
