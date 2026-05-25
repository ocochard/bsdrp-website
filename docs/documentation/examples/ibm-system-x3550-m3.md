---
title: IBM System x3550 M3
---
### dmesg

```
Copyright (c) 1992-2013 The FreeBSD Project.
Copyright (c) 1979, 1980, 1983, 1986, 1988, 1989, 1991, 1992, 1993, 1994
        The Regents of the University of California. All rights reserved.
FreeBSD is a registered trademark of The FreeBSD Foundation.
FreeBSD 9.2-RC4 #0 r255473M: Sat Sep 14 22:53:03 CEST 2013
    root@orange.bsdrp.net:/usr/obj/BSDRP.amd64/usr/local/BSDRP/BSDRP/FreeBSD/src/sys/amd64 amd64
gcc version 4.2.1 20070831 patched [FreeBSD]
CPU: Intel(R) Xeon(R) CPU           L5630  @ 2.13GHz (2133.45-MHz K8-class CPU)
  Origin = "GenuineIntel"  Id = 0x206c2  Family = 0x6  Model = 0x2c  Stepping = 2
  Features=0xbfebfbff<FPU,VME,DE,PSE,TSC,MSR,PAE,MCE,CX8,APIC,SEP,MTRR,PGE,MCA,CMOV,PAT,PSE36,CLFLUSH,DTS,ACPI,MMX,FXSR,SSE,SSE2,SS,HTT,TM,PBE>
  Features2=0x29ee3ff<SSE3,PCLMULQDQ,DTES64,MON,DS_CPL,VMX,SMX,EST,TM2,SSSE3,CX16,xTPR,PDCM,PCID,DCA,SSE4.1,SSE4.2,POPCNT,AESNI>
  AMD Features=0x2c100800<SYSCALL,NX,Page1GB,RDTSCP,LM>
  AMD Features2=0x1<LAHF>
  TSC: P-state invariant, performance statistics
real memory  = 17179869184 (16384 MB)
avail memory = 16475496448 (15712 MB)
Event timer "LAPIC" quality 600
ACPI APIC Table: <IBM    THURLEY >
FreeBSD/SMP: Multiprocessor System Detected: 4 CPUs
FreeBSD/SMP: 1 package(s) x 4 core(s)
 cpu0 (BSP): APIC ID:  0
 cpu1 (AP): APIC ID:  2
 cpu2 (AP): APIC ID: 18
 cpu3 (AP): APIC ID: 20
ACPI Warning: Invalid length for Pm1aControlBlock: 32, using default 16 (20110527/tbfadt-638)
ioapic0 <Version 2.0> irqs 0-23 on motherboard
ioapic1 <Version 2.0> irqs 24-47 on motherboard
netmap: loaded module
cryptosoft0: <software crypto> on motherboard
acpi0: <IBM THURLEY> on motherboard
acpi0: Power Button (fixed)
Timecounter "HPET" frequency 14318180 Hz quality 950
Event timer "HPET" frequency 14318180 Hz quality 450
Event timer "HPET1" frequency 14318180 Hz quality 440
Event timer "HPET2" frequency 14318180 Hz quality 440
Event timer "HPET3" frequency 14318180 Hz quality 440
cpu0: <ACPI CPU> on acpi0
cpu1: <ACPI CPU> on acpi0
cpu2: <ACPI CPU> on acpi0
cpu3: <ACPI CPU> on acpi0
atrtc0: <AT realtime clock> port 0x70-0x77 irq 8 on acpi0
atrtc0: Warning: Couldn't map I/O.
Event timer "RTC" frequency 32768 Hz quality 0
attimer0: <AT timer> port 0x40-0x43,0x50-0x53 irq 0 on acpi0
Timecounter "i8254" frequency 1193182 Hz quality 0
Event timer "i8254" frequency 1193182 Hz quality 100
Timecounter "ACPI-fast" frequency 3579545 Hz quality 900
acpi_timer0: <24-bit timer at 3.579545MHz> port 0x588-0x58b on acpi0
pcib0: <ACPI Host-PCI bridge> port 0xcf8-0xcff on acpi0
pcib0: Length mismatch for 3 range: 1 vs 8100000000
pci0: <ACPI PCI bus> on pcib0
pcib1: <ACPI PCI-PCI bridge> irq 28 at device 1.0 on pci0
pci11: <ACPI PCI bus> on pcib1
bce0: <Broadcom NetXtreme II BCM5709 1000Base-T (C0)> mem 0x92000000-0x93ffffff irq 28 at device 0.0 on pci11
miibus0: <MII bus> on bce0
brgphy0: <BCM5709 10/100/1000baseT PHY> PHY 1 on miibus0
brgphy0:  10baseT, 10baseT-FDX, 100baseTX, 100baseTX-FDX, 1000baseT, 1000baseT-master, 1000baseT-FDX, 1000baseT-FDX-master, auto, auto-flow
bce0: Ethernet address: 5c:f3:fc:e5:a2:f8
bce0: ASIC (0x57092003); Rev (C0); Bus (PCIe x2, 5Gbps); B/C (6.2.0); Bufs (RX:2;TX:2;PG:8); Flags (SPLT|MSI|MFW); MFW (NCSI 2.0.11)
Coal (RX:6,6,18,18; TX:20,20,80,80)
bce1: <Broadcom NetXtreme II BCM5709 1000Base-T (C0)> mem 0x94000000-0x95ffffff irq 40 at device 0.1 on pci11
miibus1: <MII bus> on bce1
brgphy1: <BCM5709 10/100/1000baseT PHY> PHY 1 on miibus1
brgphy1:  10baseT, 10baseT-FDX, 100baseTX, 100baseTX-FDX, 1000baseT, 1000baseT-master, 1000baseT-FDX, 1000baseT-FDX-master, auto, auto-flow
bce1: Ethernet address: 5c:f3:fc:e5:a2:fa
bce1: ASIC (0x57092003); Rev (C0); Bus (PCIe x2, 5Gbps); B/C (6.2.0); Bufs (RX:2;TX:2;PG:8); Flags (SPLT|MSI|MFW); MFW (NCSI 2.0.11)
Coal (RX:6,6,18,18; TX:20,20,80,80)
pcib2: <PCI-PCI bridge> irq 29 at device 2.0 on pci0
pci16: <PCI bus> on pcib2
pcib3: <ACPI PCI-PCI bridge> irq 24 at device 3.0 on pci0
pci21: <ACPI PCI bus> on pcib3
ix0: <Intel(R) PRO/10GbE PCI-Express Network Driver, Version - 2.5.15> mem 0xfbc00000-0xfbdfffff,0xfbe04000-0xfbe07fff irq 34 at device 0.0 on pci21
ix0: Using MSIX interrupts with 5 vectors
ix0: Ethernet address: a0:36:9f:1e:1e:d8
ix0: PCI Express Bus: Speed 5.0GT/s Width x8
001.000007 netmap_attach [1696] success for ix0
ix1: <Intel(R) PRO/10GbE PCI-Express Network Driver, Version - 2.5.15> mem 0xfba00000-0xfbbfffff,0xfbe00000-0xfbe03fff irq 24 at device 0.1 on pci21
ix1: Using MSIX interrupts with 5 vectors
ix1: Ethernet address: a0:36:9f:1e:1e:da
ix1: PCI Express Bus: Speed 5.0GT/s Width x8
001.000008 netmap_attach [1696] success for ix1
pcib4: <ACPI PCI-PCI bridge> irq 30 at device 7.0 on pci0
pci26: <ACPI PCI bus> on pcib4
igb0: <Intel(R) PRO/1000 Network Connection version - 2.3.10> mem 0x97b80000-0x97bfffff,0x97c0c000-0x97c0ffff irq 30 at device 0.0 on pci26
igb0: Using MSIX interrupts with 5 vectors
igb0: Ethernet address: 00:1b:21:d4:3f:28
igb0: Bound queue 0 to cpu 0
igb0: Bound queue 1 to cpu 1
igb0: Bound queue 2 to cpu 2
igb0: Bound queue 3 to cpu 3
001.000009 netmap_attach [1696] success for igb0
igb1: <Intel(R) PRO/1000 Network Connection version - 2.3.10> mem 0x97b00000-0x97b7ffff,0x97c08000-0x97c0bfff irq 37 at device 0.1 on pci26
igb1: Using MSIX interrupts with 5 vectors
igb1: Ethernet address: 00:1b:21:d4:3f:29
igb1: Bound queue 0 to cpu 0
igb1: Bound queue 1 to cpu 1
igb1: Bound queue 2 to cpu 2
igb1: Bound queue 3 to cpu 3
001.000010 netmap_attach [1696] success for igb1
igb2: <Intel(R) PRO/1000 Network Connection version - 2.3.10> mem 0x97a80000-0x97afffff,0x97c04000-0x97c07fff irq 39 at device 0.2 on pci26
igb2: Using MSIX interrupts with 5 vectors
igb2: Ethernet address: 00:1b:21:d4:3f:2a
igb2: Bound queue 0 to cpu 0
igb2: Bound queue 1 to cpu 1
igb2: Bound queue 2 to cpu 2
igb2: Bound queue 3 to cpu 3
001.000011 netmap_attach [1696] success for igb2
igb3: <Intel(R) PRO/1000 Network Connection version - 2.3.10> mem 0x97a00000-0x97a7ffff,0x97c00000-0x97c03fff irq 38 at device 0.3 on pci26
igb3: Using MSIX interrupts with 5 vectors
igb3: Ethernet address: 00:1b:21:d4:3f:2b
igb3: Bound queue 0 to cpu 0
igb3: Bound queue 1 to cpu 1
igb3: Bound queue 2 to cpu 2
igb3: Bound queue 3 to cpu 3
001.000012 netmap_attach [1696] success for igb3
pci0: <base peripheral, interrupt controller> at device 16.0 (no driver attached)
pci0: <base peripheral, interrupt controller> at device 16.1 (no driver attached)
pci0: <base peripheral, interrupt controller> at device 17.0 (no driver attached)
pci0: <base peripheral, interrupt controller> at device 17.1 (no driver attached)
pci0: <base peripheral, interrupt controller> at device 20.0 (no driver attached)
pci0: <base peripheral, interrupt controller> at device 20.1 (no driver attached)
pci0: <base peripheral, interrupt controller> at device 20.2 (no driver attached)
pci0: <base peripheral, interrupt controller> at device 20.3 (no driver attached)
pci0: <base peripheral> at device 22.0 (no driver attached)
pci0: <base peripheral> at device 22.1 (no driver attached)
pci0: <base peripheral> at device 22.2 (no driver attached)
pci0: <base peripheral> at device 22.3 (no driver attached)
pci0: <base peripheral> at device 22.4 (no driver attached)
pci0: <base peripheral> at device 22.5 (no driver attached)
pci0: <base peripheral> at device 22.6 (no driver attached)
pci0: <base peripheral> at device 22.7 (no driver attached)
uhci0: <Intel 82801JI (ICH10) USB controller USB-D> port 0x20a0-0x20bf irq 17 at device 26.0 on pci0
usbus0 on uhci0
uhci1: <Intel 82801JI (ICH10) USB controller USB-E> port 0x2080-0x209f irq 18 at device 26.1 on pci0
usbus1 on uhci1
ehci0: <Intel 82801JI (ICH10) USB 2.0 controller USB-B> mem 0x97d21000-0x97d213ff irq 19 at device 26.7 on pci0
usbus2: EHCI version 1.0
usbus2 on ehci0
pcib5: <ACPI PCI-PCI bridge> irq 16 at device 28.0 on pci0
pci1: <ACPI PCI bus> on pcib5
mpt0: <LSILogic SAS/SATA Adapter> port 0x1000-0x10ff mem 0x97910000-0x97913fff,0x97900000-0x9790ffff irq 16 at device 0.0 on pci1
mpt0: MPI Version=1.5.20.0
mpt0: Capabilities: ( RAID-0 RAID-1E RAID-1 )
mpt0: 1 Active Volume (2 Max)
mpt0: 2 Hidden Drive Members (14 Max)
pcib6: <PCI-PCI bridge> irq 16 at device 28.4 on pci0
pci6: <PCI bus> on pcib6
pcib7: <PCI-PCI bridge> irq 16 at device 0.0 on pci6
pci7: <PCI bus> on pcib7
vgapci0: <VGA-compatible display> mem 0x96000000-0x96ffffff,0x97800000-0x97803fff,0x97000000-0x977fffff irq 16 at device 0.0 on pci7
uhci2: <Intel 82801JI (ICH10) USB controller USB-A> port 0x2060-0x207f irq 17 at device 29.0 on pci0
usbus3 on uhci2
uhci3: <Intel 82801JI (ICH10) USB controller USB-B> port 0x2040-0x205f irq 18 at device 29.1 on pci0
usbus4 on uhci3
uhci4: <Intel 82801JI (ICH10) USB controller USB-C> port 0x2020-0x203f irq 19 at device 29.2 on pci0
usbus5 on uhci4
ehci1: <Intel 82801JI (ICH10) USB 2.0 controller USB-A> mem 0x97d20000-0x97d203ff irq 17 at device 29.7 on pci0
usbus6: EHCI version 1.0
usbus6 on ehci1
pcib8: <PCI-PCI bridge> at device 30.0 on pci0
pci31: <PCI bus> on pcib8
isab0: <PCI-ISA bridge> at device 31.0 on pci0
isa0: <ISA bus> on isab0
atapci0: <Intel ICH10 SATA300 controller> port 0x2118-0x211f,0x212c-0x212f,0x2110-0x2117,0x2128-0x212b,0x20f0-0x20ff,0x20e0-0x20ef irq 16 at device 31.2 on pci0
ata2: <ATA channel> at channel 0 on atapci0
ata3: <ATA channel> at channel 1 on atapci0
pci0: <serial bus, SMBus> at device 31.3 (no driver attached)
atapci1: <Intel ICH10 SATA300 controller> port 0x2108-0x210f,0x2124-0x2127,0x2100-0x2107,0x2120-0x2123,0x20d0-0x20df,0x20c0-0x20cf irq 21 at device 31.5 on pci0
ata4: <ATA channel> at channel 0 on atapci1
ata5: <ATA channel> at channel 1 on atapci1
uart0: <16550 or compatible> port 0x3f8-0x3ff irq 4 flags 0x10 on acpi0
uart1: <16550 or compatible> port 0x2f8-0x2ff irq 3 on acpi0
qpi0: <QPI system bus> on motherboard
pcib9: <QPI Host-PCI bridge> pcibus 255 on qpi0
pci255: <PCI bus> on pcib9
orm0: <ISA Option ROM> at iomem 0xc0000-0xc7fff on isa0
sc0: <System console> at flags 0x100 on isa0
sc0: VGA <16 virtual consoles, flags=0x300>
vga0: <Generic ISA VGA> at port 0x3c0-0x3df iomem 0xa0000-0xbffff on isa0
atkbdc0: <Keyboard controller (i8042)> at port 0x60,0x64 on isa0
atkbd0: <AT Keyboard> irq 1 on atkbdc0
atkbd0: [GIANT-LOCKED]
est0: <Enhanced SpeedStep Frequency Control> on cpu0
est: CPU supports Enhanced Speedstep, but is not recognized.
est: cpu_vendor GenuineIntel, msr 11
device_attach: est0 attach returned 6
p4tcc0: <CPU Frequency Thermal Control> on cpu0
est1: <Enhanced SpeedStep Frequency Control> on cpu1
est: CPU supports Enhanced Speedstep, but is not recognized.
est: cpu_vendor GenuineIntel, msr 11
device_attach: est1 attach returned 6
p4tcc1: <CPU Frequency Thermal Control> on cpu1
est2: <Enhanced SpeedStep Frequency Control> on cpu2
est: CPU supports Enhanced Speedstep, but is not recognized.
est: cpu_vendor GenuineIntel, msr 11
device_attach: est2 attach returned 6
p4tcc2: <CPU Frequency Thermal Control> on cpu2
est3: <Enhanced SpeedStep Frequency Control> on cpu3
est: CPU supports Enhanced Speedstep, but is not recognized.
est: cpu_vendor GenuineIntel, msr 11
device_attach: est3 attach returned 6
p4tcc3: <CPU Frequency Thermal Control> on cpu3
Timecounters tick every 1.000 msec
IPsec: Initialized Security Association Processing.
usbus0: 12Mbps Full Speed USB v1.0
usbus1: 12Mbps Full Speed USB v1.0
usbus2: 480Mbps High Speed USB v2.0
usbus3: 12Mbps Full Speed USB v1.0
usbus4: 12Mbps Full Speed USB v1.0
usbus5: 12Mbps Full Speed USB v1.0
usbus6: 480Mbps High Speed USB v2.0
ugen0.1: <Intel> at usbus0
uhub0: <Intel UHCI root HUB, class 9/0, rev 1.00/1.00, addr 1> on usbus0
ugen1.1: <Intel> at usbus1
uhub1: <Intel UHCI root HUB, class 9/0, rev 1.00/1.00, addr 1> on usbus1
ugen2.1: <Intel> at usbus2
uhub2: <Intel EHCI root HUB, class 9/0, rev 2.00/1.00, addr 1> on usbus2
ugen3.1: <Intel> at usbus3
uhub3: <Intel UHCI root HUB, class 9/0, rev 1.00/1.00, addr 1> on usbus3
ugen4.1: <Intel> at usbus4
uhub4: <Intel UHCI root HUB, class 9/0, rev 1.00/1.00, addr 1> on usbus4
ugen5.1: <Intel> at usbus5
uhub5: <Intel UHCI root HUB, class 9/0, rev 1.00/1.00, addr 1> on usbus5
ugen6.1: <Intel> at usbus6
uhub6: <Intel EHCI root HUB, class 9/0, rev 2.00/1.00, addr 1> on usbus6
uhub0: 2 ports with 2 removable, self powered
uhub1: 2 ports with 2 removable, self powered
uhub3: 2 ports with 2 removable, self powered
uhub4: 2 ports with 2 removable, self powered
uhub5: 2 ports with 2 removable, self powered
mpt0: mpt_read_cfg_page: Config Info Status 22
mpt0:vol0(mpt0:0:0): mpt_refresh_raid_vol: Failed to read RAID Vol Page(0)
mpt0:vol0(mpt0:0:0): Settings ( )
mpt0:vol0(mpt0:0:0): 0 Members:
mpt0:vol0(mpt0:0:0): RAID-0 - Optimal
(mpt0:0:4): Physical (mpt0:0:4:0), Pass-thru (mpt0:1:0:0)
(mpt0:0:4): Online
(mpt0:0:5): Physical (mpt0:0:5:0), Pass-thru (mpt0:1:1:0)
(mpt0:0:5): Online
pass1 at ata2 bus 0 scbus2 target 0 lun 0
da0 at mpt0 bus 0 scbus0 target 3 lun 0
da0: <LSILOGIC Logical Volume 3000> Fixed Direct Access SCSI-2 device 
da0: 300.000MB/s transfers
da0: Command Queueing enabled
da0: 33378MB (68358144 512 byte sectors: 255H 63S/T 4255C)
pass1: <TSSTcorp DVD-ROM TS-L333H ID03> Removable CD-ROM SCSI-0 device 
pass1: 150.000MB/s transfers (SATA 1.x, UDMA2, ATAPI 12bytes, PIO 8192bytes)
SMP: AP CPU #1 Launched!
SMP: AP CPU #2 Launched!
SMP: AP CPU #3 Launched!
Timecounter "TSC" frequency 2133449161 Hz quality 1000
Trying to mount root from ufs:/dev/ufs/BSDRPs1a [ro]...
ugen3.2: <IBM> at usbus3
ichsmb0: <Intel 82801JI (ICH10) SMBus controller> port 0x2000-0x201f mem 0x97d22000-0x97d220ff irq 22 at device 31.3 on pci0
smbus0: <System Management Bus> on ichsmb0
coretemp0: <CPU On-Die Thermal Sensors> on cpu0
est0: <Enhanced SpeedStep Frequency Control> on cpu0
est: CPU supports Enhanced Speedstep, but is not recognized.
est: cpu_vendor GenuineIntel, msr 11
device_attach: est0 attach returned 6
coretemp1: <CPU On-Die Thermal Sensors> on cpu1
est1: <Enhanced SpeedStep Frequency Control> on cpu1
est: CPU supports Enhanced Speedstep, but is not recognized.
est: cpu_vendor GenuineIntel, msr 11
device_attach: est1 attach returned 6
coretemp2: <CPU On-Die Thermal Sensors> on cpu2
est2: <Enhanced SpeedStep Frequency Control> on cpu2
est: CPU supports Enhanced Speedstep, but is not recognized.
est: cpu_vendor GenuineIntel, msr 11
device_attach: est2 attach returned 6
coretemp3: <CPU On-Die Thermal Sensors> on cpu3
est3: <Enhanced SpeedStep Frequency Control> on cpu3
est: CPU supports Enhanced Speedstep, but is not recognized.
est: cpu_vendor GenuineIntel, msr 11
device_attach: est3 attach returned 6
aesni0: <AES-CBC,AES-XTS> on motherboard
```

### pciconf

```
hostb0@pci0:0:0:0:      class=0x060000 card=0x72701014 chip=0x34068086 rev=0x22 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '5520 I/O Hub to ESI Port'
    class      = bridge
    subclass   = HOST-PCI
    cap 05[60] = MSI supports 2 messages, vector masks 
    cap 10[90] = PCI-Express 2 root port max data 128(128) link x4(x4)
                 speed 2.5(2.5) ASPM disabled(L0s/L1)
    cap 01[e0] = powerspec 3  supports D0 D3  current D0
ecap 0001[100] = AER 1 0 fatal 0 non-fatal 0 corrected
ecap 000d[150] = ACS 1
ecap 000b[160] = Vendor 0
pcib1@pci0:0:1:0:       class=0x060400 card=0x34081014 chip=0x34088086 rev=0x22 hdr=0x01
    vendor     = 'Intel Corporation'
    device     = '5520/5500/X58 I/O Hub PCI Express Root Port 1'
    class      = bridge
    subclass   = PCI-PCI
    cap 0d[40] = PCI Bridge card=0x34081014
    cap 05[60] = MSI supports 2 messages, vector masks 
    cap 10[90] = PCI-Express 2 root port max data 256(256) link x2(x2)
                 speed 5.0(5.0)
    cap 01[e0] = powerspec 3  supports D0 D3  current D0
ecap 0001[100] = AER 1 0 fatal 0 non-fatal 0 corrected
ecap 000d[150] = ACS 1
ecap 000b[160] = Vendor 0
pcib2@pci0:0:2:0:       class=0x060400 card=0x34091014 chip=0x34098086 rev=0x22 hdr=0x01
    vendor     = 'Intel Corporation'
    device     = '5520/5500/X58 I/O Hub PCI Express Root Port 2'
    class      = bridge
    subclass   = PCI-PCI
    cap 0d[40] = PCI Bridge card=0x34091014
    cap 05[60] = MSI supports 2 messages, vector masks 
    cap 10[90] = PCI-Express 2 root port max data 256(256) link x0(x2)
                 speed 0.0(5.0)
    cap 01[e0] = powerspec 3  supports D0 D3  current D0
ecap 0001[100] = AER 1 0 fatal 0 non-fatal 0 corrected
ecap 000d[150] = ACS 1
pcib3@pci0:0:3:0:       class=0x060400 card=0x340a1014 chip=0x340a8086 rev=0x22 hdr=0x01
    vendor     = 'Intel Corporation'
    device     = '5520/5500/X58 I/O Hub PCI Express Root Port 3'
    class      = bridge
    subclass   = PCI-PCI
    cap 0d[40] = PCI Bridge card=0x340a1014
    cap 05[60] = MSI supports 2 messages, vector masks 
    cap 10[90] = PCI-Express 2 root port slot max data 256(256) link x8(x16)
                 speed 5.0(5.0)
    cap 01[e0] = powerspec 3  supports D0 D3  current D0
ecap 0001[100] = AER 1 0 fatal 0 non-fatal 0 corrected
ecap 000d[150] = ACS 1
ecap 000b[160] = Vendor 0
pcib4@pci0:0:7:0:       class=0x060400 card=0x340e1014 chip=0x340e8086 rev=0x22 hdr=0x01
    vendor     = 'Intel Corporation'
    device     = '5520/5500/X58 I/O Hub PCI Express Root Port 7'
    class      = bridge
    subclass   = PCI-PCI
    cap 0d[40] = PCI Bridge card=0x340e1014
    cap 05[60] = MSI supports 2 messages, vector masks 
    cap 10[90] = PCI-Express 2 root port slot max data 256(256) link x4(x16)
                 speed 5.0(5.0)
    cap 01[e0] = powerspec 3  supports D0 D3  current D0
ecap 0001[100] = AER 1 0 fatal 0 non-fatal 0 corrected
ecap 000d[150] = ACS 1
ecap 000b[160] = Vendor 0
none0@pci0:0:16:0:      class=0x080000 card=0x00000000 chip=0x34258086 rev=0x22 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '5520/5500/X58 Physical and Link Layer Registers Port 0'
    class      = base peripheral
    subclass   = interrupt controller
    cap 09[50] = vendor (length 255) Intel cap 15 version 0
none1@pci0:0:16:1:      class=0x080000 card=0x00000000 chip=0x34268086 rev=0x22 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '5520/5500/X58 Routing and Protocol Layer Registers Port 0'
    class      = base peripheral
    subclass   = interrupt controller
none2@pci0:0:17:0:      class=0x080000 card=0x00000000 chip=0x34278086 rev=0x22 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '5520/5500 Physical and Link Layer Registers Port 1'
    class      = base peripheral
    subclass   = interrupt controller
    cap 09[50] = vendor (length 255) Intel cap 15 version 0
none3@pci0:0:17:1:      class=0x080000 card=0x00000000 chip=0x34288086 rev=0x22 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '5520/5500 Routing & Protocol Layer Register Port 1'
    class      = base peripheral
    subclass   = interrupt controller
none4@pci0:0:20:0:      class=0x080000 card=0x00000000 chip=0x342e8086 rev=0x22 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '5520/5500/X58 I/O Hub System Management Registers'
    class      = base peripheral
    subclass   = interrupt controller
    cap 10[40] = PCI-Express 2 root endpoint max data 128(128) link x0(x0)
                 ASPM disabled(L0s)
none5@pci0:0:20:1:      class=0x080000 card=0x00000000 chip=0x34228086 rev=0x22 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '5520/5500/X58 I/O Hub GPIO and Scratch Pad Registers'
    class      = base peripheral
    subclass   = interrupt controller
    cap 10[40] = PCI-Express 2 root endpoint max data 128(128) link x0(x0)
                 ASPM disabled(L0s)
none6@pci0:0:20:2:      class=0x080000 card=0x00000000 chip=0x34238086 rev=0x22 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '5520/5500/X58 I/O Hub Control Status and RAS Registers'
    class      = base peripheral
    subclass   = interrupt controller
    cap 10[40] = PCI-Express 2 root endpoint max data 128(128) link x0(x0)
                 ASPM disabled(L0s)
none7@pci0:0:20:3:      class=0x080000 card=0x00000000 chip=0x34388086 rev=0x22 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '5520/5500/X58 I/O Hub Throttle Registers'
    class      = base peripheral
    subclass   = interrupt controller
ioapic0@pci0:0:21:0:    class=0x080020 card=0x00000000 chip=0x342f8086 rev=0x22 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '5520/5500/X58 Trusted Execution Technology Registers'
    class      = base peripheral
    subclass   = interrupt controller
none8@pci0:0:22:0:      class=0x088000 card=0x34301014 chip=0x34308086 rev=0x22 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '5520/5500/X58 Chipset QuickData Technology Device'
    class      = base peripheral
    bar   [10] = type Memory, range 64, base 0x97d00000, size 16384, enabled
    cap 11[80] = MSI-X supports 1 message in map 0x10
    cap 10[90] = PCI-Express 2 root endpoint max data 128(128) link x0(x0)
    cap 01[e0] = powerspec 3  supports D0 D3  current D3
none9@pci0:0:22:1:      class=0x088000 card=0x34311014 chip=0x34318086 rev=0x22 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '5520/5500/X58 Chipset QuickData Technology Device'
    class      = base peripheral
    bar   [10] = type Memory, range 64, base 0x97d04000, size 16384, enabled
    cap 11[80] = MSI-X supports 1 message in map 0x10
    cap 10[90] = PCI-Express 2 root endpoint max data 128(128) link x0(x0)
    cap 01[e0] = powerspec 3  supports D0 D3  current D3
none10@pci0:0:22:2:     class=0x088000 card=0x34321014 chip=0x34328086 rev=0x22 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '5520/5500/X58 Chipset QuickData Technology Device'
    class      = base peripheral
    bar   [10] = type Memory, range 64, base 0x97d08000, size 16384, enabled
    cap 11[80] = MSI-X supports 1 message in map 0x10
    cap 10[90] = PCI-Express 2 root endpoint max data 128(128) link x0(x0)
    cap 01[e0] = powerspec 3  supports D0 D3  current D3
none11@pci0:0:22:3:     class=0x088000 card=0x34331014 chip=0x34338086 rev=0x22 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '5520/5500/X58 Chipset QuickData Technology Device'
    class      = base peripheral
    bar   [10] = type Memory, range 64, base 0x97d0c000, size 16384, enabled
    cap 11[80] = MSI-X supports 1 message in map 0x10
    cap 10[90] = PCI-Express 2 root endpoint max data 128(128) link x0(x0)
    cap 01[e0] = powerspec 3  supports D0 D3  current D3
none12@pci0:0:22:4:     class=0x088000 card=0x34291014 chip=0x34298086 rev=0x22 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '5520/5500/X58 Chipset QuickData Technology Device'
    class      = base peripheral
    bar   [10] = type Memory, range 64, base 0x97d10000, size 16384, enabled
    cap 11[80] = MSI-X supports 1 message in map 0x10
    cap 10[90] = PCI-Express 2 root endpoint max data 128(128) link x0(x0)
    cap 01[e0] = powerspec 3  supports D0 D3  current D3
none13@pci0:0:22:5:     class=0x088000 card=0x342a1014 chip=0x342a8086 rev=0x22 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '5520/5500/X58 Chipset QuickData Technology Device'
    class      = base peripheral
    bar   [10] = type Memory, range 64, base 0x97d14000, size 16384, enabled
    cap 11[80] = MSI-X supports 1 message in map 0x10
    cap 10[90] = PCI-Express 2 root endpoint max data 128(128) link x0(x0)
    cap 01[e0] = powerspec 3  supports D0 D3  current D3
none14@pci0:0:22:6:     class=0x088000 card=0x342b1014 chip=0x342b8086 rev=0x22 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '5520/5500/X58 Chipset QuickData Technology Device'
    class      = base peripheral
    bar   [10] = type Memory, range 64, base 0x97d18000, size 16384, enabled
    cap 11[80] = MSI-X supports 1 message in map 0x10
    cap 10[90] = PCI-Express 2 root endpoint max data 128(128) link x0(x0)
    cap 01[e0] = powerspec 3  supports D0 D3  current D3
none15@pci0:0:22:7:     class=0x088000 card=0x342c1014 chip=0x342c8086 rev=0x22 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '5520/5500/X58 Chipset QuickData Technology Device'
    class      = base peripheral
    bar   [10] = type Memory, range 64, base 0x97d1c000, size 16384, enabled
    cap 11[80] = MSI-X supports 1 message in map 0x10
    cap 10[90] = PCI-Express 2 root endpoint max data 128(128) link x0(x0)
    cap 01[e0] = powerspec 3  supports D0 D3  current D3
uhci0@pci0:0:26:0:      class=0x0c0300 card=0x3a371014 chip=0x3a378086 rev=0x00 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '82801JI (ICH10 Family) USB UHCI Controller'
    class      = serial bus
    subclass   = USB
    bar   [20] = type I/O Port, range 32, base 0x20a0, size 32, enabled
    cap 13[50] = PCI Advanced Features: FLR TP
uhci1@pci0:0:26:1:      class=0x0c0300 card=0x3a381014 chip=0x3a388086 rev=0x00 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '82801JI (ICH10 Family) USB UHCI Controller'
    class      = serial bus
    subclass   = USB
    bar   [20] = type I/O Port, range 32, base 0x2080, size 32, enabled
    cap 13[50] = PCI Advanced Features: FLR TP
ehci0@pci0:0:26:7:      class=0x0c0320 card=0x3a3c1014 chip=0x3a3c8086 rev=0x00 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '82801JI (ICH10 Family) USB2 EHCI Controller'
    class      = serial bus
    subclass   = USB
    bar   [10] = type Memory, range 32, base 0x97d21000, size 1024, enabled
    cap 01[50] = powerspec 2  supports D0 D3  current D0
    cap 0a[58] = EHCI Debug Port at offset 0xa0 in map 0x14
    cap 13[98] = PCI Advanced Features: FLR TP
pcib5@pci0:0:28:0:      class=0x060400 card=0x3a401014 chip=0x3a408086 rev=0x00 hdr=0x01
    vendor     = 'Intel Corporation'
    device     = '82801JI (ICH10 Family) PCI Express Root Port 1'
    class      = bridge
    subclass   = PCI-PCI
    cap 10[40] = PCI-Express 1 root port slot max data 128(128) link x4(x4)
                 speed 2.5(2.5)
    cap 05[80] = MSI supports 1 message 
    cap 0d[90] = PCI Bridge card=0x3a401014
    cap 01[a0] = powerspec 2  supports D0 D3  current D0
ecap 0002[100] = VC 1 max VC0
ecap 0005[180] = Root Complex Link Declaration 1
pcib6@pci0:0:28:4:      class=0x060400 card=0x3a481014 chip=0x3a488086 rev=0x00 hdr=0x01
    vendor     = 'Intel Corporation'
    device     = '82801JI (ICH10 Family) PCI Express Root Port 5'
    class      = bridge
    subclass   = PCI-PCI
    cap 10[40] = PCI-Express 1 root port max data 128(128) link x1(x1)
                 speed 2.5(2.5)
    cap 05[80] = MSI supports 1 message 
    cap 0d[90] = PCI Bridge card=0x3a481014
    cap 01[a0] = powerspec 2  supports D0 D3  current D0
ecap 0002[100] = VC 1 max VC0
ecap 0005[180] = Root Complex Link Declaration 1
uhci2@pci0:0:29:0:      class=0x0c0300 card=0x3a341014 chip=0x3a348086 rev=0x00 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '82801JI (ICH10 Family) USB UHCI Controller'
    class      = serial bus
    subclass   = USB
    bar   [20] = type I/O Port, range 32, base 0x2060, size 32, enabled
    cap 13[50] = PCI Advanced Features: FLR TP
uhci3@pci0:0:29:1:      class=0x0c0300 card=0x3a351014 chip=0x3a358086 rev=0x00 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '82801JI (ICH10 Family) USB UHCI Controller'
    class      = serial bus
    subclass   = USB
    bar   [20] = type I/O Port, range 32, base 0x2040, size 32, enabled
    cap 13[50] = PCI Advanced Features: FLR TP
uhci4@pci0:0:29:2:      class=0x0c0300 card=0x3a361014 chip=0x3a368086 rev=0x00 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '82801JI (ICH10 Family) USB UHCI Controller'
    class      = serial bus
    subclass   = USB
    bar   [20] = type I/O Port, range 32, base 0x2020, size 32, enabled
    cap 13[50] = PCI Advanced Features: FLR TP
ehci1@pci0:0:29:7:      class=0x0c0320 card=0x3a3a1014 chip=0x3a3a8086 rev=0x00 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '82801JI (ICH10 Family) USB2 EHCI Controller'
    class      = serial bus
    subclass   = USB
    bar   [10] = type Memory, range 32, base 0x97d20000, size 1024, enabled
    cap 01[50] = powerspec 2  supports D0 D3  current D0
    cap 0a[58] = EHCI Debug Port at offset 0xa0 in map 0x14
    cap 13[98] = PCI Advanced Features: FLR TP
pcib8@pci0:0:30:0:      class=0x060401 card=0x244e1014 chip=0x244e8086 rev=0x90 hdr=0x01
    vendor     = 'Intel Corporation'
    device     = '82801 PCI Bridge'
    class      = bridge
    subclass   = PCI-PCI
    cap 0d[50] = PCI Bridge card=0x244e1014
isab0@pci0:0:31:0:      class=0x060100 card=0x3a181014 chip=0x3a188086 rev=0x00 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '82801JIB (ICH10) LPC Interface Controller'
    class      = bridge
    subclass   = PCI-ISA
    cap 09[e0] = vendor (length 12) Intel cap 1 version 0
                 features: Quick Resume, SATA RAID-5, 4 PCI-e x1 slots, SATA RAID-0/1/10
atapci0@pci0:0:31:2:    class=0x01018f card=0x3a201014 chip=0x3a208086 rev=0x00 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '82801JI (ICH10 Family) 4 port SATA IDE Controller'
    class      = mass storage
    subclass   = ATA
    bar   [10] = type I/O Port, range 32, base 0x2118, size  8, enabled
    bar   [14] = type I/O Port, range 32, base 0x212c, size  4, enabled
    bar   [18] = type I/O Port, range 32, base 0x2110, size  8, enabled
    bar   [1c] = type I/O Port, range 32, base 0x2128, size  4, enabled
    bar   [20] = type I/O Port, range 32, base 0x20f0, size 16, enabled
    bar   [24] = type I/O Port, range 32, base 0x20e0, size 16, enabled
    cap 01[70] = powerspec 3  supports D0 D3  current D0
    cap 13[b0] = PCI Advanced Features: FLR TP
ichsmb0@pci0:0:31:3:    class=0x0c0500 card=0x3a301014 chip=0x3a308086 rev=0x00 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '82801JI (ICH10 Family) SMBus Controller'
    class      = serial bus
    subclass   = SMBus
    bar   [10] = type Memory, range 64, base 0x97d22000, size 256, enabled
    bar   [20] = type I/O Port, range 32, base 0x2000, size 32, enabled
atapci1@pci0:0:31:5:    class=0x010185 card=0x3a261014 chip=0x3a268086 rev=0x00 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '82801JI (ICH10 Family) 2 port SATA IDE Controller'
    class      = mass storage
    subclass   = ATA
    bar   [10] = type I/O Port, range 32, base 0x2108, size  8, enabled
    bar   [14] = type I/O Port, range 32, base 0x2124, size  4, enabled
    bar   [18] = type I/O Port, range 32, base 0x2100, size  8, enabled
    bar   [1c] = type I/O Port, range 32, base 0x2120, size  4, enabled
    bar   [20] = type I/O Port, range 32, base 0x20d0, size 16, enabled
    bar   [24] = type I/O Port, range 32, base 0x20c0, size 16, enabled
    cap 01[70] = powerspec 3  supports D0 D3  current D0
    cap 13[b0] = PCI Advanced Features: FLR TP
bce0@pci0:11:0:0:       class=0x020000 card=0x03a91014 chip=0x163914e4 rev=0x20 hdr=0x00
    vendor     = 'Broadcom Corporation'
    device     = 'NetXtreme II BCM5709 Gigabit Ethernet'
    class      = network
    subclass   = ethernet
    bar   [10] = type Memory, range 64, base 0x92000000, size 33554432, enabled
    cap 01[48] = powerspec 3  supports D0 D3  current D0
    cap 03[50] = VPD
    cap 05[58] = MSI supports 16 messages, 64 bit enabled with 1 message
    cap 11[a0] = MSI-X supports 9 messages in map 0x10
    cap 10[ac] = PCI-Express 2 endpoint max data 256(512) link x2(x4)
                 speed 5.0(5.0) ASPM disabled(L0s/L1)
ecap 0003[100] = Serial 1 5cf3fcfffee5a2f8
ecap 0001[110] = AER 1 0 fatal 0 non-fatal 1 corrected
ecap 0004[150] = Power Budgeting 1
ecap 0002[160] = VC 1 max VC0
bce1@pci0:11:0:1:       class=0x020000 card=0x03a91014 chip=0x163914e4 rev=0x20 hdr=0x00
    vendor     = 'Broadcom Corporation'
    device     = 'NetXtreme II BCM5709 Gigabit Ethernet'
    class      = network
    subclass   = ethernet
    bar   [10] = type Memory, range 64, base 0x94000000, size 33554432, enabled
    cap 01[48] = powerspec 3  supports D0 D3  current D0
    cap 03[50] = VPD
    cap 05[58] = MSI supports 16 messages, 64 bit enabled with 1 message
    cap 11[a0] = MSI-X supports 9 messages in map 0x10
    cap 10[ac] = PCI-Express 2 endpoint max data 256(512) link x2(x4)
                 speed 5.0(5.0) ASPM disabled(L0s/L1)
ecap 0003[100] = Serial 1 5cf3fcfffee5a2fa
ecap 0001[110] = AER 1 0 fatal 0 non-fatal 1 corrected
ecap 0004[150] = Power Budgeting 1
ecap 0002[160] = VC 1 max VC0
ix0@pci0:21:0:0:        class=0x020000 card=0x00018086 chip=0x15288086 rev=0x01 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = 'Ethernet Controller 10 Gigabit X540-AT2'
    class      = network
    subclass   = ethernet
    bar   [10] = type Prefetchable Memory, range 64, base 0xfbc00000, size 2097152, enabled
    bar   [20] = type Prefetchable Memory, range 64, base 0xfbe04000, size 16384, enabled
    cap 01[40] = powerspec 3  supports D0 D3  current D0
    cap 05[50] = MSI supports 1 message, 64 bit, vector masks 
    cap 11[70] = MSI-X supports 64 messages in map 0x20 enabled
    cap 10[a0] = PCI-Express 2 endpoint max data 256(512) FLR link x8(x8)
                 speed 5.0(5.0) ASPM disabled(L0s/L1)
ecap 0001[100] = AER 2 0 fatal 0 non-fatal 1 corrected
ecap 0003[140] = Serial 1 a0369fffff1e1ed8
ecap 000e[150] = ARI 1
ecap 0010[160] = SRIOV 1
ecap 000d[1d0] = ACS 1
ix1@pci0:21:0:1:        class=0x020000 card=0x00018086 chip=0x15288086 rev=0x01 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = 'Ethernet Controller 10 Gigabit X540-AT2'
    class      = network
    subclass   = ethernet
    bar   [10] = type Prefetchable Memory, range 64, base 0xfba00000, size 2097152, enabled
    bar   [20] = type Prefetchable Memory, range 64, base 0xfbe00000, size 16384, enabled
    cap 01[40] = powerspec 3  supports D0 D3  current D0
    cap 05[50] = MSI supports 1 message, 64 bit, vector masks 
    cap 11[70] = MSI-X supports 64 messages in map 0x20 enabled
    cap 10[a0] = PCI-Express 2 endpoint max data 256(512) FLR link x8(x8)
                 speed 5.0(5.0) ASPM disabled(L0s/L1)
ecap 0001[100] = AER 2 0 fatal 0 non-fatal 1 corrected
ecap 0003[140] = Serial 1 a0369fffff1e1ed8
ecap 000e[150] = ARI 1
ecap 0010[160] = SRIOV 1
ecap 000d[1d0] = ACS 1
igb0@pci0:26:0:0:       class=0x020000 card=0x12a28086 chip=0x150e8086 rev=0x01 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '82580 Gigabit Network Connection'
    class      = network
    subclass   = ethernet
    bar   [10] = type Memory, range 32, base 0x97b80000, size 524288, enabled
    bar   [1c] = type Memory, range 32, base 0x97c0c000, size 16384, enabled
    cap 01[40] = powerspec 3  supports D0 D3  current D0
    cap 05[50] = MSI supports 1 message, 64 bit, vector masks 
    cap 11[70] = MSI-X supports 10 messages in map 0x1c enabled
    cap 10[a0] = PCI-Express 2 endpoint max data 256(512) FLR link x4(x4)
                 speed 5.0(5.0) ASPM disabled(L0s/L1)
ecap 0001[100] = AER 1 0 fatal 0 non-fatal 1 corrected
ecap 0003[140] = Serial 1 001b21ffffd43f28
ecap 0017[1a0] = TPH Requester 1
ecap 0018[1c0] = LTR 1
igb1@pci0:26:0:1:       class=0x020000 card=0x12a28086 chip=0x150e8086 rev=0x01 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '82580 Gigabit Network Connection'
    class      = network
    subclass   = ethernet
    bar   [10] = type Memory, range 32, base 0x97b00000, size 524288, enabled
    bar   [1c] = type Memory, range 32, base 0x97c08000, size 16384, enabled
    cap 01[40] = powerspec 3  supports D0 D3  current D0
    cap 05[50] = MSI supports 1 message, 64 bit, vector masks 
    cap 11[70] = MSI-X supports 10 messages in map 0x1c enabled
    cap 10[a0] = PCI-Express 2 endpoint max data 256(512) FLR link x4(x4)
                 speed 5.0(5.0) ASPM disabled(L0s/L1)
ecap 0001[100] = AER 1 0 fatal 0 non-fatal 1 corrected
ecap 0003[140] = Serial 1 001b21ffffd43f28
ecap 0017[1a0] = TPH Requester 1
igb2@pci0:26:0:2:       class=0x020000 card=0x12a28086 chip=0x150e8086 rev=0x01 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '82580 Gigabit Network Connection'
    class      = network
    subclass   = ethernet
    bar   [10] = type Memory, range 32, base 0x97a80000, size 524288, enabled
    bar   [1c] = type Memory, range 32, base 0x97c04000, size 16384, enabled
    cap 01[40] = powerspec 3  supports D0 D3  current D0
    cap 05[50] = MSI supports 1 message, 64 bit, vector masks 
    cap 11[70] = MSI-X supports 10 messages in map 0x1c enabled
    cap 10[a0] = PCI-Express 2 endpoint max data 256(512) FLR link x4(x4)
                 speed 5.0(5.0) ASPM disabled(L0s/L1)
ecap 0001[100] = AER 1 0 fatal 0 non-fatal 1 corrected
ecap 0003[140] = Serial 1 001b21ffffd43f28
ecap 0017[1a0] = TPH Requester 1
igb3@pci0:26:0:3:       class=0x020000 card=0x12a28086 chip=0x150e8086 rev=0x01 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '82580 Gigabit Network Connection'
    class      = network
    subclass   = ethernet
    bar   [10] = type Memory, range 32, base 0x97a00000, size 524288, enabled
    bar   [1c] = type Memory, range 32, base 0x97c00000, size 16384, enabled
    cap 01[40] = powerspec 3  supports D0 D3  current D0
    cap 05[50] = MSI supports 1 message, 64 bit, vector masks 
    cap 11[70] = MSI-X supports 10 messages in map 0x1c enabled
    cap 10[a0] = PCI-Express 2 endpoint max data 256(512) FLR link x4(x4)
                 speed 5.0(5.0) ASPM disabled(L0s/L1)
ecap 0001[100] = AER 1 0 fatal 0 non-fatal 1 corrected
ecap 0003[140] = Serial 1 001b21ffffd43f28
ecap 0017[1a0] = TPH Requester 1
mpt0@pci0:1:0:0:        class=0x010000 card=0x03941014 chip=0x00581000 rev=0x10 hdr=0x00
    vendor     = 'LSI Logic / Symbios Logic'
    device     = 'SAS1068E PCI-Express Fusion-MPT SAS'
    class      = mass storage
    subclass   = SCSI
    bar   [10] = type I/O Port, range 32, base 0x1000, size 256, disabled
    bar   [14] = type Memory, range 64, base 0x97910000, size 16384, enabled
    bar   [1c] = type Memory, range 64, base 0x97900000, size 65536, enabled
    cap 01[50] = powerspec 2  supports D0 D1 D2 D3  current D0
    cap 10[68] = PCI-Express 1 endpoint max data 128(4096) link x4(x8)
                 speed 2.5(2.5) ASPM disabled(L0s/L1)
    cap 05[98] = MSI supports 1 message, 64 bit 
    cap 11[b0] = MSI-X supports 1 message in map 0x14 enabled
ecap 0001[100] = AER 1 0 fatal 1 non-fatal 0 corrected
pcib7@pci0:6:0:0:       class=0x060400 card=0x03691014 chip=0x0452101b rev=0x01 hdr=0x01
    vendor     = 'Vitesse Semiconductor'
    device     = 'VSC452 [SuperBMC]'
    class      = bridge
    subclass   = PCI-PCI
    cap 05[50] = MSI supports 2 messages, 64 bit 
    cap 01[78] = powerspec 3  supports D0 D3  current D0
    cap 10[80] = PCI-Express 1 PCI bridge max data 128(128) link x1(x1)
                 speed 2.5(2.5) ASPM disabled(L0s)
    cap 0d[a4] = PCI Bridge card=0x03691014
ecap 0002[100] = VC 1 max VC0
vgapci0@pci0:7:0:0:     class=0x030000 card=0x03691014 chip=0x0530102b rev=0x00 hdr=0x00
    vendor     = 'Matrox Graphics, Inc.'
    device     = 'MGA G200EV'
    class      = display
    subclass   = VGA
    bar   [10] = type Prefetchable Memory, range 32, base 0x96000000, size 16777216, enabled
    bar   [14] = type Memory, range 32, base 0x97800000, size 16384, enabled
    bar   [18] = type Memory, range 32, base 0x97000000, size 8388608, enabled
    cap 01[dc] = powerspec 1  supports D0 D3  current D0
hostb1@pci0:255:0:0:    class=0x060000 card=0x80868086 chip=0x2c708086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = 'Xeon 5600 Series QuickPath Architecture Generic Non-core Registers'
    class      = bridge
    subclass   = HOST-PCI
hostb2@pci0:255:0:1:    class=0x060000 card=0x80868086 chip=0x2d818086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = 'Xeon 5600 Series QuickPath Architecture System Address Decoder'
    class      = bridge
    subclass   = HOST-PCI
hostb3@pci0:255:2:0:    class=0x060000 card=0x80868086 chip=0x2d908086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = 'Xeon 5600 Series QPI Link 0'
    class      = bridge
    subclass   = HOST-PCI
hostb4@pci0:255:2:1:    class=0x060000 card=0x80868086 chip=0x2d918086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = 'Xeon 5600 Series QPI Physical 0'
    class      = bridge
    subclass   = HOST-PCI
hostb5@pci0:255:2:2:    class=0x060000 card=0x80868086 chip=0x2d928086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = 'Xeon 5600 Series Mirror Port Link 0'
    class      = bridge
    subclass   = HOST-PCI
hostb6@pci0:255:2:3:    class=0x060000 card=0x80868086 chip=0x2d938086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = 'Xeon 5600 Series Mirror Port Link 1'
    class      = bridge
    subclass   = HOST-PCI
hostb7@pci0:255:2:4:    class=0x060000 card=0x80868086 chip=0x2d948086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = 'Xeon 5600 Series QPI Link 1'
    class      = bridge
    subclass   = HOST-PCI
hostb8@pci0:255:2:5:    class=0x060000 card=0x80868086 chip=0x2d958086 rev=0x02 hdr=0x00                               [48/1639]
    vendor     = 'Intel Corporation'
    device     = 'Xeon 5600 Series QPI Physical 1'
    class      = bridge
    subclass   = HOST-PCI
hostb9@pci0:255:3:0:    class=0x060000 card=0x80868086 chip=0x2d988086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = 'Xeon 5600 Series Integrated Memory Controller Registers'
    class      = bridge
    subclass   = HOST-PCI
hostb10@pci0:255:3:1:   class=0x060000 card=0x80868086 chip=0x2d998086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = 'Xeon 5600 Series Integrated Memory Controller Target Address Decoder'
    class      = bridge
    subclass   = HOST-PCI
hostb11@pci0:255:3:2:   class=0x060000 card=0x80868086 chip=0x2d9a8086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = 'Xeon 5600 Series Integrated Memory Controller RAS Registers'
    class      = bridge
    subclass   = HOST-PCI
hostb12@pci0:255:3:4:   class=0x060000 card=0x80868086 chip=0x2d9c8086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = 'Xeon 5600 Series Integrated Memory Controller Test Registers'
    class      = bridge
    subclass   = HOST-PCI
hostb13@pci0:255:4:0:   class=0x060000 card=0x80868086 chip=0x2da08086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = 'Xeon 5600 Series Integrated Memory Controller Channel 0 Control'
    class      = bridge
    subclass   = HOST-PCI
hostb14@pci0:255:4:1:   class=0x060000 card=0x80868086 chip=0x2da18086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = 'Xeon 5600 Series Integrated Memory Controller Channel 0 Address'
    class      = bridge
    subclass   = HOST-PCI
hostb15@pci0:255:4:2:   class=0x060000 card=0x80868086 chip=0x2da28086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = 'Xeon 5600 Series Integrated Memory Controller Channel 0 Rank'
    class      = bridge
    subclass   = HOST-PCI
hostb16@pci0:255:4:3:   class=0x060000 card=0x80868086 chip=0x2da38086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = 'Xeon 5600 Series Integrated Memory Controller Channel 0 Thermal Control'
    class      = bridge
    subclass   = HOST-PCI
hostb17@pci0:255:5:0:   class=0x060000 card=0x80868086 chip=0x2da88086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = 'Xeon 5600 Series Integrated Memory Controller Channel 1 Control'
    class      = bridge
    subclass   = HOST-PCI
hostb18@pci0:255:5:1:   class=0x060000 card=0x80868086 chip=0x2da98086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = 'Xeon 5600 Series Integrated Memory Controller Channel 1 Address'
    class      = bridge
    subclass   = HOST-PCI
hostb19@pci0:255:5:2:   class=0x060000 card=0x80868086 chip=0x2daa8086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = 'Xeon 5600 Series Integrated Memory Controller Channel 1 Rank'
    class      = bridge
    subclass   = HOST-PCI
hostb20@pci0:255:5:3:   class=0x060000 card=0x80868086 chip=0x2dab8086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = 'Xeon 5600 Series Integrated Memory Controller Channel 1 Thermal Control'
    class      = bridge
    subclass   = HOST-PCI
hostb21@pci0:255:6:0:   class=0x060000 card=0x80868086 chip=0x2db08086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = 'Xeon 5600 Series Integrated Memory Controller Channel 2 Control'
    class      = bridge
    subclass   = HOST-PCI
hostb22@pci0:255:6:1:   class=0x060000 card=0x80868086 chip=0x2db18086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = 'Xeon 5600 Series Integrated Memory Controller Channel 2 Address'
    class      = bridge
    subclass   = HOST-PCI
hostb23@pci0:255:6:2:   class=0x060000 card=0x80868086 chip=0x2db28086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = 'Xeon 5600 Series Integrated Memory Controller Channel 2 Rank'
    class      = bridge
    subclass   = HOST-PCI
hostb24@pci0:255:6:3:   class=0x060000 card=0x80868086 chip=0x2db38086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = 'Xeon 5600 Series Integrated Memory Controller Channel 2 Thermal Control'
    class      = bridge
    subclass   = HOST-PCI

[root@bsdrp1]~# pciconf -lvcb
hostb0@pci0:0:0:0:      class=0x060000 card=0x72701014 chip=0x34068086 rev=0x22 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '5520 I/O Hub to ESI Port'
    class      = bridge
    subclass   = HOST-PCI
    cap 05[60] = MSI supports 2 messages, vector masks
    cap 10[90] = PCI-Express 2 root port max data 128(128) link x4(x4)
                 speed 2.5(2.5)
    cap 01[e0] = powerspec 3  supports D0 D3  current D0
ecap 0001[100] = AER 1 0 fatal 0 non-fatal 0 corrected
ecap 000d[150] = ACS 1
ecap 000b[160] = Vendor 0
pcib1@pci0:0:1:0:       class=0x060400 card=0x34081014 chip=0x34088086 rev=0x22 hdr=0x01
    vendor     = 'Intel Corporation'
    device     = '5520/5500/X58 I/O Hub PCI Express Root Port 1'
    class      = bridge
    subclass   = PCI-PCI
    cap 0d[40] = PCI Bridge card=0x34081014
    cap 05[60] = MSI supports 2 messages, vector masks
    cap 10[90] = PCI-Express 2 root port max data 256(256) link x2(x2)
                 speed 5.0(5.0)
    cap 01[e0] = powerspec 3  supports D0 D3  current D0
ecap 0001[100] = AER 1 0 fatal 0 non-fatal 0 corrected
ecap 000d[150] = ACS 1
ecap 000b[160] = Vendor 0
pcib2@pci0:0:2:0:       class=0x060400 card=0x34091014 chip=0x34098086 rev=0x22 hdr=0x01
    vendor     = 'Intel Corporation'
    device     = '5520/5500/X58 I/O Hub PCI Express Root Port 2'
    class      = bridge
    subclass   = PCI-PCI
    cap 0d[40] = PCI Bridge card=0x34091014
    cap 05[60] = MSI supports 2 messages, vector masks
    cap 10[90] = PCI-Express 2 root port max data 256(256) link x0(x2)
                 speed 0.0(5.0)
    cap 01[e0] = powerspec 3  supports D0 D3  current D0
ecap 0001[100] = AER 1 0 fatal 0 non-fatal 0 corrected
ecap 000d[150] = ACS 1
pcib3@pci0:0:3:0:       class=0x060400 card=0x340a1014 chip=0x340a8086 rev=0x22 hdr=0x01
    vendor     = 'Intel Corporation'
    device     = '5520/5500/X58 I/O Hub PCI Express Root Port 3'
    class      = bridge
    subclass   = PCI-PCI
    cap 0d[40] = PCI Bridge card=0x340a1014
    cap 05[60] = MSI supports 2 messages, vector masks
    cap 10[90] = PCI-Express 2 root port slot max data 256(256) link x0(x16)
                 speed 0.0(5.0)
    cap 01[e0] = powerspec 3  supports D0 D3  current D0
ecap 0001[100] = AER 1 0 fatal 0 non-fatal 0 corrected
ecap 000d[150] = ACS 1
ecap 000b[160] = Vendor 0
pcib4@pci0:0:7:0:       class=0x060400 card=0x340e1014 chip=0x340e8086 rev=0x22 hdr=0x01
    vendor     = 'Intel Corporation'
    device     = '5520/5500/X58 I/O Hub PCI Express Root Port 7'
    class      = bridge
    subclass   = PCI-PCI
    cap 0d[40] = PCI Bridge card=0x340e1014
    cap 05[60] = MSI supports 2 messages, vector masks
    cap 10[90] = PCI-Express 2 root port slot max data 256(256) link x4(x16)
                 speed 5.0(5.0)
    cap 01[e0] = powerspec 3  supports D0 D3  current D0
ecap 0001[100] = AER 1 0 fatal 0 non-fatal 0 corrected
ecap 000d[150] = ACS 1
ecap 000b[160] = Vendor 0
none0@pci0:0:16:0:      class=0x080000 card=0x00000000 chip=0x34258086 rev=0x22 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '5520/5500/X58 Physical and Link Layer Registers Port 0'
    class      = base peripheral
    subclass   = interrupt controller
    cap 09[50] = vendor (length 255) Intel cap 15 version 0
none1@pci0:0:16:1:      class=0x080000 card=0x00000000 chip=0x34268086 rev=0x22 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '5520/5500/X58 Routing and Protocol Layer Registers Port 0'
    class      = base peripheral
    subclass   = interrupt controller
none2@pci0:0:17:0:      class=0x080000 card=0x00000000 chip=0x34278086 rev=0x22 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '5520/5500 Physical and Link Layer Registers Port 1'
    class      = base peripheral
    subclass   = interrupt controller
    cap 09[50] = vendor (length 255) Intel cap 15 version 0
none3@pci0:0:17:1:      class=0x080000 card=0x00000000 chip=0x34288086 rev=0x22 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '5520/5500 Routing & Protocol Layer Register Port 1'
    class      = base peripheral
    subclass   = interrupt controller
none4@pci0:0:20:0:      class=0x080000 card=0x00000000 chip=0x342e8086 rev=0x22 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '5520/5500/X58 I/O Hub System Management Registers'
    class      = base peripheral
    subclass   = interrupt controller
    cap 10[40] = PCI-Express 2 root endpoint max data 128(128) link x0(x0)
none5@pci0:0:20:1:      class=0x080000 card=0x00000000 chip=0x34228086 rev=0x22 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '5520/5500/X58 I/O Hub GPIO and Scratch Pad Registers'
    class      = base peripheral
    subclass   = interrupt controller
    cap 10[40] = PCI-Express 2 root endpoint max data 128(128) link x0(x0)
none6@pci0:0:20:2:      class=0x080000 card=0x00000000 chip=0x34238086 rev=0x22 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '5520/5500/X58 I/O Hub Control Status and RAS Registers'
    class      = base peripheral
    subclass   = interrupt controller
    cap 10[40] = PCI-Express 2 root endpoint max data 128(128) link x0(x0)
none7@pci0:0:20:3:      class=0x080000 card=0x00000000 chip=0x34388086 rev=0x22 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '5520/5500/X58 I/O Hub Throttle Registers'
    class      = base peripheral
    subclass   = interrupt controller
ioapic0@pci0:0:21:0:    class=0x080020 card=0x00000000 chip=0x342f8086 rev=0x22 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '5520/5500/X58 Trusted Execution Technology Registers'
    class      = base peripheral
    subclass   = interrupt controller
none8@pci0:0:22:0:      class=0x088000 card=0x34301014 chip=0x34308086 rev=0x22 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '5520/5500/X58 Chipset QuickData Technology Device'
    class      = base peripheral
    bar   [10] = type Memory, range 64, base 0x97d00000, size 16384, enabled
    cap 11[80] = MSI-X supports 1 message in map 0x10
    cap 10[90] = PCI-Express 2 root endpoint max data 128(128) link x0(x0)
    cap 01[e0] = powerspec 3  supports D0 D3  current D3
none9@pci0:0:22:1:      class=0x088000 card=0x34311014 chip=0x34318086 rev=0x22 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '5520/5500/X58 Chipset QuickData Technology Device'
    class      = base peripheral
    bar   [10] = type Memory, range 64, base 0x97d04000, size 16384, enabled
    cap 11[80] = MSI-X supports 1 message in map 0x10
    cap 10[90] = PCI-Express 2 root endpoint max data 128(128) link x0(x0)
    cap 01[e0] = powerspec 3  supports D0 D3  current D3
none10@pci0:0:22:2:     class=0x088000 card=0x34321014 chip=0x34328086 rev=0x22 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '5520/5500/X58 Chipset QuickData Technology Device'
    class      = base peripheral
    bar   [10] = type Memory, range 64, base 0x97d08000, size 16384, enabled
    cap 11[80] = MSI-X supports 1 message in map 0x10
    cap 10[90] = PCI-Express 2 root endpoint max data 128(128) link x0(x0)
    cap 01[e0] = powerspec 3  supports D0 D3  current D3
none11@pci0:0:22:3:     class=0x088000 card=0x34331014 chip=0x34338086 rev=0x22 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '5520/5500/X58 Chipset QuickData Technology Device'
    class      = base peripheral
    bar   [10] = type Memory, range 64, base 0x97d0c000, size 16384, enabled
    cap 11[80] = MSI-X supports 1 message in map 0x10
    cap 10[90] = PCI-Express 2 root endpoint max data 128(128) link x0(x0)
    cap 01[e0] = powerspec 3  supports D0 D3  current D3
none12@pci0:0:22:4:     class=0x088000 card=0x34291014 chip=0x34298086 rev=0x22 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '5520/5500/X58 Chipset QuickData Technology Device'
    class      = base peripheral
    bar   [10] = type Memory, range 64, base 0x97d10000, size 16384, enabled
    cap 11[80] = MSI-X supports 1 message in map 0x10
    cap 10[90] = PCI-Express 2 root endpoint max data 128(128) link x0(x0)
    cap 01[e0] = powerspec 3  supports D0 D3  current D3
none13@pci0:0:22:5:     class=0x088000 card=0x342a1014 chip=0x342a8086 rev=0x22 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '5520/5500/X58 Chipset QuickData Technology Device'
    class      = base peripheral
    bar   [10] = type Memory, range 64, base 0x97d14000, size 16384, enabled
    cap 11[80] = MSI-X supports 1 message in map 0x10
    cap 10[90] = PCI-Express 2 root endpoint max data 128(128) link x0(x0)
    cap 01[e0] = powerspec 3  supports D0 D3  current D3
none14@pci0:0:22:6:     class=0x088000 card=0x342b1014 chip=0x342b8086 rev=0x22 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '5520/5500/X58 Chipset QuickData Technology Device'
    class      = base peripheral
    bar   [10] = type Memory, range 64, base 0x97d18000, size 16384, enabled
    cap 11[80] = MSI-X supports 1 message in map 0x10
    cap 10[90] = PCI-Express 2 root endpoint max data 128(128) link x0(x0)
    cap 01[e0] = powerspec 3  supports D0 D3  current D3
none15@pci0:0:22:7:     class=0x088000 card=0x342c1014 chip=0x342c8086 rev=0x22 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '5520/5500/X58 Chipset QuickData Technology Device'
    class      = base peripheral
    bar   [10] = type Memory, range 64, base 0x97d1c000, size 16384, enabled
    cap 11[80] = MSI-X supports 1 message in map 0x10
    cap 10[90] = PCI-Express 2 root endpoint max data 128(128) link x0(x0)
    cap 01[e0] = powerspec 3  supports D0 D3  current D3
uhci0@pci0:0:26:0:      class=0x0c0300 card=0x3a371014 chip=0x3a378086 rev=0x00 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '82801JI (ICH10 Family) USB UHCI Controller'
    class      = serial bus
    subclass   = USB
    bar   [20] = type I/O Port, range 32, base 0x20a0, size 32, enabled
    cap 13[50] = PCI Advanced Features: FLR TP
uhci1@pci0:0:26:1:      class=0x0c0300 card=0x3a381014 chip=0x3a388086 rev=0x00 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '82801JI (ICH10 Family) USB UHCI Controller'
    class      = serial bus
    subclass   = USB
    bar   [20] = type I/O Port, range 32, base 0x2080, size 32, enabled
    cap 13[50] = PCI Advanced Features: FLR TP
ehci0@pci0:0:26:7:      class=0x0c0320 card=0x3a3c1014 chip=0x3a3c8086 rev=0x00 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '82801JI (ICH10 Family) USB2 EHCI Controller'
    class      = serial bus
    subclass   = USB
    bar   [10] = type Memory, range 32, base 0x97d21000, size 1024, enabled
    cap 01[50] = powerspec 2  supports D0 D3  current D0
    cap 0a[58] = EHCI Debug Port at offset 0xa0 in map 0x14
    cap 13[98] = PCI Advanced Features: FLR TP
pcib5@pci0:0:28:0:      class=0x060400 card=0x3a401014 chip=0x3a408086 rev=0x00 hdr=0x01                                        [300/1837]
    vendor     = 'Intel Corporation'
    device     = '82801JI (ICH10 Family) PCI Express Root Port 1'
    class      = bridge
    subclass   = PCI-PCI
    cap 10[40] = PCI-Express 1 root port slot max data 128(128) link x4(x4)
                 speed 2.5(2.5)
    cap 05[80] = MSI supports 1 message
    cap 0d[90] = PCI Bridge card=0x3a401014
    cap 01[a0] = powerspec 2  supports D0 D3  current D0
ecap 0002[100] = VC 1 max VC0
ecap 0005[180] = Root Complex Link Declaration 1
pcib6@pci0:0:28:4:      class=0x060400 card=0x3a481014 chip=0x3a488086 rev=0x00 hdr=0x01
    vendor     = 'Intel Corporation'
    device     = '82801JI (ICH10 Family) PCI Express Root Port 5'
    class      = bridge
    subclass   = PCI-PCI
    cap 10[40] = PCI-Express 1 root port max data 128(128) link x1(x1)
                 speed 2.5(2.5)
    cap 05[80] = MSI supports 1 message
    cap 0d[90] = PCI Bridge card=0x3a481014
    cap 01[a0] = powerspec 2  supports D0 D3  current D0
ecap 0002[100] = VC 1 max VC0
ecap 0005[180] = Root Complex Link Declaration 1
uhci2@pci0:0:29:0:      class=0x0c0300 card=0x3a341014 chip=0x3a348086 rev=0x00 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '82801JI (ICH10 Family) USB UHCI Controller'
    class      = serial bus
    subclass   = USB
    bar   [20] = type I/O Port, range 32, base 0x2060, size 32, enabled
    cap 13[50] = PCI Advanced Features: FLR TP
uhci3@pci0:0:29:1:      class=0x0c0300 card=0x3a351014 chip=0x3a358086 rev=0x00 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '82801JI (ICH10 Family) USB UHCI Controller'
    class      = serial bus
    subclass   = USB
    bar   [20] = type I/O Port, range 32, base 0x2040, size 32, enabled
    cap 13[50] = PCI Advanced Features: FLR TP
uhci4@pci0:0:29:2:      class=0x0c0300 card=0x3a361014 chip=0x3a368086 rev=0x00 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '82801JI (ICH10 Family) USB UHCI Controller'
    class      = serial bus
    subclass   = USB
    bar   [20] = type I/O Port, range 32, base 0x2020, size 32, enabled
    cap 13[50] = PCI Advanced Features: FLR TP
ehci1@pci0:0:29:7:      class=0x0c0320 card=0x3a3a1014 chip=0x3a3a8086 rev=0x00 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '82801JI (ICH10 Family) USB2 EHCI Controller'
    class      = serial bus
    subclass   = USB
    bar   [10] = type Memory, range 32, base 0x97d20000, size 1024, enabled
    cap 01[50] = powerspec 2  supports D0 D3  current D0
    cap 0a[58] = EHCI Debug Port at offset 0xa0 in map 0x14
    cap 13[98] = PCI Advanced Features: FLR TP
pcib8@pci0:0:30:0:      class=0x060401 card=0x244e1014 chip=0x244e8086 rev=0x90 hdr=0x01
    vendor     = 'Intel Corporation'
    device     = '82801 PCI Bridge'
    class      = bridge
    subclass   = PCI-PCI
    cap 0d[50] = PCI Bridge card=0x244e1014
isab0@pci0:0:31:0:      class=0x060100 card=0x3a181014 chip=0x3a188086 rev=0x00 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '82801JIB (ICH10) LPC Interface Controller'
    class      = bridge
    subclass   = PCI-ISA
    cap 09[e0] = vendor (length 12) Intel cap 1 version 0
                 features: Quick Resume, SATA RAID-5, 4 PCI-e x1 slots, SATA RAID-0/1/10
atapci0@pci0:0:31:2:    class=0x01018f card=0x3a201014 chip=0x3a208086 rev=0x00 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '82801JI (ICH10 Family) 4 port SATA IDE Controller'
    class      = mass storage
    subclass   = ATA
    bar   [10] = type I/O Port, range 32, base 0x2118, size  8, enabled
    bar   [14] = type I/O Port, range 32, base 0x212c, size  4, enabled
    bar   [18] = type I/O Port, range 32, base 0x2110, size  8, enabled
    bar   [1c] = type I/O Port, range 32, base 0x2128, size  4, enabled
    bar   [20] = type I/O Port, range 32, base 0x20f0, size 16, enabled
    bar   [24] = type I/O Port, range 32, base 0x20e0, size 16, enabled
    cap 01[70] = powerspec 3  supports D0 D3  current D0
    cap 13[b0] = PCI Advanced Features: FLR TP
ichsmb0@pci0:0:31:3:    class=0x0c0500 card=0x3a301014 chip=0x3a308086 rev=0x00 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '82801JI (ICH10 Family) SMBus Controller'
    class      = serial bus
    subclass   = SMBus
    bar   [10] = type Memory, range 64, base 0x97d22000, size 256, enabled
    bar   [20] = type I/O Port, range 32, base 0x2000, size 32, enabled
atapci1@pci0:0:31:5:    class=0x010185 card=0x3a261014 chip=0x3a268086 rev=0x00 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '82801JI (ICH10 Family) 2 port SATA IDE Controller'
    class      = mass storage
    subclass   = ATA
    bar   [10] = type I/O Port, range 32, base 0x2108, size  8, enabled
    bar   [14] = type I/O Port, range 32, base 0x2124, size  4, enabled
    bar   [18] = type I/O Port, range 32, base 0x2100, size  8, enabled
    bar   [1c] = type I/O Port, range 32, base 0x2120, size  4, enabled
    bar   [20] = type I/O Port, range 32, base 0x20d0, size 16, enabled
    bar   [24] = type I/O Port, range 32, base 0x20c0, size 16, enabled
    cap 01[70] = powerspec 3  supports D0 D3  current D0
    cap 13[b0] = PCI Advanced Features: FLR TP
bce0@pci0:11:0:0:       class=0x020000 card=0x03a91014 chip=0x163914e4 rev=0x20 hdr=0x00
    vendor     = 'Broadcom Corporation'
    device     = 'NetXtreme II BCM5709 Gigabit Ethernet'
    class      = network
    subclass   = ethernet
    bar   [10] = type Memory, range 64, base 0x92000000, size 33554432, enabled
    cap 01[48] = powerspec 3  supports D0 D3  current D0
    cap 03[50] = VPD
    cap 05[58] = MSI supports 16 messages, 64 bit enabled with 1 message
    cap 11[a0] = MSI-X supports 9 messages in map 0x10
    cap 10[ac] = PCI-Express 2 endpoint max data 256(512) link x2(x4)
                 speed 5.0(5.0)
ecap 0003[100] = Serial 1 5cf3fcfffee5a2f8
ecap 0001[110] = AER 1 0 fatal 0 non-fatal 1 corrected
ecap 0004[150] = Power Budgeting 1
ecap 0002[160] = VC 1 max VC0
bce1@pci0:11:0:1:       class=0x020000 card=0x03a91014 chip=0x163914e4 rev=0x20 hdr=0x00
    vendor     = 'Broadcom Corporation'
    device     = 'NetXtreme II BCM5709 Gigabit Ethernet'
    class      = network
    subclass   = ethernet
    bar   [10] = type Memory, range 64, base 0x94000000, size 33554432, enabled
    cap 01[48] = powerspec 3  supports D0 D3  current D0
    cap 03[50] = VPD
    cap 05[58] = MSI supports 16 messages, 64 bit enabled with 1 message
    cap 11[a0] = MSI-X supports 9 messages in map 0x10
    cap 10[ac] = PCI-Express 2 endpoint max data 256(512) link x2(x4)
                 speed 5.0(5.0)
ecap 0003[100] = Serial 1 5cf3fcfffee5a2fa
ecap 0001[110] = AER 1 0 fatal 0 non-fatal 1 corrected
ecap 0004[150] = Power Budgeting 1
ecap 0002[160] = VC 1 max VC0
igb0@pci0:26:0:0:       class=0x020000 card=0x12a28086 chip=0x150e8086 rev=0x01 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '82580 Gigabit Network Connection'
    class      = network
    subclass   = ethernet
    bar   [10] = type Memory, range 32, base 0x97b80000, size 524288, enabled
    bar   [1c] = type Memory, range 32, base 0x97c0c000, size 16384, enabled
    cap 01[40] = powerspec 3  supports D0 D3  current D0
    cap 05[50] = MSI supports 1 message, 64 bit, vector masks
    cap 11[70] = MSI-X supports 10 messages in map 0x1c enabled
    cap 10[a0] = PCI-Express 2 endpoint max data 256(512) FLR link x4(x4)
                 speed 5.0(5.0)
ecap 0001[100] = AER 1 0 fatal 0 non-fatal 1 corrected
ecap 0003[140] = Serial 1 001b21ffffd43f28
ecap 0017[1a0] = TPH Requester 1
ecap 0018[1c0] = LTR 1
igb1@pci0:26:0:1:       class=0x020000 card=0x12a28086 chip=0x150e8086 rev=0x01 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '82580 Gigabit Network Connection'
    class      = network
    subclass   = ethernet
    bar   [10] = type Memory, range 32, base 0x97b00000, size 524288, enabled
    bar   [1c] = type Memory, range 32, base 0x97c08000, size 16384, enabled
    cap 01[40] = powerspec 3  supports D0 D3  current D0
    cap 05[50] = MSI supports 1 message, 64 bit, vector masks
    cap 11[70] = MSI-X supports 10 messages in map 0x1c enabled
    cap 10[a0] = PCI-Express 2 endpoint max data 256(512) FLR link x4(x4)
                 speed 5.0(5.0)
ecap 0001[100] = AER 1 0 fatal 0 non-fatal 1 corrected
ecap 0003[140] = Serial 1 001b21ffffd43f28
ecap 0017[1a0] = TPH Requester 1
igb2@pci0:26:0:2:       class=0x020000 card=0x12a28086 chip=0x150e8086 rev=0x01 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '82580 Gigabit Network Connection'
    class      = network
    subclass   = ethernet
    bar   [10] = type Memory, range 32, base 0x97a80000, size 524288, enabled
    bar   [1c] = type Memory, range 32, base 0x97c04000, size 16384, enabled
    cap 01[40] = powerspec 3  supports D0 D3  current D0
    cap 05[50] = MSI supports 1 message, 64 bit, vector masks
    cap 11[70] = MSI-X supports 10 messages in map 0x1c enabled
    cap 10[a0] = PCI-Express 2 endpoint max data 256(512) FLR link x4(x4)
                 speed 5.0(5.0)
ecap 0001[100] = AER 1 0 fatal 0 non-fatal 1 corrected
ecap 0003[140] = Serial 1 001b21ffffd43f28
ecap 0017[1a0] = TPH Requester 1
igb3@pci0:26:0:3:       class=0x020000 card=0x12a28086 chip=0x150e8086 rev=0x01 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = '82580 Gigabit Network Connection'
    class      = network
    subclass   = ethernet
    bar   [10] = type Memory, range 32, base 0x97a00000, size 524288, enabled
    bar   [1c] = type Memory, range 32, base 0x97c00000, size 16384, enabled
    cap 01[40] = powerspec 3  supports D0 D3  current D0
    cap 05[50] = MSI supports 1 message, 64 bit, vector masks
    cap 11[70] = MSI-X supports 10 messages in map 0x1c enabled
    cap 10[a0] = PCI-Express 2 endpoint max data 256(512) FLR link x4(x4)
                 speed 5.0(5.0)
ecap 0001[100] = AER 1 0 fatal 0 non-fatal 1 corrected
ecap 0003[140] = Serial 1 001b21ffffd43f28
ecap 0017[1a0] = TPH Requester 1
mpt0@pci0:1:0:0:        class=0x010000 card=0x03941014 chip=0x00581000 rev=0x10 hdr=0x00
    vendor     = 'LSI Logic / Symbios Logic'
    device     = 'SAS1068E PCI-Express Fusion-MPT SAS'
    class      = mass storage
    subclass   = SCSI
    bar   [10] = type I/O Port, range 32, base 0x1000, size 256, disabled
    bar   [14] = type Memory, range 64, base 0x97910000, size 16384, enabled
    bar   [1c] = type Memory, range 64, base 0x97900000, size 65536, enabled
    cap 01[50] = powerspec 2  supports D0 D1 D2 D3  current D0
    cap 10[68] = PCI-Express 1 endpoint max data 128(4096) link x4(x8)
                 speed 2.5(2.5)
    cap 05[98] = MSI supports 1 message, 64 bit
    cap 11[b0] = MSI-X supports 1 message in map 0x14 enabled
ecap 0001[100] = AER 1 0 fatal 1 non-fatal 0 corrected
pcib7@pci0:6:0:0:       class=0x060400 card=0x03691014 chip=0x0452101b rev=0x01 hdr=0x01
    vendor     = 'Vitesse Semiconductor'
    device     = 'VSC452 [SuperBMC]'
    class      = bridge
    subclass   = PCI-PCI
    cap 05[50] = MSI supports 2 messages, 64 bit
    cap 01[78] = powerspec 3  supports D0 D3  current D0
    cap 10[80] = PCI-Express 1 PCI bridge max data 128(128) link x1(x1)
                 speed 2.5(2.5)
    cap 0d[a4] = PCI Bridge card=0x03691014
ecap 0002[100] = VC 1 max VC0
vgapci0@pci0:7:0:0:     class=0x030000 card=0x03691014 chip=0x0530102b rev=0x00 hdr=0x00
    vendor     = 'Matrox Graphics, Inc.'
    device     = 'MGA G200EV'
    class      = display
    subclass   = VGA
    bar   [10] = type Prefetchable Memory, range 32, base 0x96000000, size 16777216, enabled
    bar   [14] = type Memory, range 32, base 0x97800000, size 16384, enabled
    bar   [18] = type Memory, range 32, base 0x97000000, size 8388608, enabled
    cap 01[dc] = powerspec 1  supports D0 D3  current D0
hostb1@pci0:255:0:0:    class=0x060000 card=0x80868086 chip=0x2c708086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = 'Xeon 5600 Series QuickPath Architecture Generic Non-core Registers'
    class      = bridge
    subclass   = HOST-PCI
hostb2@pci0:255:0:1:    class=0x060000 card=0x80868086 chip=0x2d818086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = 'Xeon 5600 Series QuickPath Architecture System Address Decoder'
    class      = bridge
    subclass   = HOST-PCI
hostb3@pci0:255:2:0:    class=0x060000 card=0x80868086 chip=0x2d908086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = 'Xeon 5600 Series QPI Link 0'
    class      = bridge
    subclass   = HOST-PCI
hostb4@pci0:255:2:1:    class=0x060000 card=0x80868086 chip=0x2d918086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = 'Xeon 5600 Series QPI Physical 0'
    class      = bridge
    subclass   = HOST-PCI
hostb5@pci0:255:2:2:    class=0x060000 card=0x80868086 chip=0x2d928086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = 'Xeon 5600 Series Mirror Port Link 0'
    class      = bridge
    subclass   = HOST-PCI
hostb6@pci0:255:2:3:    class=0x060000 card=0x80868086 chip=0x2d938086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = 'Xeon 5600 Series Mirror Port Link 1'
    class      = bridge
    subclass   = HOST-PCI
hostb7@pci0:255:2:4:    class=0x060000 card=0x80868086 chip=0x2d948086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = 'Xeon 5600 Series QPI Link 1'
    class      = bridge
    subclass   = HOST-PCI
hostb8@pci0:255:2:5:    class=0x060000 card=0x80868086 chip=0x2d958086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = 'Xeon 5600 Series QPI Physical 1'
    class      = bridge
    subclass   = HOST-PCI
hostb9@pci0:255:3:0:    class=0x060000 card=0x80868086 chip=0x2d988086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = 'Xeon 5600 Series Integrated Memory Controller Registers'
    class      = bridge
    subclass   = HOST-PCI
hostb10@pci0:255:3:1:   class=0x060000 card=0x80868086 chip=0x2d998086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = 'Xeon 5600 Series Integrated Memory Controller Target Address Decoder'
    class      = bridge
    subclass   = HOST-PCI
hostb11@pci0:255:3:2:   class=0x060000 card=0x80868086 chip=0x2d9a8086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = 'Xeon 5600 Series Integrated Memory Controller RAS Registers'
    class      = bridge
    subclass   = HOST-PCI
hostb12@pci0:255:3:4:   class=0x060000 card=0x80868086 chip=0x2d9c8086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = 'Xeon 5600 Series Integrated Memory Controller Test Registers'
    class      = bridge
    subclass   = HOST-PCI
hostb13@pci0:255:4:0:   class=0x060000 card=0x80868086 chip=0x2da08086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = 'Xeon 5600 Series Integrated Memory Controller Channel 0 Control'
    class      = bridge
    subclass   = HOST-PCI
hostb14@pci0:255:4:1:   class=0x060000 card=0x80868086 chip=0x2da18086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = 'Xeon 5600 Series Integrated Memory Controller Channel 0 Address'
    class      = bridge
    subclass   = HOST-PCI
hostb15@pci0:255:4:2:   class=0x060000 card=0x80868086 chip=0x2da28086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = 'Xeon 5600 Series Integrated Memory Controller Channel 0 Rank'
    class      = bridge
    subclass   = HOST-PCI
hostb16@pci0:255:4:3:   class=0x060000 card=0x80868086 chip=0x2da38086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = 'Xeon 5600 Series Integrated Memory Controller Channel 0 Thermal Control'
    class      = bridge
    subclass   = HOST-PCI
hostb17@pci0:255:5:0:   class=0x060000 card=0x80868086 chip=0x2da88086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = 'Xeon 5600 Series Integrated Memory Controller Channel 1 Control'
    class      = bridge
    subclass   = HOST-PCI
hostb18@pci0:255:5:1:   class=0x060000 card=0x80868086 chip=0x2da98086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = 'Xeon 5600 Series Integrated Memory Controller Channel 1 Address'
    class      = bridge
    subclass   = HOST-PCI
hostb19@pci0:255:5:2:   class=0x060000 card=0x80868086 chip=0x2daa8086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = 'Xeon 5600 Series Integrated Memory Controller Channel 1 Rank'
    class      = bridge
    subclass   = HOST-PCI
hostb20@pci0:255:5:3:   class=0x060000 card=0x80868086 chip=0x2dab8086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = 'Xeon 5600 Series Integrated Memory Controller Channel 1 Thermal Control'
    class      = bridge
    subclass   = HOST-PCI
hostb21@pci0:255:6:0:   class=0x060000 card=0x80868086 chip=0x2db08086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = 'Xeon 5600 Series Integrated Memory Controller Channel 2 Control'
    class      = bridge
    subclass   = HOST-PCI
hostb22@pci0:255:6:1:   class=0x060000 card=0x80868086 chip=0x2db18086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = 'Xeon 5600 Series Integrated Memory Controller Channel 2 Address'
    class      = bridge
    subclass   = HOST-PCI
hostb23@pci0:255:6:2:   class=0x060000 card=0x80868086 chip=0x2db28086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = 'Xeon 5600 Series Integrated Memory Controller Channel 2 Rank'
    class      = bridge
    subclass   = HOST-PCI
hostb24@pci0:255:6:3:   class=0x060000 card=0x80868086 chip=0x2db38086 rev=0x02 hdr=0x00
    vendor     = 'Intel Corporation'
    device     = 'Xeon 5600 Series Integrated Memory Controller Channel 2 Thermal Control'
    class      = bridge
    subclass   = HOST-PCI
```
