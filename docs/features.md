---
title: Features
description: BSD Router Project features list
---
## Requirements

- 4 GB USB key, CompactFlash, SSD or disk (the image is 3.95 GB)
- 1 GB of RAM (512 MB is enough for virtualized tests)
- Processors: x86_64 (amd64) and arm64 (aarch64)

## Base System

- Base OS: embedded [FreeBSD](https://www.freebsd.org/) built with [Poudriere-image](documentation/technical-docs/poudriere.md)
- Easy upgrade process using two system partitions
- ZFS and gmirror available for the data slice

## Routing features

### Unicast

- [FRRouting](https://frrouting.org/) 10: BGP, OSPFv2, OSPFv3, IS-IS,
  OpenFabric, RIP, RIPng, EIGRP, Babel, BFD and static routing
- [Bird](https://bird.network.cz/) 3: BGP, OSPFv2, OSPFv3, RIP, RIPng, Babel,
  BFD, BMP, router advertisements and static routing
- [ExaBGP](https://github.com/Exa-Networks/exabgp): BGP engine and route
  injector, for announcing routes from scripts
- RPKI origin validation over RTR, in both FRRouting and Bird
- [bgpq4](https://github.com/bgp/bgpq4): prefix list generator from IRR data
- [mrtparse](https://github.com/t2mune/mrtparse): MRT routing table dump parser

### Multicast

- [DVMRP](https://github.com/troglobit/mrouted) with mrouted
- PIM Dense Mode with pimdd
- [PIM Sparse Mode and SSM](https://github.com/troglobit/pimd) with pimd

### Forwarding

- Multiple FIB: 16 routing tables available
- Selectable FIB lookup algorithms: the default radix tree, DXR, and the DPDK
  LPM implementations for IPv4 and IPv6
- [netmap](https://github.com/luigirizzo/netmap) and netmap-fwd for
  high-performance forwarding experiments

### High availability

- CARP, which also supports load balancing of incoming connections
- VRRPv3, using carp(4) in VRRP mode
- pfsync for firewall state synchronization

### Tunnels and VPN

- [Multi-link PPP](https://sourceforge.net/projects/mpd/): PPTP, PPPoE, L2TP, etc.
- GRE, GIF, VXLAN and GENEVE
- IPsec, IKEv1 and IKEv2 with [strongSwan](https://www.strongswan.org/)
- [OpenVPN](https://openvpn.net/community/), with the kernel data channel
  offload driver (if_ovpn)
- [WireGuard](https://www.wireguard.com/)
- [MLVPN](https://zehome.github.io/MLVPN/) for link aggregation over VPN
- [tinc](https://www.tinc-vpn.org/)

### IPv6 transition

- Native 6to4 tunnels
- Stateless and stateful NAT64 with [IPFW](https://man.freebsd.org/ipfw/8)
- NAT64 with [Tayga](http://www.litech.org/tayga/)
- NPTv6 prefix translation with IPFW

## Firewall

- [pf](https://man.freebsd.org/pf/4), with pflog for logging and pfsync for
  high availability
- [IPFW](https://man.freebsd.org/ipfw/8), with in-kernel NAT, NAT64, NPTv6 and
  protocol modification
- [IPFilter](https://man.freebsd.org/ipf/8)

## QoS

- Traffic shaper with [IPFW](https://man.freebsd.org/ipfw/8) + [dummynet](https://man.freebsd.org/dummynet/4), supporting FIFO, WF2Q+, RR (Deficit Round Robin), and QFQ
- [Committed Access Rate with netgraph](https://man.freebsd.org/ng_car/4): single-rate three-color marker (RFC 2697), two-rate three-color marker (RFC 2698), RED-like, and traffic shaping with RED

## Ethernet features

- 802.1Q VLAN tagging
- Link aggregation and link failover
- Bridging with support for Rapid Spanning Tree Protocol (802.1w)
- LLDP (802.1ab) with [lldpd](https://lldpd.github.io/)

## Network services

- DHCP server and relay, with [dnsmasq](https://thekelleys.org.uk/dnsmasq/doc.html) or ISC DHCP and dhcprelya
- DHCPv6 client, server and relay
- DNS forwarder and TFTP server with dnsmasq

## Management

### Multi-tenant

- [Isolated routers and firewalls for multiple customers](documentation/examples/multi-tenant-router-and-firewall.md) (using jail/vnet)

### Command line

- Local console, serial, and SSH access
- Command completion for BSDRP tools: `config`, `show`, and `system`

### Automation tools

- cloud-init support for first-boot configuration
- Any Python-based automation tool, such as [Ansible](https://www.ansible.com)

## Monitoring

- [monit](https://mmonit.com/monit/)
- [Nagios](https://www.nagios.org/) plugins and NRPE remote executor
- SNMP v1, v2c, and v3
- Syslog
- Mail
- NetFlow with native [ng_netflow](https://man.freebsd.org/ng_netflow/4) (v5 and v9) and [pmacct](http://www.pmacct.net/)
- DTrace, with the DTraceToolkit

## Security

- mtree reference files available for system integrity checks (SHA-256)
- CPU microcode updates for AMD and Intel processors

## Extra tools

### Benchmark

- [netmap's pkt-gen](https://github.com/luigirizzo/netmap): high-performance packet generator/receiver
- [IPsec equilibrium throughput](documentation/examples/setting-up-a-vpn-ipsec-gre-etc-performance-benchmark-lab.md)
- [netperf](https://hewlettpackard.github.io/netperf/), [iperf2](https://sourceforge.net/projects/iperf2/), and [iperf3](https://software.es.net/iperf/)
- FreeBSD tools: netblast, netreceive, netsend

### Diagnostic

- [graphpath](documentation/examples/graphpath.md): ASCII network diagram generated from the routing table
- mtr, traceroute, arping and nstat

### Hardware

- IPMI with ipmitool, DMI decoding with dmidecode
- BIOS and flash chip handling with flashrom
- Intel NVM update utilities for the I210, I225/I226 and X550 series, plus the
  Intel Ethernet Port Configuration Tool and intel-pcm
- Mellanox firmware tools with mstflint
- SFP qualification unlock for Intel XL710 cards
- VMware guest support with open-vm-tools
