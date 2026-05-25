---
title: Features
description: BSD Router Project features list
---
## Requirements

- 4GB USB key/Compact flash media,
- 1GB of RAM (512MB are enough for virtualized tests)
- processors: x86_64 (amd64) and arm64 (aarch64)

## Base System

- Base OS: Embedded [FreeBSD](http://www.freebsd.org/) using [Poudriere-image](documentation/technical-docs/poudriere.md)
- Easy upgrade process using two system partitions

## Routing features

- All routing protocol supported by [FRRouting](https://frrouting.org/): BGP, RIP and RIPng (IPv6), OSPF v2 and OSFP v3 (IPv6), ISIS
- All routing protocol supported by [Bird](http://bird.network.cz/): BGP, RIP and RIPng (IPv6), OSPF v2 and OSFP v3 (IPv6)
- Multicast: [DVMRP](http://freecode.com/projects/mrouted), PIM Dense Mode, [PIM Sparse Mode](http://troglobit.com/pimd.html) and [static](https://github.com/troglobit/smcroute/)
- Multiple FIB: 16 Routing Tables available
- High availability with CARP (support also load balancing the incoming connections) and VRRP.
- [Multi-link PPP](http://mpd.sourceforge.net/): PPTP, PPPoE, L2TP, etc…
- VPN: GRE, GIF, IPSec (IKEv1 and IKEv2 with [strongswan](https://www.strongswan.org/)), [OpenVPN](http://openvpn.net/index.php/open-source.html) and [Wireguard](https://www.wireguard.com/)
- IPv6: native 6to4 tunnels, [stateless and stateful NAT64 with IPFW](https://svnweb.freebsd.org/baseview=revision&revision=304046) and [Tayga](http://www.litech.org/tayga/) for NAT64

## Qos

- Traffic shaper with [IPFW](http://www.freebsd.org/cgi/man.cgiquery=ipfw)+[dummynet](http://www.freebsd.org/cgi/man.cgiquery=dummynet) supporting: FIFO, WF2Q+, RR (Deficit Round Robin), QFQ
- [Committed Access Rate with netgraph](http://www.freebsd.org/cgi/man.cgiquery=ng_car): Single rate three color marker (RFC 2697), two rate three color marker (RFC 2698), RED-like, Traffic shaping with RED

## Ethernet features

- 802.1q vlan tagging
- link aggregation and link failover interface
- bridging with support of Rapid Spanning Tree Protocol (802.1w)

## Network services

- DHCP Relay
- DHCP Server

## Management

### Multi-tenant

    * Allows to [create.md isolated router/firewall for multiple customers](documentation/examples/multi-tenant-router-and-firewall.md) (using jail/vnet)

### Command Line

- local console, serial and SSH access
- Command completion with somes BSDRP tools: config, system, show and upgrade

### Automation tools

- All automation tools using python like [Ansible](http://www.ansible.com)

## Monitoring

- [monit](http://mmonit.com/monit/)
- SNMP v1,v2c and v3
- Syslog
- Mail
- Netflow with native [ng_netflow](http://www.freebsd.org/cgi/man.cgiquery=ng_netflow) (v5 and v9) and [pmacct](http://www.pmacct.net/)

## Security

- mtree reference files available for system integrity check (sha256)

## Extra tools

### benchmark

- [netmap's pkt-gen](http://info.iet.unipi.it/~luigi/netmap/): high performance packet generator/receiver
- [IPSec Equilibrium throughput](documentation/examples/setting-up-a-vpn-ipsec-gre-etc-performance-benchmark-lab.md)
- [netperf](https://hewlettpackard.github.io/netperf/), [iperf2](https://sourceforge.net/projects/iperf2/) and [Iperf3](http://software.es.net/iperf/)
- FreeBSD tools netblast/netreceive/netsend
