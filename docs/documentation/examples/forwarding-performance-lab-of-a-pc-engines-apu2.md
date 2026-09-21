---
title: Forwarding performance lab of a PC Engines APU 2
description: Forwarding performance lab of a quad-core AMD GX-412TC (1 GHz) with 3 Intel i210AT Gigabit ports
---
## Hardware detail

This lab tests a [PC Engines APU 2C4](http://www.pcengines.ch/apu2.htm) ([dmesg](pc-engines-apu2.md)):

- Quad-core [AMD GX-412TC Processor](https://www.amd.com/Documents/AMDGSeriesSOCProductBrief.pdf) (1 GHz with AES-NI)
- 3x Intel i210AT Gigabit ports
- 4 GB of RAM

## Lab set-up

For more information about the full setup of this lab: [Setting up a forwarding performance benchmark lab](setting-up-a-forwarding-performance-benchmark-lab.md) (switch configuration, etc.).

BSDRP release 2.3, based on FreeBSD 16-CURRENT (n313366), is used.

### Diagram

```
 +------------------------------------------+      +-----------------------+
 |             Device under Test            |      |  Packet gen & receiv  |
 |                                          |      |                       |
 |                igb1:    198.18.0.205/24  |<=====| igb2: 198.18.0.203/24 |
 |                            2001:2::8/64  |      |        2001:2::203/64 |
 |                       00:0d:b9:41:ca:3d  |      |     00:1b:21:c4:95:7a |
 |                                          |      |                       |
 |                igb2:    198.19.0.205/24  |=====>| igb3: 198.19.0.203/24 |
 |                     2001:2:0:8000::8/64  |      | 2001:2:0:8000::203/64 |
 |                       00:0d:b9:41:ca:3e  |      |     00:1b:21:c4:95:7b |
 |                                          |      |                       |
 |               static routes              |      |                       |
 |      198.19.0.0/16 => 198.19.0.203       |      |                       |
 |      198.18.0.0/16 => 198.18.0.203       |      |                       |
 |        2001:2::/49 => 2001:2::203        |      |                       |
 | 2001:2:0:8000::/49 => 2001:2:0:8000::203 |      |                       |
 |                                          |      |                       |
 |            static arp and ndp            |      |                       |
 | 198.18.0.203        => 00:1b:21:c4:95:7a |      |                       |
 | 2001:2::203                              |      |                       |
 |                                          |      |                       |
 | 198.19.0.203        => 00:1b:21:c4:95:7b |      |                       |
 | 2001:2:0:8000::203                       |      |                       |
 +------------------------------------------+      +-----------------------+
```

The generator **MUST** generate lots of IP flows (multiple source/destination IP addresses and/or UDP src/dst ports) with the minimum packet size (to produce the maximum packet rate), using one of these commands:

Multiple source/destination IP addresses (don't forget to specify the UDP port to avoid using port 0, which is filtered by pf):

```
pkt-gen -U -i igb2 -f tx -n 80000000 -l 60 -d 198.19.10.1:2000-198.19.10.20 -D 00:0d:b9:41:ca:3d -s 198.18.10.1:2000-198.18.10.100 -w 4
```

And the same with IPv6 flows:

```
pkt-gen -N -f tx -i igb2 -n 1000000000 -l 60 -6 -d "[2001:2:0:8001::1]-[2001:2:0:8001::64]" -D 00:0d:b9:41:ca:3d -s "[2001:2:0:1::1]-[2001:2:0:1::14]" -S 00:07:43:2e:e4:72 -w 4
```

The receiver will use this command:

```
pkt-gen -i igb3 -f rx -w 4
```

## Basic configuration

### Disabling Ethernet flow control

```
echo "dev.igb.1.fc=0" >> /etc/sysctl.conf
echo "dev.igb.2.fc=0" >> /etc/sysctl.conf
service sysctl restart
```

### Enabling Tx abdicate (iflib drivers)

If the NIC driver is iflib-based, you should enable TX abdicate (done automatically by BSDRP but not on a generic FreeBSD):

```
cat <<EOF >> /etc/sysctl.conf
# Enabling Tx abdicate
dev.igb.1.iflib.tx_abdicate=1
dev.igb.2.iflib.tx_abdicate=1
EOF
service sysctl restart
```

### Disabling ICMP redirect

ICMP redirect is enabled by default on a generic FreeBSD (it is disabled by default on BSDRP), and this feature disables the fast tryforward code path.

```
cat <<EOF >> /etc/sysctl.conf
# Enabling fastforwarding by disabling ICMP redirect
net.inet.ip.redirect=0
net.inet6.ip6.redirect=0
EOF
service sysctl restart
```

### Static routes and ARP/NDP entries

Configure static routes, IP addresses, and static ARP, and exclude some entropy sources.

A router [should not use LRO and TSO](../technical-docs/performance.md). BSDRP disables them by default via an RC script (`disablelrotso_enable="YES"` in `/etc/rc.conf.misc`).

```
sysrc gateway_enable="YES"
sysrc static_routes="generator receiver"
sysrc route_generator="-net 198.18.0.0/16 198.18.0.203"
sysrc route_receiver="-net 198.19.0.0/16 198.19.0.203"
sysrc static_arp_pairs="receiver generator"
sysrc static_arp_generator="198.18.0.203 00:1b:21:c4:95:7a"
sysrc static_arp_receiver="198.19.0.203 00:1b:21:c4:95:7b"
sysrc ifconfig_igb1="inet 198.18.0.205/24 -tso4 -tso6 -lro -vlanhwtso"
sysrc ifconfig_igb2="inet 198.19.0.205/24 -tso4 -tso6 -lro -vlanhwtso"

sysrc ipv6_gateway_enable="YES"
sysrc ipv6_activate_all_interfaces="YES"
sysrc ipv6_static_routes="generator receiver"
sysrc ipv6_route_generator="2001:2:: -prefixlen 49 2001:2::203"
sysrc ipv6_route_receiver="2001:2:0:8000:: -prefixlen 49 2001:2:0:8000::203"
sysrc ifconfig_igb1_ipv6="inet6 2001:2::205 prefixlen 64"
sysrc ifconfig_igb2_ipv6="inet6 2001:2:0:8000::205 prefixlen 64"
sysrc static_ndp_pairs="receiver generator"
sysrc static_ndp_generator="2001:2::203 00:1b:21:c4:95:7a"
sysrc static_ndp_receiver="2001:2:0:8000::203 00:1b:21:c4:95:7b"

# Reduce number of source for entropy device harvests
harvest_mask="351"
```

## Default forwarding rate

The first test uses one packet generator at Gigabit line rate
(1.489 Mpps inet4 / 1.453 Mpps inet6), with 2000 flows of smallest UDP
packets. Each data point is 5 iterations with a reboot between each.

- The APU2 stays responsive during the test: NIC multiqueue distributes the
  load across all 4 cores.
- About 966 Kpps are forwarded on inet4, 916 Kpps on inet6.

The 5 inet4 iterations, in pps:

```
965776
970935
957160
967726
956754
```

## Firewalls impact

This test generates 2000 different flows by using 2000 different UDP
destination ports.

The pf and ipfw configurations used are detailed in the earlier [Forwarding performance lab of an IBM System x3550 M3 with Intel 82580](forwarding-performance-lab-of-an-ibm-system-x3550-m3-with-intel-82580.md#firewall-impact).

![Impact of enabling firewalls on forwarding performance, PC Engines APU2 running FreeBSD 16-CURRENT](../../assets/images/documentation/examples/bench.forwarding.and.firewalling.rate.on.pc.engines.apu2.png)

Median values, in pps:

| configuration  | inet4  | inet6  |
|----------------|--------|--------|
| forwarding     | 965776 | 915611 |
| ipf-stateful   | 268170 | 275307 |
| ipf-stateless  | 435643 | 364259 |
| ipfw-stateful  | 566841 | 471844 |
| ipfw-stateless | 740992 | 676658 |
| pf-stateful    | 304591 | 309438 |
| pf-stateless   | 278955 | 268687 |

ipfw is the fastest of the three firewalls in both modes: stateless 741 Kpps
(23% below plain forwarding), stateful 567 Kpps. ipf is the slowest in
stateful mode (268 Kpps, a 72% drop from plain forwarding), and pf sits
between the two.

For ipf and pf in stateful mode the inet6 result equals or slightly exceeds
inet4, because state lookup dominates and the larger IPv6 header stops being
the limiting factor. Where the firewall is cheaper (plain forwarding,
ipf-stateless, ipfw-*) inet6 costs 5 to 16% relative to inet4.

!!! note
    ipfw-stateful is the one noisy data point here. Its iterations cluster
    into two groups (about 565 Kpps and 600 Kpps on inet4, about 465 Kpps
    and 520 Kpps on inet6), giving a 6.5% inet4 and 12.7% inet6 spread
    against under 1.5% for most other sets. The min/max bars in the graph
    show it. The cause was not investigated.

### pf with state is faster than pf without state

In this run, pf is the one firewall where enabling state *increases*
throughput: 304591 pps stateful against 278955 pps stateless on inet4.

This is not a measurement artifact, since both sets have a spread under
1.2%. It is not a standing property of pf on this platform either: the
behavior is not present in every run of this lab.
