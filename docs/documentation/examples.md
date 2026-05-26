---
title: Examples, labs and benchmarks
description: Some use cases with BSD Router Project
---
Routing lab examples:

- [Multi-tenant router and firewall](examples/multi-tenant-router-and-firewall.md)
- [Simple BGP/RIP/OSPF/ISIS/BABEL lab with FRRouting](examples/simple-bgp-rip-ospf-lab.md)
- [Simple BGP/RIP/OSPF/BABEL lab with bird](examples/simple-bgp-rip-ospf-lab-with-bird.md)
- [BGP Route Reflector and Confederation using FRRouting and Bird](examples/bgp-route-reflector-and-confederation-using-quagga-and-bird.md)
- [OSPF inter-area loop prevention](examples/ospf-inter-area-loop-prevention.md)
- [Multicast with PIM-DM](examples/multicast-with-pim-dm.md)
- [Multicast with PIM-SM](examples/multicast-with-pim-sm.md)
- [Equal-cost multi-path routing (ECMP)](examples/ecmp.md)

High availability examples:

- [Multi-tenant HA pf firewalls](examples/multi-tenant-ha-pf-firewalls.md)
- [Simple VRRP lab](examples/simple-vrrp-lab.md)
- [Simple uCarp lab](examples/simple-ucarp-lab.md)
- [pf, pfsync, carp and pflog lab](examples/pf-and-carp-lab.md)

VPN examples:

- [Simple PPPoE (client/server) and L2TP (LAC/LNS) lab with mpd](examples/pppoe-and-l2tp-lab.md)
- [Simple VPN with GRE, GIF, IPsec, OpenVPN and WireGuard](examples/gre-ipsec-and-openvpn.md)
- [Validating OpenVPN's low-latency server-selection patch](examples/validating-openvpn-s-low-latency-servers-selection-patch.md)
- [Aggregating multiple ISP links with ML-PPP (mpd5)](examples/aggregating-multiple-isp-links.md)
- [Aggregating multiple ISP links with MLVPN](examples/aggregating-multiple-isp-links-with-mlvpn.md)
- [strongSwan IPsec mediation feature (NAT hole punching)](examples/strongswan-ipsec-mediation-feature.md)

DHCP examples:

- [DHCP relay and DHCP server lab](examples/dhcp-relay-and-server-lab.md)

Firewall:

- [Dropping packets at a high rate](examples/dropping-packets-at-high-rate.md)

Traffic shaping:

- [Fair traffic shaping per IP with IPFW-Dummynet](examples/fair-traffic-shaping-per-ip-with-ipfw-dummynet.md)

IPv6:

- [NAT64](examples/nat64.md)
- [IPv6-only BGP/OSPF/RIPNG/ISIS lab with FRRouting](examples/ipv6-only-bgp-ospf-ripng-isis-lab-frrouting.md)

Benchmarks:

- [Setting up a forwarding-performance benchmark lab](examples/setting-up-a-forwarding-performance-benchmark-lab.md)
- [Setting up a VPN (IPsec, GRE, etc.) performance benchmark lab](examples/setting-up-a-vpn-ipsec-gre-etc-performance-benchmark-lab.md)
- HP ProLiant DL360p Gen8 (Intel Xeon E5-2650, 8 cores)
  - [Forwarding performance lab of an HP ProLiant DL360p Gen8 with 10-Gigabit Chelsio T540-CR](examples/forwarding-performance-lab-of-a-hp-proliant-dl360p-gen8-with-10-gigabit-with-10-gigabit-chelsio-t540-cr.md)
- SuperMicro SuperServer 5018A-FTN4 (Intel Rangeley Atom C2758, 8 cores)
  - [Forwarding performance lab of a SuperServer 5018A-FTN4 with 10-Gigabit Chelsio T540-CR](examples/forwarding-performance-lab-of-a-superserver-5018a-ftn4-with-10-gigabit-chelsio-t540-cr.md)
  - [IPsec performance of a SuperServer 5018A-FTN4](examples/ipsec-performance-of-a-superserver-5018a-ftn4.md)
- PC Engines APU 2 (quad-core AMD GX-412TC with Intel i210AT)
  - [Forwarding performance lab of a PC Engines APU2](examples/forwarding-performance-lab-of-a-pc-engines-apu2.md)
  - [IPsec performance of a PC Engines APU2](examples/ipsec-performance-of-a-pc-engines-apu2.md)
- Netgate RCC-VE 4860 (quad-core Intel Atom C2558 with 2 Intel i211 and 4 Intel i350 NICs)
  - [Forwarding performance lab of a Netgate RCC-VE 4860](examples/forwarding-performance-lab-of-a-netgate-rcc-ve-4860.md)
  - [IPsec performance of a Netgate RCC-VE 4860](examples/ipsec-performance-of-a-netgate-rcc-ve-4860.md)
- IBM System x3550 M3 (Intel Xeon L5630, 4 cores)
  - [Forwarding performance lab of an IBM System x3550 M3 with Intel 82580](examples/forwarding-performance-lab-of-an-ibm-system-x3550-m3-with-intel-82580.md)
  - [IPsec performance lab of an IBM System x3550 M3 with Intel 82580](examples/ipsec-performance-lab-of-an-ibm-system-x3550-m3-with-intel-82580.md)
  - [OpenVPN performance lab of an IBM System x3550 M3 with Intel 82580](examples/openvpn-performance-lab-of-an-ibm-system-x3550-m3-with-intel-82580.md)
  - [Forwarding performance lab of an IBM System x3550 M3 with 10-Gigabit Intel X540-AT2](examples/forwarding-performance-lab-of-an-ibm-system-x3550-m3-with-10-gigabit-intel-x540-at2.md)
  - [Forwarding performance lab of an IBM System x3550 M3 with 10-Gigabit Intel 82599EB](examples/forwarding-performance-lab-of-an-ibm-system-x3550-m3-with-10-gigabit-intel-82599eb.md)
- PC Engines APU 1 (dual-core AMD G-T40E with legacy NIC)
  - [Forwarding performance lab of a PC Engines APU](examples/forwarding-performance-lab-of-a-pc-engines-apu.md)
  - [IPsec performance of a PC Engines APU](examples/ipsec-performance-of-a-pc-engines-apu.md)

Misc:

- [Management of BSDRP](end-users-docs.md#system-management)
- [Maximum BSDRP features lab](examples/maximum-bsdrp-features-lab.md) (used to test BSDRP before publishing a release)
- [Testing graphpath, the ASCII network diagram tool](examples/graphpath.md)
- [FreeBSD performance regression lab](examples/freebsd-performance-regression-lab.md)

To easily build a router lab, follow [How to build a BSDRP router lab](examples/how-to-build-a-bsdrp-router-lab.md).
