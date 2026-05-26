---
title: Forwarding performance lab of Netgate RCC-VE 4860
description: Forwarding performance lab of a quad core Intel Atom C2558E (2.40GHz) with 2+4 Gigabit Intel NIC
---
## Hardware detail

This lab tests a [Netgate RCC-VE 4860](http://store.netgate.com/ADI/RCC-VE-4860.aspx) ([dmesg](netgate-rcc-ve-4860.md)):

- Quad-core Intel Atom C2558 (2.40 GHz)
- 2x Gigabit Intel i211
- 4x Gigabit Intel i350
- 8 GB of RAM

## Lab set-up

For more information about full setup of this lab: [Setting up a forwarding performance benchmark lab](setting-up-a-forwarding-performance-benchmark-lab.md) (switch configuration, etc.).

### Diagram

```
 +------------------------------------------+    +-----------------------+
 |            Device under Test             |    |     Packet gen        |
 |                  igb2:   198.18.0.209/24 |<===| igb2: 198.18.0.203    |
 |                           2001:2::209/64 |    |     2001:2::203/64    |
 |                     (00:08:a2:09:33:da)  |    | (00:1b:21:c4:95:7a)   |
 |                                          |    |                       |
 |                  igb3:   198.19.0.209/24 |    | igb3: 198.19.0.203    |
 |                    2001:2:0:8000::209/64 |    | 2001:2:0:8000::203/64 |
 |                     (00:08:a2:09:33:db)  |===>| (00:1b:21:c4:95:7b)   |
 |                                          |    |                       |
 |               static routes              |    |                       |
 |      198.19.0.0/16 => 198.19.0.203       |    +-----------------------+
 |      198.18.0.0/16 => 198.18.0.203       |
 | 2001:2::/49        => 2001:2::203        |
 | 2001:2:0:8000::/49 => 2001:2:0:8000::203 |
 |                                          |
 |            static arp and ndp            |
 | 198.18.0.203        => 00:1b:21:c4:95:7a |
 | 2001:2::203                              |
 |                                          |
 | 198.19.0.203        => 00:1b:21:c4:95:7b |
 | 2001:2:0:8000::203                       |
 |                                          |
 |                                          |
 +------------------------------------------+
```

This device uses two kinds of Intel NIC:

- igb0 and igb1: Intel i211 with 2 queues, intended for admin purposes
- igb2 to igb5: Intel i350 with 4 queues (and iPXE support), intended for forwarding/firewalling

The generator **MUST** generate lots of IP flows (multiple source/destination IP addresses and/or UDP src/dst ports) with the minimum packet size (to produce the maximum packet rate) with one of these commands:

Multiple source/destination IP addresses (don't forget to specify the UDP port to avoid using port 0, which is filtered by pf):

```
pkt-gen -i igb2 -f tx -n 80000000 -l 60 -d 198.19.10.1:2000-198.19.10.20 -D 00:08:a2:09:33:da -s 198.18.10.1:2000-198.18.10.100 -S 00:1b:21:c4:95:7a -w 4 -U
```

And the same with IPv6 flows (minimum frame size of 62 for a valid empty UDP packet):

```
pkt-gen -f tx -i igb2 -n 1000000000 -l 62 -6 -d "[2001:2:0:8001::1]-[2001:2:0:8001::64]" -D 00:08:a2:09:33:da -s "[2001:2:0:1::1]-[2001:2:0:1::14]" -S 00:1b:21:c4:95:7a -w 4 -U
```

The receiver will use this command:

```
pkt-gen -i igb3 -f rx -w 4
```

## Configuration and tuning

[Configuration repository](https://github.com/ocochard/netbenches/tree/master/Atom_C2558_4Cores-Intel_i350/forwarding-pf-ipfw/configs)

## Results

![](https://raw.githubusercontent.com/ocochard/netbenches/master/Atom_C2558_4Cores-Intel_i350/forwarding-pf-ipfw/results/fbsd12-stable.r354440.BSDRP.1.96/graph.png)
