---
title: PC Engines APU2C4
---
## dmesg

```
Copyright (c) 1992-2026 The FreeBSD Project.
Copyright (c) 1979, 1980, 1983, 1986, 1988, 1989, 1991, 1992, 1993, 1994
	The Regents of the University of California. All rights reserved.
FreeBSD is a registered trademark of The FreeBSD Foundation.
FreeBSD 16.0-CURRENT BSDRP-AMD64 amd64
FreeBSD clang version 21.1.8 (https://github.com/llvm/llvm-project.git llvmorg-21.1.8-0-g2078da43e25a)
VT(vga): text 80x25
CPU: AMD GX-412TC SOC                                (998.17-MHz K8-class CPU)
  Origin="AuthenticAMD"  Id=0x730f01  Family=0x16  Model=0x30  Stepping=1
  Features=0x178bfbff<FPU,VME,DE,PSE,TSC,MSR,PAE,MCE,CX8,APIC,SEP,MTRR,PGE,MCA,CMOV,PAT,PSE36,CLFLUSH,MMX,FXSR,SSE,SSE2,HTT>
  Features2=0x3ed8220b<SSE3,PCLMULQDQ,MON,SSSE3,CX16,SSE4.1,SSE4.2,MOVBE,POPCNT,AESNI,XSAVE,OSXSAVE,AVX,F16C>
  AMD Features=0x2e500800<SYSCALL,NX,MMX+,FFXSR,Page1GB,RDTSCP,LM>
  AMD Features2=0x1d4037ff<LAHF,CMP,SVM,ExtAPIC,CR8,ABM,SSE4A,MAS,Prefetch,OSVW,IBS,SKINIT,WDT,Topology,PNXC,DBE,PTSC,PL2I>
  Structured Extended Features=0x8<BMI1>
  XSAVE Features=0x1<XSAVEOPT>
  SVM: NP,NRIP,AFlush,DAssist,NAsids=8
  TSC: P-state invariant, performance statistics
real memory  = 4294967296 (4096 MB)
avail memory = 4108115968 (3917 MB)
Event timer "LAPIC" quality 100
ACPI APIC Table: <COREv4 COREBOOT>
FreeBSD/SMP: Multiprocessor System Detected: 4 CPUs
FreeBSD/SMP: 1 package(s) x 4 core(s)
random: unblocking device.
ioapic0 <Version 2.1> irqs 0-23
ioapic1 <Version 2.1> irqs 24-55
Launching APs: 1 2 3
random: entropy device external interface
vtvga0: <VT VGA driver>
smbios0: <System Management BIOS> at iomem 0xf29c0-0xf29d7
smbios0: Entry point: v3 (64-bit), Version: 3.0
aesni0: <AES-CBC,AES-CCM,AES-GCM,AES-ICM,AES-XTS>
acpi0: <COREv4 COREBOOT>
acpi0: Power Button (fixed)
atrtc0: <AT realtime clock> port 0x70-0x71 irq 8 on acpi0
atrtc0: registered as a time-of-day clock, resolution 1.000000s
Event timer "RTC" frequency 32768 Hz quality 0
attimer0: <AT timer> port 0x40-0x43 irq 0 on acpi0
Timecounter "i8254" frequency 1193182 Hz quality 0
Event timer "i8254" frequency 1193182 Hz quality 100
apei0: <ACPI Platform Error Interface> on acpi0
hest0: <APEI Hardware Errors> on apei0
hpet0: <High Precision Event Timer> iomem 0xfed00000-0xfed003ff on acpi0
Timecounter "HPET" frequency 14318180 Hz quality 950
Timecounter "ACPI-fast" frequency 3579545 Hz quality 900
acpi_timer0: <32-bit timer at 3.579545MHz> port 0x818-0x81b on acpi0
cpu0: <ACPI CPU> on acpi0
pcib0: <ACPI Host-PCI bridge> port 0xcf8-0xcff on acpi0
pci0: <ACPI PCI bus> on pcib0
pci0: <base peripheral, IOMMU> at device 0.2 (no driver attached)
pcib1: <ACPI PCI-PCI bridge> irq 25 at device 2.2 on pci0
pcib1: failed to allocate initial I/O port window: 0x1000-0x1fff
pci1: <ACPI PCI bus> on pcib1
igb0: <Intel(R) I210 Flashless (Copper)> port 0x2000-0x201f mem 0xd0000000-0xd001ffff,0xd0020000-0xd0023fff irq 28 at device 0.0 on pci1
igb0: NVM V0.6 imgtype5
igb0: Using 1024 TX descriptors and 1024 RX descriptors
igb0: Using 4 RX queues 4 TX queues
igb0: Using MSI-X interrupts with 5 vectors
igb0: Ethernet address: 00:0d:b9:41:ca:3c
igb0: netmap queues/slots: TX 4/1024, RX 4/1024
pcib2: <ACPI PCI-PCI bridge> irq 26 at device 2.3 on pci0
pcib2: failed to allocate initial I/O port window: 0x2000-0x2fff
pci2: <ACPI PCI bus> on pcib2
igb1: <Intel(R) I210 Flashless (Copper)> port 0x3000-0x301f mem 0xd0100000-0xd011ffff,0xd0120000-0xd0123fff irq 32 at device 0.0 on pci2
igb1: NVM V0.6 imgtype5
igb1: Using 1024 TX descriptors and 1024 RX descriptors
igb1: Using 4 RX queues 4 TX queues
igb1: Using MSI-X interrupts with 5 vectors
igb1: Ethernet address: 00:0d:b9:41:ca:3d
igb1: netmap queues/slots: TX 4/1024, RX 4/1024
pcib3: <ACPI PCI-PCI bridge> irq 27 at device 2.4 on pci0
pcib3: failed to allocate initial I/O port window: 0x3000-0x3fff
pci3: <ACPI PCI bus> on pcib3
igb2: <Intel(R) I210 Flashless (Copper)> port 0x5000-0x501f mem 0xd0200000-0xd021ffff,0xd0220000-0xd0223fff irq 36 at device 0.0 on pci3
igb2: NVM V0.6 imgtype5
igb2: Using 1024 TX descriptors and 1024 RX descriptors
igb2: Using 4 RX queues 4 TX queues
igb2: Using MSI-X interrupts with 5 vectors
igb2: Ethernet address: 00:0d:b9:41:ca:3e
igb2: netmap queues/slots: TX 4/1024, RX 4/1024
pci0: <encrypt/decrypt> at device 8.0 (no driver attached)
xhci0: <AMD FCH USB 3.0 controller> mem 0xd0522000-0xd0523fff irq 18 at device 16.0 on pci0
xhci0: 32 bytes context size, 64-bit DMA
xhci0: xECP capabilities <LEGACY,PROTO,PROTO,DEBUG>
usbus0 on xhci0
usbus0: 5.0Gbps Super Speed USB v3.0
ahci0: <AMD Hudson-2 AHCI SATA controller> port 0x4010-0x4017,0x4020-0x4023,0x4018-0x401f,0x4024-0x4027,0x4000-0x400f mem 0xd0525000-0xd05253ff at device 17.0 on pci0
ahci0: AHCI v1.30 with 2 6Gbps ports, Port Multiplier supported with FBS
ahcich0: <AHCI channel> at channel 0 on ahci0
ahcich1: <AHCI channel> at channel 1 on ahci0
sdhci_pci0: <Generic SD HCI> mem 0xd0527000-0xd05270ff at device 20.7 on pci0
sdhci_pci0: 1 slot(s) allocated
acpi_tz0: <Thermal Zone> on acpi0
uart0: <16550 or compatible> port 0x3f8-0x3ff irq 4 flags 0x10 on acpi0
uart1: <16550 or compatible> port 0x2f8-0x2ff irq 3 on acpi0
hwpstate_amd0: <Cool`n'Quiet 2.0> on cpu0
cpufreq0: <CPU frequency control> on cpu0
cpufreq1: <CPU frequency control> on cpu1
cpufreq2: <CPU frequency control> on cpu2
cpufreq3: <CPU frequency control> on cpu3
Timecounter "TSC" frequency 998127958 Hz quality 1000
Timecounters tick every 1.000 msec
ugen0.1: <AMD XHCI root HUB> at usbus0
uhub0 on usbus0
uhub0: <AMD XHCI root HUB, class 9/0, rev 3.00/1.00, addr 1> on usbus0
ada0 at ahcich0 bus 0 scbus0 target 0 lun 0
ada0: <SATA SSD S9FM02.8> ACS-3 ATA SATA 3.x device
ada0: Serial Number 1B060766160804907006
ada0: 600.000MB/s transfers (SATA 3.x, UDMA6, PIO 8192bytes)
ada0: Command Queueing enabled
ada0: 15272MB (31277232 512 byte sectors)
Trying to mount root from ufs:/dev/gpt/BSDRP1 [ro]...
uhub0: 4 ports with 4 removable, self powered
lo0: link state changed to UP
igb0: link state changed to UP
igb1: link state changed to UP
igb2: link state changed to UP
```

## pciconf

```
hostb0@pci0:0:0:0:	class=0x060000 rev=0x00 hdr=0x00 vendor=0x1022 device=0x1566 subvendor=0x1022 subdevice=0x1566
    vendor     = 'Advanced Micro Devices, Inc. [AMD]'
    device     = 'Family 16h (Models 30h-3fh) Processor Root Complex'
    class      = bridge
    subclass   = HOST-PCI
none0@pci0:0:0:2:	class=0x080600 rev=0x00 hdr=0x00 vendor=0x1022 device=0x1567 subvendor=0x1022 subdevice=0x1567
    vendor     = 'Advanced Micro Devices, Inc. [AMD]'
    device     = 'Mullins IOMMU'
    class      = base peripheral
    subclass   = IOMMU
    cap 0f[40] = AMD IOMMU Base Capability Base=000000000000000000/Disabled
		CapExt,EFRSup,IotlbSup
		UnitId=0
		MsiNum=0 MsiNumPPR=0 HtAtsResv=0 MsiNumGA=0
		VAsize=64bit PAsize=48bit GVAsize=48bit
    cap 05[64] = MSI supports 4 messages, 64 bit 
    cap 08[74] = HT MSI fixed address window enabled at 0xfee00000
hostb1@pci0:0:2:0:	class=0x060000 rev=0x00 hdr=0x00 vendor=0x1022 device=0x156b subvendor=0x0000 subdevice=0x0000
    vendor     = 'Advanced Micro Devices, Inc. [AMD]'
    device     = 'Family 16h (Models 30h-3fh) Host Bridge'
    class      = bridge
    subclass   = HOST-PCI
pcib1@pci0:0:2:2:	class=0x060400 rev=0x00 hdr=0x01 vendor=0x1022 device=0x1439 subvendor=0x1022 subdevice=0x1234
    vendor     = 'Advanced Micro Devices, Inc. [AMD]'
    device     = 'Family 16h Processor Functions 5:1'
    class      = bridge
    subclass   = PCI-PCI
    cap 01[50] = powerspec 3  supports D0 D3  current D0
    cap 10[58] = PCI-Express 2 root port max data 256(512) RO NS
                 max read 512
                 link x1(x1) speed 2.5(5.0) ASPM disabled(L0s/L1)
                 slot 0 power limit 0 mW
    cap 05[a0] = MSI supports 1 message, 64 bit 
    cap 0d[b0] = PCI Bridge subvendor=0x1022 subdevice=0x1234
    cap 08[b8] = HT MSI fixed address window enabled at 0xfee00000
    ecap 000b[100] = Vendor [1] ID 0001 Rev 1 Length 16
    ecap 0001[150] = AER 2 0 fatal 0 non-fatal 0 corrected
    ecap 000d[2a0] = ACS 1 Source Validation disabled, Translation Blocking disabled
                     P2P Req Redirect unavailable, P2P Cmpl Redirect unavailable
                     P2P Upstream Forwarding unavailable, P2P Egress Control unavailable
                     P2P Direct Translated unavailable, Enhanced Capability unavailable
pcib2@pci0:0:2:3:	class=0x060400 rev=0x00 hdr=0x01 vendor=0x1022 device=0x1439 subvendor=0x1022 subdevice=0x1234
    vendor     = 'Advanced Micro Devices, Inc. [AMD]'
    device     = 'Family 16h Processor Functions 5:1'
    class      = bridge
    subclass   = PCI-PCI
    cap 01[50] = powerspec 3  supports D0 D3  current D0
    cap 10[58] = PCI-Express 2 root port max data 256(512) RO NS
                 max read 512
                 link x1(x1) speed 2.5(5.0) ASPM disabled(L0s/L1)
                 slot 0 power limit 0 mW
    cap 05[a0] = MSI supports 1 message, 64 bit 
    cap 0d[b0] = PCI Bridge subvendor=0x1022 subdevice=0x1234
    cap 08[b8] = HT MSI fixed address window enabled at 0xfee00000
    ecap 000b[100] = Vendor [1] ID 0001 Rev 1 Length 16
    ecap 0001[150] = AER 2 0 fatal 0 non-fatal 0 corrected
    ecap 000d[2a0] = ACS 1 Source Validation disabled, Translation Blocking disabled
                     P2P Req Redirect unavailable, P2P Cmpl Redirect unavailable
                     P2P Upstream Forwarding unavailable, P2P Egress Control unavailable
                     P2P Direct Translated unavailable, Enhanced Capability unavailable
pcib3@pci0:0:2:4:	class=0x060400 rev=0x00 hdr=0x01 vendor=0x1022 device=0x1439 subvendor=0x1022 subdevice=0x1234
    vendor     = 'Advanced Micro Devices, Inc. [AMD]'
    device     = 'Family 16h Processor Functions 5:1'
    class      = bridge
    subclass   = PCI-PCI
    cap 01[50] = powerspec 3  supports D0 D3  current D0
    cap 10[58] = PCI-Express 2 root port max data 256(512) RO NS
                 max read 512
                 link x1(x1) speed 2.5(5.0) ASPM disabled(L0s/L1)
                 slot 0 power limit 0 mW
    cap 05[a0] = MSI supports 1 message, 64 bit 
    cap 0d[b0] = PCI Bridge subvendor=0x1022 subdevice=0x1234
    cap 08[b8] = HT MSI fixed address window enabled at 0xfee00000
    ecap 000b[100] = Vendor [1] ID 0001 Rev 1 Length 16
    ecap 0001[150] = AER 2 0 fatal 0 non-fatal 0 corrected
    ecap 000d[2a0] = ACS 1 Source Validation disabled, Translation Blocking disabled
                     P2P Req Redirect unavailable, P2P Cmpl Redirect unavailable
                     P2P Upstream Forwarding unavailable, P2P Egress Control unavailable
                     P2P Direct Translated unavailable, Enhanced Capability unavailable
none1@pci0:0:8:0:	class=0x108000 rev=0x00 hdr=0x00 vendor=0x1022 device=0x1537 subvendor=0x1022 subdevice=0x1537
    vendor     = 'Advanced Micro Devices, Inc. [AMD]'
    device     = 'Kabini/Mullins PSP-Platform Security Processor'
    class      = encrypt/decrypt
    bar   [10] = type Prefetchable Memory, range 64, base 0xd0500000, size 131072, enabled
    bar   [18] = type Memory, range 32, base 0xd0300000, size 1048576, enabled
    bar   [1c] = type Memory, range 32, base 0xd0524000, size 4096, enabled
    bar   [20] = type Memory, range 32, base 0xd0400000, size 1048576, enabled
    bar   [24] = type Memory, range 32, base 0xd0520000, size 8192, enabled
    cap 11[50] = MSI-X supports 2 messages
                 Table in map 0x24[0x0], PBA in map 0x24[0x1000]
    cap 08[5c] = HT MSI fixed address window enabled at 0xfee00000
    cap 01[60] = powerspec 3  supports D0 D3  current D0
xhci0@pci0:0:16:0:	class=0x0c0330 rev=0x11 hdr=0x00 vendor=0x1022 device=0x7814 subvendor=0x1022 subdevice=0x1410
    vendor     = 'Advanced Micro Devices, Inc. [AMD]'
    device     = 'FCH USB XHCI Controller'
    class      = serial bus
    subclass   = USB
    bar   [10] = type Memory, range 64, base 0xd0522000, size 8192, enabled
    cap 01[50] = powerspec 3  supports D0 D3  current D0
    cap 05[70] = MSI supports 8 messages, 64 bit 
    cap 11[90] = MSI-X supports 8 messages, enabled
                 Table in map 0x10[0x1000], PBA in map 0x10[0x1080]
    cap 10[a0] = PCI-Express 2 root endpoint max data 128(128) NS
                 max read 512
    ecap 0018[100] = LTR 1
ahci0@pci0:0:17:0:	class=0x010601 rev=0x40 hdr=0x00 vendor=0x1022 device=0x7801 subvendor=0x1022 subdevice=0x7801
    vendor     = 'Advanced Micro Devices, Inc. [AMD]'
    device     = 'FCH SATA Controller [AHCI mode]'
    class      = mass storage
    subclass   = SATA
    bar   [10] = type I/O Port, range 32, base 0x4010, size 8, enabled
    bar   [14] = type I/O Port, range 32, base 0x4020, size 4, enabled
    bar   [18] = type I/O Port, range 32, base 0x4018, size 8, enabled
    bar   [1c] = type I/O Port, range 32, base 0x4024, size 4, enabled
    bar   [20] = type I/O Port, range 32, base 0x4000, size 16, enabled
    bar   [24] = type Memory, range 32, base 0xd0525000, size 1024, enabled
    cap 01[60] = powerspec 3  supports D0 D3  current D0
    cap 12[70] = SATA Index-Data Pair
none2@pci0:0:19:0:	class=0x0c0320 rev=0x39 hdr=0x00 vendor=0x1022 device=0x7808 subvendor=0x1022 subdevice=0x7808
    vendor     = 'Advanced Micro Devices, Inc. [AMD]'
    device     = 'FCH USB EHCI Controller'
    class      = serial bus
    subclass   = USB
    bar   [10] = type Memory, range 32, base 0xd0526000, size 256, enabled
    cap 01[c0] = powerspec 2  supports D0 D1 D2 D3  current D0
    cap 0a[e4] = EHCI Debug Port at offset 0xe0 in map 0x14
none3@pci0:0:20:0:	class=0x0c0500 rev=0x42 hdr=0x00 vendor=0x1022 device=0x780b subvendor=0x1022 subdevice=0x780b
    vendor     = 'Advanced Micro Devices, Inc. [AMD]'
    device     = 'FCH SMBus Controller'
    class      = serial bus
    subclass   = SMBus
none4@pci0:0:20:3:	class=0x060100 rev=0x11 hdr=0x00 vendor=0x1022 device=0x780e subvendor=0x1022 subdevice=0x780e
    vendor     = 'Advanced Micro Devices, Inc. [AMD]'
    device     = 'FCH LPC Bridge'
    class      = bridge
    subclass   = PCI-ISA
sdhci_pci0@pci0:0:20:7:	class=0x080501 rev=0x01 hdr=0x00 vendor=0x1022 device=0x7813 subvendor=0x1022 subdevice=0x7806
    vendor     = 'Advanced Micro Devices, Inc. [AMD]'
    device     = 'FCH SD Flash Controller'
    class      = base peripheral
    subclass   = SD host controller
    bar   [10] = type Memory, range 64, base 0xd0527000, size 256, enabled
hostb2@pci0:0:24:0:	class=0x060000 rev=0x00 hdr=0x00 vendor=0x1022 device=0x1580 subvendor=0x0000 subdevice=0x0000
    vendor     = 'Advanced Micro Devices, Inc. [AMD]'
    device     = 'Family 16h (Models 30h-3fh) Processor Function 0'
    class      = bridge
    subclass   = HOST-PCI
hostb3@pci0:0:24:1:	class=0x060000 rev=0x00 hdr=0x00 vendor=0x1022 device=0x1581 subvendor=0x0000 subdevice=0x0000
    vendor     = 'Advanced Micro Devices, Inc. [AMD]'
    device     = 'Family 16h (Models 30h-3fh) Processor Function 1'
    class      = bridge
    subclass   = HOST-PCI
hostb4@pci0:0:24:2:	class=0x060000 rev=0x00 hdr=0x00 vendor=0x1022 device=0x1582 subvendor=0x0000 subdevice=0x0000
    vendor     = 'Advanced Micro Devices, Inc. [AMD]'
    device     = 'Family 16h (Models 30h-3fh) Processor Function 2'
    class      = bridge
    subclass   = HOST-PCI
hostb5@pci0:0:24:3:	class=0x060000 rev=0x00 hdr=0x00 vendor=0x1022 device=0x1583 subvendor=0x0000 subdevice=0x0000
    vendor     = 'Advanced Micro Devices, Inc. [AMD]'
    device     = 'Family 16h (Models 30h-3fh) Processor Function 3'
    class      = bridge
    subclass   = HOST-PCI
    cap 0f[f0] = Secure Device Type=0x0 Rev=0x02

hostb6@pci0:0:24:4:	class=0x060000 rev=0x00 hdr=0x00 vendor=0x1022 device=0x1584 subvendor=0x0000 subdevice=0x0000
    vendor     = 'Advanced Micro Devices, Inc. [AMD]'
    device     = 'Family 16h (Models 30h-3fh) Processor Function 4'
    class      = bridge
    subclass   = HOST-PCI
hostb7@pci0:0:24:5:	class=0x060000 rev=0x00 hdr=0x00 vendor=0x1022 device=0x1585 subvendor=0x0000 subdevice=0x0000
    vendor     = 'Advanced Micro Devices, Inc. [AMD]'
    device     = 'Family 16h (Models 30h-3fh) Processor Function 5'
    class      = bridge
    subclass   = HOST-PCI
igb0@pci0:1:0:0:	class=0x020000 rev=0x03 hdr=0x00 vendor=0x8086 device=0x157b subvendor=0x8086 subdevice=0x0000
    vendor     = 'Intel Corporation'
    device     = 'I210 Gigabit Network Connection'
    class      = network
    subclass   = ethernet
    bar   [10] = type Memory, range 32, base 0xd0000000, size 131072, enabled
    bar   [18] = type I/O Port, range 32, base 0x2000, size 32, enabled
    bar   [1c] = type Memory, range 32, base 0xd0020000, size 16384, enabled
    cap 01[40] = powerspec 3  supports D0 D3  current D0
    cap 05[50] = MSI supports 1 message, 64 bit, vector masks 
    cap 11[70] = MSI-X supports 5 messages, enabled
                 Table in map 0x1c[0x0], PBA in map 0x1c[0x2000]
    cap 10[a0] = PCI-Express 2 endpoint max data 256(512) FLR RO NS
                 max read 512
                 link x1(x1) speed 2.5(2.5) ASPM disabled(L0s/L1)
    ecap 0001[100] = AER 2 0 fatal 0 non-fatal 0 corrected
    ecap 0003[140] = Serial 1 000db9ffff41ca3c
    ecap 0017[1a0] = TPH Requester 1
igb1@pci0:2:0:0:	class=0x020000 rev=0x03 hdr=0x00 vendor=0x8086 device=0x157b subvendor=0x8086 subdevice=0x0000
    vendor     = 'Intel Corporation'
    device     = 'I210 Gigabit Network Connection'
    class      = network
    subclass   = ethernet
    bar   [10] = type Memory, range 32, base 0xd0100000, size 131072, enabled
    bar   [18] = type I/O Port, range 32, base 0x3000, size 32, enabled
    bar   [1c] = type Memory, range 32, base 0xd0120000, size 16384, enabled
    cap 01[40] = powerspec 3  supports D0 D3  current D0
    cap 05[50] = MSI supports 1 message, 64 bit, vector masks 
    cap 11[70] = MSI-X supports 5 messages, enabled
                 Table in map 0x1c[0x0], PBA in map 0x1c[0x2000]
    cap 10[a0] = PCI-Express 2 endpoint max data 256(512) FLR RO NS
                 max read 512
                 link x1(x1) speed 2.5(2.5) ASPM disabled(L0s/L1)
    ecap 0001[100] = AER 2 0 fatal 0 non-fatal 0 corrected
    ecap 0003[140] = Serial 1 000db9ffff41ca3d
    ecap 0017[1a0] = TPH Requester 1
igb2@pci0:3:0:0:	class=0x020000 rev=0x03 hdr=0x00 vendor=0x8086 device=0x157b subvendor=0x8086 subdevice=0x0000
    vendor     = 'Intel Corporation'
    device     = 'I210 Gigabit Network Connection'
    class      = network
    subclass   = ethernet
    bar   [10] = type Memory, range 32, base 0xd0200000, size 131072, enabled
    bar   [18] = type I/O Port, range 32, base 0x5000, size 32, enabled
    bar   [1c] = type Memory, range 32, base 0xd0220000, size 16384, enabled
    cap 01[40] = powerspec 3  supports D0 D3  current D0
    cap 05[50] = MSI supports 1 message, 64 bit, vector masks 
    cap 11[70] = MSI-X supports 5 messages, enabled
                 Table in map 0x1c[0x0], PBA in map 0x1c[0x2000]
    cap 10[a0] = PCI-Express 2 endpoint max data 256(512) FLR RO NS
                 max read 512
                 link x1(x1) speed 2.5(2.5) ASPM disabled(L0s/L1)
    ecap 0001[100] = AER 2 0 fatal 0 non-fatal 0 corrected
    ecap 0003[140] = Serial 1 000db9ffff41ca3e
    ecap 0017[1a0] = TPH Requester 1
```
