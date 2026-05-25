---
title: HP ProLiant DL360p Gen8
---
### dmesg

```
Copyright (c) 1992-2019 The FreeBSD Project.
Copyright (c) 1979, 1980, 1983, 1986, 1988, 1989, 1991, 1992, 1993, 1994
    The Regents of the University of California. All rights reserved.
FreeBSD is a registered trademark of The FreeBSD Foundation.
FreeBSD 13.0-CURRENT #0 r356081M: Sun Jan 19 17:13:28 CET 2020
FreeBSD clang version 9.0.1 (git@github.com:llvm/llvm-project.git c1a0a213378a458fbea1a5c77b315c7dce08fd05) (based on LLVM 9.0.1)
VT(vga): text 80x25
CPU: Intel(R) Xeon(R) CPU E5-2650 v2 @ 2.60GHz (2593.80-MHz K8-class CPU)
  Origin="GenuineIntel"  Id=0x306e4  Family=0x6  Model=0x3e  Stepping=4
  Features=0xbfebfbff<FPU,VME,DE,PSE,TSC,MSR,PAE,MCE,CX8,APIC,SEP,MTRR,PGE,MCA,CMOV,PAT,PSE36,CLFLUSH,DTS,ACPI,MMX,FXSR,SSE,SSE2,SS,HTT,TM,PBE>
  Features2=0x7fbee3ff<SSE3,PCLMULQDQ,DTES64,MON,DS_CPL,VMX,SMX,EST,TM2,SSSE3,CX16,xTPR,PDCM,PCID,DCA,SSE4.1,SSE4.2,x2APIC,POPCNT,TSCDLT,AESNI,XSAVE,OSXSAVE,AVX,F16C,RDRAND>
  AMD Features=0x2c100800<SYSCALL,NX,Page1GB,RDTSCP,LM>
  AMD Features2=0x1<LAHF>
  Structured Extended Features=0x281<FSGSBASE,SMEP,ERMS>
  XSAVE Features=0x1<XSAVEOPT>
  VT-x: PAT,HLT,MTF,PAUSE,EPT,UG,VPID,VID,PostIntr
  TSC: P-state invariant, performance statistics
real memory  = 68719476736 (65536 MB)
avail memory = 66795122688 (63700 MB)
Event timer "LAPIC" quality 600
ACPI APIC Table: <HP     ProLiant>
FreeBSD/SMP: Multiprocessor System Detected: 8 CPUs
FreeBSD/SMP: 1 package(s) x 8 core(s) x 2 hardware threads
FreeBSD/SMP Online: 1 package(s) x 8 core(s)
random: registering fast source Intel Secure Key RNG
random: fast provider: "Intel Secure Key RNG"
random: unblocking device.
Firmware Warning (ACPI): Invalid length for FADT/Pm1aControlBlock: 32, using default 16 (20191213/tbfadt-850)
Firmware Warning (ACPI): Invalid length for FADT/Pm2ControlBlock: 32, using default 8 (20191213/tbfadt-850)
ioapic1 <Version 2.0> irqs 24-47
ioapic0 <Version 2.0> irqs 0-23
Launching APs: 7 1 6 2 5 3 4
Timecounter "TSC-low" frequency 1296900156 Hz quality 1000
random: entropy device external interface
WARNING: Device "kbd" is Giant locked and may be deleted before FreeBSD 13.0.
kbd1 at kbdmux0
000.000051 [4336] netmap_init               netmap: loaded module
[ath_hal] loaded
nexus0
vtvga0: <VT VGA driver>
cryptosoft0: <software crypto>
acpi0: <HP ProLiant>
acpi0: Power Button (fixed)
cpu0: <ACPI CPU> numa-domain 0 on acpi0
attimer0: <AT timer> port 0x40-0x43 irq 0 on acpi0
Timecounter "i8254" frequency 1193182 Hz quality 0
Event timer "i8254" frequency 1193182 Hz quality 100
hpet0: <High Precision Event Timer> iomem 0xfed00000-0xfed003ff on acpi0
Timecounter "HPET" frequency 14318180 Hz quality 950
Event timer "HPET" frequency 14318180 Hz quality 550
atrtc0: <AT realtime clock> port 0x70-0x71 on acpi0
atrtc0: registered as a time-of-day clock, resolution 1.000000s
Event timer "RTC" frequency 32768 Hz quality 0
Timecounter "ACPI-fast" frequency 3579545 Hz quality 900
acpi_timer0: <24-bit timer at 3.579545MHz> port 0x908-0x90b on acpi0
pcib0: <ACPI Host-PCI bridge> numa-domain 0 on acpi0
pci0: <ACPI PCI bus> numa-domain 0 on pcib0
pcib1: <ACPI PCI-PCI bridge> at device 1.0 numa-domain 0 on pci0
pci1: <ACPI PCI bus> numa-domain 0 on pcib1
igb0: <Intel(R) PRO/1000 PCI-Express Network Driver> mem 0xf9b00000-0xf9bfffff,0xf9af0000-0xf9af3fff irq 26 at device 0.0 numa-domain 0 on pci1
igb0: Using 1024 TX descriptors and 1024 RX descriptors
igb0: Using 8 RX queues 8 TX queues
igb0: Using MSI-X interrupts with 9 vectors
igb0: Ethernet address: 38:ea:a7:38:4d:74
igb0: netmap queues/slots: TX 8/1024, RX 8/1024
igb1: <Intel(R) PRO/1000 PCI-Express Network Driver> mem 0xf9900000-0xf99fffff,0xf98f0000-0xf98f3fff irq 28 at device 0.1 numa-domain 0 on pci1
igb1: Using 1024 TX descriptors and 1024 RX descriptors
igb1: Using 8 RX queues 8 TX queues
igb1: Using MSI-X interrupts with 9 vectors
igb1: Ethernet address: 38:ea:a7:38:4d:75
igb1: netmap queues/slots: TX 8/1024, RX 8/1024
pcib2: <ACPI PCI-PCI bridge> at device 1.1 numa-domain 0 on pci0
pci2: <ACPI PCI bus> numa-domain 0 on pcib2
pcib3: <ACPI PCI-PCI bridge> at device 2.0 numa-domain 0 on pci0
pci3: <ACPI PCI bus> numa-domain 0 on pcib3
pci3: <network, ethernet> at device 0.0 (no driver attached)
pci3: <network, ethernet> at device 0.1 (no driver attached)
pci3: <mass storage> at device 0.2 (no driver attached)
pci3: <mass storage> at device 0.3 (no driver attached)
pcib4: <ACPI PCI-PCI bridge> at device 2.1 numa-domain 0 on pci0
pci4: <ACPI PCI bus> numa-domain 0 on pcib4
pcib5: <ACPI PCI-PCI bridge> at device 2.2 numa-domain 0 on pci0
pci5: <ACPI PCI bus> numa-domain 0 on pcib5
pcib6: <ACPI PCI-PCI bridge> at device 2.3 numa-domain 0 on pci0
pci6: <ACPI PCI bus> numa-domain 0 on pcib6
pcib7: <ACPI PCI-PCI bridge> at device 3.0 numa-domain 0 on pci0
pci7: <ACPI PCI bus> numa-domain 0 on pcib7
t5nex0: <Chelsio T540-CR> mem 0xfb980000-0xfb9fffff,0xfa000000-0xfaffffff,0xf9ff0000-0xf9ff1fff irq 40 at device 0.4 numa-domain 0 on pci7
cxl0: <port 0> numa-domain 0 on t5nex0
cxl0: Ethernet address: 00:07:43:2e:e4:70
cxl0: 8 txq, 8 rxq (NIC)
vcxl0: <port 0 vi 1> numa-domain 0 on cxl0
vcxl0: Ethernet address: 00:07:43:2e:e4:71
vcxl0: netmap queues/slots: TX 2/1023, RX 2/1024
vcxl0: 1 txq, 1 rxq (NIC); 2 txq, 2 rxq (netmap)
cxl1: <port 1> numa-domain 0 on t5nex0
cxl1: Ethernet address: 00:07:43:2e:e4:78
cxl1: 8 txq, 8 rxq (NIC)
vcxl1: <port 1 vi 1> numa-domain 0 on cxl1
vcxl1: Ethernet address: 00:07:43:2e:e4:79
vcxl1: netmap queues/slots: TX 2/1023, RX 2/1024
vcxl1: 1 txq, 1 rxq (NIC); 2 txq, 2 rxq (netmap)
cxl2: <port 2> numa-domain 0 on t5nex0
cxl2: Ethernet address: 00:07:43:2e:e4:80
cxl2: 8 txq, 8 rxq (NIC)
vcxl2: <port 2 vi 1> numa-domain 0 on cxl2
vcxl2: Ethernet address: 00:07:43:2e:e4:81
vcxl2: netmap queues/slots: TX 2/1023, RX 2/1024
vcxl2: 1 txq, 1 rxq (NIC); 2 txq, 2 rxq (netmap)
cxl3: <port 3> numa-domain 0 on t5nex0
cxl3: Ethernet address: 00:07:43:2e:e4:88
cxl3: 8 txq, 8 rxq (NIC)
vcxl3: <port 3 vi 1> numa-domain 0 on cxl3
vcxl3: Ethernet address: 00:07:43:2e:e4:89
vcxl3: netmap queues/slots: TX 2/1023, RX 2/1024
vcxl3: 1 txq, 1 rxq (NIC); 2 txq, 2 rxq (netmap)
t5nex0: PCIe gen3 x8, 4 ports, 42 MSI-X interrupts, 92 eq, 45 iq
pci7: <mass storage, SCSI> at device 0.5 (no driver attached)
pci7: <serial bus, Fibre Channel> at device 0.6 (no driver attached)
pcib8: <ACPI PCI-PCI bridge> at device 3.1 numa-domain 0 on pci0
pci8: <ACPI PCI bus> numa-domain 0 on pcib8
pcib9: <ACPI PCI-PCI bridge> at device 3.2 numa-domain 0 on pci0
pci9: <ACPI PCI bus> numa-domain 0 on pcib9
pcib10: <ACPI PCI-PCI bridge> at device 3.3 numa-domain 0 on pci0
pci10: <ACPI PCI bus> numa-domain 0 on pcib10
pcib11: <ACPI PCI-PCI bridge> at device 17.0 numa-domain 0 on pci0
pci11: <ACPI PCI bus> numa-domain 0 on pcib11
ehci0: <Intel Patsburg USB 2.0 controller> mem 0xf8460000-0xf84603ff irq 21 at device 26.0 numa-domain 0 on pci0
usbus0: EHCI version 1.0
usbus0 numa-domain 0 on ehci0
usbus0: 480Mbps High Speed USB v2.0
pcib12: <ACPI PCI-PCI bridge> at device 28.0 numa-domain 0 on pci0
pci12: <ACPI PCI bus> numa-domain 0 on pcib12
pcib13: <ACPI PCI-PCI bridge> at device 28.7 numa-domain 0 on pci0
pci13: <ACPI PCI bus> numa-domain 0 on pcib13
vgapci0: <VGA-compatible display> mem 0xf7000000-0xf7ffffff,0xf95e0000-0xf95e3fff,0xf8800000-0xf8ffffff irq 16 at device 0.1 numa-domain 0 on pci13
vgapci0: Boot video device
uhci0: <HP iLO Standard Virtual USB controller> port 0x3c00-0x3c1f irq 16 at device 0.4 numa-domain 0 on pci13
usbus1 numa-domain 0 on uhci0
usbus1: 12Mbps Full Speed USB v1.0
ehci1: <Intel Patsburg USB 2.0 controller> mem 0xf8450000-0xf84503ff irq 20 at device 29.0 numa-domain 0 on pci0
usbus2: EHCI version 1.0
usbus2 numa-domain 0 on ehci1
usbus2: 480Mbps High Speed USB v2.0
pcib14: <PCI-PCI bridge> at device 30.0 numa-domain 0 on pci0
pci14: <PCI bus> numa-domain 0 on pcib14
isab0: <PCI-ISA bridge> at device 31.0 numa-domain 0 on pci0
isa0: <ISA bus> numa-domain 0 on isab0
acpi_tz0: <Thermal Zone> on acpi0
acpi_syscontainer0: <System Container> port 0x2e-0x2f on acpi0
atkbdc0: <Keyboard controller (i8042)> port 0x60,0x64 irq 1 on acpi0
atkbd0: <AT Keyboard> irq 1 on atkbdc0
kbd0 at atkbd0
atkbd0: [GIANT-LOCKED]
uart0: <Non-standard ns8250 class UART with FIFOs> port 0x3f8-0x3ff irq 4 flags 0x10 on acpi0
uart0: console (115200,n,8,1)
orm0: <ISA Option ROM> at iomem 0xc0000-0xc7fff pnpid ORM0000 on isa0
vga0: <Generic ISA VGA> at port 0x3c0-0x3df iomem 0xa0000-0xbffff pnpid PNP0900 on isa0
uart1: <Non-standard ns8250 class UART with FIFOs> at port 0x2f8 irq 3 on isa0
est0: <Enhanced SpeedStep Frequency Control> numa-domain 0 on cpu0
est: CPU supports Enhanced Speedstep, but is not recognized.
est: cpu_vendor GenuineIntel, msr 208100001e00
device_attach: est0 attach returned 6
est: CPU supports Enhanced Speedstep, but is not recognized.
est: cpu_vendor GenuineIntel, msr 208100001e00
device_attach: est1 attach returned 6
est: CPU supports Enhanced Speedstep, but is not recognized.
est: cpu_vendor GenuineIntel, msr 208100001e00
device_attach: est2 attach returned 6
est: CPU supports Enhanced Speedstep, but is not recognized.
est: cpu_vendor GenuineIntel, msr 208100001e00
device_attach: est3 attach returned 6
est: CPU supports Enhanced Speedstep, but is not recognized.
est: cpu_vendor GenuineIntel, msr 208100001e00
device_attach: est4 attach returned 6
est: CPU supports Enhanced Speedstep, but is not recognized.
est: cpu_vendor GenuineIntel, msr 208100001e00
device_attach: est5 attach returned 6
est: CPU supports Enhanced Speedstep, but is not recognized.
est: cpu_vendor GenuineIntel, msr 208100001e00
device_attach: est6 attach returned 6
est: CPU supports Enhanced Speedstep, but is not recognized.
est: cpu_vendor GenuineIntel, msr 208100001e00
device_attach: est7 attach returned 6
Timecounters tick every 1.000 msec
Trying to mount root from ufs:/dev/ufs/BSDRPs1a [ro]...
Root mount waiting for: usbus0ugen0.1: <Intel EHCI root HUB> at usbus0
ugen2.1: <Intel EHCI root HUB> at usbus2
ugen1.1: <HP UHCI root HUB> at usbus1
 usbus1 usbus2
uhub0 numa-domain 0 on usbus2
uhub0: <Intel EHCI root HUB, class 9/0, rev 2.00/1.00, addr 1> on usbus2
uhub1 numa-domain 0 on usbus1
uhub1: <HP UHCI root HUB, class 9/0, rev 1.00/1.00, addr 1> on usbus1
uhub2 numa-domain 0 on usbus0
uhub2: <Intel EHCI root HUB, class 9/0, rev 2.00/1.00, addr 1> on usbus0
uhub1: 2 ports with 2 removable, self powered
uhub0: 2 ports with 2 removable, self powered
uhub2: 2 ports with 2 removable, self powered
Root mount waiting for: usbus0 usbus2
ugen2.2: <vendor 0x8087 product 0x0024> at usbus2
uhub3 numa-domain 0 on uhub0
uhub3: <vendor 0x8087 product 0x0024, class 9/0, rev 2.00/0.00, addr 2> on usbus2
ugen0.2: <vendor 0x8087 product 0x0024> at usbus0
uhub4 numa-domain 0 on uhub2
uhub4: <vendor 0x8087 product 0x0024, class 9/0, rev 2.00/0.00, addr 2> on usbus0
Root mount waiting for: usbus0 usbus2
uhub4: 6 ports with 6 removable, self powered
uhub3: 8 ports with 8 removable, self powered
Root mount waiting for: usbus0 usbus2
ugen2.3: <vendor 0x0424 product 0x2660> at usbus2
uhub5 numa-domain 0 on uhub3
uhub5: <vendor 0x0424 product 0x2660, class 9/0, rev 2.00/8.01, addr 3> on usbus2
uhub5: 2 ports with 1 removable, self powered
ugen0.3: <Generic AutoRUN/Partition> at usbus0
umass0 numa-domain 0 on uhub4
umass0: <Generic AutoRUN/Partition, class 0/0, rev 2.00/1.00, addr 3> on usbus0
umass0:  SCSI over Bulk-Only; quirks = 0xc100
umass0:0:0: Attached to scbus0
da0 at umass-sim0 bus 0 scbus0 target 0 lun 0
da0: <Mass Storage Device > Removable Direct Access SCSI device
da0: Serial Number 125B00000000
da0: 40.000MB/s transfers
da0: 1902MB (3897343 512 byte sectors)
da0: quirks=0x2<NO_6_BYTE>
mountroot: waiting for device /dev/ufs/BSDRPs1a...
debugnet_any_ifnet_update: Bad dn_init result from igb0 (ifp 0xfffff80003fe5000), ignoring.
ioat0: <IVB IOAT Ch0> mem 0xf84f0000-0xf84f3fff irq 31 at device 4.0 numa-domain 0 on pci0
ioat0: Capabilities: 2f7<PQ,Extended_APIC_ID,Block_Fill,Move_CRC,DCA,Marker_Skipping,CRC,Page_Break>
ioat1: <IVB IOAT Ch1> mem 0xf84e0000-0xf84e3fff irq 39 at device 4.1 numa-domain 0 on pci0
ioat1: Capabilities: 2f7<PQ,Extended_APIC_ID,Block_Fill,Move_CRC,DCA,Marker_Skipping,CRC,Page_Break>
ioat2: <IVB IOAT Ch2> mem 0xf84d0000-0xf84d3fff irq 31 at device 4.2 numa-domain 0 on pci0
ioat2: Capabilities: f7<Extended_APIC_ID,Block_Fill,Move_CRC,DCA,Marker_Skipping,CRC,Page_Break>
ioat3: <IVB IOAT Ch3> mem 0xf84c0000-0xf84c3fff irq 39 at device 4.3 numa-domain 0 on pci0
ioat3: Capabilities: f7<Extended_APIC_ID,Block_Fill,Move_CRC,DCA,Marker_Skipping,CRC,Page_Break>
ioat4: <IVB IOAT Ch4> mem 0xf84b0000-0xf84b3fff irq 31 at device 4.4 numa-domain 0 on pci0
ioat4: Capabilities: f7<Extended_APIC_ID,Block_Fill,Move_CRC,DCA,Marker_Skipping,CRC,Page_Break>
ioat5: <IVB IOAT Ch5> mem 0xf84a0000-0xf84a3fff irq 39 at device 4.5 numa-domain 0 on pci0
ioat5: Capabilities: f7<Extended_APIC_ID,Block_Fill,Move_CRC,DCA,Marker_Skipping,CRC,Page_Break>
ioat6: <IVB IOAT Ch6> mem 0xf8490000-0xf8493fff irq 31 at device 4.6 numa-domain 0 on pci0
ioat6: Capabilities: f7<Extended_APIC_ID,Block_Fill,Move_CRC,DCA,Marker_Skipping,CRC,Page_Break>
ioat7: <IVB IOAT Ch7> mem 0xf8480000-0xf8483fff irq 39 at device 4.7 numa-domain 0 on pci0
ioat7: Capabilities: f7<Extended_APIC_ID,Block_Fill,Move_CRC,DCA,Marker_Skipping,CRC,Page_Break>
aesni0: <AES-CBC,AES-CCM,AES-GCM,AES-ICM,AES-XTS>
```

### pciconf

```
hostb0@pci0:0:0:0:  class=0x060000 rev=0x04 hdr=0x00 vendor=0x8086 device=0x0e00 subvendor=0x103c subdevice=0x18a8
    vendor     = 'Intel Corporation'
    device     = 'Xeon E7 v2/Xeon E5 v2/Core i7 DMI2'
    class      = bridge
    subclass   = HOST-PCI
pcib1@pci0:0:1:0:   class=0x060400 rev=0x04 hdr=0x01 vendor=0x8086 device=0x0e02 subvendor=0x103c subdevice=0x18a8
    vendor     = 'Intel Corporation'
    device     = 'Xeon E7 v2/Xeon E5 v2/Core i7 PCI Express Root Port 1a'
    class      = bridge
    subclass   = PCI-PCI
pcib2@pci0:0:1:1:   class=0x060400 rev=0x04 hdr=0x01 vendor=0x8086 device=0x0e03 subvendor=0x103c subdevice=0x18a8
    vendor     = 'Intel Corporation'
    device     = 'Xeon E7 v2/Xeon E5 v2/Core i7 PCI Express Root Port 1b'
    class      = bridge
    subclass   = PCI-PCI
pcib3@pci0:0:2:0:   class=0x060400 rev=0x04 hdr=0x01 vendor=0x8086 device=0x0e04 subvendor=0x103c subdevice=0x18a8
    vendor     = 'Intel Corporation'
    device     = 'Xeon E7 v2/Xeon E5 v2/Core i7 PCI Express Root Port 2a'
    class      = bridge
    subclass   = PCI-PCI
pcib4@pci0:0:2:1:   class=0x060400 rev=0x04 hdr=0x01 vendor=0x8086 device=0x0e05 subvendor=0x103c subdevice=0x18a8
    vendor     = 'Intel Corporation'
    device     = 'Xeon E7 v2/Xeon E5 v2/Core i7 PCI Express Root Port 2b'
    class      = bridge
    subclass   = PCI-PCI
pcib5@pci0:0:2:2:   class=0x060400 rev=0x04 hdr=0x01 vendor=0x8086 device=0x0e06 subvendor=0x103c subdevice=0x18a8
    vendor     = 'Intel Corporation'
    device     = 'Xeon E7 v2/Xeon E5 v2/Core i7 PCI Express Root Port 2c'
    class      = bridge
    subclass   = PCI-PCI
pcib6@pci0:0:2:3:   class=0x060400 rev=0x04 hdr=0x01 vendor=0x8086 device=0x0e07 subvendor=0x103c subdevice=0x18a8
    vendor     = 'Intel Corporation'
    device     = 'Xeon E7 v2/Xeon E5 v2/Core i7 PCI Express Root Port 2d'
    class      = bridge
    subclass   = PCI-PCI
pcib7@pci0:0:3:0:   class=0x060400 rev=0x04 hdr=0x01 vendor=0x8086 device=0x0e08 subvendor=0x103c subdevice=0x18a8
    vendor     = 'Intel Corporation'
    device     = 'Xeon E7 v2/Xeon E5 v2/Core i7 PCI Express Root Port 3a'
    class      = bridge
    subclass   = PCI-PCI
pcib8@pci0:0:3:1:   class=0x060400 rev=0x04 hdr=0x01 vendor=0x8086 device=0x0e09 subvendor=0x103c subdevice=0x18a8
    vendor     = 'Intel Corporation'
    device     = 'Xeon E7 v2/Xeon E5 v2/Core i7 PCI Express Root Port 3b'
    class      = bridge
    subclass   = PCI-PCI
pcib9@pci0:0:3:2:   class=0x060400 rev=0x04 hdr=0x01 vendor=0x8086 device=0x0e0a subvendor=0x103c subdevice=0x18a8
    vendor     = 'Intel Corporation'
    device     = 'Xeon E7 v2/Xeon E5 v2/Core i7 PCI Express Root Port 3c'
    class      = bridge
    subclass   = PCI-PCI
pcib10@pci0:0:3:3:  class=0x060400 rev=0x04 hdr=0x01 vendor=0x8086 device=0x0e0b subvendor=0x103c subdevice=0x18a8
    vendor     = 'Intel Corporation'
    device     = 'Xeon E7 v2/Xeon E5 v2/Core i7 PCI Express Root Port 3d'
    class      = bridge
    subclass   = PCI-PCI
ioat0@pci0:0:4:0:   class=0x088000 rev=0x04 hdr=0x00 vendor=0x8086 device=0x0e20 subvendor=0x103c subdevice=0x18a8
    vendor     = 'Intel Corporation'
    device     = 'Xeon E7 v2/Xeon E5 v2/Core i7 Crystal Beach DMA Channel 0'
    class      = base peripheral
ioat1@pci0:0:4:1:   class=0x088000 rev=0x04 hdr=0x00 vendor=0x8086 device=0x0e21 subvendor=0x103c subdevice=0x18a8
    vendor     = 'Intel Corporation'
    device     = 'Xeon E7 v2/Xeon E5 v2/Core i7 Crystal Beach DMA Channel 1'
    class      = base peripheral
ioat2@pci0:0:4:2:   class=0x088000 rev=0x04 hdr=0x00 vendor=0x8086 device=0x0e22 subvendor=0x103c subdevice=0x18a8
    vendor     = 'Intel Corporation'
    device     = 'Xeon E7 v2/Xeon E5 v2/Core i7 Crystal Beach DMA Channel 2'
    class      = base peripheral
ioat3@pci0:0:4:3:   class=0x088000 rev=0x04 hdr=0x00 vendor=0x8086 device=0x0e23 subvendor=0x103c subdevice=0x18a8
    vendor     = 'Intel Corporation'
    device     = 'Xeon E7 v2/Xeon E5 v2/Core i7 Crystal Beach DMA Channel 3'
    class      = base peripheral
ioat4@pci0:0:4:4:   class=0x088000 rev=0x04 hdr=0x00 vendor=0x8086 device=0x0e24 subvendor=0x103c subdevice=0x18a8
    vendor     = 'Intel Corporation'
    device     = 'Xeon E7 v2/Xeon E5 v2/Core i7 Crystal Beach DMA Channel 4'
    class      = base peripheral
ioat5@pci0:0:4:5:   class=0x088000 rev=0x04 hdr=0x00 vendor=0x8086 device=0x0e25 subvendor=0x103c subdevice=0x18a8
    vendor     = 'Intel Corporation'
    device     = 'Xeon E7 v2/Xeon E5 v2/Core i7 Crystal Beach DMA Channel 5'
    class      = base peripheral
ioat6@pci0:0:4:6:   class=0x088000 rev=0x04 hdr=0x00 vendor=0x8086 device=0x0e26 subvendor=0x103c subdevice=0x18a8
    vendor     = 'Intel Corporation'
    device     = 'Xeon E7 v2/Xeon E5 v2/Core i7 Crystal Beach DMA Channel 6'
    class      = base peripheral
ioat7@pci0:0:4:7:   class=0x088000 rev=0x04 hdr=0x00 vendor=0x8086 device=0x0e27 subvendor=0x103c subdevice=0x18a8
    vendor     = 'Intel Corporation'
    device     = 'Xeon E7 v2/Xeon E5 v2/Core i7 Crystal Beach DMA Channel 7'
    class      = base peripheral
none0@pci0:0:5:0:   class=0x088000 rev=0x04 hdr=0x00 vendor=0x8086 device=0x0e28 subvendor=0x103c subdevice=0x18a8
    vendor     = 'Intel Corporation'
    device     = 'Xeon E7 v2/Xeon E5 v2/Core i7 VTd/Memory Map/Misc'
    class      = base peripheral
none1@pci0:0:5:2:   class=0x088000 rev=0x04 hdr=0x00 vendor=0x8086 device=0x0e2a subvendor=0x103c subdevice=0x18a8
    vendor     = 'Intel Corporation'
    device     = 'Xeon E7 v2/Xeon E5 v2/Core i7 IIO RAS'
    class      = base peripheral
ioapic0@pci0:0:5:4: class=0x080020 rev=0x04 hdr=0x00 vendor=0x8086 device=0x0e2c subvendor=0x103c subdevice=0x18a8
    vendor     = 'Intel Corporation'
    device     = 'Xeon E7 v2/Xeon E5 v2/Core i7 IOAPIC'
    class      = base peripheral
    subclass   = interrupt controller
pcib11@pci0:0:17:0: class=0x060400 rev=0x05 hdr=0x01 vendor=0x8086 device=0x1d3e subvendor=0x103c subdevice=0x18a9
    vendor     = 'Intel Corporation'
    device     = 'C600/X79 series chipset PCI Express Virtual Root Port'
    class      = bridge
    subclass   = PCI-PCI
ehci0@pci0:0:26:0:  class=0x0c0320 rev=0x05 hdr=0x00 vendor=0x8086 device=0x1d2d subvendor=0x103c subdevice=0x18a9
    vendor     = 'Intel Corporation'
    device     = 'C600/X79 series chipset USB2 Enhanced Host Controller'
    class      = serial bus
    subclass   = USB
pcib12@pci0:0:28:0: class=0x060400 rev=0xb5 hdr=0x01 vendor=0x8086 device=0x1d10 subvendor=0x103c subdevice=0x18a9
    vendor     = 'Intel Corporation'
    device     = 'C600/X79 series chipset PCI Express Root Port 1'
    class      = bridge
    subclass   = PCI-PCI
pcib13@pci0:0:28:7: class=0x060400 rev=0xb5 hdr=0x01 vendor=0x8086 device=0x1d1e subvendor=0x103c subdevice=0x18a9
    vendor     = 'Intel Corporation'
    device     = 'C600/X79 series chipset PCI Express Root Port 8'
    class      = bridge
    subclass   = PCI-PCI
ehci1@pci0:0:29:0:  class=0x0c0320 rev=0x05 hdr=0x00 vendor=0x8086 device=0x1d26 subvendor=0x103c subdevice=0x18a9
    vendor     = 'Intel Corporation'
    device     = 'C600/X79 series chipset USB2 Enhanced Host Controller'
    class      = serial bus
    subclass   = USB
pcib14@pci0:0:30:0: class=0x060401 rev=0xa5 hdr=0x01 vendor=0x8086 device=0x244e subvendor=0x103c subdevice=0x18a9
    vendor     = 'Intel Corporation'
    device     = '82801 PCI Bridge'
    class      = bridge
    subclass   = PCI-PCI
isab0@pci0:0:31:0:  class=0x060100 rev=0x05 hdr=0x00 vendor=0x8086 device=0x1d41 subvendor=0x0000 subdevice=0x0000
    vendor     = 'Intel Corporation'
    device     = 'C600/X79 series chipset LPC Controller'
    class      = bridge
    subclass   = PCI-ISA
igb0@pci0:4:0:0:    class=0x020000 rev=0x01 hdr=0x00 vendor=0x8086 device=0x1521 subvendor=0x103c subdevice=0x339e
    vendor     = 'Intel Corporation'
    device     = 'I350 Gigabit Network Connection'
    class      = network
    subclass   = ethernet
igb1@pci0:4:0:1:    class=0x020000 rev=0x01 hdr=0x00 vendor=0x8086 device=0x1521 subvendor=0x103c subdevice=0x339e
    vendor     = 'Intel Corporation'
    device     = 'I350 Gigabit Network Connection'
    class      = network
    subclass   = ethernet
none2@pci0:3:0:0:   class=0x020000 rev=0x01 hdr=0x00 vendor=0x19a2 device=0x0710 subvendor=0x103c subdevice=0x3376
    vendor     = 'Emulex Corporation'
    device     = 'OneConnect 10Gb NIC (be3)'
    class      = network
    subclass   = ethernet
none3@pci0:3:0:1:   class=0x020000 rev=0x01 hdr=0x00 vendor=0x19a2 device=0x0710 subvendor=0x103c subdevice=0x3376
    vendor     = 'Emulex Corporation'
    device     = 'OneConnect 10Gb NIC (be3)'
    class      = network
    subclass   = ethernet
none4@pci0:3:0:2:   class=0x018000 rev=0x01 hdr=0x00 vendor=0x19a2 device=0x0712 subvendor=0x103c subdevice=0x3376
    vendor     = 'Emulex Corporation'
    device     = 'OneConnect 10Gb iSCSI Initiator (be3)'
    class      = mass storage
none5@pci0:3:0:3:   class=0x018000 rev=0x01 hdr=0x00 vendor=0x19a2 device=0x0712 subvendor=0x103c subdevice=0x3376
    vendor     = 'Emulex Corporation'
    device     = 'OneConnect 10Gb iSCSI Initiator (be3)'
    class      = mass storage
t5iov0@pci0:7:0:0:  class=0x020000 rev=0x00 hdr=0x00 vendor=0x1425 device=0x5003 subvendor=0x1425 subdevice=0x0000
    vendor     = 'Chelsio Communications Inc'
    device     = 'T540-CR Unified Wire Ethernet Controller'
    class      = network
    subclass   = ethernet
t5iov1@pci0:7:0:1:  class=0x020000 rev=0x00 hdr=0x00 vendor=0x1425 device=0x5003 subvendor=0x1425 subdevice=0x0000
    vendor     = 'Chelsio Communications Inc'
    device     = 'T540-CR Unified Wire Ethernet Controller'
    class      = network
    subclass   = ethernet
t5iov2@pci0:7:0:2:  class=0x020000 rev=0x00 hdr=0x00 vendor=0x1425 device=0x5003 subvendor=0x1425 subdevice=0x0000
    vendor     = 'Chelsio Communications Inc'
    device     = 'T540-CR Unified Wire Ethernet Controller'
    class      = network
    subclass   = ethernet
t5iov3@pci0:7:0:3:  class=0x020000 rev=0x00 hdr=0x00 vendor=0x1425 device=0x5003 subvendor=0x1425 subdevice=0x0000
    vendor     = 'Chelsio Communications Inc'
    device     = 'T540-CR Unified Wire Ethernet Controller'
    class      = network
    subclass   = ethernet
t5nex0@pci0:7:0:4:  class=0x020000 rev=0x00 hdr=0x00 vendor=0x1425 device=0x5403 subvendor=0x1425 subdevice=0x0000
    vendor     = 'Chelsio Communications Inc'
    device     = 'T540-CR Unified Wire Ethernet Controller'
    class      = network
    subclass   = ethernet
none6@pci0:7:0:5:   class=0x010000 rev=0x00 hdr=0x00 vendor=0x1425 device=0x5503 subvendor=0x1425 subdevice=0x0000
    vendor     = 'Chelsio Communications Inc'
    device     = 'T540-CR Unified Wire Storage Controller'
    class      = mass storage
    subclass   = SCSI
none7@pci0:7:0:6:   class=0x0c0400 rev=0x00 hdr=0x00 vendor=0x1425 device=0x5603 subvendor=0x1425 subdevice=0x0000
    vendor     = 'Chelsio Communications Inc'
    device     = 'T540-CR Unified Wire Storage Controller'
    class      = serial bus
    subclass   = Fibre Channel
none8@pci0:1:0:0:   class=0x088000 rev=0x05 hdr=0x00 vendor=0x103c device=0x3306 subvendor=0x103c subdevice=0x3381
    vendor     = 'Hewlett-Packard Company'
    device     = 'Integrated Lights-Out Standard Slave Instrumentation & System Support'
    class      = base peripheral
vgapci0@pci0:1:0:1: class=0x030000 rev=0x00 hdr=0x00 vendor=0x102b device=0x0533 subvendor=0x103c subdevice=0x3381
    vendor     = 'Matrox Electronics Systems Ltd.'
    device     = 'MGA G200EH'
    class      = display
    subclass   = VGA
none9@pci0:1:0:2:   class=0x088000 rev=0x05 hdr=0x00 vendor=0x103c device=0x3307 subvendor=0x103c subdevice=0x3381
    vendor     = 'Hewlett-Packard Company'
    device     = 'Integrated Lights-Out Standard Management Processor Support and Messaging'
    class      = base peripheral
uhci0@pci0:1:0:4:   class=0x0c0300 rev=0x02 hdr=0x00 vendor=0x103c device=0x3300 subvendor=0x103c subdevice=0x3381
    vendor     = 'Hewlett-Packard Company'
    device     = 'Integrated Lights-Out Standard Virtual USB Controller'
    class      = serial bus
    subclass   = USB
```
