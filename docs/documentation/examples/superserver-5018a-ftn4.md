---
title: SuperServer 5018A-FTN4
---
This is the hardware reference for the SuperMicro
[SuperServer 5018A-FTN4](https://www.supermicro.com/en/products/system/1U/5018/SYS-5018A-FTN4.cfm)
used as a device under test in the [bench lab](../technical-docs/bench-lab.md).

The capture below comes from a system running BSDRP 2.3
(FreeBSD 16.0-CURRENT), fitted with a dual-port Chelsio T520-SO in the
PCIe slot alongside the on-board quad-port Intel i354.

## dmesg

```
Copyright (c) 1992-2026 The FreeBSD Project.
Copyright (c) 1979, 1980, 1983, 1986, 1988, 1989, 1991, 1992, 1993, 1994
	The Regents of the University of California. All rights reserved.
FreeBSD is a registered trademark of The FreeBSD Foundation.
FreeBSD 16.0-CURRENT BSDRP-AMD64 amd64
FreeBSD clang version 21.1.8 (https://github.com/llvm/llvm-project.git llvmorg-21.1.8-0-g2078da43e25a)
VT(efifb): resolution 800x600
CPU: Intel(R) Atom(TM) CPU  C2758  @ 2.40GHz (2400.25-MHz K8-class CPU)
  Origin="GenuineIntel"  Id=0x406d8  Family=0x6  Model=0x4d  Stepping=8
  Features=0xbfebfbff<FPU,VME,DE,PSE,TSC,MSR,PAE,MCE,CX8,APIC,SEP,MTRR,PGE,MCA,CMOV,PAT,PSE36,CLFLUSH,DTS,ACPI,MMX,FXSR,SSE,SSE2,SS,HTT,TM,PBE>
  Features2=0x43d8e3bf<SSE3,PCLMULQDQ,DTES64,MON,DS_CPL,VMX,EST,TM2,SSSE3,CX16,xTPR,PDCM,SSE4.1,SSE4.2,MOVBE,POPCNT,TSCDLT,AESNI,RDRAND>
  AMD Features=0x28100800<SYSCALL,NX,RDTSCP,LM>
  AMD Features2=0x101<LAHF,Prefetch>
  Structured Extended Features=0x2282<TSCADJ,SMEP,ERMS,NFPUSG>
  Structured Extended Features3=0xc000400<MD_CLEAR,IBPB,STIBP>
  VT-x: PAT,HLT,MTF,PAUSE,EPT,UG,VPID
  TSC: P-state invariant, performance statistics
real memory  = 17179869184 (16384 MB)
avail memory = 16637947904 (15867 MB)
Event timer "LAPIC" quality 600
ACPI APIC Table: <INTEL  TIANO   >
WARNING: L1 data cache covers fewer APIC IDs than a core (0 < 1)
FreeBSD/SMP: Multiprocessor System Detected: 8 CPUs
FreeBSD/SMP: 1 package(s) x 8 core(s)
random: registering fast source Intel Secure Key RNG
random: fast provider: "Intel Secure Key RNG"
random: unblocking device.
ioapic0 <Version 2.0> irqs 0-23
Launching APs: 3 1 7 4 6 2 5
random: entropy device external interface
efirtc0: <EFI Realtime Clock>
efirtc0: registered as a time-of-day clock, resolution 1.000000s
smbios0: <System Management BIOS> at iomem 0x7f3efd18-0x7f3efd36
smbios0: Entry point: v2.1 (32-bit), Version: 2.8, BCD Revision: 2.7
aesni0: <AES-CBC,AES-CCM,AES-GCM,AES-ICM,AES-XTS>
acpi0: <ALASKA A M I >
acpi0: Power Button (fixed)
cpu0: <ACPI CPU> on acpi0
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
Timecounter "ACPI-fast" frequency 3579545 Hz quality 900
acpi_timer0: <24-bit timer at 3.579545MHz> port 0x408-0x40b on acpi0
pcib0: <ACPI Host-PCI bridge> port 0xcf8-0xcff on acpi0
pci0: <ACPI PCI bus> on pcib0
pcib1: <ACPI PCI-PCI bridge> mem 0xdd9e0000-0xdd9fffff at device 1.0 on pci0
pci1: <ACPI PCI bus> on pcib1
pcib2: <ACPI PCI-PCI bridge> at device 0.0 on pci1
pci2: <ACPI PCI bus> on pcib2
vgapci0: <VGA-compatible display> port 0xd000-0xd07f mem 0xde000000-0xdeffffff,0xdf000000-0xdf01ffff at device 0.0 on pci2
vgapci0: Boot video device
pcib3: <ACPI PCI-PCI bridge> mem 0xdd9c0000-0xdd9dffff at device 2.0 on pci0
pci3: <ACPI PCI bus> on pcib3
xhci0: <XHCI (generic) USB 3.0 controller> mem 0xdf200000-0xdf201fff at device 0.0 on pci3
xhci0: 64 bytes context size, 32-bit DMA
xhci0: xECP capabilities <LEGACY,PROTO,PROTO,VEND(c0),DEBUG>
usbus0 on xhci0
usbus0: 5.0Gbps Super Speed USB v3.0
pcib4: <ACPI PCI-PCI bridge> mem 0xdd9a0000-0xdd9bffff at device 3.0 on pci0
pci4: <ACPI PCI bus> on pcib4
t5nex0: <Chelsio T520-SO> mem 0xdd300000-0xdd37ffff,0xdc000000-0xdcffffff,0xdd884000-0xdd885fff at device 0.4 on pci4
cxl0: <port 0> on t5nex0
cxl0: Ethernet address: 00:07:43:3b:11:30
cxl0: 8 txq, 8 rxq (NIC)
cxl1: <port 1> on t5nex0
cxl1: Ethernet address: 00:07:43:3b:11:38
cxl1: 8 txq, 8 rxq (NIC)
t5nex0: PCIe gen2 x8, 2 ports, 18 MSI-X interrupts, 34 eq, 17 iq
pci4: <mass storage, SCSI> at device 0.5 (no driver attached)
pci4: <serial bus, Fibre Channel> at device 0.6 (no driver attached)
pci0: <processor> at device 11.0 (no driver attached)
pci0: <base peripheral, IOMMU> at device 15.0 (no driver attached)
igb0: <Intel(R) I354 (SGMII)> port 0xe0c0-0xe0df mem 0xdd960000-0xdd97ffff,0xdda0c000-0xdda0ffff at device 20.0 on pci0
igb0: EEPROM V1.0-5
igb0: Using 1024 TX descriptors and 1024 RX descriptors
igb0: Using 8 RX queues 8 TX queues
igb0: Using MSI-X interrupts with 9 vectors
igb0: Ethernet address: 0c:c4:7a:ab:29:34
igb0: netmap queues/slots: TX 8/1024, RX 8/1024
igb1: <Intel(R) I354 (SGMII)> port 0xe0a0-0xe0bf mem 0xdd940000-0xdd95ffff,0xdda08000-0xdda0bfff at device 20.1 on pci0
igb1: EEPROM V1.0-5
igb1: Using 1024 TX descriptors and 1024 RX descriptors
igb1: Using 8 RX queues 8 TX queues
igb1: Using MSI-X interrupts with 9 vectors
igb1: Ethernet address: 0c:c4:7a:ab:29:35
igb1: netmap queues/slots: TX 8/1024, RX 8/1024
igb2: <Intel(R) I354 (SGMII)> port 0xe080-0xe09f mem 0xdd920000-0xdd93ffff,0xdda04000-0xdda07fff at device 20.2 on pci0
igb2: EEPROM V1.0-5
igb2: Using 1024 TX descriptors and 1024 RX descriptors
igb2: Using 8 RX queues 8 TX queues
igb2: Using MSI-X interrupts with 9 vectors
igb2: Ethernet address: 0c:c4:7a:ab:29:36
igb2: netmap queues/slots: TX 8/1024, RX 8/1024
igb3: <Intel(R) I354 (SGMII)> port 0xe060-0xe07f mem 0xdd900000-0xdd91ffff,0xdda00000-0xdda03fff at device 20.3 on pci0
igb3: EEPROM V1.0-5
igb3: Using 1024 TX descriptors and 1024 RX descriptors
igb3: Using 8 RX queues 8 TX queues
igb3: Using MSI-X interrupts with 9 vectors
igb3: Ethernet address: 0c:c4:7a:ab:29:37
igb3: netmap queues/slots: TX 8/1024, RX 8/1024
ehci0: <Intel Avoton USB 2.0 controller> mem 0xdda17000-0xdda173ff at device 22.0 on pci0
usbus1: EHCI version 1.0
usbus1 on ehci0
usbus1: 480Mbps High Speed USB v2.0
ahci0: <Intel Avoton AHCI SATA controller> port 0xe150-0xe157,0xe140-0xe143,0xe130-0xe137,0xe120-0xe123,0xe040-0xe05f mem 0xdda16000-0xdda167ff at device 23.0 on pci0
ahci0: AHCI v1.30 with 4 3Gbps ports, Port Multiplier not supported
ahcich0: <AHCI channel> at channel 0 on ahci0
ahcich1: <AHCI channel> at channel 1 on ahci0
ahcich2: <AHCI channel> at channel 2 on ahci0
ahcich3: <AHCI channel> at channel 3 on ahci0
ahci1: <Intel Avoton AHCI SATA controller> port 0xe110-0xe117,0xe100-0xe103,0xe0f0-0xe0f7,0xe0e0-0xe0e3,0xe020-0xe03f mem 0xdda15000-0xdda157ff at device 24.0 on pci0
ahci1: AHCI v1.30 with 2 6Gbps ports, Port Multiplier not supported
ahcich4: <AHCI channel> at channel 0 on ahci1
ahcich5: <AHCI channel> at channel 1 on ahci1
isab0: <PCI-ISA bridge> at device 31.0 on pci0
isa0: <ISA bus> on isab0
apei0: <ACPI Platform Error Interface> on acpi0
hest0: <APEI Hardware Errors> on apei0
uart0: <16550 or compatible> port 0x3f8-0x3ff irq 4 flags 0x10 on acpi0
uart1: <16550 or compatible> port 0x2f8-0x2ff irq 3 on acpi0
uart1: console (115200,n,8,1)
est0: <Enhanced SpeedStep Frequency Control> on cpu0
cpufreq0: <CPU frequency control> on cpu0
cpufreq1: <CPU frequency control> on cpu1
cpufreq2: <CPU frequency control> on cpu2
cpufreq3: <CPU frequency control> on cpu3
cpufreq4: <CPU frequency control> on cpu4
cpufreq5: <CPU frequency control> on cpu5
cpufreq6: <CPU frequency control> on cpu6
cpufreq7: <CPU frequency control> on cpu7
Timecounter "TSC-low" frequency 1199999760 Hz quality 1000
Timecounters tick every 1.000 msec
ugen0.1: <(0x1912) XHCI root HUB> at usbus0
ugen1.1: <Intel EHCI root HUB> at usbus1
uhub0 on usbus0
uhub0: <(0x1912) XHCI root HUB, class 9/0, rev 3.00/1.00, addr 1> on usbus0
uhub1 on usbus1
uhub1: <Intel EHCI root HUB, class 9/0, rev 2.00/1.00, addr 1> on usbus1
Trying to mount root from ufs:/dev/gpt/BSDRP2 [ro]...
ada0 at ahcich4 bus 0 scbus4 target 0 lun 0
ada0: <KINGSTON SV300S37A120G 605ABBF2> ATA8-ACS SATA 3.x device
ada0: Serial Number 50026B775A0A836C
ada0: 600.000MB/s transfers (SATA 3.x, UDMA6, PIO 512bytes)
ada0: Command Queueing enabled
ada0: 114473MB (234441648 512 byte sectors)
uhub0: 8 ports with 8 removable, self powered
Root mount waiting for: usbus1
Root mount waiting for: usbus1
uhub1: 8 ports with 8 removable, self powered
Root mount waiting for: usbus1
ugen1.2: <vendor 0x8087 product 0x07db> at usbus1
uhub2 on uhub1
uhub2: <vendor 0x8087 product 0x07db, class 9/0, rev 2.00/0.02, addr 2> on usbus1
uhub2: 4 ports with 4 removable, self powered
Root mount waiting for: usbus1
ugen1.3: <vendor 0x04cc product 0x1122> at usbus1
uhub3 on uhub2
uhub3: <vendor 0x04cc product 0x1122, class 9/0, rev 1.10/1.10, addr 3> on usbus1
Root mount waiting for: usbus1
uhub3: 2 ports with 2 removable, bus powered
ugen1.4: <Prolific Technology Inc. IEEE-1284 Controller> at usbus1
ugen1.5: <vendor 0x067b product 0x2303> at usbus1
Root mount waiting for: usbus1
ugen1.6: <vendor 0x0557 product 0x7000> at usbus1
uhub4 on uhub2
uhub4: <vendor 0x0557 product 0x7000, class 9/0, rev 2.00/0.00, addr 6> on usbus1
uhub4: 4 ports with 3 removable, self powered
ugen1.7: <vendor 0x0557 product 0x2419> at usbus1
usbhid0 on uhub4
usbhid0: <vendor 0x0557 product 0x2419, class 0/0, rev 1.10/1.00, addr 7> on usbus1
hidbus0: <HID bus> on usbhid0
hkbd0: <vendor 0x0557 product 0x2419 Keyboard> on hidbus0
usbhid1 on uhub4
usbhid1: <vendor 0x0557 product 0x2419, class 0/0, rev 1.10/1.00, addr 7> on usbus1
hidbus1: <HID bus> on usbhid1
Dual Console: Video Primary, Serial Secondary
ichsmb0: <Intel Avoton SMBus controller> port 0xe000-0xe01f mem 0xdda14000-0xdda1401f at device 31.3 on pci0
smbus0: <System Management Bus> on ichsmb0
igb0: link state changed to UP
igb1: link state changed to UP
igb2: link state changed to UP
igb3: link state changed to UP
lo0: link state changed to UP
cxl0: link state changed to UP
igb0: link state changed to DOWN
cxl1: link state changed to UP
cxl1: link state changed to DOWN
cxl1: link state changed to UP
igb0: link state changed to UP
uplcom0 on uhub3
uplcom0: <vendor 0x067b product 0x2303, class 0/0, rev 1.10/2.02, addr 5> on usbus1
hwpmc: SOFT/16/64/0x67<INT,USR,SYS,REA,WRI> TSC/1/64/0x20<REA> IAP/2/40/0x3ff<INT,USR,SYS,EDG,THR,REA,WRI,INV,QUA,PRC> IAF/3/40/0x67<INT,USR,SYS,REA,WRI> PERF/2/64/0x20<REA> RAPL/2/64/0x2020<REA>
```

## pciconf

```
hostb0@pci0:0:0:0:	class=0x060000 rev=0x02 hdr=0x00 vendor=0x8086 device=0x1f08 subvendor=0x0000 subdevice=0x0000
    vendor     = 'Intel Corporation'
    device     = 'Atom processor C2000 SoC Transaction Router'
    class      = bridge
    subclass   = HOST-PCI
pcib1@pci0:0:1:0:	class=0x060400 rev=0x02 hdr=0x01 vendor=0x8086 device=0x1f10 subvendor=0x8086 subdevice=0x7270
    vendor     = 'Intel Corporation'
    device     = 'Atom processor C2000 PCIe Root Port 1'
    class      = bridge
    subclass   = PCI-PCI
    bar   [10] = type Memory, range 64, base 0xdd9e0000, size 131072, enabled
    cap 10[40] = PCI-Express 2 root port max data 128(256) ARI disabled
                 max read 128
                 link x1(x4) speed 2.5(5.0) ASPM disabled(L1)
                 slot 0 power limit 250 mW
    cap 01[80] = powerspec 3  supports D0 D3  current D0
    cap 0d[88] = PCI Bridge subvendor=0x8086 subdevice=0x7270
    cap 05[90] = MSI supports 1 message, vector masks 
    ecap 0001[100] = AER 1 0 fatal 0 non-fatal 0 corrected
pcib3@pci0:0:2:0:	class=0x060400 rev=0x02 hdr=0x01 vendor=0x8086 device=0x1f11 subvendor=0x8086 subdevice=0x7270
    vendor     = 'Intel Corporation'
    device     = 'Atom processor C2000 PCIe Root Port 2'
    class      = bridge
    subclass   = PCI-PCI
    bar   [10] = type Memory, range 64, base 0xdd9c0000, size 131072, enabled
    cap 10[40] = PCI-Express 2 root port max data 128(256) ARI disabled
                 max read 128
                 link x1(x4) speed 5.0(5.0) ASPM disabled(L1)
                 slot 1 power limit 250 mW
    cap 01[80] = powerspec 3  supports D0 D3  current D0
    cap 0d[88] = PCI Bridge subvendor=0x8086 subdevice=0x7270
    cap 05[90] = MSI supports 1 message, vector masks 
    ecap 0001[100] = AER 1 0 fatal 0 non-fatal 0 corrected
pcib4@pci0:0:3:0:	class=0x060400 rev=0x02 hdr=0x01 vendor=0x8086 device=0x1f12 subvendor=0x8086 subdevice=0x7270
    vendor     = 'Intel Corporation'
    device     = 'Atom processor C2000 PCIe Root Port 3'
    class      = bridge
    subclass   = PCI-PCI
    bar   [10] = type Memory, range 64, base 0xdd9a0000, size 131072, enabled
    cap 10[40] = PCI-Express 2 root port max data 256(256) ARI enabled
                 max read 128
                 link x8(x8) speed 5.0(5.0) ASPM disabled(L1)
                 slot 2 power limit 250 mW
    cap 01[80] = powerspec 3  supports D0 D3  current D0
    cap 0d[88] = PCI Bridge subvendor=0x8086 subdevice=0x7270
    cap 05[90] = MSI supports 1 message, vector masks 
    ecap 0001[100] = AER 1 0 fatal 0 non-fatal 0 corrected
none0@pci0:0:11:0:	class=0x0b4000 rev=0x02 hdr=0x00 vendor=0x8086 device=0x1f18 subvendor=0x8086 subdevice=0x0000
    vendor     = 'Intel Corporation'
    device     = 'Atom processor C2000 QAT'
    class      = processor
    bar   [18] = type Memory, range 64, base 0xdd980000, size 131072, enabled
    bar   [20] = type Memory, range 64, base 0xdda10000, size 16384, enabled
    cap 05[b0] = MSI supports 1 message, 64 bit, vector masks 
    cap 11[60] = MSI-X supports 17 messages
                 Table in map 0x18[0x1b000], PBA in map 0x18[0x1b800]
    cap 01[6c] = powerspec 3  supports D0 D3  current D3
    cap 10[74] = PCI-Express 2 root endpoint max data 256(256) FLR NS
                 max read 512
    ecap 0001[100] = AER 1 0 fatal 0 non-fatal 0 corrected
hostb1@pci0:0:14:0:	class=0x060000 rev=0x02 hdr=0x00 vendor=0x8086 device=0x1f14 subvendor=0x8086 subdevice=0x0000
    vendor     = 'Intel Corporation'
    device     = 'Atom processor C2000 RAS'
    class      = bridge
    subclass   = HOST-PCI
    cap 10[40] = PCI-Express 2 root endpoint max data 256(256)
                 max read 128
none1@pci0:0:15:0:	class=0x080600 rev=0x02 hdr=0x00 vendor=0x8086 device=0x1f16 subvendor=0x8086 subdevice=0x0000
    vendor     = 'Intel Corporation'
    device     = 'Atom processor C2000 RCEC'
    class      = base peripheral
    subclass   = IOMMU
    cap 10[40] = PCI-Express 2 event collector max data 256(256)
                 max read 128
    cap 01[80] = powerspec 3  supports D0 D3  current D3
    cap 05[90] = MSI supports 1 message, vector masks 
    ecap 0001[100] = AER 1 0 fatal 0 non-fatal 0 corrected
    ecap 0007[150] = Root Complex Event Collector ASsociation 1
none2@pci0:0:19:0:	class=0x088000 rev=0x02 hdr=0x00 vendor=0x8086 device=0x1f15 subvendor=0x8086 subdevice=0x0000
    vendor     = 'Intel Corporation'
    device     = 'Atom processor C2000 SMBus 2.0'
    class      = base peripheral
    bar   [10] = type Memory, range 64, base 0xdda18000, size 1024, enabled
    cap 10[40] = PCI-Express 2 root endpoint max data 256(256) FLR NS
                 max read 128
    cap 01[80] = powerspec 3  supports D0 D3  current D3
    cap 05[8c] = MSI supports 1 message, 64 bit, vector masks 
    ecap 0001[100] = AER 1 0 fatal 0 non-fatal 0 corrected
igb0@pci0:0:20:0:	class=0x020000 rev=0x03 hdr=0x00 vendor=0x8086 device=0x1f41 subvendor=0x15d9 subdevice=0x1f41
    vendor     = 'Intel Corporation'
    device     = 'Ethernet Connection I354'
    class      = network
    subclass   = ethernet
    bar   [10] = type Memory, range 64, base 0xdd960000, size 131072, enabled
    bar   [18] = type I/O Port, range 32, base 0xe0c0, size 32, enabled
    bar   [20] = type Memory, range 64, base 0xdda0c000, size 16384, enabled
    cap 01[40] = powerspec 3  supports D0 D3  current D0
    cap 05[50] = MSI supports 1 message, 64 bit, vector masks 
    cap 11[70] = MSI-X supports 10 messages, enabled
                 Table in map 0x20[0x0], PBA in map 0x20[0x2000]
    cap 10[a0] = PCI-Express 2 root endpoint max data 512(512) FLR NS
                 max read 512
    ecap 0001[100] = AER 2 0 fatal 0 non-fatal 0 corrected
    ecap 0003[140] = Serial 1 0cc47affffab2934
    ecap 0017[1a0] = TPH Requester 1
    ecap 000d[1d0] = ACS 1 Source Validation unavailable, Translation Blocking unavailable
                     P2P Req Redirect unavailable, P2P Cmpl Redirect unavailable
                     P2P Upstream Forwarding unavailable, P2P Egress Control unavailable
                     P2P Direct Translated unavailable, Enhanced Capability unavailable
igb1@pci0:0:20:1:	class=0x020000 rev=0x03 hdr=0x00 vendor=0x8086 device=0x1f41 subvendor=0x15d9 subdevice=0x1f41
    vendor     = 'Intel Corporation'
    device     = 'Ethernet Connection I354'
    class      = network
    subclass   = ethernet
    bar   [10] = type Memory, range 64, base 0xdd940000, size 131072, enabled
    bar   [18] = type I/O Port, range 32, base 0xe0a0, size 32, enabled
    bar   [20] = type Memory, range 64, base 0xdda08000, size 16384, enabled
    cap 01[40] = powerspec 3  supports D0 D3  current D0
    cap 05[50] = MSI supports 1 message, 64 bit, vector masks 
    cap 11[70] = MSI-X supports 10 messages, enabled
                 Table in map 0x20[0x0], PBA in map 0x20[0x2000]
    cap 10[a0] = PCI-Express 2 root endpoint max data 512(512) FLR NS
                 max read 512
    ecap 0001[100] = AER 2 0 fatal 0 non-fatal 0 corrected
    ecap 0003[140] = Serial 1 0cc47affffab2934
    ecap 0017[1a0] = TPH Requester 1
    ecap 000d[1d0] = ACS 1 Source Validation unavailable, Translation Blocking unavailable
                     P2P Req Redirect unavailable, P2P Cmpl Redirect unavailable
                     P2P Upstream Forwarding unavailable, P2P Egress Control unavailable
                     P2P Direct Translated unavailable, Enhanced Capability unavailable
igb2@pci0:0:20:2:	class=0x020000 rev=0x03 hdr=0x00 vendor=0x8086 device=0x1f41 subvendor=0x15d9 subdevice=0x1f41
    vendor     = 'Intel Corporation'
    device     = 'Ethernet Connection I354'
    class      = network
    subclass   = ethernet
    bar   [10] = type Memory, range 64, base 0xdd920000, size 131072, enabled
    bar   [18] = type I/O Port, range 32, base 0xe080, size 32, enabled
    bar   [20] = type Memory, range 64, base 0xdda04000, size 16384, enabled
    cap 01[40] = powerspec 3  supports D0 D3  current D0
    cap 05[50] = MSI supports 1 message, 64 bit, vector masks 
    cap 11[70] = MSI-X supports 10 messages, enabled
                 Table in map 0x20[0x0], PBA in map 0x20[0x2000]
    cap 10[a0] = PCI-Express 2 root endpoint max data 512(512) FLR NS
                 max read 512
    ecap 0001[100] = AER 2 0 fatal 0 non-fatal 0 corrected
    ecap 0003[140] = Serial 1 0cc47affffab2934
    ecap 0017[1a0] = TPH Requester 1
    ecap 000d[1d0] = ACS 1 Source Validation unavailable, Translation Blocking unavailable
                     P2P Req Redirect unavailable, P2P Cmpl Redirect unavailable
                     P2P Upstream Forwarding unavailable, P2P Egress Control unavailable
                     P2P Direct Translated unavailable, Enhanced Capability unavailable
igb3@pci0:0:20:3:	class=0x020000 rev=0x03 hdr=0x00 vendor=0x8086 device=0x1f41 subvendor=0x15d9 subdevice=0x1f41
    vendor     = 'Intel Corporation'
    device     = 'Ethernet Connection I354'
    class      = network
    subclass   = ethernet
    bar   [10] = type Memory, range 64, base 0xdd900000, size 131072, enabled
    bar   [18] = type I/O Port, range 32, base 0xe060, size 32, enabled
    bar   [20] = type Memory, range 64, base 0xdda00000, size 16384, enabled
    cap 01[40] = powerspec 3  supports D0 D3  current D0
    cap 05[50] = MSI supports 1 message, 64 bit, vector masks 
    cap 11[70] = MSI-X supports 10 messages, enabled
                 Table in map 0x20[0x0], PBA in map 0x20[0x2000]
    cap 10[a0] = PCI-Express 2 root endpoint max data 512(512) FLR NS
                 max read 512
    ecap 0001[100] = AER 2 0 fatal 0 non-fatal 0 corrected
    ecap 0003[140] = Serial 1 0cc47affffab2934
    ecap 0017[1a0] = TPH Requester 1
    ecap 000d[1d0] = ACS 1 Source Validation unavailable, Translation Blocking unavailable
                     P2P Req Redirect unavailable, P2P Cmpl Redirect unavailable
                     P2P Upstream Forwarding unavailable, P2P Egress Control unavailable
                     P2P Direct Translated unavailable, Enhanced Capability unavailable
ehci0@pci0:0:22:0:	class=0x0c0320 rev=0x02 hdr=0x00 vendor=0x8086 device=0x1f2c subvendor=0x8086 subdevice=0x7270
    vendor     = 'Intel Corporation'
    device     = 'Atom processor C2000 USB Enhanced Host Controller'
    class      = serial bus
    subclass   = USB
    bar   [10] = type Memory, range 32, base 0xdda17000, size 1024, enabled
    cap 01[50] = powerspec 3  supports D0 D3  current D0
    cap 0a[58] = EHCI Debug Port at offset 0xa0 in map 0x14
    cap 13[98] = PCI Advanced Features: FLR TP
ahci0@pci0:0:23:0:	class=0x010601 rev=0x02 hdr=0x00 vendor=0x8086 device=0x1f22 subvendor=0x8086 subdevice=0x7270
    vendor     = 'Intel Corporation'
    device     = 'Atom processor C2000 AHCI SATA2 Controller'
    class      = mass storage
    subclass   = SATA
    bar   [10] = type I/O Port, range 32, base 0xe150, size 8, enabled
    bar   [14] = type I/O Port, range 32, base 0xe140, size 4, enabled
    bar   [18] = type I/O Port, range 32, base 0xe130, size 8, enabled
    bar   [1c] = type I/O Port, range 32, base 0xe120, size 4, enabled
    bar   [20] = type I/O Port, range 32, base 0xe040, size 32, enabled
    bar   [24] = type Memory, range 32, base 0xdda16000, size 2048, enabled
    cap 05[80] = MSI supports 1 message enabled with 1 message
    cap 01[70] = powerspec 3  supports D0 D3  current D0
    cap 12[a8] = SATA Index-Data Pair
ahci1@pci0:0:24:0:	class=0x010601 rev=0x02 hdr=0x00 vendor=0x8086 device=0x1f32 subvendor=0x8086 subdevice=0x7270
    vendor     = 'Intel Corporation'
    device     = 'Atom processor C2000 AHCI SATA3 Controller'
    class      = mass storage
    subclass   = SATA
    bar   [10] = type I/O Port, range 32, base 0xe110, size 8, enabled
    bar   [14] = type I/O Port, range 32, base 0xe100, size 4, enabled
    bar   [18] = type I/O Port, range 32, base 0xe0f0, size 8, enabled
    bar   [1c] = type I/O Port, range 32, base 0xe0e0, size 4, enabled
    bar   [20] = type I/O Port, range 32, base 0xe020, size 32, enabled
    bar   [24] = type Memory, range 32, base 0xdda15000, size 2048, enabled
    cap 05[80] = MSI supports 1 message enabled with 1 message
    cap 01[70] = powerspec 3  supports D0 D3  current D0
    cap 12[a8] = SATA Index-Data Pair
isab0@pci0:0:31:0:	class=0x060100 rev=0x02 hdr=0x00 vendor=0x8086 device=0x1f38 subvendor=0x8086 subdevice=0x7270
    vendor     = 'Intel Corporation'
    device     = 'Atom processor C2000 PCU'
    class      = bridge
    subclass   = PCI-ISA
    cap 09[e0] = vendor (length 12) Intel cap 1 version 0
		 features: 4 PCI-e x1 slots
ichsmb0@pci0:0:31:3:	class=0x0c0500 rev=0x02 hdr=0x00 vendor=0x8086 device=0x1f3c subvendor=0x8086 subdevice=0x7270
    vendor     = 'Intel Corporation'
    device     = 'Atom processor C2000 PCU SMBus'
    class      = serial bus
    subclass   = SMBus
    bar   [10] = type Memory, range 32, base 0xdda14000, size 32, enabled
    bar   [20] = type I/O Port, range 32, base 0xe000, size 32, enabled
pcib2@pci0:1:0:0:	class=0x060400 rev=0x03 hdr=0x01 vendor=0x1a03 device=0x1150 subvendor=0x1a03 subdevice=0x1150
    vendor     = 'ASPEED Technology, Inc.'
    device     = 'AST1150 PCI-to-PCI Bridge'
    class      = bridge
    subclass   = PCI-PCI
    cap 05[50] = MSI supports 1 message, 64 bit 
    cap 01[78] = powerspec 3  supports D0 D1 D2 D3  current D0
    cap 10[80] = PCI-Express 1 PCI bridge max data 128(128) NS
                 max read 512
                 link x1(x1) speed 2.5(2.5) ASPM disabled(L0s/L1)
    cap 0d[a4] = PCI Bridge subvendor=0x1a03 subdevice=0x1150
    ecap 0002[100] = VC 1 max VC0
    ecap 0001[800] = AER 1 0 fatal 0 non-fatal 1 corrected
vgapci0@pci0:2:0:0:	class=0x030000 rev=0x30 hdr=0x00 vendor=0x1a03 device=0x2000 subvendor=0x15d9 subdevice=0x0813
    vendor     = 'ASPEED Technology, Inc.'
    device     = 'ASPEED Graphics Family'
    class      = display
    subclass   = VGA
    bar   [10] = type Memory, range 32, base 0xde000000, size 16777216, enabled
    bar   [14] = type Memory, range 32, base 0xdf000000, size 131072, enabled
    bar   [18] = type I/O Port, range 32, base 0xd000, size 128, enabled
    cap 01[40] = powerspec 3  supports D0 D1 D2 D3  current D0
    cap 05[50] = MSI supports 4 messages, 64 bit 
xhci0@pci0:3:0:0:	class=0x0c0330 rev=0x03 hdr=0x00 vendor=0x1912 device=0x0014 subvendor=0x15d9 subdevice=0x0813
    vendor     = 'Renesas Electronics Corp.'
    device     = 'uPD720201 USB 3.0 Host Controller'
    class      = serial bus
    subclass   = USB
    bar   [10] = type Memory, range 64, base 0xdf200000, size 8192, enabled
    cap 01[50] = powerspec 3  supports D0 D3  current D0
    cap 05[70] = MSI supports 8 messages, 64 bit 
    cap 11[90] = MSI-X supports 8 messages, enabled
                 Table in map 0x10[0x1000], PBA in map 0x10[0x1080]
    cap 10[a0] = PCI-Express 2 endpoint max data 128(128) NS
                 max read 512
                 link x1(x1) speed 5.0(5.0) ASPM disabled(L0s/L1) ClockPM disabled
    ecap 0001[100] = AER 1 0 fatal 0 non-fatal 0 corrected
    ecap 0018[150] = LTR 1
t5iov0@pci0:4:0:0:	class=0x020000 rev=0x00 hdr=0x00 vendor=0x1425 device=0x5007 subvendor=0x1425 subdevice=0x0000
    vendor     = 'Chelsio Communications Inc'
    device     = 'T520-SO Unified Wire Ethernet Controller'
    class      = network
    subclass   = ethernet
    bar   [10] = type Memory, range 64, base 0xdd800000, size 524288, enabled
    bar   [18] = type Memory, range 64, base 0xdd780000, size 524288, enabled
    bar   [20] = type Memory, range 64, base 0xdd88c000, size 8192, enabled
    cap 01[40] = powerspec 3  supports D0 D3  current D0
    cap 05[50] = MSI supports 8 messages, 64 bit, vector masks 
    cap 10[70] = PCI-Express 2 endpoint max data 256(2048) FLR NS
                 max read 512
                 link x8(x8) speed 5.0(8.0)
    cap 11[b0] = MSI-X supports 34 messages
                 Table in map 0x20[0x0], PBA in map 0x20[0x1000]
    cap 03[d0] = VPD
    ecap 0001[100] = AER 2 0 fatal 0 non-fatal 1 corrected
    ecap 0002[140] = VC 1 max VC1
    ecap 0003[170] = Serial 1 0000000000000000
    ecap 000e[190] = ARI 1
    ecap 0019[1a0] = PCIe Sec 1 lane errors 0
    ecap 0010[1c0] = SR-IOV 1 IOV disabled, Memory Space disabled, ARI disabled
                     0 VFs configured out of 16 supported
                     First VF RID Offset 0x0008, VF RID Stride 0x0004
                     VF Device ID 0x5807
                     Page Sizes: 4096 (enabled), 8192, 65536, 262144, 1048576, 4194304
    ecap 0017[200] = TPH Requester 1
t5iov1@pci0:4:0:1:	class=0x020000 rev=0x00 hdr=0x00 vendor=0x1425 device=0x5007 subvendor=0x1425 subdevice=0x0000
    vendor     = 'Chelsio Communications Inc'
    device     = 'T520-SO Unified Wire Ethernet Controller'
    class      = network
    subclass   = ethernet
    bar   [10] = type Memory, range 64, base 0xdd680000, size 524288, enabled
    bar   [18] = type Memory, range 64, base 0xdd600000, size 524288, enabled
    bar   [20] = type Memory, range 64, base 0xdd88a000, size 8192, enabled
    cap 01[40] = powerspec 3  supports D0 D3  current D0
    cap 05[50] = MSI supports 8 messages, 64 bit, vector masks 
    cap 10[70] = PCI-Express 2 endpoint max data 256(2048) FLR NS
                 max read 512
                 link x8(x8) speed 5.0(8.0)
    cap 11[b0] = MSI-X supports 34 messages
                 Table in map 0x20[0x0], PBA in map 0x20[0x1000]
    cap 03[d0] = VPD
    ecap 0001[100] = AER 2 0 fatal 0 non-fatal 1 corrected
    ecap 0003[170] = Serial 1 0000000000000000
    ecap 000e[190] = ARI 1
    ecap 0019[1a0] = PCIe Sec 1 lane errors 0
    ecap 0010[1c0] = SR-IOV 1 IOV disabled, Memory Space disabled, ARI disabled
                     0 VFs configured out of 16 supported
                     First VF RID Offset 0x0008, VF RID Stride 0x0004
                     VF Device ID 0x5807
                     Page Sizes: 4096 (enabled), 8192, 65536, 262144, 1048576, 4194304
    ecap 0017[200] = TPH Requester 1
t5iov2@pci0:4:0:2:	class=0x020000 rev=0x00 hdr=0x00 vendor=0x1425 device=0x5007 subvendor=0x1425 subdevice=0x0000
    vendor     = 'Chelsio Communications Inc'
    device     = 'T520-SO Unified Wire Ethernet Controller'
    class      = network
    subclass   = ethernet
    bar   [10] = type Memory, range 64, base 0xdd500000, size 524288, enabled
    bar   [18] = type Memory, range 64, base 0xdd480000, size 524288, enabled
    bar   [20] = type Memory, range 64, base 0xdd888000, size 8192, enabled
    cap 01[40] = powerspec 3  supports D0 D3  current D0
    cap 05[50] = MSI supports 8 messages, 64 bit, vector masks 
    cap 10[70] = PCI-Express 2 endpoint max data 256(2048) FLR NS
                 max read 512
                 link x8(x8) speed 5.0(8.0)
    cap 11[b0] = MSI-X supports 34 messages
                 Table in map 0x20[0x0], PBA in map 0x20[0x1000]
    cap 03[d0] = VPD
    ecap 0001[100] = AER 2 0 fatal 0 non-fatal 1 corrected
    ecap 0003[170] = Serial 1 0000000000000000
    ecap 000e[190] = ARI 1
    ecap 0019[1a0] = PCIe Sec 1 lane errors 0
    ecap 0010[1c0] = SR-IOV 1 IOV disabled, Memory Space disabled, ARI disabled
                     0 VFs configured out of 16 supported
                     First VF RID Offset 0x0008, VF RID Stride 0x0004
                     VF Device ID 0x5807
                     Page Sizes: 4096 (enabled), 8192, 65536, 262144, 1048576, 4194304
    ecap 0017[200] = TPH Requester 1
t5iov3@pci0:4:0:3:	class=0x020000 rev=0x00 hdr=0x00 vendor=0x1425 device=0x5007 subvendor=0x1425 subdevice=0x0000
    vendor     = 'Chelsio Communications Inc'
    device     = 'T520-SO Unified Wire Ethernet Controller'
    class      = network
    subclass   = ethernet
    bar   [10] = type Memory, range 64, base 0xdd400000, size 524288, enabled
    bar   [18] = type Memory, range 64, base 0xdd380000, size 524288, enabled
    bar   [20] = type Memory, range 64, base 0xdd886000, size 8192, enabled
    cap 01[40] = powerspec 3  supports D0 D3  current D0
    cap 05[50] = MSI supports 8 messages, 64 bit, vector masks 
    cap 10[70] = PCI-Express 2 endpoint max data 256(2048) FLR NS
                 max read 512
                 link x8(x8) speed 5.0(8.0)
    cap 11[b0] = MSI-X supports 34 messages
                 Table in map 0x20[0x0], PBA in map 0x20[0x1000]
    cap 03[d0] = VPD
    ecap 0001[100] = AER 2 0 fatal 0 non-fatal 1 corrected
    ecap 0003[170] = Serial 1 0000000000000000
    ecap 000e[190] = ARI 1
    ecap 0019[1a0] = PCIe Sec 1 lane errors 0
    ecap 0010[1c0] = SR-IOV 1 IOV disabled, Memory Space disabled, ARI disabled
                     0 VFs configured out of 16 supported
                     First VF RID Offset 0x0008, VF RID Stride 0x0004
                     VF Device ID 0x5807
                     Page Sizes: 4096 (enabled), 8192, 65536, 262144, 1048576, 4194304
    ecap 0017[200] = TPH Requester 1
t5nex0@pci0:4:0:4:	class=0x020000 rev=0x00 hdr=0x00 vendor=0x1425 device=0x5407 subvendor=0x1425 subdevice=0x0000
    vendor     = 'Chelsio Communications Inc'
    device     = 'T520-SO Unified Wire Ethernet Controller'
    class      = network
    subclass   = ethernet
    bar   [10] = type Memory, range 64, base 0xdd300000, size 524288, enabled
    bar   [18] = type Memory, range 64, base 0xdc000000, size 16777216, enabled
    bar   [20] = type Memory, range 64, base 0xdd884000, size 8192, enabled
    cap 01[40] = powerspec 3  supports D0 D3  current D0
    cap 05[50] = MSI supports 32 messages, 64 bit, vector masks 
    cap 10[70] = PCI-Express 2 endpoint max data 256(2048) FLR NS
                 max read 4096
                 link x8(x8) speed 5.0(8.0)
    cap 11[b0] = MSI-X supports 256 messages, enabled
                 Table in map 0x20[0x0], PBA in map 0x20[0x1000]
    cap 03[d0] = VPD
    ecap 0001[100] = AER 2 0 fatal 0 non-fatal 1 corrected
    ecap 0003[170] = Serial 1 0000000000000000
    ecap 000e[190] = ARI 1
    ecap 0019[1a0] = PCIe Sec 1 lane errors 0
    ecap 0010[1c0] = SR-IOV 1 IOV disabled, Memory Space disabled, ARI disabled
                     0 VFs configured out of 0 supported
                     First VF RID Offset 0x0008, VF RID Stride 0x0004
                     VF Device ID 0x5807
                     Page Sizes: 4096 (enabled), 8192, 65536, 262144, 1048576, 4194304
    ecap 0017[200] = TPH Requester 1
none3@pci0:4:0:5:	class=0x010000 rev=0x00 hdr=0x00 vendor=0x1425 device=0x5507 subvendor=0x1425 subdevice=0x0000
    vendor     = 'Chelsio Communications Inc'
    device     = 'T520-SO Unified Wire Storage Controller'
    class      = mass storage
    subclass   = SCSI
    bar   [10] = type Memory, range 64, base 0xdd280000, size 524288, enabled
    bar   [18] = type Memory, range 64, base 0xdd200000, size 524288, enabled
    bar   [20] = type Memory, range 64, base 0xdd882000, size 8192, enabled
    cap 01[40] = powerspec 3  supports D0 D3  current D3
    cap 05[50] = MSI supports 32 messages, 64 bit, vector masks 
    cap 10[70] = PCI-Express 2 endpoint max data 256(2048) FLR NS
                 max read 512
                 link x8(x8) speed 5.0(8.0)
    cap 11[b0] = MSI-X supports 40 messages
                 Table in map 0x20[0x0], PBA in map 0x20[0x1000]
    cap 03[d0] = VPD
    ecap 0001[100] = AER 2 0 fatal 0 non-fatal 1 corrected
    ecap 0003[170] = Serial 1 0000000000000000
    ecap 000e[190] = ARI 1
    ecap 0019[1a0] = PCIe Sec 1 lane errors 0
    ecap 0010[1c0] = SR-IOV 1 IOV disabled, Memory Space disabled, ARI disabled
                     0 VFs configured out of 0 supported
                     First VF RID Offset 0x0008, VF RID Stride 0x0004
                     VF Device ID 0x5807
                     Page Sizes: 4096 (enabled), 8192, 65536, 262144, 1048576, 4194304
    ecap 0017[200] = TPH Requester 1
none4@pci0:4:0:6:	class=0x0c0400 rev=0x00 hdr=0x00 vendor=0x1425 device=0x5607 subvendor=0x1425 subdevice=0x0000
    vendor     = 'Chelsio Communications Inc'
    device     = 'T520-SO Unified Wire Storage Controller'
    class      = serial bus
    subclass   = Fibre Channel
    bar   [10] = type Memory, range 64, base 0xdd100000, size 524288, enabled
    bar   [18] = type Memory, range 64, base 0xdd080000, size 524288, enabled
    bar   [20] = type Memory, range 64, base 0xdd880000, size 8192, enabled
    cap 01[40] = powerspec 3  supports D0 D3  current D3
    cap 05[50] = MSI supports 32 messages, 64 bit, vector masks 
    cap 10[70] = PCI-Express 2 endpoint max data 256(2048) FLR NS
                 max read 512
                 link x8(x8) speed 5.0(8.0)
    cap 11[b0] = MSI-X supports 40 messages
                 Table in map 0x20[0x0], PBA in map 0x20[0x1000]
    cap 03[d0] = VPD
    ecap 0001[100] = AER 2 0 fatal 0 non-fatal 1 corrected
    ecap 0003[170] = Serial 1 0000000000000000
    ecap 000e[190] = ARI 1
    ecap 0019[1a0] = PCIe Sec 1 lane errors 0
    ecap 0010[1c0] = SR-IOV 1 IOV disabled, Memory Space disabled, ARI disabled
                     0 VFs configured out of 0 supported
                     First VF RID Offset 0x0008, VF RID Stride 0x0004
                     VF Device ID 0x5807
                     Page Sizes: 4096 (enabled), 8192, 65536, 262144, 1048576, 4194304
    ecap 0017[200] = TPH Requester 1
```
