---
title: PC Engines APU
---
## dmesg

```
Copyright (c) 1992-2014 The FreeBSD Project.
Copyright (c) 1979, 1980, 1983, 1986, 1988, 1989, 1991, 1992, 1993, 1994
        The Regents of the University of California. All rights reserved.
FreeBSD is a registered trademark of The FreeBSD Foundation.
FreeBSD 11.0-CURRENT #1 r263096M: Wed Mar 12 23:05:33 CET 2014
    root@orange.bsdrp.net:/usr/obj/EINBOX.amd64/usr/local/BSDRP/EINBOX/FreeBSD/src/sys/amd64 amd64
FreeBSD clang version 3.4 (tags/RELEASE_34/final 197956) 20140216
CPU: AMD G-T40E Processor (1000.02-MHz K8-class CPU)
  Origin="AuthenticAMD"  Id=0x500f20  Family=0x14  Model=0x2  Stepping=0
  Features=0x178bfbff<FPU,VME,DE,PSE,TSC,MSR,PAE,MCE,CX8,APIC,SEP,MTRR,PGE,MCA,CMOV,PAT,PSE36,CLFLUSH,MMX,FXSR,SSE,SSE2,HTT>
  Features2=0x802209<SSE3,MON,SSSE3,CX16,POPCNT>
  AMD Features=0x2e500800<SYSCALL,NX,MMX+,FFXSR,Page1GB,RDTSCP,LM>
  AMD Features2=0x35ff<LAHF,CMP,SVM,ExtAPIC,CR8,ABM,SSE4A,MAS,Prefetch,IBS,SKINIT,WDT>
  TSC: P-state invariant, performance statistics
real memory  = 2115428352 (2017 MB)
avail memory = 2028584960 (1934 MB)
Event timer "LAPIC" quality 400
ACPI APIC Table: <CORE   COREBOOT>
FreeBSD/SMP: Multiprocessor System Detected: 2 CPUs
FreeBSD/SMP: 1 package(s) x 2 core(s)
 cpu0 (BSP): APIC ID:  0
 cpu1 (AP): APIC ID:  1
ioapic0 <Version 2.1> irqs 0-23 on motherboard
netmap: loaded module
random: <Software, Yarrow> initialized
module_register_init: MOD_LOAD (vesa, 0xffffffff808c64e0, 0) error 19
cryptosoft0: <software crypto> on motherboard
acpi0: <CORE COREBOOT> on motherboard
acpi0: Power Button (fixed)
cpu0: <ACPI CPU> on acpi0
cpu1: <ACPI CPU> on acpi0
atrtc0: <AT realtime clock> port 0x70-0x71 irq 8 on acpi0
Event timer "RTC" frequency 32768 Hz quality 0
attimer0: <AT timer> port 0x40-0x43 irq 0 on acpi0
Timecounter "i8254" frequency 1193182 Hz quality 0
Event timer "i8254" frequency 1193182 Hz quality 100
hpet0: <High Precision Event Timer> iomem 0xfed00000-0xfed003ff on acpi0
Timecounter "HPET" frequency 14318180 Hz quality 950
Event timer "HPET" frequency 14318180 Hz quality 550
Event timer "HPET1" frequency 14318180 Hz quality 450
Timecounter "ACPI-fast" frequency 3579545 Hz quality 900
acpi_timer0: <32-bit timer at 3.579545MHz> port 0x808-0x80b on acpi0
pcib0: <ACPI Host-PCI bridge> port 0xcf8-0xcff on acpi0
pci0: <ACPI PCI bus> on pcib0
pcib1: <ACPI PCI-PCI bridge> at device 4.0 on pci0
pci1: <ACPI PCI bus> on pcib1
re0: <RealTek 8168/8111 B/C/CP/D/DP/E/F/G PCIe Gigabit Ethernet> port 0x1000-0x10ff mem 0xfe500000-0xfe500fff,0xfe400000-0xfe403fff at device 0.0 on pci1
re0: Using 1 MSI-X message
re0: ASPM disabled
re0: Chip rev. 0x2c000000
re0: MAC rev. 0x00200000
miibus0: <MII bus> on re0
rgephy0: <RTL8169S/8110S/8211 1000BASE-T media interface> PHY 1 on miibus0
rgephy0:  none, 10baseT, 10baseT-FDX, 10baseT-FDX-flow, 100baseTX, 100baseTX-FDX, 100baseTX-FDX-flow, 1000baseT, 1000baseT-master, 1000baseT-FDX, 1000baseT-FDX-master, 1000baseT-FDX-flow, 1000baseT-FDX-flow-master, auto, auto-flow
re0: Ethernet address: 00:0d:b9:33:12:64
001.000008 [2258] netmap_attach             success for re0
pcib2: <ACPI PCI-PCI bridge> at device 5.0 on pci0
pci2: <ACPI PCI bus> on pcib2
re1: <RealTek 8168/8111 B/C/CP/D/DP/E/F/G PCIe Gigabit Ethernet> port 0x2000-0x20ff mem 0xfe700000-0xfe700fff,0xfe600000-0xfe603fff at device 0.0 on pci2
re1: Using 1 MSI-X message
re1: ASPM disabled
re1: Chip rev. 0x2c000000
re1: MAC rev. 0x00200000
miibus1: <MII bus> on re1
rgephy1: <RTL8169S/8110S/8211 1000BASE-T media interface> PHY 1 on miibus1
rgephy1:  none, 10baseT, 10baseT-FDX, 10baseT-FDX-flow, 100baseTX, 100baseTX-FDX, 100baseTX-FDX-flow, 1000baseT, 1000baseT-master, 1000baseT-FDX, 1000baseT-FDX-master, 1000baseT-FDX-flow, 1000baseT-FDX-flow-master, auto, auto-flow
re1: Ethernet address: 00:0d:b9:33:12:65
001.000009 [2258] netmap_attach             success for re1
pcib3: <ACPI PCI-PCI bridge> at device 6.0 on pci0
pci3: <ACPI PCI bus> on pcib3
re2: <RealTek 8168/8111 B/C/CP/D/DP/E/F/G PCIe Gigabit Ethernet> port 0x3000-0x30ff mem 0xfe900000-0xfe900fff,0xfe800000-0xfe803fff at device 0.0 on pci3
re2: Using 1 MSI-X message
re2: ASPM disabled
re2: Chip rev. 0x2c000000
re2: MAC rev. 0x00200000
miibus2: <MII bus> on re2
rgephy2: <RTL8169S/8110S/8211 1000BASE-T media interface> PHY 1 on miibus2
rgephy2:  none, 10baseT, 10baseT-FDX, 10baseT-FDX-flow, 100baseTX, 100baseTX-FDX, 100baseTX-FDX-flow, 1000baseT, 1000baseT-master, 1000baseT-FDX, 1000baseT-FDX-master, 1000baseT-FDX-flow, 1000baseT-FDX-flow-master, auto, auto-flow
re2: Ethernet address: 00:0d:b9:33:12:66
001.000010 [2258] netmap_attach             success for re2
pcib4: <ACPI PCI-PCI bridge> at device 7.0 on pci0
pci4: <ACPI PCI bus> on pcib4
ath0: <Atheros 9280> mem 0xfea00000-0xfea0ffff at device 0.0 on pci4
ath0: [HT] enabling HT modes
ath0: [HT] 1 stream STBC receive enabled
ath0: [HT] 1 stream STBC transmit enabled
ath0: [HT] 2 RX streams; 2 TX streams
ath0: AR9280 mac 128.2 RF5133 phy 13.0
ath0: 2GHz radio: 0x0000; 5GHz radio: 0x00c0
ahci0: <ATI IXP700 AHCI SATA controller> port 0x4020-0x4027,0x4040-0x4043,0x4028-0x402f,0x4044-0x4047,0x4000-0x400f mem 0xfeb08000-0xfeb083ff at device 17.0 on pci0
ahci0: AHCI v1.20 with 4 6Gbps ports, Port Multiplier supported
ahcich0: <AHCI channel> at channel 0 on ahci0
ahcich1: <AHCI channel> at channel 1 on ahci0
ahcich2: <AHCI channel> at channel 2 on ahci0
ahcich3: <AHCI channel> at channel 3 on ahci0
ohci0: <AMD SB7x0/SB8x0/SB9x0 USB controller> mem 0xfeb04000-0xfeb04fff at device 18.0 on pci0
usbus0 on ohci0
ehci0: <AMD SB7x0/SB8x0/SB9x0 USB 2.0 controller> mem 0xfeb08400-0xfeb084ff at device 18.2 on pci0
usbus1: EHCI version 1.0
usbus1 on ehci0
ohci1: <AMD SB7x0/SB8x0/SB9x0 USB controller> mem 0xfeb05000-0xfeb05fff at device 19.0 on pci0
usbus2 on ohci1
ehci1: <AMD SB7x0/SB8x0/SB9x0 USB 2.0 controller> mem 0xfeb08500-0xfeb085ff at device 19.2 on pci0
usbus3: EHCI version 1.0
usbus3 on ehci1
pci0: <serial bus, SMBus> at device 20.0 (no driver attached)
atapci0: <ATI IXP700/800 UDMA133 controller> port 0x1f0-0x1f7,0x3f6,0x170-0x177,0x376,0x4010-0x401f at device 20.1 on pci0
ata0: <ATA channel> at channel 0 on atapci0
ata1: <ATA channel> at channel 1 on atapci0
isab0: <PCI-ISA bridge> at device 20.3 on pci0
isa0: <ISA bus> on isab0
pcib5: <ACPI PCI-PCI bridge> at device 20.4 on pci0
pcib5: failed to allocate initial memory window: 0-0xfffff
pcib5: failed to allocate initial prefetch window: 0-0xfffff
pci6: <ACPI PCI bus> on pcib5
ohci2: <AMD SB7x0/SB8x0/SB9x0 USB controller> mem 0xfeb06000-0xfeb06fff at device 20.5 on pci0
usbus4 on ohci2
pcib6: <ACPI PCI-PCI bridge> at device 21.0 on pci0
pci5: <ACPI PCI bus> on pcib6
ohci3: <AMD SB7x0/SB8x0/SB9x0 USB controller> mem 0xfeb07000-0xfeb07fff at device 22.0 on pci0
usbus5 on ohci3
ehci2: <AMD SB7x0/SB8x0/SB9x0 USB 2.0 controller> mem 0xfeb08600-0xfeb086ff at device 22.2 on pci0
usbus6: EHCI version 1.0
usbus6 on ehci2
acpi_button0: <Power Button> on acpi0
orm0: <ISA Option ROM> at iomem 0xee000-0xeffff on isa0
uart0: <16550 or compatible> at port 0x3f8-0x3ff irq 4 flags 0x10 on isa0
uart0: console (115200,n,8,1)
uart1: <16550 or compatible> at port 0x2f8-0x2ff irq 3 on isa0
acpi_throttle0: <ACPI CPU Throttling> on cpu0
Timecounters tick every 1.000 msec
IPsec: Initialized Security Association Processing.
random: unblocking device.
usbus0: 12Mbps Full Speed USB v1.0
usbus1: 480Mbps High Speed USB v2.0
usbus2: 12Mbps Full Speed USB v1.0
usbus3: 480Mbps High Speed USB v2.0
ugen0.1: <ATI> at usbus0
uhub0: <ATI OHCI root HUB, class 9/0, rev 1.00/1.00, addr 1> on usbus0
ugen1.1: <ATI> at usbus1
uhub1: <ATI EHCI root HUB, class 9/0, rev 2.00/1.00, addr 1> on usbus1
ugen2.1: <ATI> at usbus2
uhub2: <ATI OHCI root HUB, class 9/0, rev 1.00/1.00, addr 1> on usbus2
ugen3.1: <ATI> at usbus3
uhub3: <ATI EHCI root HUB, class 9/0, rev 2.00/1.00, addr 1> on usbus3
usbus4: 12Mbps Full Speed USB v1.0
usbus5: 12Mbps Full Speed USB v1.0
usbus6: 480Mbps High Speed USB v2.0
ugen4.1: <ATI> at usbus4
uhub4: <ATI OHCI root HUB, class 9/0, rev 1.00/1.00, addr 1> on usbus4
ugen5.1: <ATI> at usbus5
uhub5: <ATI OHCI root HUB, class 9/0, rev 1.00/1.00, addr 1> on usbus5
ugen6.1: <ATI> at usbus6
uhub6: <ATI EHCI root HUB, class 9/0, rev 2.00/1.00, addr 1> on usbus6
uhub6: <ATI EHCI root HUB, class 9/0, rev 2.00/1.00, addr 1> on usbus6
uhub4: 2 ports with 2 removable, self powered
uhub0: 5 ports with 5 removable, self powered
uhub2: 5 ports with 5 removable, self powered
uhub5: 4 ports with 4 removable, self powered
uhub6: 4 ports with 4 removable, self powered
uhub1: 5 ports with 5 removable, self powered
uhub3: 5 ports with 5 removable, self powered
ugen6.2: <Generic> at usbus6
umass0: <Generic Flash Card ReaderWriter, class 0/0, rev 2.01/1.00, addr 2> on usbus6
umass0:  SCSI over Bulk-Only; quirks = 0x4001
umass0:6:0: Attached to scbus6
ada0 at ahcich0 bus 0 scbus0 target 0 lun 0
ada0: <SuperSSpeed S238 16GB V4629> ATA-7 SATA 2.x device
ada0: Serial Number YTAK13450504
ada0: 300.000MB/s transfers (SATA 2.x, UDMA6, PIO 8192bytes)
ada0: Command Queueing enabled
ada0: 15258MB (31248704 512 byte sectors: 16H 63S/T 16383C)
ada0: Previously was known as ad4
da0 at umass-sim0 bus 0 scbus6 target 0 lun 0
da0: <Multiple Card  Reader 1.00> Removable Direct Access SCSI-4 device
da0: Serial Number 058F63666485
da0: 40.000MB/s transfers
da0: Attempt to query device size failed: NOT READY, Medium not present
da0: quirks=0x2<NO_6_BYTE>
SMP: AP CPU #1 Launched!
Timecounter "TSC" frequency 1000021999 Hz quality 800
amdtemp0: <AMD CPU On-Die Thermal Sensors> on hostb4
```

## pciconf

```
hostb0@pci0:0:0:0:      class=0x060000 card=0x15101022 chip=0x15101022 rev=0x00 hdr=0x00
    vendor     = 'Advanced Micro Devices [AMD]'
    device     = 'Family 14h Processor Root Complex'
    class      = bridge
    subclass   = HOST-PCI
pcib1@pci0:0:4:0:       class=0x060400 card=0x12341022 chip=0x15121022 rev=0x00 hdr=0x01
    vendor     = 'Advanced Micro Devices [AMD]'
    device     = 'Family 14h Processor Root Port'
    class      = bridge
    subclass   = PCI-PCI
    cap 01[50] = powerspec 3  supports D0 D3  current D0
    cap 10[58] = PCI-Express 2 root port slot max data 128(128) link x1(x1)
                 speed 2.5(5.0) ASPM L0s/L1(L0s/L1)
    cap 05[a0] = MSI supports 1 message, 64 bit
    cap 0d[b0] = PCI Bridge card=0x12341022
    cap 08[b8] = HT MSI fixed address window enabled at 0xfee00000
pcib2@pci0:0:5:0:       class=0x060400 card=0x12341022 chip=0x15131022 rev=0x00 hdr=0x01
    vendor     = 'Advanced Micro Devices [AMD]'
    device     = 'Family 14h Processor Root Port'
    class      = bridge
    subclass   = PCI-PCI
    cap 01[50] = powerspec 3  supports D0 D3  current D0
    cap 10[58] = PCI-Express 2 root port slot max data 128(128) link x1(x1)
                 speed 2.5(5.0) ASPM L0s/L1(L0s/L1)
    cap 05[a0] = MSI supports 1 message, 64 bit
    cap 0d[b0] = PCI Bridge card=0x12341022
    cap 08[b8] = HT MSI fixed address window enabled at 0xfee00000
pcib3@pci0:0:6:0:       class=0x060400 card=0x12341022 chip=0x15141022 rev=0x00 hdr=0x01
    vendor     = 'Advanced Micro Devices [AMD]'
    device     = 'Family 14h Processor Root Port'
    class      = bridge
    subclass   = PCI-PCI
    cap 01[50] = powerspec 3  supports D0 D3  current D0
    cap 10[58] = PCI-Express 2 root port slot max data 128(128) link x1(x1)
                 speed 2.5(5.0) ASPM L0s/L1(L0s/L1)
    cap 05[a0] = MSI supports 1 message, 64 bit
    cap 0d[b0] = PCI Bridge card=0x12341022
    cap 08[b8] = HT MSI fixed address window enabled at 0xfee00000
pcib4@pci0:0:7:0:       class=0x060400 card=0x12341022 chip=0x15151022 rev=0x00 hdr=0x01
    vendor     = 'Advanced Micro Devices [AMD]'
    device     = 'Family 14h Processor Root Port'
    class      = bridge
    subclass   = PCI-PCI
    cap 01[50] = powerspec 3  supports D0 D3  current D0
    cap 10[58] = PCI-Express 2 root port slot max data 128(128) link x1(x1)
                 speed 2.5(5.0) ASPM L1(L0s/L1)
    cap 05[a0] = MSI supports 1 message, 64 bit
    cap 0d[b0] = PCI Bridge card=0x12341022
    cap 08[b8] = HT MSI fixed address window enabled at 0xfee00000
ahci0@pci0:0:17:0:      class=0x010601 card=0x43911002 chip=0x43911002 rev=0x40 hdr=0x00
    vendor     = 'Advanced Micro Devices [AMD] nee ATI'
    device     = 'SB7x0/SB8x0/SB9x0 SATA Controller [AHCI mode]'
    class      = mass storage
    subclass   = SATA
    bar   [10] = type I/O Port, range 32, base 0x4020, size 8, enabled
    bar   [14] = type I/O Port, range 32, base 0x4040, size 4, enabled
    bar   [18] = type I/O Port, range 32, base 0x4028, size 8, enabled
    bar   [1c] = type I/O Port, range 32, base 0x4044, size 4, enabled
    bar   [20] = type I/O Port, range 32, base 0x4000, size 16, enabled
    bar   [24] = type Memory, range 32, base 0xfeb08000, size 1024, enabled
    cap 12[70] = SATA Index-Data Pair
    cap 13[a4] = PCI Advanced Features: FLR TP
ohci0@pci0:0:18:0:      class=0x0c0310 card=0x43971002 chip=0x43971002 rev=0x00 hdr=0x00
    vendor     = 'Advanced Micro Devices [AMD] nee ATI'
    device     = 'SB7x0/SB8x0/SB9x0 USB OHCI0 Controller'
    class      = serial bus
    subclass   = USB
    bar   [10] = type Memory, range 32, base 0xfeb04000, size 4096, enabled
ehci0@pci0:0:18:2:      class=0x0c0320 card=0x43961002 chip=0x43961002 rev=0x00 hdr=0x00
    vendor     = 'Advanced Micro Devices [AMD] nee ATI'
    device     = 'SB7x0/SB8x0/SB9x0 USB EHCI Controller'
    class      = serial bus
    subclass   = USB
    bar   [10] = type Memory, range 32, base 0xfeb08400, size 256, enabled
    cap 01[c0] = powerspec 2  supports D0 D1 D2 D3  current D0
    cap 0a[e4] = EHCI Debug Port at offset 0xe0 in map 0x14
ohci1@pci0:0:19:0:      class=0x0c0310 card=0x43971002 chip=0x43971002 rev=0x00 hdr=0x00
    vendor     = 'Advanced Micro Devices [AMD] nee ATI'
    device     = 'SB7x0/SB8x0/SB9x0 USB OHCI0 Controller'
    class      = serial bus
    subclass   = USB
    bar   [10] = type Memory, range 32, base 0xfeb05000, size 4096, enabled
ehci1@pci0:0:19:2:      class=0x0c0320 card=0x43961002 chip=0x43961002 rev=0x00 hdr=0x00
    vendor     = 'Advanced Micro Devices [AMD] nee ATI'
    device     = 'SB7x0/SB8x0/SB9x0 USB EHCI Controller'
    class      = serial bus
    subclass   = USB
    bar   [10] = type Memory, range 32, base 0xfeb08500, size 256, enabled
    cap 01[c0] = powerspec 2  supports D0 D1 D2 D3  current D0
    cap 0a[e4] = EHCI Debug Port at offset 0xe0 in map 0x14
none0@pci0:0:20:0:      class=0x0c0500 card=0x15101022 chip=0x43851002 rev=0x42 hdr=0x00
    vendor     = 'Advanced Micro Devices [AMD] nee ATI'
    device     = 'SBx00 SMBus Controller'
    class      = serial bus
    subclass   = SMBus
atapci0@pci0:0:20:1:    class=0x01018a card=0x439c1002 chip=0x439c1002 rev=0x40 hdr=0x00
    vendor     = 'Advanced Micro Devices [AMD] nee ATI'
    device     = 'SB7x0/SB8x0/SB9x0 IDE Controller'
    class      = mass storage
    subclass   = ATA
    bar   [20] = type I/O Port, range 32, base 0x4010, size 16, enabled
isab0@pci0:0:20:3:      class=0x060100 card=0x439d1002 chip=0x439d1002 rev=0x40 hdr=0x00
    vendor     = 'Advanced Micro Devices [AMD] nee ATI'
    device     = 'SB7x0/SB8x0/SB9x0 LPC host controller'
    class      = bridge
    subclass   = PCI-ISA
pcib5@pci0:0:20:4:      class=0x060401 card=0x00000000 chip=0x43841002 rev=0x40 hdr=0x01
    vendor     = 'Advanced Micro Devices [AMD] nee ATI'
    device     = 'SBx00 PCI to PCI Bridge'
    class      = bridge
    subclass   = PCI-PCI
ohci2@pci0:0:20:5:      class=0x0c0310 card=0x43991002 chip=0x43991002 rev=0x00 hdr=0x00
    vendor     = 'Advanced Micro Devices [AMD] nee ATI'
    device     = 'SB7x0/SB8x0/SB9x0 USB OHCI2 Controller'
    class      = serial bus
    subclass   = USB
    bar   [10] = type Memory, range 32, base 0xfeb06000, size 4096, enabled
pcib6@pci0:0:21:0:      class=0x060400 card=0x00001002 chip=0x43a01002 rev=0x00 hdr=0x01
    vendor     = 'Advanced Micro Devices [AMD] nee ATI'
    device     = 'SB700/SB800/SB900 PCI to PCI bridge (PCIE port 0)'
    class      = bridge
    subclass   = PCI-PCI
    cap 01[50] = powerspec 3  supports D0 D1 D2 D3  current D0
    cap 10[58] = PCI-Express 2 root port max data 128(128) link x16(x4)
                 speed undef(2.5) ASPM disabled(L0s/L1)
    cap 05[a0] = MSI supports 1 message, 64 bit
    cap 0d[b0] = PCI Bridge card=0x00001002
    cap 08[b8] = HT MSI fixed address window enabled at 0xfee00000
ohci3@pci0:0:22:0:      class=0x0c0310 card=0x43971002 chip=0x43971002 rev=0x00 hdr=0x00
    vendor     = 'Advanced Micro Devices [AMD] nee ATI'
    device     = 'SB7x0/SB8x0/SB9x0 USB OHCI0 Controller'
    class      = serial bus
    subclass   = USB
    bar   [10] = type Memory, range 32, base 0xfeb07000, size 4096, enabled
ehci2@pci0:0:22:2:      class=0x0c0320 card=0x43961002 chip=0x43961002 rev=0x00 hdr=0x00
    vendor     = 'Advanced Micro Devices [AMD] nee ATI'
    device     = 'SB7x0/SB8x0/SB9x0 USB EHCI Controller'
    class      = serial bus
    subclass   = USB
    bar   [10] = type Memory, range 32, base 0xfeb08600, size 256, enabled
    cap 01[c0] = powerspec 2  supports D0 D1 D2 D3  current D0
    cap 0a[e4] = EHCI Debug Port at offset 0xe0 in map 0x14
hostb1@pci0:0:24:0:     class=0x060000 card=0x00000000 chip=0x17001022 rev=0x43 hdr=0x00
    vendor     = 'Advanced Micro Devices [AMD]'
    device     = 'Family 12h/14h Processor Function 0'
    class      = bridge
    subclass   = HOST-PCI
hostb2@pci0:0:24:1:     class=0x060000 card=0x00000000 chip=0x17011022 rev=0x00 hdr=0x00
    vendor     = 'Advanced Micro Devices [AMD]'
    device     = 'Family 12h/14h Processor Function 1'
    class      = bridge
    subclass   = HOST-PCI
hostb3@pci0:0:24:2:     class=0x060000 card=0x00000000 chip=0x17021022 rev=0x00 hdr=0x00
    vendor     = 'Advanced Micro Devices [AMD]'
    device     = 'Family 12h/14h Processor Function 2'
    class      = bridge
    subclass   = HOST-PCI
hostb4@pci0:0:24:3:     class=0x060000 card=0x00000000 chip=0x17031022 rev=0x00 hdr=0x00
    vendor     = 'Advanced Micro Devices [AMD]'
    device     = 'Family 12h/14h Processor Function 3'
    class      = bridge
    subclass   = HOST-PCI
    cap 0f[f0] = unknown
hostb5@pci0:0:24:4:     class=0x060000 card=0x00000000 chip=0x17041022 rev=0x00 hdr=0x00
    vendor     = 'Advanced Micro Devices [AMD]'
    device     = 'Family 12h/14h Processor Function 4'
    class      = bridge
    subclass   = HOST-PCI
hostb6@pci0:0:24:5:     class=0x060000 card=0x00000000 chip=0x17181022 rev=0x00 hdr=0x00
    vendor     = 'Advanced Micro Devices [AMD]'
    device     = 'Family 12h/14h Processor Function 6'
    class      = bridge
    subclass   = HOST-PCI
hostb7@pci0:0:24:6:     class=0x060000 card=0x00000000 chip=0x17161022 rev=0x00 hdr=0x00
    vendor     = 'Advanced Micro Devices [AMD]'
    device     = 'Family 12h/14h Processor Function 5'
    class      = bridge
    subclass   = HOST-PCI
hostb8@pci0:0:24:7:     class=0x060000 card=0x00000000 chip=0x17191022 rev=0x00 hdr=0x00
    vendor     = 'Advanced Micro Devices [AMD]'
    device     = 'Family 12h/14h Processor Function 7'
    class      = bridge
    subclass   = HOST-PCI
re0@pci0:1:0:0: class=0x020000 card=0x012310ec chip=0x816810ec rev=0x06 hdr=0x00
    vendor     = 'Realtek Semiconductor Co., Ltd.'
    device     = 'RTL8111/8168B PCI Express Gigabit Ethernet controller'
    class      = network
    subclass   = ethernet
    bar   [10] = type I/O Port, range 32, base 0x1000, size 256, enabled
    bar   [18] = type Memory, range 64, base 0xfe500000, size 4096, enabled
    bar   [20] = type Prefetchable Memory, range 64, base 0xfe400000, size 16384, enabled
    cap 01[40] = powerspec 3  supports D0 D1 D2 D3  current D0
    cap 05[50] = MSI supports 1 message, 64 bit
    cap 10[70] = PCI-Express 2 endpoint IRQ 1 max data 128(128) link x1(x1)
                 speed 2.5(2.5) ASPM disabled(L0s/L1)
    cap 11[b0] = MSI-X supports 4 messages, enabled
                 Table in map 0x20[0x0], PBA in map 0x20[0x800]
    cap 03[d0] = VPD
re1@pci0:2:0:0: class=0x020000 card=0x012310ec chip=0x816810ec rev=0x06 hdr=0x00
    vendor     = 'Realtek Semiconductor Co., Ltd.'
    device     = 'RTL8111/8168B PCI Express Gigabit Ethernet controller'
    class      = network
    subclass   = ethernet
    bar   [10] = type I/O Port, range 32, base 0x2000, size 256, enabled
    bar   [18] = type Memory, range 64, base 0xfe700000, size 4096, enabled
    bar   [20] = type Prefetchable Memory, range 64, base 0xfe600000, size 16384, enabled
    cap 01[40] = powerspec 3  supports D0 D1 D2 D3  current D0
    cap 05[50] = MSI supports 1 message, 64 bit
    cap 10[70] = PCI-Express 2 endpoint IRQ 1 max data 128(128) link x1(x1)
                 speed 2.5(2.5) ASPM disabled(L0s/L1)
    cap 11[b0] = MSI-X supports 4 messages, enabled
                 Table in map 0x20[0x0], PBA in map 0x20[0x800]
    cap 03[d0] = VPD
re2@pci0:3:0:0: class=0x020000 card=0x012310ec chip=0x816810ec rev=0x06 hdr=0x00
    vendor     = 'Realtek Semiconductor Co., Ltd.'
    device     = 'RTL8111/8168B PCI Express Gigabit Ethernet controller'
    class      = network
    subclass   = ethernet
    bar   [10] = type I/O Port, range 32, base 0x3000, size 256, enabled
    bar   [18] = type Memory, range 64, base 0xfe900000, size 4096, enabled
    bar   [20] = type Prefetchable Memory, range 64, base 0xfe800000, size 16384, enabled
    cap 01[40] = powerspec 3  supports D0 D1 D2 D3  current D0
    cap 05[50] = MSI supports 1 message, 64 bit
    cap 10[70] = PCI-Express 2 endpoint IRQ 1 max data 128(128) link x1(x1)
                 speed 2.5(2.5) ASPM disabled(L0s/L1)
    cap 11[b0] = MSI-X supports 4 messages, enabled
                 Table in map 0x20[0x0], PBA in map 0x20[0x800]
    cap 03[d0] = VPD
ath0@pci0:4:0:0:        class=0x028000 card=0x3099168c chip=0x002a168c rev=0x01 hdr=0x00
    vendor     = 'Atheros Communications Inc.'
    device     = 'AR928X Wireless Network Adapter (PCI-Express)'
    class      = network
    bar   [10] = type Memory, range 64, base 0xfea00000, size 65536, enabled
    cap 01[40] = powerspec 2  supports D0 D1 D3  current D0
    cap 05[50] = MSI supports 1 message
    cap 10[60] = PCI-Express 1 legacy endpoint max data 128(128) link x1(x1)
                 speed 2.5(2.5) ASPM L1(L1)
    cap 11[90] = MSI-X supports 1 message
                 Table in map 0x10[0x0], PBA in map 0x10[0x0]
```
