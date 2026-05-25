---
title: PC Engines APU2C4
---
## dmesg

```
Copyright (c) 1992-2019 The FreeBSD Project.
Copyright (c) 1979, 1980, 1983, 1986, 1988, 1989, 1991, 1992, 1993, 1994
        The Regents of the University of California. All rights reserved.
FreeBSD is a registered trademark of The FreeBSD Foundation.
FreeBSD 12.0-STABLE #0 r348342M: Wed May 29 10:36:14 CEST 2019
    olivier@lame4.bsdrp.net:/usr/local/BSDRP/workdir/BSDRPstable.amd64/usr/local/BSDRP/BSDRPstable/FreeBSD/src/amd64.amd64/sys/amd64 amd64
FreeBSD clang version 8.0.0 (tags/RELEASE_800/final 356365) (based on LLVM 8.0.0)
VT(vga): text 80x25
CPU: AMD GX-412TC SOC                                (998.15-MHz K8-class CPU)
  Origin="AuthenticAMD"  Id=0x730f01  Family=0x16  Model=0x30  Stepping=1
  Features=0x178bfbff<FPU,VME,DE,PSE,TSC,MSR,PAE,MCE,CX8,APIC,SEP,MTRR,PGE,MCA,CMOV,PAT,PSE36,CLFLUSH,MMX,FXSR,SSE,SSE2,HTT>
  Features2=0x3ed8220b<SSE3,PCLMULQDQ,MON,SSSE3,CX16,SSE4.1,SSE4.2,MOVBE,POPCNT,AESNI,XSAVE,OSXSAVE,AVX,F16>
  AMD Features=0x2e500800<SYSCALL,NX,MMX+,FFXSR,Page1GB,RDTSCP,LM>
  AMD Features2=0x1d4037ff<LAHF,CMP,SVM,ExtAPIC,CR8,ABM,SSE4A,MAS,Prefetch,OSVW,IBS,SKINIT,WDT,Topology,PNXC,DBE,PTSC,PL2I>
  Structured Extended Features=0x8<BMI1>
  XSAVE Features=0x1<XSAVEOPT>
  SVM: NP,NRIP,AFlush,DAssist,NAsids=8
  TSC: P-state invariant, performance statistics
real memory  = 4815060992 (4592 MB)
avail memory = 4091179008 (3901 MB)
Event timer "LAPIC" quality 600
ACPI APIC Table: <CORE   COREBOOT>
FreeBSD/SMP: Multiprocessor System Detected: 4 CPUs
FreeBSD/SMP: 1 package(s) x 4 core(s)
random: unblocking device.
ioapic1: Changing APIC ID to 5
ioapic0 <Version 2.1> irqs 0-23 on motherboard
ioapic1 <Version 2.1> irqs 24-55 on motherboard
Launching APs: 1 2 3
Timecounter "TSC" frequency 998148892 Hz quality 1000
random: entropy device external interface
000.000015 [4254] netmap_init               netmap: loaded module
nexus0
vtvga0: <VT VGA driver> on motherboard
cryptosoft0: <software crypto> on motherboard
acpi0: <CORE COREBOOT> on motherboard
acpi0: Power Button (fixed)
cpu0: <ACPI CPU> on acpi0
atrtc0: <AT realtime clock> port 0x70-0x71 irq 8 on acpi0
atrtc0: registered as a time-of-day clock, resolution 1.000000s
Event timer "RTC" frequency 32768 Hz quality 0
attimer0: <AT timer> port 0x40-0x43 irq 0 on acpi0
Timecounter "i8254" frequency 1193182 Hz quality 0
Event timer "i8254" frequency 1193182 Hz quality 100
hpet0: <High Precision Event Timer> iomem 0xfed00000-0xfed003ff on acpi0
Timecounter "HPET" frequency 14318180 Hz quality 950
Timecounter "ACPI-safe" frequency 3579545 Hz quality 850
acpi_timer0: <32-bit timer at 3.579545MHz> port 0x818-0x81b on acpi0
acpi_button0: <Power Button> on acpi0
pcib0: <ACPI Host-PCI bridge> port 0xcf8-0xcff on acpi0
pci0: <ACPI PCI bus> on pcib0
pcib1: <ACPI PCI-PCI bridge> at device 2.2 on pci0
pcib1: failed to allocate initial I/O port window: 0x1000-0x1fff
pci1: <ACPI PCI bus> on pcib1
igb0: <Intel(R) PRO/1000 PCI-Express Network Driver> mem 0xfe600000-0xfe61ffff,0xfe620000-0xfe623fff at device 0.0 on pci1
igb0: Using 1024 tx descriptors and 1024 rx descriptors
igb0: Using 4 rx queues 4 tx queues
igb0: Using MSI-X interrupts with 5 vectors
igb0: Ethernet address: 00:0d:b9:41:ca:3c
igb0: netmap queues/slots: TX 4/1024, RX 4/1024
pcib2: <ACPI PCI-PCI bridge> at device 2.3 on pci0
pci2: <ACPI PCI bus> on pcib2
igb1: <Intel(R) PRO/1000 PCI-Express Network Driver> port 0x2000-0x201f mem 0xfe700000-0xfe71ffff,0xfe720000-0xfe723fff at device 0.0 on pci2
igb1: Using 1024 tx descriptors and 1024 rx descriptors
igb1: Using 4 rx queues 4 tx queues
igb1: Using MSI-X interrupts with 5 vectors
igb1: Ethernet address: 00:0d:b9:41:ca:3d
igb1: netmap queues/slots: TX 4/1024, RX 4/1024
pcib3: <ACPI PCI-PCI bridge> at device 2.4 on pci0
pci3: <ACPI PCI bus> on pcib3
igb2: <Intel(R) PRO/1000 PCI-Express Network Driver> port 0x3000-0x301f mem 0xfe800000-0xfe81ffff,0xfe820000-0xfe823fff at device 0.0 on pci3
igb2: Using 1024 tx descriptors and 1024 rx descriptors
igb2: Using 4 rx queues 4 tx queues
igb2: Using MSI-X interrupts with 5 vectors
igb2: Ethernet address: 00:0d:b9:41:ca:3e
igb2: netmap queues/slots: TX 4/1024, RX 4/1024
pci0: <encrypt/decrypt> at device 8.0 (no driver attached)
xhci0: <AMD FCH USB 3.0 controller> mem 0xfeb22000-0xfeb23fff at device 16.0 on pci0
xhci0: 32 bytes context size, 64-bit DMA
xhci0: Unable to map MSI-X table
usbus0 on xhci0
usbus0: 5.0Gbps Super Speed USB v3.0
ahci0: <AMD Hudson-2 AHCI SATA controller> port 0x4010-0x4017,0x4020-0x4023,0x4018-0x401f,0x4024-0x4027,0x4000-0x400f mem 0xfeb25000-0xfeb25
3ff at device 17.0 on pci0
ahci0: AHCI v1.30 with 2 6Gbps ports, Port Multiplier supported with FBS
ahcich0: <AHCI channel> at channel 0 on ahci0
ahcich1: <AHCI channel> at channel 1 on ahci0
ehci0: <AMD FCH USB 2.0 controller> mem 0xfeb25400-0xfeb254ff at device 19.0 on pci0
usbus1: EHCI version 1.0
usbus1 on ehci0
usbus1: 480Mbps High Speed USB v2.0
isab0: <PCI-ISA bridge> at device 20.3 on pci0
isa0: <ISA bus> on isab0
sdhci_pci0: <Generic SD HCI> mem 0xfeb25500-0xfeb255ff at device 20.7 on pci0
sdhci_pci0: 1 slot(s) allocated
uart0: <16550 or compatible> port 0x3f8-0x3ff irq 4 flags 0x10 on acpi0
uart0: console (115200,n,8,1)
orm0: <ISA Option ROMs> at iomem 0xc0000-0xc0fff,0xef000-0xeffff pnpid ORM0000 on isa0
uart1: <16550 or compatible> at port 0x2f8 irq 3 on isa0
hwpstate0: <Cool`n'Quiet 2.0> on cpu0
Timecounters tick every 1.000 msec
ugen1.1: <AMD EHCI root HUB> at usbus1
uhub0: <AMD EHCI root HUB, class 9/0, rev 2.00/1.00, addr 1> on usbus1
ugen0.1: <0x1022 XHCI root HUB> at usbus0
ada0 at ahcich0 bus 0 scbus0 target 0 lun 0
ada0: <SATA SSD S9FM02.8> ACS-3 ATA SATA 3.x device
ada0: Serial Number 1B060766160804907006
ada0: 600.000MB/s transfers (SATA 3.x, UDMA6, PIO 8192bytes)
ada0: Command Queueing enabled
ada0: 15272MB (31277232 512 byte sectors)
uhub1: <0x1022 XHCI root HUB, class 9/0, rev 3.00/1.00, addr 1> on usbus0
Trying to mount root from ufs:/dev/ufs/BSDRPs2a [ro]...
uhub1: 4 ports with 4 removable, self powered
uhub0: 2 ports with 2 removable, self powered
lo0: link state changed to UP
ugen1.2: <vendor 0x0438 product 0x7900> at usbus1
uhub2 on uhub0
uhub2: <vendor 0x0438 product 0x7900, class 9/0, rev 2.00/0.18, addr 2> on usbus1
uhub2: 4 ports with 4 removable, self powered
igb0: link state changed to UP
igb1: link state changed to UP
igb2: link state changed to UP
intsmb0: <AMD FCH SMBus Controller> at device 20.0 on pci0
smbus0: <System Management Bus> on intsmb0
aesni0: <AES-CBC,AES-XTS,AES-GCM,AES-ICM> on motherboard
```

## pciconf

```
hostb0@pci0:0:0:0:      class=0x060000 card=0x15661022 chip=0x15661022 rev=0x00 hdr=0x00
    vendor     = 'Advanced Micro Devices, Inc. [AMD]'
    class      = bridge
    subclass   = HOST-PCI
hostb1@pci0:0:2:0:      class=0x060000 card=0x00000000 chip=0x156b1022 rev=0x00 hdr=0x00
    vendor     = 'Advanced Micro Devices, Inc. [AMD]'
    class      = bridge
    subclass   = HOST-PCI
pcib1@pci0:0:2:2:       class=0x060400 card=0x12341022 chip=0x14391022 rev=0x00 hdr=0x01
    vendor     = 'Advanced Micro Devices, Inc. [AMD]'
    device     = 'Family 16h Processor Functions 5:1'
    class      = bridge
    subclass   = PCI-PCI
    cap 01[50] = powerspec 3  supports D0 D3  current D0
    cap 10[58] = PCI-Express 2 root port slot max data 256(512) RO NS link x1(x1)
                 speed 2.5(5.0) ASPM disabled(L0s/L1)
    cap 05[a0] = MSI supports 1 message, 64 bit
    cap 0d[b0] = PCI Bridge card=0x12341022
    cap 08[b8] = HT MSI fixed address window enabled at 0xfee00000
pcib2@pci0:0:2:3:       class=0x060400 card=0x12341022 chip=0x14391022 rev=0x00 hdr=0x01
    vendor     = 'Advanced Micro Devices, Inc. [AMD]'
    device     = 'Family 16h Processor Functions 5:1'
    class      = bridge
    subclass   = PCI-PCI
    cap 01[50] = powerspec 3  supports D0 D3  current D0
    cap 10[58] = PCI-Express 2 root port slot max data 256(512) RO NS link x1(x1)
                 speed 2.5(5.0) ASPM disabled(L0s/L1)
    cap 05[a0] = MSI supports 1 message, 64 bit
    cap 0d[b0] = PCI Bridge card=0x12341022
    cap 08[b8] = HT MSI fixed address window enabled at 0xfee00000
pcib3@pci0:0:2:4:       class=0x060400 card=0x12341022 chip=0x14391022 rev=0x00 hdr=0x01
    vendor     = 'Advanced Micro Devices, Inc. [AMD]'
    device     = 'Family 16h Processor Functions 5:1'
    class      = bridge
    subclass   = PCI-PCI
    cap 01[50] = powerspec 3  supports D0 D3  current D0
    cap 10[58] = PCI-Express 2 root port slot max data 256(512) RO NS link x1(x1)
                 speed 2.5(5.0) ASPM disabled(L0s/L1)
    cap 05[a0] = MSI supports 1 message, 64 bit
    cap 0d[b0] = PCI Bridge card=0x12341022
    cap 08[b8] = HT MSI fixed address window enabled at 0xfee00000
none0@pci0:0:8:0:       class=0x108000 card=0x15371022 chip=0x15371022 rev=0x00 hdr=0x00
    vendor     = 'Advanced Micro Devices, Inc. [AMD]'
    class      = encrypt/decrypt
    bar   [10] = type Prefetchable Memory, range 64, base 0xfeb00000, size 131072, enabled
    bar   [18] = type Memory, range 32, base 0xfe900000, size 1048576, enabled
    bar   [1c] = type Memory, range 32, base 0xfeb24000, size 4096, enabled
    bar   [20] = type Memory, range 32, base 0xfea00000, size 1048576, enabled
    bar   [24] = type Memory, range 32, base 0xfeb20000, size 8192, enabled
    cap 11[50] = MSI-X supports 2 messages
                 Table in map 0x24[0x0], PBA in map 0x24[0x1000]
    cap 08[5c] = HT MSI fixed address window enabled at 0xfee00000
    cap 01[60] = powerspec 3  supports D0 D3  current D0
xhci0@pci0:0:16:0:      class=0x0c0330 card=0x14101022 chip=0x78141022 rev=0x11 hdr=0x00
    vendor     = 'Advanced Micro Devices, Inc. [AMD]'
    device     = 'FCH USB XHCI Controller'
    class      = serial bus
    subclass   = USB
    bar   [10] = type Memory, range 64, base 0xfeb22000, size 8192, enabled
    cap 01[50] = powerspec 3  supports D0 D3  current D0
    cap 05[70] = MSI supports 8 messages, 64 bit enabled with 1 message
    cap 11[90] = MSI-X supports 8 messages
                 Table in map 0x10[0x1000], PBA in map 0x10[0x1080]
    cap 10[a0] = PCI-Express 2 root endpoint max data 128(128) NS link x0(x0)
ahci0@pci0:0:17:0:      class=0x01018f card=0x78001022 chip=0x78001022 rev=0x40 hdr=0x00
    vendor     = 'Advanced Micro Devices, Inc. [AMD]'
    device     = 'FCH SATA Controller [IDE mode]'
    class      = mass storage
    subclass   = ATA
    bar   [10] = type I/O Port, range 32, base 0x4010, size 8, enabled
    bar   [14] = type I/O Port, range 32, base 0x4020, size 4, enabled
    bar   [18] = type I/O Port, range 32, base 0x4018, size 8, enabled
    bar   [1c] = type I/O Port, range 32, base 0x4024, size 4, enabled
    bar   [20] = type I/O Port, range 32, base 0x4000, size 16, enabled
    bar   [24] = type Memory, range 32, base 0xfeb25000, size 1024, enabled
    cap 01[60] = powerspec 3  supports D0 D3  current D0
    cap 12[70] = SATA Index-Data Pair
ehci0@pci0:0:19:0:      class=0x0c0320 card=0x78081022 chip=0x78081022 rev=0x39 hdr=0x00
    vendor     = 'Advanced Micro Devices, Inc. [AMD]'
    device     = 'FCH USB EHCI Controller'
    class      = serial bus
    subclass   = USB
    bar   [10] = type Memory, range 32, base 0xfeb25400, size 256, enabled
    cap 01[c0] = powerspec 2  supports D0 D1 D2 D3  current D0
    cap 0a[e4] = EHCI Debug Port at offset 0xe0 in map 0x14
none1@pci0:0:20:0:      class=0x0c0500 card=0x780b1022 chip=0x780b1022 rev=0x42 hdr=0x00
    vendor     = 'Advanced Micro Devices, Inc. [AMD]'
    device     = 'FCH SMBus Controller'
    class      = serial bus
    subclass   = SMBus
isab0@pci0:0:20:3:      class=0x060100 card=0x780e1022 chip=0x780e1022 rev=0x11 hdr=0x00
    vendor     = 'Advanced Micro Devices, Inc. [AMD]'
    device     = 'FCH LPC Bridge'
    class      = bridge
    subclass   = PCI-ISA
sdhci_pci0@pci0:0:20:7: class=0x080501 card=0x78061022 chip=0x78131022 rev=0x01 hdr=0x00
    vendor     = 'Advanced Micro Devices, Inc. [AMD]'
    device     = 'FCH SD Flash Controller'
    class      = base peripheral
    subclass   = SD host controller
    bar   [10] = type Memory, range 64, base 0xfeb25500, size 256, enabled
hostb2@pci0:0:24:0:     class=0x060000 card=0x00000000 chip=0x15801022 rev=0x00 hdr=0x00
    vendor     = 'Advanced Micro Devices, Inc. [AMD]'
    class      = bridge
    subclass   = HOST-PCI
hostb3@pci0:0:24:1:     class=0x060000 card=0x00000000 chip=0x15811022 rev=0x00 hdr=0x00
    vendor     = 'Advanced Micro Devices, Inc. [AMD]'
    class      = bridge
    subclass   = HOST-PCI
hostb4@pci0:0:24:2:     class=0x060000 card=0x00000000 chip=0x15821022 rev=0x00 hdr=0x00
    vendor     = 'Advanced Micro Devices, Inc. [AMD]'
    class      = bridge
    subclass   = HOST-PCI
hostb5@pci0:0:24:3:     class=0x060000 card=0x00000000 chip=0x15831022 rev=0x00 hdr=0x00
    vendor     = 'Advanced Micro Devices, Inc. [AMD]'
    class      = bridge
    subclass   = HOST-PCI
    cap 0f[f0] = unknown
hostb6@pci0:0:24:4:     class=0x060000 card=0x00000000 chip=0x15841022 rev=0x00 hdr=0x00
    vendor     = 'Advanced Micro Devices, Inc. [AMD]'
    class      = bridge
    subclass   = HOST-PCI
hostb7@pci0:0:24:5:     class=0x060000 card=0x00000000 chip=0x15851022 rev=0x00 hdr=0x00
    vendor     = 'Advanced Micro Devices, Inc. [AMD]'
    class      = bridge
    subclass   = HOST-PCI
igb0@pci0:1:0:0:        class=0x020000 card=0x00008086 chip=0x157b8086 rev=0x03 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = 'I210 Gigabit Network Connection'
    class      = network
    subclass   = ethernet
    bar   [10] = type Memory, range 32, base 0xfe600000, size 131072, enabled
    bar   [18] = type I/O Port, range 32, base 0x1000, size 32, disabled
    bar   [1c] = type Memory, range 32, base 0xfe620000, size 16384, enabled
    cap 01[40] = powerspec 3  supports D0 D3  current D0
    cap 05[50] = MSI supports 1 message, 64 bit, vector masks
    cap 11[70] = MSI-X supports 5 messages, enabled
                 Table in map 0x1c[0x0], PBA in map 0x1c[0x2000]
    cap 10[a0] = PCI-Express 2 endpoint max data 256(512) FLR RO NS link x1(x1)
                 speed 2.5(2.5) ASPM disabled(L0s/L1)
igb1@pci0:2:0:0:        class=0x020000 card=0x00008086 chip=0x157b8086 rev=0x03 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = 'I210 Gigabit Network Connection'
    class      = network
    subclass   = ethernet
    bar   [10] = type Memory, range 32, base 0xfe700000, size 131072, enabled
    bar   [18] = type I/O Port, range 32, base 0x2000, size 32, enabled
    bar   [1c] = type Memory, range 32, base 0xfe720000, size 16384, enabled
    cap 01[40] = powerspec 3  supports D0 D3  current D0
    cap 05[50] = MSI supports 1 message, 64 bit, vector masks
    cap 11[70] = MSI-X supports 5 messages, enabled
                 Table in map 0x1c[0x0], PBA in map 0x1c[0x2000]
    cap 10[a0] = PCI-Express 2 endpoint max data 256(512) FLR RO NS link x1(x1)
                 speed 2.5(2.5) ASPM disabled(L0s/L1)
igb2@pci0:3:0:0:        class=0x020000 card=0x00008086 chip=0x157b8086 rev=0x03 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = 'I210 Gigabit Network Connection'
    class      = network
    subclass   = ethernet
    bar   [10] = type Memory, range 32, base 0xfe800000, size 131072, enabled
    bar   [18] = type I/O Port, range 32, base 0x3000, size 32, enabled
    bar   [1c] = type Memory, range 32, base 0xfe820000, size 16384, enabled
    cap 01[40] = powerspec 3  supports D0 D3  current D0
    cap 05[50] = MSI supports 1 message, 64 bit, vector masks
    cap 11[70] = MSI-X supports 5 messages, enabled
                 Table in map 0x1c[0x0], PBA in map 0x1c[0x2000]
    cap 10[a0] = PCI-Express 2 endpoint max data 256(512) FLR RO NS link x1(x1)
                 speed 2.5(2.5) ASPM disabled(L0s/L1)
```
