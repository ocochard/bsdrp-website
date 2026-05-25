---
title: Features
description: BSD Router Project features list
---
## Requirements

- 4 GB USB key or CompactFlash media
- 1 GB of RAM (512 MB is enough for virtualized tests)
- Processors: x86_64 (amd64) and arm64 (aarch64)

## Base System

- Base OS: embedded [FreeBSD](http://www.freebsd.org/) built with [Poudriere-image](documentation/technical-docs/poudriere.md)
- Easy upgrade process using two system partitions

## Routing features

- All routing protocols supported by [FRRouting](https://frrouting.org/): BGP, RIP and RIPng (IPv6), OSPF v2 and OSPF v3 (IPv6), IS-IS
- All routing protocols supported by [Bird](http://bird.network.cz/): BGP, RIP and RIPng (IPv6), OSPF v2 and OSPF v3 (IPv6)
- Multicast: [DVMRP](http://freecode.com/projects/mrouted), PIM Dense Mode, [PIM Sparse Mode](http://troglobit.com/pimd.html), and [static](https://github.com/troglobit/smcroute/)
- Multiple FIB: 16 routing tables available
- High availability with CARP (which also supports load balancing of incoming connections) and VRRP
- [Multi-link PPP](http://mpd.sourceforge.net/): PPTP, PPPoE, L2TP, etc.
- VPN: GRE, GIF, IPsec (IKEv1 and IKEv2 with [strongSwan](https://www.strongswan.org/)), [OpenVPN](http://openvpn.net/index.php/open-source.html), and [WireGuard](https://www.wireguard.com/)
- IPv6: native 6to4 tunnels, [stateless and stateful NAT64 with IPFW](https://svnweb.freebsd.org/baseview=revision&revision=304046), and [Tayga](http://www.litech.org/tayga/) for NAT64

## QoS

- Traffic shaper with [IPFW](http://www.freebsd.org/cgi/man.cgiquery=ipfw) + [dummynet](http://www.freebsd.org/cgi/man.cgiquery=dummynet), supporting FIFO, WF2Q+, RR (Deficit Round Robin), and QFQ
- [Committed Access Rate with netgraph](http://www.freebsd.org/cgi/man.cgiquery=ng_car): single-rate three-color marker (RFC 2697), two-rate three-color marker (RFC 2698), RED-like, and traffic shaping with RED

## Ethernet features

- 802.1Q VLAN tagging
- Link aggregation and link failover
- Bridging with support for Rapid Spanning Tree Protocol (802.1w)

## Network services

- DHCP relay
- DHCP server

## Management

### Multi-tenant

- [Isolated routers and firewalls for multiple customers](documentation/examples/multi-tenant-router-and-firewall.md) (using jail/vnet)

### Command line

- Local console, serial, and SSH access
- Command completion for BSDRP tools: `config`, `system`, `show`, and `upgrade`

### Automation tools

- Any Python-based automation tool, such as [Ansible](http://www.ansible.com)

## Monitoring

- [monit](http://mmonit.com/monit/)
- SNMP v1, v2c, and v3
- Syslog
- Mail
- NetFlow with native [ng_netflow](http://www.freebsd.org/cgi/man.cgiquery=ng_netflow) (v5 and v9) and [pmacct](http://www.pmacct.net/)

## Security

- mtree reference files available for system integrity checks (SHA-256)

## Extra tools

### Benchmark

- [netmap's pkt-gen](http://info.iet.unipi.it/~luigi/netmap/): high-performance packet generator/receiver
- [IPsec equilibrium throughput](documentation/examples/setting-up-a-vpn-ipsec-gre-etc-performance-benchmark-lab.md)
- [netperf](https://hewlettpackard.github.io/netperf/), [iperf2](https://sourceforge.net/projects/iperf2/), and [iperf3](http://software.es.net/iperf/)
- FreeBSD tools: netblast, netreceive, netsend
