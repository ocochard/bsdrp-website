---
title: Forwarding performance lab of a SuperServer 5018A-FTN4 with 10-Gigabit Chelsio T540-CR
description: Forwarding performance lab of a 8 cores Atom C2758 at 2.41GHz with 10-Gigabit Chelsio T540-CR
---
## Hardware detail

This lab will test a [SuperMicro](http://www.supermicro.com/products/system/1U/5018/SYS-5018A-FTN4.cfm) [SuperServer 5018A-FTN4](superserver-5018a-ftn4.md):

- Intel Rangeley: [Atom C2758 (8 cores) at 2.4GHz](http://ark.intel.com/products/77988/Intel-Atom-Processor-C2758-4M-Cache-2_40-GHz)
- 8Gb of RAM
- Quad port Chelsio 10-Gigabit T540-CR and OPT SFP (SFP-10G-LR)

## Lab set-up

For more information about full setup of this lab: [Setting up a forwarding performance benchmark lab](setting-up-a-forwarding-performance-benchmark-lab.md) (switch configuration, etc.).

### Diagram

```
+------------------------------------------+ +-------+ +------------------------------+
|        Device under test                 | |Juniper| | Packet generator & receiver  |
|                                          | |  QFX  | |                              |
|                cxl0: 198.18.0.8/24       |=|   <   |=| vcxl0: 198.18.0.110/24       |
|                      2001:2::8/64        | |       | |        2001:2::110/64        |
|                      (00:07:43:2e:e5:90) | |       | |        (00:07:43:2e:e4:71)   |
|                                          | |       | |                              |
|                cxl1: 198.19.0.8/24       |=|   >   |=| vcxl1: 198.19.0.110/24       |
|                      2001:2:0:8000::8/64 | |       | |        2001:2:0:8000::110/64 |
|                      (00:07:43:2e:e5:98) | +-------+ |        (00:07:43:2e:e4:79)   |
|                                          |           |                              |
|            static routes                 |           |                              |
| 192.18.0.0/16      => 198.18.0.110       |           |                              |
| 192.19.0.0/16      => 198.19.0.110       |           |                              |
| 2001:2::/49        => 2001:2::110        |           |                              |
| 2001:2:0:8000::/49 => 2001:2:0:8000::110 |           |                              |
|                                          |           |                              |
|        static arp and ndp                |           | /boot/loader.conf:           |
| 198.18.0.110        => 00:07:43:2e:e4:71 |           |      hw.cxgbe.num_vis=2      |
| 2001:2::110                              |           |                              |
|                                          |           |                              |
| 198.19.0.110        => 00:07:43:2e:e4:79 |           |                              |
| 2001:2:0:8000::110                       |           |                              |
+------------------------------------------+           +------------------------------+
```

The generator **MUST** generate lot’s of smallest IP flows (multiple source/destination IP addresses and/or UDP src/dst port).

Here is an example for generating 2000 IPv4 flows (100 destination IP addresses * 20 source IP addresses) with a Chelsio NIC:

```
pkt-gen -i vcxl0 -f tx -n 1000000000 -l 60 -d 198.19.10.1:2000-198.19.10.100 -D 00:07:43:2e:e5:90 -s 198.18.10.1:2000-198.18.10.20 -w 4 -p 2
```

And the same with IPv6 flows (minimum frame size of 62 here):

```
pkt-gen -f tx -i vcxl0 -n 1000000000 -l 62 -6 -d "[2001:2:0:8010::1]-[2001:2:0:8010::64]" -D 00:07:43:2e:e5:90 -s "[2001:2:0:10::1]-[2001:2:0:10::14]" -S 00:07:43:2e:e4:72 -w 4 -p 2
```


!!! warning
    This version of pkt-gen is improved with: IPv6 support, software checksum and optional unit normalization. [BSDRP's patch to netmap pkt-gen](https://raw.githubusercontent.com/ocochard/BSDRP/master/BSDRPcur/patches/freebsd.pkt-gen.ae-ipv6.patch).
 Receiver will use this command:

```
pkt-gen -i vcxl1 -f rx -w 4
```

## configuration and tuning

[DUT configurations repository](https://github.com/ocochard/netbenches/tree/master/Atom_C2758_8Cores-Chelsio_T540-CR/forwarding-pf-ipfw/configs)

## Results

![](https://raw.githubusercontent.com/ocochard/netbenches/master/Atom_C2758_8Cores-Chelsio_T540-CR/forwarding-pf-ipfw/results/fbsd12-stable.r354440.BSDRP.1.96/graph.png)
