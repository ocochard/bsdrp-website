---
title: SuperServer 5018A-FTN4
---
## dmesg

```
Copyright (c) 1992-2018 The FreeBSD Project.                                                                                                                                        [151/841]
Copyright (c) 1979, 1980, 1983, 1986, 1988, 1989, 1991, 1992, 1993, 1994
        The Regents of the University of California. All rights reserved.
FreeBSD is a registered trademark of The FreeBSD Foundation.
FreeBSD 11.1-STABLE  r332078M amd64
FreeBSD clang version 6.0.0 (tags/RELEASE_600/final 326565) (based on LLVM 6.0.0)
VT(vga): text 80x25
CPU: Intel(R) Atom(TM) CPU  C2758  @ 2.40GHz (2400.06-MHz K8-class CPU)
  Origin="GenuineIntel"  Id=0x406d8  Family=0x6  Model=0x4d  Stepping=8
  Features=0xbfebfbff<FPU,VME,DE,PSE,TSC,MSR,PAE,MCE,CX8,APIC,SEP,MTRR,PGE,MCA,CMOV,PAT,PSE36,CLFLUSH,DTS,ACPI,MMX,FXSR,SSE,SSE2,SS,HTT,TM,PBE>
  Features2=0x43d8e3bf<SSE3,PCLMULQDQ,DTES64,MON,DS_CPL,VMX,EST,TM2,SSSE3,CX16,xTPR,PDCM,SSE4.1,SSE4.2,MOVBE,POPCNT,TSCDLT,AESNI,RDRAND>
  AMD Features=0x28100800<SYSCALL,NX,RDTSCP,LM>
  AMD Features2=0x101<LAHF,Prefetch>
  Structured Extended Features=0x2282<TSCADJ,SMEP,ERMS,NFPUSG>
  VT-x: PAT,HLT,MTF,PAUSE,EPT,UG,VPID
  TSC: P-state invariant, performance statistics
real memory  = 8589934592 (8192 MB)
avail memory = 8205664256 (7825 MB)
Event timer "LAPIC" quality 600
ACPI APIC Table: <INTEL  TIANO   >
WARNING: L1 data cache covers less APIC IDs than a core
0 < 1
FreeBSD/SMP: Multiprocessor System Detected: 8 CPUs
FreeBSD/SMP: 1 package(s) x 8 core(s)
WARNING: VIMAGE (virtualized network stack) is a highly experimental feature.
ioapic0 <Version 2.0> irqs 0-23 on motherboard
SMP: AP CPU #1 Launched!
SMP: AP CPU #3 Launched!
SMP: AP CPU #2 Launched!
SMP: AP CPU #6 Launched!
SMP: AP CPU #7 Launched!
SMP: AP CPU #4 Launched!
SMP: AP CPU #5 Launched!
Timecounter "TSC-low" frequency 1200028944 Hz quality 1000
random: entropy device external interface
netmap: loaded module
random: registering fast source Intel Secure Key RNG
random: fast provider: "Intel Secure Key RNG"
nexus0
vtvga0: <VT VGA driver> on motherboard
cryptosoft0: <software crypto> on motherboard
acpi0: <ALASKA A M I > on motherboard
acpi0: Power Button (fixed)
cpu0: <ACPI CPU> on acpi0
cpu1: <ACPI CPU> on acpi0
cpu2: <ACPI CPU> on acpi0
cpu3: <ACPI CPU> on acpi0
cpu4: <ACPI CPU> on acpi0
cpu5: <ACPI CPU> on acpi0
cpu6: <ACPI CPU> on acpi0
cpu7: <ACPI CPU> on acpi0
hpet0: <High Precision Event Timer> iomem 0xfed00000-0xfed003ff on acpi0
Timecounter "HPET" frequency 14318180 Hz quality 950
Event timer "HPET" frequency 14318180 Hz quality 350
Event timer "HPET1" frequency 14318180 Hz quality 340
Event timer "HPET2" frequency 14318180 Hz quality 340
atrtc0: <AT realtime clock> port 0x70-0x77 irq 8 on acpi0
atrtc0: Warning: Couldn't map I/O.
atrtc0: registered as a time-of-day clock, resolution 1.000000s
Event timer "RTC" frequency 32768 Hz quality 0
attimer0: <AT timer> port 0x40-0x43,0x50-0x53 irq 0 on acpi0
Timecounter "i8254" frequency 1193182 Hz quality 0
Event timer "i8254" frequency 1193182 Hz quality 100
Timecounter "ACPI-safe" frequency 3579545 Hz quality 850
acpi_timer0: <24-bit timer at 3.579545MHz> port 0x408-0x40b on acpi0
pcib0: <ACPI Host-PCI bridge> port 0xcf8-0xcff on acpi0
pcib0: _OSC returned error 0x10
pci0: <ACPI PCI bus> on pcib0
pcib1: <ACPI PCI-PCI bridge> mem 0xdf2e0000-0xdf2fffff irq 16 at device 1.0 on pci0
pci1: <ACPI PCI bus> on pcib1
pcib2: <ACPI PCI-PCI bridge> at device 0.0 on pci1
pci2: <ACPI PCI bus> on pcib2
vgapci0: <VGA-compatible display> port 0xd000-0xd07f mem 0xde000000-0xdeffffff,0xdf000000-0xdf01ffff irq 16 at device 0.0 on pci2
vgapci0: Boot video device
pcib3: <ACPI PCI-PCI bridge> mem 0xdf2c0000-0xdf2dffff irq 16 at device 2.0 on pci0
pci3: <ACPI PCI bus> on pcib3
xhci0: <XHCI (generic) USB 3.0 controller> mem 0xdf100000-0xdf101fff irq 17 at device 0.0 on pci3
xhci0: 64 bytes context size, 32-bit DMA
xhci0: Unable to map MSI-X table
usbus0 on xhci0
usbus0: 5.0Gbps Super Speed USB v3.0
pcib4: <ACPI PCI-PCI bridge> mem 0xdf2a0000-0xdf2bffff irq 20 at device 3.0 on pci0
pci4: <ACPI PCI bus> on pcib4
ix0: <Intel(R) PRO/10GbE PCI-Express Network Driver, Version - 3.2.12-k> port 0xc020-0xc03f mem 0xdfe80000-0xdfefffff,0xdff04000-0xdff07fff irq 22 at device 0.0 on pci4
ix0: Using MSI-X interrupts with 9 vectors
WARNING: Intel (R) Network Connections are quality tested using Intel (R) Ethernet Optics. Using untested modules is not supported and may cause unstable operation or damage to the module o
r the adapter. Intel Corporation is not responsible for any harm caused by using untested modules.
ix0: Ethernet address: 90:e2:ba:84:20:38
WARNING: Intel (R) Network Connections are quality tested using Intel (R) Ethernet Optics. Using untested modules is not supported and may cause unstable operation or damage to the module o
r the adapter. Intel Corporation is not responsible for any harm caused by using untested modules.
ix0: PCI Express Bus: Speed 5.0GT/s Width x8
ix0: netmap queues/slots: TX 8/2048, RX 8/2048
ix1: <Intel(R) PRO/10GbE PCI-Express Network Driver, Version - 3.2.12-k> port 0xc000-0xc01f mem 0xdfe00000-0xdfe7ffff,0xdff00000-0xdff03fff irq 23 at device 0.1 on pci4
ix1: Using MSI-X interrupts with 9 vectors
WARNING: Intel (R) Network Connections are quality tested using Intel (R) Ethernet Optics. Using untested modules is not supported and may cause unstable operation or damage to the module o
r the adapter. Intel Corporation is not responsible for any harm caused by using untested modules.
ix1: Ethernet address: 90:e2:ba:84:20:39
WARNING: Intel (R) Network Connections are quality tested using Intel (R) Ethernet Optics. Using untested modules is not supported and may cause unstable operation or damage to the module o
r the adapter. Intel Corporation is not responsible for any harm caused by using untested modules.
ix1: PCI Express Bus: Speed 5.0GT/s Width x8
ix1: netmap queues/slots: TX 8/2048, RX 8/2048
pci0: <processor> at device 11.0 (no driver attached)
pci0: <base peripheral, IOMMU> at device 15.0 (no driver attached)
igb0: <Intel(R) PRO/1000 Network Connection, Version - 2.5.3-k> port 0xe0c0-0xe0df mem 0xdf260000-0xdf27ffff,0xdf30c000-0xdf30ffff irq 20 at device 20.0 on pci0
igb0: Using MSIX interrupts with 9 vectors
igb0: Ethernet address: 0c:c4:7a:da:3c:10
igb0: Bound queue 0 to cpu 0
igb0: Bound queue 1 to cpu 1
igb0: Bound queue 2 to cpu 2
igb0: Bound queue 3 to cpu 3
igb0: Bound queue 4 to cpu 4
igb0: Bound queue 5 to cpu 5
igb0: Bound queue 6 to cpu 6
igb0: Bound queue 7 to cpu 7
igb0: netmap queues/slots: TX 8/1024, RX 8/1024
igb1: <Intel(R) PRO/1000 Network Connection, Version - 2.5.3-k> port 0xe0a0-0xe0bf mem 0xdf240000-0xdf25ffff,0xdf308000-0xdf30bfff irq 21 at device 20.1 on pci0
igb1: Using MSIX interrupts with 9 vectors
igb1: Ethernet address: 0c:c4:7a:da:3c:11
igb1: Bound queue 0 to cpu 0
igb1: Bound queue 1 to cpu 1
igb1: Bound queue 2 to cpu 2
igb1: Bound queue 3 to cpu 3
igb1: Bound queue 4 to cpu 4
igb1: Bound queue 5 to cpu 5
igb1: Bound queue 6 to cpu 6
igb1: Bound queue 7 to cpu 7
igb1: netmap queues/slots: TX 8/1024, RX 8/1024
igb2: <Intel(R) PRO/1000 Network Connection, Version - 2.5.3-k> port 0xe080-0xe09f mem 0xdf220000-0xdf23ffff,0xdf304000-0xdf307fff irq 22 at device 20.2 on pci0
igb2: Using MSIX interrupts with 9 vectors
igb2: Ethernet address: 0c:c4:7a:da:3c:12
igb2: Bound queue 0 to cpu 0
igb2: Bound queue 1 to cpu 1
igb2: Bound queue 2 to cpu 2
igb2: Bound queue 3 to cpu 3
igb2: Bound queue 4 to cpu 4
igb2: Bound queue 5 to cpu 5
igb2: Bound queue 6 to cpu 6
igb2: Bound queue 7 to cpu 7
igb2: netmap queues/slots: TX 8/1024, RX 8/1024
igb3: <Intel(R) PRO/1000 Network Connection, Version - 2.5.3-k> port 0xe060-0xe07f mem 0xdf200000-0xdf21ffff,0xdf300000-0xdf303fff irq 23 at device 20.3 on pci0
igb3: Using MSIX interrupts with 9 vectors
igb3: Ethernet address: 0c:c4:7a:da:3c:13
igb3: Bound queue 0 to cpu 0
igb3: Bound queue 1 to cpu 1
igb3: Bound queue 2 to cpu 2
igb3: Bound queue 3 to cpu 3
igb3: Bound queue 4 to cpu 4
igb3: Bound queue 5 to cpu 5
igb3: Bound queue 6 to cpu 6
igb3: Bound queue 7 to cpu 7
igb3: netmap queues/slots: TX 8/1024, RX 8/1024
ehci0: <Intel Avoton USB 2.0 controller> mem 0xdf317000-0xdf3173ff irq 23 at device 22.0 on pci0
usbus1: EHCI version 1.0
usbus1 on ehci0
usbus1: 480Mbps High Speed USB v2.0
ahci0: <Intel Avoton AHCI SATA controller> port 0xe150-0xe157,0xe140-0xe143,0xe130-0xe137,0xe120-0xe123,0xe040-0xe05f mem 0xdf316000-0xdf3167ff irq 19 at device 23.0 on pci0
ahci0: AHCI v1.30 with 4 3Gbps ports, Port Multiplier not supported
ahcich0: <AHCI channel> at channel 0 on ahci0
ahcich1: <AHCI channel> at channel 1 on ahci0
ahcich2: <AHCI channel> at channel 2 on ahci0
ahcich3: <AHCI channel> at channel 3 on ahci0
ahci1: <Intel Avoton AHCI SATA controller> port 0xe110-0xe117,0xe100-0xe103,0xe0f0-0xe0f7,0xe0e0-0xe0e3,0xe020-0xe03f mem 0xdf315000-0xdf3157ff irq 19 at device 24.0 on pci0
ahci1: AHCI v1.30 with 2 6Gbps ports, Port Multiplier not supported
ahcich4: <AHCI channel> at channel 0 on ahci1
ahcich5: <AHCI channel> at channel 1 on ahci1
isab0: <PCI-ISA bridge> at device 31.0 on pci0
isa0: <ISA bus> on isab0
uart0: <16550 or compatible> port 0x3f8-0x3ff irq 4 flags 0x10 on acpi0
uart1: <16550 or compatible> port 0x2f8-0x2ff irq 3 on acpi0
uart1: console (115200,n,8,1)
orm0: <ISA Option ROMs> at iomem 0xc0000-0xc7fff,0xc8000-0xc8fff on isa0
atkbdc0: <Keyboard controller (i8042)> at port 0x60,0x64 on isa0
atkbd0: <AT Keyboard> irq 1 on atkbdc0
atkbd0: [GIANT-LOCKED]
est0: <Enhanced SpeedStep Frequency Control> on cpu0
est1: <Enhanced SpeedStep Frequency Control> on cpu1
est2: <Enhanced SpeedStep Frequency Control> on cpu2
est3: <Enhanced SpeedStep Frequency Control> on cpu3
est4: <Enhanced SpeedStep Frequency Control> on cpu4
est5: <Enhanced SpeedStep Frequency Control> on cpu5
est6: <Enhanced SpeedStep Frequency Control> on cpu6
est7: <Enhanced SpeedStep Frequency Control> on cpu7
Timecounters tick every 1.000 msec
ugen1.1: <Intel EHCI root HUB> at usbus1
ugen0.1: <0x1912 XHCI root HUB> at usbus0
uhub0: <Intel EHCI root HUB, class 9/0, rev 2.00/1.00, addr 1> on usbus1
uhub1: <0x1912 XHCI root HUB, class 9/0, rev 3.00/1.00, addr 1> on usbus0
ada0 at ahcich4 bus 0 scbus4 target 0 lun 0
ada0: <SATA SSD S9FM02.1> ACS-3 ATA SATA 3.x device
ada0: Serial Number B4500757042400104267
ada0: 600.000MB/s transfers (SATA 3.x, UDMA6, PIO 8192bytes)
ada0: Command Queueing enabled
ada0: 30533MB (62533296 512 byte sectors)
```

## pciconf

```
hostb0@pci0:0:0:0:      class=0x060000 card=0x00000000 chip=0x1f088086 rev=0x02 hdr=0x00                                                                                                                                                                             [147/1862]
    vendor     = 'Intel Corporation'
    class      = bridge
    subclass   = HOST-PCI
pcib1@pci0:0:1:0:       class=0x060400 card=0x72708086 chip=0x1f108086 rev=0x02 hdr=0x01
    vendor     = 'Intel Corporation'
    class      = bridge
    subclass   = PCI-PCI
    bar   [10] = type Memory, range 64, base 0xdf2e0000, size 131072, enabled
    cap 10[40] = PCI-Express 2 root port slot max data 128(256) link x1(x4)
                 speed 2.5(5.0) ASPM disabled(L1)
    cap 01[80] = powerspec 3  supports D0 D3  current D0
    cap 0d[88] = PCI Bridge card=0x72708086
    cap 05[90] = MSI supports 1 message, vector masks
    ecap 0001[100] = AER 1 0 fatal 0 non-fatal 0 corrected
pcib3@pci0:0:2:0:       class=0x060400 card=0x72708086 chip=0x1f118086 rev=0x02 hdr=0x01
    vendor     = 'Intel Corporation'
    class      = bridge
    subclass   = PCI-PCI
    bar   [10] = type Memory, range 64, base 0xdf2c0000, size 131072, enabled
    cap 10[40] = PCI-Express 2 root port slot max data 128(256) link x1(x4)
                 speed 5.0(5.0) ASPM disabled(L1)
    cap 01[80] = powerspec 3  supports D0 D3  current D0
    cap 0d[88] = PCI Bridge card=0x72708086
    cap 05[90] = MSI supports 1 message, vector masks
    ecap 0001[100] = AER 1 0 fatal 0 non-fatal 0 corrected
pcib4@pci0:0:3:0:       class=0x060400 card=0x72708086 chip=0x1f128086 rev=0x02 hdr=0x01
    vendor     = 'Intel Corporation'
    class      = bridge
    subclass   = PCI-PCI
    bar   [10] = type Memory, range 64, base 0xdf2a0000, size 131072, enabled
    cap 10[40] = PCI-Express 2 root port slot max data 256(256) link x0(x8)
                 speed 0.0(5.0) ASPM disabled(L1)
    cap 01[80] = powerspec 3  supports D0 D3  current D0
    cap 0d[88] = PCI Bridge card=0x72708086
    cap 05[90] = MSI supports 1 message, vector masks
    ecap 0001[100] = AER 1 0 fatal 0 non-fatal 0 corrected
none0@pci0:0:11:0:      class=0x0b4000 card=0x00008086 chip=0x1f188086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    class      = processor
    bar   [18] = type Memory, range 64, base 0xdf280000, size 131072, enabled
    bar   [20] = type Memory, range 64, base 0xdf310000, size 16384, enabled
    cap 05[b0] = MSI supports 1 message, 64 bit, vector masks
    cap 11[60] = MSI-X supports 17 messages
                 Table in map 0x18[0x1b000], PBA in map 0x18[0x1b800]
    cap 01[6c] = powerspec 3  supports D0 D3  current D3
    cap 10[74] = PCI-Express 2 root endpoint max data 256(256) FLR link x0(x0)
    ecap 0001[100] = AER 1 0 fatal 0 non-fatal 0 corrected
    ecap 000e[138] = ARI 1
    ecap 0010[140] = SRIOV 1
hostb1@pci0:0:14:0:     class=0x060000 card=0x00008086 chip=0x1f148086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    class      = bridge
    subclass   = HOST-PCI
    cap 10[40] = PCI-Express 2 root endpoint max data 256(256) link x0(x0)
none1@pci0:0:15:0:      class=0x080600 card=0x00008086 chip=0x1f168086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    class      = base peripheral
    cap 10[40] = PCI-Express 2 event collector max data 256(256) link x0(x0)
    cap 01[80] = powerspec 3  supports D0 D3  current D3
    cap 05[90] = MSI supports 1 message, vector masks
    ecap 0001[100] = AER 1 0 fatal 0 non-fatal 1 corrected
    ecap 0007[150] = Root Complex Event Collector ASsociation 1
none2@pci0:0:19:0:      class=0x088000 card=0x00008086 chip=0x1f158086 rev=0x02 hdr=0x00                                                                                                                                                                              [84/1862]
    vendor     = 'Intel Corporation'
    class      = base peripheral
    bar   [10] = type Memory, range 64, base 0xdf318000, size 1024, enabled
    cap 10[40] = PCI-Express 2 root endpoint max data 256(256) FLR link x0(x0)
    cap 01[80] = powerspec 3  supports D0 D3  current D3
    cap 05[8c] = MSI supports 1 message, 64 bit, vector masks
    ecap 0001[100] = AER 1 0 fatal 0 non-fatal 0 corrected
igb0@pci0:0:20:0:       class=0x020000 card=0x1f4115d9 chip=0x1f418086 rev=0x03 hdr=0x00
    vendor     = 'Intel Corporation'
    class      = network
    subclass   = ethernet
    bar   [10] = type Memory, range 64, base 0xdf260000, size 131072, enabled
    bar   [18] = type I/O Port, range 32, base 0xe0c0, size 32, enabled
    bar   [20] = type Memory, range 64, base 0xdf30c000, size 16384, enabled
    cap 01[40] = powerspec 3  supports D0 D3  current D0
    cap 05[50] = MSI supports 1 message, 64 bit, vector masks
    cap 11[70] = MSI-X supports 10 messages, enabled
                 Table in map 0x20[0x0], PBA in map 0x20[0x2000]
    cap 10[a0] = PCI-Express 2 root endpoint max data 256(512) FLR link x0(x0)
    ecap 0001[100] = AER 2 0 fatal 0 non-fatal 0 corrected
    ecap 0003[140] = Serial 1 002590ffff829a6c
    ecap 0017[1a0] = TPH Requester 1
    ecap 000d[1d0] = ACS 1
igb1@pci0:0:20:1:       class=0x020000 card=0x1f4115d9 chip=0x1f418086 rev=0x03 hdr=0x00
    vendor     = 'Intel Corporation'
    class      = network
    subclass   = ethernet
    bar   [10] = type Memory, range 64, base 0xdf240000, size 131072, enabled
    bar   [18] = type I/O Port, range 32, base 0xe0a0, size 32, enabled
    bar   [20] = type Memory, range 64, base 0xdf308000, size 16384, enabled
    cap 01[40] = powerspec 3  supports D0 D3  current D0
    cap 05[50] = MSI supports 1 message, 64 bit, vector masks
    cap 11[70] = MSI-X supports 10 messages, enabled
                 Table in map 0x20[0x0], PBA in map 0x20[0x2000]
    cap 10[a0] = PCI-Express 2 root endpoint max data 256(512) FLR link x0(x0)
    ecap 0001[100] = AER 2 0 fatal 0 non-fatal 0 corrected
    ecap 0003[140] = Serial 1 002590ffff829a6c
    ecap 0017[1a0] = TPH Requester 1
    ecap 000d[1d0] = ACS 1
igb2@pci0:0:20:2:       class=0x020000 card=0x1f4115d9 chip=0x1f418086 rev=0x03 hdr=0x00
    vendor     = 'Intel Corporation'
    class      = network
    subclass   = ethernet
    bar   [10] = type Memory, range 64, base 0xdf220000, size 131072, enabled
    bar   [18] = type I/O Port, range 32, base 0xe080, size 32, enabled
    bar   [20] = type Memory, range 64, base 0xdf304000, size 16384, enabled
    cap 01[40] = powerspec 3  supports D0 D3  current D0
    cap 05[50] = MSI supports 1 message, 64 bit, vector masks
    cap 11[70] = MSI-X supports 10 messages, enabled
                 Table in map 0x20[0x0], PBA in map 0x20[0x2000]
    cap 10[a0] = PCI-Express 2 root endpoint max data 256(512) FLR link x0(x0)
    ecap 0001[100] = AER 2 0 fatal 0 non-fatal 0 corrected
    ecap 0003[140] = Serial 1 002590ffff829a6c
    ecap 0017[1a0] = TPH Requester 1
    ecap 000d[1d0] = ACS 1
igb3@pci0:0:20:3:       class=0x020000 card=0x1f4115d9 chip=0x1f418086 rev=0x03 hdr=0x00
    vendor     = 'Intel Corporation'
    class      = network
    subclass   = ethernet
    bar   [10] = type Memory, range 64, base 0xdf200000, size 131072, enabled
    bar   [18] = type I/O Port, range 32, base 0xe060, size 32, enabled
    bar   [20] = type Memory, range 64, base 0xdf300000, size 16384, enabled
    cap 01[40] = powerspec 3  supports D0 D3  current D0
    cap 05[50] = MSI supports 1 message, 64 bit, vector masks
    cap 11[70] = MSI-X supports 10 messages, enabled
                 Table in map 0x20[0x0], PBA in map 0x20[0x2000]
    cap 10[a0] = PCI-Express 2 root endpoint max data 256(512) FLR link x0(x0)
    ecap 0001[100] = AER 2 0 fatal 0 non-fatal 0 corrected
    ecap 0003[140] = Serial 1 002590ffff829a6c                                                                                                                                                                                                                        [15/1862]
    ecap 0017[1a0] = TPH Requester 1
    ecap 000d[1d0] = ACS 1
ehci0@pci0:0:22:0:      class=0x0c0320 card=0x72708086 chip=0x1f2c8086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    class      = serial bus
    subclass   = USB
    bar   [10] = type Memory, range 32, base 0xdf317000, size 1024, enabled
    cap 01[50] = powerspec 3  supports D0 D3  current D0
    cap 0a[58] = EHCI Debug Port at offset 0xa0 in map 0x14
    cap 13[98] = PCI Advanced Features: FLR TP
ahci0@pci0:0:23:0:      class=0x010601 card=0x72708086 chip=0x1f228086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    class      = mass storage
    subclass   = SATA
    bar   [10] = type I/O Port, range 32, base 0xe150, size 8, enabled
    bar   [14] = type I/O Port, range 32, base 0xe140, size 4, enabled
    bar   [18] = type I/O Port, range 32, base 0xe130, size 8, enabled
    bar   [1c] = type I/O Port, range 32, base 0xe120, size 4, enabled
    bar   [20] = type I/O Port, range 32, base 0xe040, size 32, enabled
    bar   [24] = type Memory, range 32, base 0xdf316000, size 2048, enabled
    cap 05[80] = MSI supports 1 message enabled with 1 message
    cap 01[70] = powerspec 3  supports D0 D3  current D0
    cap 12[a8] = SATA Index-Data Pair
ahci1@pci0:0:24:0:      class=0x010601 card=0x72708086 chip=0x1f328086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    class      = mass storage
    subclass   = SATA
    bar   [10] = type I/O Port, range 32, base 0xe110, size 8, enabled
    bar   [14] = type I/O Port, range 32, base 0xe100, size 4, enabled
    bar   [18] = type I/O Port, range 32, base 0xe0f0, size 8, enabled
    bar   [1c] = type I/O Port, range 32, base 0xe0e0, size 4, enabled
    bar   [20] = type I/O Port, range 32, base 0xe020, size 32, enabled
    bar   [24] = type Memory, range 32, base 0xdf315000, size 2048, enabled
    cap 05[80] = MSI supports 1 message enabled with 1 message
    cap 01[70] = powerspec 3  supports D0 D3  current D0
    cap 12[a8] = SATA Index-Data Pair
isab0@pci0:0:31:0:      class=0x060100 card=0x72708086 chip=0x1f388086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    class      = bridge
    subclass   = PCI-ISA
    cap 09[e0] = vendor (length 12) Intel cap 1 version 0
                 features: 4 PCI-e x1 slots
none3@pci0:0:31:3:      class=0x0c0500 card=0x72708086 chip=0x1f3c8086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    class      = serial bus
    subclass   = SMBus
    bar   [10] = type Memory, range 32, base 0xdf314000, size 32, enabled
    bar   [20] = type I/O Port, range 32, base 0xe000, size 32, enabled
pcib2@pci0:1:0:0:       class=0x060400 card=0x11501a03 chip=0x11501a03 rev=0x03 hdr=0x01
    vendor     = 'ASPEED Technology, Inc.'
    device     = 'AST1150 PCI-to-PCI Bridge'
    class      = bridge
    subclass   = PCI-PCI
    cap 05[50] = MSI supports 1 message, 64 bit
    cap 01[78] = powerspec 3  supports D0 D1 D2 D3  current D0
    cap 10[80] = PCI-Express 1 PCI bridge max data 128(128) link x1(x1)
                 speed 2.5(2.5) ASPM disabled(L0s/L1)
    cap 0d[a4] = PCI Bridge card=0x11501a03
    ecap 0002[100] = VC 1 max VC0
vgapci0@pci0:2:0:0:     class=0x030000 card=0x081315d9 chip=0x20001a03 rev=0x30 hdr=0x00
    vendor     = 'ASPEED Technology, Inc.'
    device     = 'ASPEED Graphics Family'
    class      = display
    subclass   = VGA
    bar   [10] = type Memory, range 32, base 0xde000000, size 16777216, enabled
    bar   [14] = type Memory, range 32, base 0xdf000000, size 131072, enabled
    bar   [18] = type I/O Port, range 32, base 0xd000, size 128, enabled
    cap 01[40] = powerspec 3  supports D0 D1 D2 D3  current D0
    cap 05[50] = MSI supports 4 messages, 64 bit
xhci0@pci0:3:0:0:       class=0x0c0330 card=0x081315d9 chip=0x00141912 rev=0x03 hdr=0x00
    vendor     = 'Renesas Technology Corp.'
    class      = serial bus
    subclass   = USB
    bar   [10] = type Memory, range 64, base 0xdf100000, size 8192, enabled
    cap 01[50] = powerspec 3  supports D0 D3  current D0
    cap 05[70] = MSI supports 8 messages, 64 bit enabled with 1 message
    cap 11[90] = MSI-X supports 8 messages
                 Table in map 0x10[0x1000], PBA in map 0x10[0x1080]
    cap 10[a0] = PCI-Express 2 endpoint max data 128(128) link x1(x1)
                 speed 5.0(5.0) ASPM disabled(L0s/L1)
    ecap 0001[100] = AER 1 0 fatal 0 non-fatal 0 corrected
    ecap 0018[150] = LTR 1
```
