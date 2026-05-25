---
title: Netgate RCC-VE 4860
---
## dmesg

```
Copyright (c) 1992-2014 The FreeBSD Project.
Copyright (c) 1979, 1980, 1983, 1986, 1988, 1989, 1991, 1992, 1993, 1994
        The Regents of the University of California. All rights reserved.
FreeBSD is a registered trademark of The FreeBSD Foundation.
FreeBSD 10.1-RELEASE-p10 #0 r282880M: Fri May 15 23:47:37 CEST 2015
    root@orange.bsdrp.net:/usr/obj/BSDRP.amd64/usr/local/BSDRP/BSDRP/FreeBSD/src/sys/amd64 amd64
FreeBSD clang version 3.4.1 (tags/RELEASE_34/dot1-final 208032) 20140512
CPU: Intel(R) Atom(TM) CPU  C2558  @ 2.40GHz (2400.06-MHz K8-class CPU)
  Origin = "GenuineIntel"  Id = 0x406d8  Family = 0x6  Model = 0x4d  Stepping = 8
  Features=0xbfebfbff<FPU,VME,DE,PSE,TSC,MSR,PAE,MCE,CX8,APIC,SEP,MTRR,PGE,MCA,CMOV,PAT,PSE36,CLFLUSH,DTS,ACPI,M
MX,FXSR,SSE,SSE2,SS,HTT,TM,PBE>
  Features2=0x43d8e3bf<SSE3,PCLMULQDQ,DTES64,MON,DS_CPL,VMX,EST,TM2,SSSE3,CX16,xTPR,PDCM,SSE4.1,SSE4.2,MOVBE,POP
CNT,TSCDLT,AESNI,RDRAND>
  AMD Features=0x28100800<SYSCALL,NX,RDTSCP,LM>
  AMD Features2=0x101<LAHF,Prefetch>
  Structured Extended Features=0x2282<TSCADJ,SMEP,ERMS>
  VT-x: PAT,HLT,MTF,PAUSE,EPT,UG,VPID
  TSC: P-state invariant, performance statistics
real memory  = 10737418240 (10240 MB)
avail memory = 8235925504 (7854 MB)
Event timer "LAPIC" quality 600
ACPI APIC Table: <CORE   COREBOOT>
FreeBSD/SMP: Multiprocessor System Detected: 4 CPUs
FreeBSD/SMP: 1 package(s) x 4 core(s)
 cpu0 (BSP): APIC ID:  0
 cpu1 (AP): APIC ID:  2
 cpu2 (AP): APIC ID:  4
 cpu3 (AP): APIC ID:  6
ioapic0 <Version 2.0> irqs 0-23 on motherboard
netmap: loaded module
random: <Software, Yarrow> initialized
module_register_init: MOD_LOAD (vesa, 0xffffffff80b873e0, 0) error 19
cryptosoft0: <software crypto> on motherboard
acpi0: <CORE COREBOOT> on motherboard
acpi0: Power Button (fixed)
hpet0: invalid period
device_attach: hpet0 attach returned 6
cpu0: <ACPI CPU> on acpi0
cpu1: <ACPI CPU> on acpi0
cpu2: <ACPI CPU> on acpi0
cpu3: <ACPI CPU> on acpi0
hpet0: invalid period
device_attach: hpet0 attach returned 6
atrtc0: <AT realtime clock> port 0x70-0x77 on acpi0
Event timer "RTC" frequency 32768 Hz quality 0
attimer0: <AT timer> port 0x40-0x43,0x50-0x53 irq 0 on acpi0
Timecounter "i8254" frequency 1193182 Hz quality 0
Event timer "i8254" frequency 1193182 Hz quality 100
Timecounter "ACPI-safe" frequency 3579545 Hz quality 850
acpi_timer0: <24-bit timer at 3.579545MHz> port 0x408-0x40b on acpi0
pcib0: <ACPI Host-PCI bridge> port 0xcf8-0xcff on acpi0
pci0: <ACPI PCI bus> on pcib0
pcib1: <ACPI PCI-PCI bridge> mem 0xdfe00000-0xdfe1ffff irq 16 at device 1.0 on pci0
pci1: <ACPI PCI bus> on pcib1
pcib2: <ACPI PCI-PCI bridge> mem 0xdfe20000-0xdfe3ffff irq 19 at device 2.0 on pci0
pci2: <ACPI PCI bus> on pcib2
pcib3: <ACPI PCI-PCI bridge> mem 0xdfe40000-0xdfe5ffff irq 20 at device 3.0 on pci0
pci3: <ACPI PCI bus> on pcib3
igb0: <Intel(R) PRO/1000 Network Connection version - 2.4.0> port 0x1000-0x101f mem 0xdfc00000-0xdfc1ffff,0xdfc2
0000-0xdfc23fff irq 18 at device 0.0 on pci3
igb0: Using MSIX interrupts with 3 vectors
igb0: Ethernet address: 00:08:a2:09:33:de
igb0: Bound queue 0 to cpu 0
igb0: Bound queue 1 to cpu 1
001.000008 [2705] netmap_attach             success for igb0 tx 2/2048 rx 2/2048 queues/slots
pcib4: <ACPI PCI-PCI bridge> mem 0xdfe60000-0xdfe7ffff irq 23 at device 4.0 on pci0
pci4: <ACPI PCI bus> on pcib4
igb1: <Intel(R) PRO/1000 Network Connection version - 2.4.0> port 0x2000-0x201f mem 0xdfd00000-0xdfd1ffff,0xdfd2
0000-0xdfd23fff irq 19 at device 0.0 on pci4
igb1: Using MSIX interrupts with 3 vectors
igb1: Ethernet address: 00:08:a2:09:33:df
igb1: Bound queue 0 to cpu 2
igb1: Bound queue 1 to cpu 3
001.000009 [2705] netmap_attach             success for igb1 tx 2/2048 rx 2/2048 queues/slots
pci0: <processor> at device 11.0 (no driver attached)
pci0: <base peripheral, IOMMU> at device 15.0 (no driver attached)
igb2: <Intel(R) PRO/1000 Network Connection version - 2.4.0> port 0x3000-0x301f mem 0xdfea0000-0xdfebffff,0xdff2
4000-0xdff27fff irq 18 at device 20.0 on pci0
igb2: Using MSIX interrupts with 5 vectors
igb2: Ethernet address: 00:08:a2:09:33:da
igb2: Bound queue 0 to cpu 0
igb2: Bound queue 1 to cpu 1
igb2: Bound queue 2 to cpu 2
igb2: Bound queue 3 to cpu 3
001.000010 [2705] netmap_attach             success for igb2 tx 4/2048 rx 4/2048 queues/slots
igb3: <Intel(R) PRO/1000 Network Connection version - 2.4.0> port 0x3020-0x303f mem 0xdfec0000-0xdfedffff,0xdff2
8000-0xdff2bfff irq 19 at device 20.1 on pci0
igb3: Using MSIX interrupts with 5 vectors
igb3: Ethernet address: 00:08:a2:09:33:db
igb3: Bound queue 0 to cpu 0
igb3: Bound queue 1 to cpu 1
igb3: Bound queue 2 to cpu 2
igb3: Bound queue 3 to cpu 3
001.000011 [2705] netmap_attach             success for igb3 tx 4/2048 rx 4/2048 queues/slots
igb4: <Intel(R) PRO/1000 Network Connection version - 2.4.0> port 0x3040-0x305f mem 0xdfee0000-0xdfefffff,0xdff2
c000-0xdff2ffff irq 20 at device 20.2 on pci0
igb4: Using MSIX interrupts with 5 vectors
igb4: Ethernet address: 00:08:a2:09:33:dc
igb4: Bound queue 0 to cpu 0
igb4: Bound queue 1 to cpu 1
igb4: Bound queue 2 to cpu 2
igb4: Bound queue 3 to cpu 3
001.000012 [2705] netmap_attach             success for igb4 tx 4/2048 rx 4/2048 queues/slots
igb5: <Intel(R) PRO/1000 Network Connection version - 2.4.0> port 0x3060-0x307f mem 0xdff00000-0xdff1ffff,0xdff3
0000-0xdff33fff irq 21 at device 20.3 on pci0
igb5: Using MSIX interrupts with 5 vectors
igb5: Ethernet address: 00:08:a2:09:33:dd
igb5: Bound queue 0 to cpu 0
igb5: Bound queue 1 to cpu 1
igb5: Bound queue 2 to cpu 2
igb5: Bound queue 3 to cpu 3
001.000013 [2705] netmap_attach             success for igb5 tx 4/2048 rx 4/2048 queues/slots
ehci0: <Intel Avoton USB 2.0 controller> mem 0xdff35400-0xdff357ff irq 22 at device 22.0 on pci0
usbus0: EHCI version 1.0
usbus0 on ehci0
ahci0: <Intel Avoton AHCI SATA controller> port 0x30c0-0x30c7,0x30e0-0x30e3,0x30c8-0x30cf,0x30e4-0x30e7,0x3080-0
x309f mem 0xdff34000-0xdff347ff irq 23 at device 23.0 on pci0
ahci0: AHCI v1.30 with 4 3Gbps ports, Port Multiplier not supported
ahci1: <Intel Avoton AHCI SATA controller> port 0x30d0-0x30d7,0x30e8-0x30eb,0x30d8-0x30df,0x30ec-0x30ef,0x30a0-0
x30bf mem 0xdff34800-0xdff34fff irq 16 at device 24.0 on pci0
ahci1: AHCI v1.30 with 2 6Gbps ports, Port Multiplier not supported
isab0: <PCI-ISA bridge> at device 31.0 on pci0
isa0: <ISA bus> on isab0
orm0: <ISA Option ROM> at iomem 0xc0000-0xc0fff on isa0
uart0: <16550 or compatible> at port 0x3f8-0x3ff irq 4 flags 0x10 on isa0
uart1: <16550 or compatible> at port 0x2f8-0x2ff irq 3 on isa0
uart1: console (115200,n,8,1)
est0: <Enhanced SpeedStep Frequency Control> on cpu0
p4tcc0: <CPU Frequency Thermal Control> on cpu0
est1: <Enhanced SpeedStep Frequency Control> on cpu1
p4tcc1: <CPU Frequency Thermal Control> on cpu1
est2: <Enhanced SpeedStep Frequency Control> on cpu2
p4tcc2: <CPU Frequency Thermal Control> on cpu2
est3: <Enhanced SpeedStep Frequency Control> on cpu3
p4tcc3: <CPU Frequency Thermal Control> on cpu3
Timecounters tick every 1.000 msec
IPsec: Initialized Security Association Processing.
random: unblocking device.
usbus0: 480Mbps High Speed USB v2.0
ugen0.1: <Intel> at usbus0
uhub0: <Intel EHCI root HUB, class 9/0, rev 2.00/1.00, addr 1> on usbus0
SMP: AP CPU #2 Launched!
SMP: AP CPU #1 Launched!
SMP: AP CPU #3 Launched!
Timecounter "TSC-low" frequency 1200029064 Hz quality 1000
Root mount waiting for: usbus0
Root mount waiting for: usbus0
Root mount waiting for: usbus0
Root mount waiting for: usbus0
uhub0: 8 ports with 8 removable, self powered
Root mount waiting for: usbus0
ugen0.2: <vendor 0x8087> at usbus0
uhub1: <vendor 0x8087 product 0x07db, class 9/0, rev 2.00/0.02, addr 2> on usbus0
uhub1: 4 ports with 4 removable, self powered
Root mount waiting for: usbus0
Root mount waiting for: usbus0
ugen0.3: <Generic> at usbus0
umass0: <Generic Ultra Fast Media, class 0/0, rev 2.00/1.98, addr 3> on usbus0
Trying to mount root from ufs:/dev/ufs/BSDRPs1a [ro]...
mountroot: waiting for device /dev/ufs/BSDRPs1a ...
da0 at umass-sim0 bus 0 scbus0 target 0 lun 0
da0: <Generic Ultra HS-COMBO 1.98> Removable Direct Access SCSI-0 device
da0: Serial Number 000000225001
da0: 40.000MB/s transfers
da0: 3776MB (7733248 512 byte sectors: 255H 63S/T 481C)
da0: quirks=0x2<NO_6_BYTE>
aesni0: <AES-CBC,AES-XTS> on motherboard
coretemp0: <CPU On-Die Thermal Sensors> on cpu0
coretemp1: <CPU On-Die Thermal Sensors> on cpu1
coretemp2: <CPU On-Die Thermal Sensors> on cpu2
coretemp3: <CPU On-Die Thermal Sensors> on cpu3
```

## pciconf

```
hostb0@pci0:0:0:0:      class=0x060000 card=0x00000000 chip=0x1f0b8086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    class      = bridge
    subclass   = HOST-PCI
pcib1@pci0:0:1:0:       class=0x060400 card=0x80868086 chip=0x1f108086 rev=0x02 hdr=0x01
    vendor     = 'Intel Corporation'
    class      = bridge
    subclass   = PCI-PCI
    bar   [10] = type Memory, range 64, base 0xdfe00000, size 131072, enabled
    cap 10[40] = PCI-Express 2 root port slot max data 128(256) link x0(x4)
                 speed 0.0(5.0) ASPM disabled(L1)
    cap 01[80] = powerspec 3  supports D0 D3  current D0
    cap 0d[88] = PCI Bridge card=0x80868086
    cap 05[90] = MSI supports 1 message, vector masks
    ecap 0001[100] = AER 1 0 fatal 0 non-fatal 0 corrected
pcib2@pci0:0:2:0:       class=0x060400 card=0x80868086 chip=0x1f118086 rev=0x02 hdr=0x01
    vendor     = 'Intel Corporation'
    class      = bridge
    subclass   = PCI-PCI
    bar   [10] = type Memory, range 64, base 0xdfe20000, size 131072, enabled
    cap 10[40] = PCI-Express 2 root port slot max data 128(256) link x0(x4)
                 speed 0.0(5.0) ASPM disabled(L1)
    cap 01[80] = powerspec 3  supports D0 D3  current D0
    cap 0d[88] = PCI Bridge card=0x80868086
    cap 05[90] = MSI supports 1 message, vector masks
    ecap 0001[100] = AER 1 0 fatal 0 non-fatal 0 corrected
pcib3@pci0:0:3:0:       class=0x060400 card=0x80868086 chip=0x1f128086 rev=0x02 hdr=0x01
    vendor     = 'Intel Corporation'
    class      = bridge
    subclass   = PCI-PCI
    bar   [10] = type Memory, range 64, base 0xdfe40000, size 131072, enabled
    cap 10[40] = PCI-Express 2 root port slot max data 128(256) link x1(x4)
                 speed 2.5(5.0) ASPM disabled(L1)
    cap 01[80] = powerspec 3  supports D0 D3  current D0
    cap 0d[88] = PCI Bridge card=0x80868086
    cap 05[90] = MSI supports 1 message, vector masks
    ecap 0001[100] = AER 1 0 fatal 0 non-fatal 0 corrected
pcib4@pci0:0:4:0:       class=0x060400 card=0x80868086 chip=0x1f138086 rev=0x02 hdr=0x01
    vendor     = 'Intel Corporation'
    class      = bridge
    subclass   = PCI-PCI
    bar   [10] = type Memory, range 64, base 0xdfe60000, size 131072, enabled
    cap 10[40] = PCI-Express 2 root port slot max data 128(256) link x1(x4)
                 speed 2.5(5.0) ASPM disabled(L1)
    cap 01[80] = powerspec 3  supports D0 D3  current D0
    cap 0d[88] = PCI Bridge card=0x80868086
    cap 05[90] = MSI supports 1 message, vector masks
    ecap 0001[100] = AER 1 0 fatal 0 non-fatal 0 corrected
none0@pci0:0:11:0:      class=0x0b4000 card=0x00000000 chip=0x1f188086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    class      = processor
    bar   [18] = type Memory, range 64, base 0xdfe80000, size 131072, enabled
    bar   [20] = type Memory, range 64, base 0xdff20000, size 16384, enabled
    cap 05[b0] = MSI supports 1 message, 64 bit, vector masks
    cap 11[60] = MSI-X supports 17 messages
                 Table in map 0x18[0x1b000], PBA in map 0x18[0x1b800]
    cap 01[6c] = powerspec 3  supports D0 D3  current D0
    cap 10[74] = PCI-Express 2 root endpoint max data 128(256) FLR link x0(x0)
    ecap 0001[100] = AER 1 0 fatal 0 non-fatal 0 corrected
    ecap 000e[138] = ARI 1
    ecap 0010[140] = SRIOV 1
hostb1@pci0:0:14:0:     class=0x060000 card=0x00000000 chip=0x1f148086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    class      = bridge
    subclass   = HOST-PCI
    cap 10[40] = PCI-Express 2 root endpoint max data 128(256) link x0(x0)
none1@pci0:0:15:0:      class=0x080600 card=0x00008086 chip=0x1f168086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    class      = base peripheral
    subclass   = IOMMU
    cap 10[40] = PCI-Express 2 event collector max data 128(256) link x0(x0)
    cap 01[80] = powerspec 3  supports D0 D3  current D0
    cap 05[90] = MSI supports 1 message, vector masks
    ecap 0001[100] = AER 1 0 fatal 0 non-fatal 1 corrected
    ecap 0007[150] = Root Complex Event Collector ASsociation 1
none2@pci0:0:19:0:      class=0x088000 card=0x00000000 chip=0x1f158086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    class      = base peripheral
    bar   [10] = type Memory, range 64, base 0xdff35000, size 1024, enabled
    cap 10[40] = PCI-Express 2 root endpoint max data 128(256) FLR link x0(x0)
    cap 01[80] = powerspec 3  supports D0 D3  current D0
    cap 05[8c] = MSI supports 1 message, 64 bit, vector masks
    ecap 0001[100] = AER 1 0 fatal 0 non-fatal 0 corrected
igb2@pci0:0:20:0:       class=0x020000 card=0x1f418086 chip=0x1f418086 rev=0x03 hdr=0x00
    vendor     = 'Intel Corporation'
    class      = network
    subclass   = ethernet
    bar   [10] = type Memory, range 64, base 0xdfea0000, size 131072, enabled
    bar   [18] = type I/O Port, range 32, base 0x3000, size 32, enabled
    bar   [20] = type Memory, range 64, base 0xdff24000, size 16384, enabled
    cap 01[40] = powerspec 3  supports D0 D3  current D0
    cap 05[50] = MSI supports 1 message, 64 bit, vector masks
    cap 11[70] = MSI-X supports 10 messages, enabled
                 Table in map 0x20[0x0], PBA in map 0x20[0x2000]
    cap 10[a0] = PCI-Express 2 root endpoint max data 128(512) FLR link x0(x0)
    ecap 0001[100] = AER 2 0 fatal 0 non-fatal 0 corrected
    ecap 0003[140] = Serial 1 0008a2ffff0933da
    ecap 0017[1a0] = TPH Requester 1
    ecap 000d[1d0] = ACS 1
igb3@pci0:0:20:1:       class=0x020000 card=0x1f418086 chip=0x1f418086 rev=0x03 hdr=0x00
    vendor     = 'Intel Corporation'
    class      = network
    subclass   = ethernet
    bar   [10] = type Memory, range 64, base 0xdfec0000, size 131072, enabled
    bar   [18] = type I/O Port, range 32, base 0x3020, size 32, enabled
    bar   [20] = type Memory, range 64, base 0xdff28000, size 16384, enabled
    cap 01[40] = powerspec 3  supports D0 D3  current D0
    cap 05[50] = MSI supports 1 message, 64 bit, vector masks
    cap 11[70] = MSI-X supports 10 messages, enabled
                 Table in map 0x20[0x0], PBA in map 0x20[0x2000]
    cap 10[a0] = PCI-Express 2 root endpoint max data 128(512) FLR link x0(x0)
    ecap 0001[100] = AER 2 0 fatal 0 non-fatal 0 corrected
    ecap 0003[140] = Serial 1 0008a2ffff0933da
    ecap 0017[1a0] = TPH Requester 1
    ecap 000d[1d0] = ACS 1
igb4@pci0:0:20:2:       class=0x020000 card=0x1f418086 chip=0x1f418086 rev=0x03 hdr=0x00
    vendor     = 'Intel Corporation'
    class      = network
    subclass   = ethernet
    bar   [10] = type Memory, range 64, base 0xdfee0000, size 131072, enabled
    bar   [18] = type I/O Port, range 32, base 0x3040, size 32, enabled
    bar   [20] = type Memory, range 64, base 0xdff2c000, size 16384, enabled
    cap 01[40] = powerspec 3  supports D0 D3  current D0
    cap 05[50] = MSI supports 1 message, 64 bit, vector masks
    cap 11[70] = MSI-X supports 10 messages, enabled
                 Table in map 0x20[0x0], PBA in map 0x20[0x2000]
    cap 10[a0] = PCI-Express 2 root endpoint max data 128(512) FLR link x0(x0)
    ecap 0001[100] = AER 2 0 fatal 0 non-fatal 0 corrected
    ecap 0003[140] = Serial 1 0008a2ffff0933da
    ecap 0017[1a0] = TPH Requester 1
    ecap 000d[1d0] = ACS 1
igb5@pci0:0:20:3:       class=0x020000 card=0x1f418086 chip=0x1f418086 rev=0x03 hdr=0x00
    vendor     = 'Intel Corporation'
    class      = network
    subclass   = ethernet
    bar   [10] = type Memory, range 64, base 0xdff00000, size 131072, enabled
    bar   [18] = type I/O Port, range 32, base 0x3060, size 32, enabled
    bar   [20] = type Memory, range 64, base 0xdff30000, size 16384, enabled
    cap 01[40] = powerspec 3  supports D0 D3  current D0
    cap 05[50] = MSI supports 1 message, 64 bit, vector masks
    cap 11[70] = MSI-X supports 10 messages, enabled
                 Table in map 0x20[0x0], PBA in map 0x20[0x2000]
    cap 10[a0] = PCI-Express 2 root endpoint max data 128(512) FLR link x0(x0)
    ecap 0001[100] = AER 2 0 fatal 0 non-fatal 0 corrected
    ecap 0003[140] = Serial 1 0008a2ffff0933da
    ecap 0017[1a0] = TPH Requester 1
    ecap 000d[1d0] = ACS 1
ehci0@pci0:0:22:0:      class=0x0c0320 card=0x40634bb6 chip=0x1f2c8086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    class      = serial bus
    subclass   = USB
    bar   [10] = type Memory, range 32, base 0xdff35400, size 1024, enabled
    cap 01[50] = powerspec 3  supports D0 D3  current D0
    cap 0a[58] = EHCI Debug Port at offset 0xa0 in map 0x14
    cap 13[98] = PCI Advanced Features: FLR TP
ahci0@pci0:0:23:0:      class=0x010601 card=0x1f228086 chip=0x1f228086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    class      = mass storage
    subclass   = SATA
    bar   [10] = type I/O Port, range 32, base 0x30c0, size 8, enabled
    bar   [14] = type I/O Port, range 32, base 0x30e0, size 4, enabled
    bar   [18] = type I/O Port, range 32, base 0x30c8, size 8, enabled
    bar   [1c] = type I/O Port, range 32, base 0x30e4, size 4, enabled
    bar   [20] = type I/O Port, range 32, base 0x3080, size 32, enabled
    bar   [24] = type Memory, range 32, base 0xdff34000, size 2048, enabled
    cap 05[80] = MSI supports 1 message enabled with 1 message
    cap 01[70] = powerspec 3  supports D0 D3  current D0
    cap 12[a8] = SATA Index-Data Pair
ahci1@pci0:0:24:0:      class=0x010601 card=0x1f328086 chip=0x1f328086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    class      = mass storage
    subclass   = SATA
    bar   [10] = type I/O Port, range 32, base 0x30d0, size 8, enabled
    bar   [14] = type I/O Port, range 32, base 0x30e8, size 4, enabled
    bar   [18] = type I/O Port, range 32, base 0x30d8, size 8, enabled
    bar   [1c] = type I/O Port, range 32, base 0x30ec, size 4, enabled
    bar   [20] = type I/O Port, range 32, base 0x30a0, size 32, enabled
    bar   [24] = type Memory, range 32, base 0xdff34800, size 2048, enabled
    cap 05[80] = MSI supports 1 message enabled with 1 message
    cap 01[70] = powerspec 3  supports D0 D3  current D0
    cap 12[a8] = SATA Index-Data Pair
isab0@pci0:0:31:0:      class=0x060100 card=0x1f388086 chip=0x1f388086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    class      = bridge
    subclass   = PCI-ISA
    cap 09[e0] = vendor (length 12) Intel cap 1 version 0
                 features: 4 PCI-e x1 slots
none3@pci0:0:31:3:      class=0x0c0500 card=0x1f3c8086 chip=0x1f3c8086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    class      = serial bus
    subclass   = SMBus
    bar   [10] = type Memory, range 32, base 0xdff35800, size 32, enabled
    bar   [20] = type I/O Port, range 32, base 0xefa0, size 32, enabled
igb0@pci0:3:0:0:        class=0x020000 card=0x00008086 chip=0x15398086 rev=0x03 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = 'I211 Gigabit Network Connection'
    class      = network
    subclass   = ethernet
    bar   [10] = type Memory, range 32, base 0xdfc00000, size 131072, enabled
    bar   [18] = type I/O Port, range 32, base 0x1000, size 32, enabled
    bar   [1c] = type Memory, range 32, base 0xdfc20000, size 16384, enabled
    cap 01[40] = powerspec 3  supports D0 D3  current D0
    cap 05[50] = MSI supports 1 message, 64 bit, vector masks
    cap 11[70] = MSI-X supports 5 messages, enabled
                 Table in map 0x1c[0x0], PBA in map 0x1c[0x2000]
    cap 10[a0] = PCI-Express 2 endpoint max data 128(512) FLR link x1(x1)
                 speed 2.5(2.5) ASPM disabled(L0s/L1)
    ecap 0001[100] = AER 2 0 fatal 0 non-fatal 0 corrected
    ecap 0003[140] = Serial 1 0008a2ffff0933de
    ecap 0017[1a0] = TPH Requester 1
igb1@pci0:4:0:0:        class=0x020000 card=0x00008086 chip=0x15398086 rev=0x03 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = 'I211 Gigabit Network Connection'
    class      = network
    subclass   = ethernet
    bar   [10] = type Memory, range 32, base 0xdfd00000, size 131072, enabled
    bar   [18] = type I/O Port, range 32, base 0x2000, size 32, enabled
    bar   [1c] = type Memory, range 32, base 0xdfd20000, size 16384, enabled
    cap 01[40] = powerspec 3  supports D0 D3  current D0
    cap 05[50] = MSI supports 1 message, 64 bit, vector masks
    class      = bridge
    subclass   = PCI-ISA
    cap 09[e0] = vendor (length 12) Intel cap 1 version 0
                 features: 4 PCI-e x1 slots
none3@pci0:0:31:3:      class=0x0c0500 card=0x1f3c8086 chip=0x1f3c8086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    class      = serial bus
    subclass   = SMBus
    bar   [10] = type Memory, range 32, base 0xdff35800, size 32, enabled
    bar   [20] = type I/O Port, range 32, base 0xefa0, size 32, enabled
igb0@pci0:3:0:0:        class=0x020000 card=0x00008086 chip=0x15398086 rev=0x03 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = 'I211 Gigabit Network Connection'
    class      = network
    subclass   = ethernet
    bar   [10] = type Memory, range 32, base 0xdfc00000, size 131072, enabled
    bar   [18] = type I/O Port, range 32, base 0x1000, size 32, enabled
    bar   [1c] = type Memory, range 32, base 0xdfc20000, size 16384, enabled
    cap 01[40] = powerspec 3  supports D0 D3  current D0
    cap 05[50] = MSI supports 1 message, 64 bit, vector masks
    cap 11[70] = MSI-X supports 5 messages, enabled
                 Table in map 0x1c[0x0], PBA in map 0x1c[0x2000]
    cap 10[a0] = PCI-Express 2 endpoint max data 128(512) FLR link x1(x1)
                 speed 2.5(2.5) ASPM disabled(L0s/L1)
    ecap 0001[100] = AER 2 0 fatal 0 non-fatal 0 corrected
    ecap 0003[140] = Serial 1 0008a2ffff0933de
    ecap 0017[1a0] = TPH Requester 1
igb1@pci0:4:0:0:        class=0x020000 card=0x00008086 chip=0x15398086 rev=0x03 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = 'I211 Gigabit Network Connection'
    class      = network
    subclass   = ethernet
    bar   [10] = type Memory, range 32, base 0xdfd00000, size 131072, enabled
    bar   [18] = type I/O Port, range 32, base 0x2000, size 32, enabled
    bar   [1c] = type Memory, range 32, base 0xdfd20000, size 16384, enabled
    cap 01[40] = powerspec 3  supports D0 D3  current D0
    cap 05[50] = MSI supports 1 message, 64 bit, vector masks
    cap 11[70] = MSI-X supports 5 messages, enabled
                 Table in map 0x1c[0x0], PBA in map 0x1c[0x2000]
    cap 10[a0] = PCI-Express 2 endpoint max data 128(512) FLR link x1(x1)
                 speed 2.5(2.5) ASPM disabled(L0s/L1)
    ecap 0001[100] = AER 2 0 fatal 0 non-fatal 0 corrected
    ecap 0003[140] = Serial 1 0008a2ffff0933df
    ecap 0017[1a0] = TPH Requester 1
```
