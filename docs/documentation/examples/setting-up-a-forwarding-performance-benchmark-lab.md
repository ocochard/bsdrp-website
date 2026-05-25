---
title: Setting-up a forwarding performance benchmark lab
description: How to build a Forwarding performance benchmark lab with BSDRP
---
## Benchmark Methodology

Before to start a router benchmark, some RFC to read:

- Benchmarking Terminology for Network Interconnection Devices: [RFC1242](https://tools.ietf.org/html/rfc1242)
- Benchmarking Methodology for Network Interconnect Devices: [RFC2544](http://www.ietf.org/rfc/rfc2544.txt) (notice usage of pool 198.18.0.0/15)
- Terminology for Forwarding Information Base (FIB) based Router Performance: [RFC3222](http://tools.ietf.org/html/rfc3222)
- IPv6 Benchmarking Methodology for Network Interconnect Devices: [RFC5180](https://tools.ietf.org/html/rfc5180) (notice usage of pool 2001:0002::/48) for IPv6
- Applicability Statement for RFC 2544: Use on Production Networks Considered Harmful [RFC6815](https://tools.ietf.org/html/rfc6815)

But, we will start by a more simple lab by focusing on a wire-speed (or line-rate) packet-generator. We didn’t cover firewall benchmark ([RFC3511](https://www.ietf.org/rfc/rfc3511.txt)) but there are [a VPN benchmark lab](setting-up-a-vpn-ipsec-gre-etc-performance-benchmark-lab.md).

Reading [FreeBSD forwarding Performance](../technical-docs/performance.md) pages is a good start too.

A wire-speed packet generator should be able to generate the [maximum number of smallest packet per second on the tested media](http://www.cisco.com/web/about/security/intelligence/network_performance_metrics.html), this mean about 1,488Mpps on a Gigabit lab (because we will avoid packet fragmentation 1 packet=1 frame) and 14.88Mpps on a TenGigabit lab.

## Simplified methodology

Method used here is to bench only the “worse” case by generating:

1.  Only smallest size packet (20 bytes for IPv4, 40 bytes for IPv6): Generating packets with only 1 byte of payload, and using padding feature could be a possibility too.
2.  Offered load is the maximum line-rate of the medium (like under a Denial of Service attack)

And the value we are interested by will be the maximum forwarding rate measured at the receiving side. This mean without take care of the dropped packet.

Once obtain this “worse” value, it’s possible to estimated the expected throughput (in bit/s) by using [Internet Mix](https://en.wikipedia.org/wiki/Internet_Mix) packet size distribution.

## Diagram

For cross-checking the packet counters, we will connect our devices to a non-blocking switch that have its own traffic counters.

We can use the same device for packet generator/receiver:

```
+---------------------------+    +-------------------------+ 
| Packet generator/receiver |    | Device Under Test (DUT) | 
+---------------------------+    +-------------------------+ 
         |         |                   |         |
         |         |                   |         |
+----------------------------------------------------------+
|              Non-blocking switch with counters           |
+----------------------------------------------------------+
```

or using two different device for packet generator and receiver:

```
+------------------+    +-------------------+     +-----------------+
| Packet generator |    | Device Under Test |     | Packet receiver |
+------------------+    +-------------------+     +-----------------+
         |                   |         |                  |
         |                   |         |                  |
+------------------------------------------------------------------+
|                  Non-blocking switch with counters               |
+------------------------------------------------------------------+
```

Or for a lab without switch: Still the same device for packet generator/receiver.

```
+---------------------------+
| Packet generator/receiver |
+---------------------------+
         |         |
         |         |
+-------------------------+
| Device Under Test (DUT) | 
+-------------------------+
```

## Switch configuration

We need to take care of the switch configuration:

- The device used as “packet receiver” will not emitting any packet, then the switch can’t not learn its MAC address and then will broadcast the traffic to all ports. We Need to disable mac-address aging or configure static MAC entry on the switch;
- The switch need to be configured for not sending non-desirable frame too (spanning tree, keepalive, CDP, etc…) that will fake our counters;
- Allowing Ethernet flow control is not a good idea (it’s allays better to drop some packet and let TCP windowing slow down the connection speed), but it’s even worse when we want to build a high speed packet generator.

### Disabling Spanning-Tree

Disable STP (if you know what you are doing) on the vlan or interfaces used for the bench.

#### Cisco switch

```
no spanning-tree vlan 2
no spanning-tree vlan 3
```

#### Juniper switch

```
set protocols rstp interface xe0/0/0 disable
```

### Mac-address Table aging or static MAC

Then disabling mac-address-table aging too or configure static MAC entry (this avoid to use a ping before starting the test for populating the dynamic MAC table):

#### Cisco switch

```
mac address-table aging-time 0 vlan 2
mac address-table aging-time 0 vlan 3
```

or:

```
mac address-table static 000e.0cde.45df vlan 2 interface GigabitEthernet0/6
mac address-table static 001a.6478.267a vlan 2 interface GigabitEthernet0/5 
mac address-table static 001b.21d5.660e vlan 3 interface GigabitEthernet0/10 
mac address-table static 001b.21d5.6615 vlan 3 interface GigabitEthernet0/9 
```

#### Juniper switch

```
set vlans bench switch-options interface xe0/0/0 static-mac 000e.0cde.45df
```

### Port

Disable CDP, LLDP, DTP, keep-alive and flow-control on all ports connected to the testers and DUT. Reduce the load-interval for statistics calculation to the minimum (30seconds here).

#### Cisco switch

```
interface GigabitEthernet0/5
  description DUT-em0
  switchport access vlan 2
  switchport mode access
  switchport nonegotiate
  load-interval 30
  no keepalive
  no cdp enable
  no lldp transmit
  flowcontrol send off
  flowcontrol receive off
```

#### Juniper switch

```
set protocols lldp interface xe-0/0/0 disable
set protocols lldp-med interface xe-0/0/0 disable
```

## Configuring the packet generator/receiver

### Hardware

NIC supported by [netmap](http://www.freebsd.org/cgi/man.cgiquery=netmap) are mandatory on the server used as packet generator/receiver: Chelsio (the best one!), Intel (em, ixgbe). RealTek (re) NIC are supported but avoid them at all cost!

### Static ARP

It’s better to avoid ARP resolution on the packet generator:

```
sysrc static_arp_pairs="tester2 dut"
sysrc static_arp_tester2="1.1.1.1 00:1b:21:d5:66:0e"
sysrc static_arp_dut="2.2.2.3 00:0e:0c:de:45:de"
service static_arp start
```

### NIC drivers tunning

#### Disabling Flow-control

This step depends of the NIC used, igb(4) uses this:

```
cat >> /etc/sysctl.conf <EOF
dev.igb.0.fc=0
dev.igb.1.fc=0
dev.igb.2.fc=0
dev.igb.3.fc=0
EOF
```

#### Unleashing the power of NIC chipset

By default FreeBSD use timid drivers values, but BSDRP increase them ([source of benchs](forwarding-performance-lab-of-an-ibm-system-x3550-m3-with-intel-82580.md#igb4-drivers-tunning-with-82546gb)).

As example for em(4) or igb(4) drivers:

- Disable the limit of maximum number of received packets to process at a time:
  - hw.em\|igb.rx_process_limit 100 =\> -1
- Increase number of transmit and receive descriptors per queue to their maximum:
  - hw.em\|igb.txd 1024 =\> 2048
  - hw.em\|igb.rxd 1024 =\> 2048
- Increase the maximum number of interrupts per second generated
  - hw.igb.max_interrupt_rate 8000 =\> 16000

If you understand all the parameters on the document [Interrupt Moderation with IntelGbE Controllers](http://www.intel.com/content/dam/doc/application-note/gbe-controllers-interrupt-moderation-appl-note.pdf) you can try to tune them too.

## Testing the packet generator and receiver

We need to learn to use the packet generator/receiver and discover its limits.

### Diagram

```
+------------------+      +-----------------+
| Packet generator |=====>| Packet receiver |
+------------------+      +-----------------+
```

### Preparation

Before to start, if you didn’t use static MAC entry on the switch or static ARP on your generator, ping each other for forcing them to emitting at last one packet.

Then clear the counter on the switch

```
switch#clear counters
Clear "show interface" counters on all interfaces [confirm] <enter>
```

### netmap pkt-gen


!!! warning
    You need to use a [patched version of netmap pkt-gen](https://github.com/ocochard/BSDRP/blob/master/BSDRP/patches/ports.pkt-gen.patch) because hardware CRC checksum is disabled on Intel NIC in netmap mode (Chelsio NIC didn’t have this limitation) and to fix the range bug.


We need to generate:

- multi-flows (important for using NIC multi-queue features), these mean using multiple IP as source and destination
- Smallest Ethernet frame size (64 bytes including CRC)

Here is an example for:

- 2000 flows by using a source range of IP 198.18.0.1-198.18.0.100 and destination 198.19.0.1 to 198.18.20
- The source and destination UDP port are 2000 (it’s important to specify the port source and destination for avoiding the usage of port number 0 filtered by pf)
- The destination MAC address needs to be given
- We generate 1 Billion packets (10 Giga ethernet links are fast)
- with a 4 second timer for the link be ready (pkt-gen down/up the link)
- 60 bytes Ethernet Frame (pkt-gen didn’t include the 4 bytes CRC size)

<!-- -->

```
[root@generator]~# pkt-gen -f tx -i ix0 -n 1000000000 -l 60 -d 198.19.0.1:2000-198.19.0.100 -D a0:36:9f:1e:28:14 -s 198.18.0.1:2000-198.18.0.20 -w 4
641.226408 main [1750] interface is ix0
641.226502 extract_ip_range [293] range is 198.18.0.1:2000 to 198.18.0.20:2000
641.226510 extract_ip_range [293] range is 198.19.0.1:2000 to 198.19.0.100:2000
641.283643 main [1950] mapped 334980KB at 0x801c00000
Sending on netmap:ix0: 4 queues, 1 threads and 1 cpus.
198.18.0.1 -> 198.19.0.1 (00:00:00:00:00:00 -> a0:36:9f:1e:28:14)
641.283669 main [2012] --- SPECIAL OPTIONS: copy

641.283671 main [2034] Sending 512 packets every  0.000000000 s
641.283674 main [2036] Wait 4 secs for phy reset
645.285310 main [2038] Ready...
645.285352 nm_open [456] overriding ifname ix0 ringid 0x0 flags 0x1
645.285433 sender_body [1106] start, fd 4 main_fd 3
646.287313 main_thread [1547] 12384692 pps (12408099 pkts in 1001890 usec)
647.289311 main_thread [1547] 12099481 pps (12123644 pkts in 1001997 usec)
648.290311 main_thread [1547] 12479753 pps (12492233 pkts in 1001000 usec)
649.291310 main_thread [1547] 12478188 pps (12490666 pkts in 1001000 usec)
650.293310 main_thread [1547] 12475803 pps (12500755 pkts in 1002000 usec)
651.294310 main_thread [1547] 12478549 pps (12491028 pkts in 1001000 usec)
652.295984 main_thread [1547] 12480828 pps (12501721 pkts in 1001674 usec)
653.297310 main_thread [1547] 12481843 pps (12498394 pkts in 1001326 usec)
654.299310 main_thread [1547] 12478788 pps (12503746 pkts in 1002000 usec)
655.301310 main_thread [1547] 12475746 pps (12500697 pkts in 1002000 usec)
656.303309 main_thread [1547] 12477035 pps (12501977 pkts in 1001999 usec)
657.305309 main_thread [1547] 12479925 pps (12504885 pkts in 1002000 usec)
658.306310 main_thread [1547] 12481029 pps (12493510 pkts in 1001000 usec)
659.307312 main_thread [1547] 12479999 pps (12492516 pkts in 1001003 usec)
660.308309 main_thread [1547] 12477386 pps (12489826 pkts in 1000997 usec)
...
```

###### \> It sends at about 12.4Mpps (the line-rate is 14.8Mpps).

Don‘t use netstat ’-h’ on FreeBSD older than 11-head r287593 ====

During the tests, we meet a problem with netstat:

The receiver measure about 565Kpps:

```
main_thread [1078] 564842 pps (565406 pkts in 1000998 usec)
main_thread [1078] 564443 pps (565009 pkts in 1001002 usec)
main_thread [1078] 564822 pps (565387 pkts in 1001000 usec)
main_thread [1078] 565082 pps (565647 pkts in 1001000 usec)
main_thread [1078] 565139 pps (565704 pkts in 1000999 usec)
main_thread [1078] 565122 pps (565686 pkts in 1000998 usec)
main_thread [1078] 564752 pps (565318 pkts in 1001002 usec)
```

Now what about the router stats:

```
[root@BSDRP]~# netstat -ihw 1
            input        (Total)           output
   packets  errs idrops      bytes    packets  errs      bytes colls
      551k  906k     0        32M       552k     0        22M     0
      551k  906k     0        32M       551k     0        22M     0
      551k  906k     0        32M       552k     0        22M     0
      551k  906k     0        32M       552k     0        22M     0
      551k  906k     0        32M       551k     0        22M     0
      551k  906k     0        32M       552k     0        22M     0
      551k  906k     0        32M       552k     0        22M     0
      551k  906k     0        32M       551k     0        22M     0
      551k  906k     0        32M       552k     0        22M     0
```

The router display a forwarding rate of 552Kpps: There is a 10Kpps gap between the receiver and router stats.

We need to check the switch stats for a tie:

```
switch#sh int GigabitEthernet 1/0/6 | i output rate
  30 second output rate 289701000 bits/sec, 565821 packets/sec
```

=\> Switch stats confirm the number of 565Kpps received.

There were a problem with FreeBSD self-counters that misses about 10Kpps in this case. Hopefully a contributer give me an hint: 564842 / 1024 = 551.6 Kpps. The [netstat '-h' (human readable) have a bug by converting 1k packets/errors in 1024 packets/errors](http://www.freebsd.org/cgi/query-pr.cgipr=183598) (fixed in 11-head r287593).

If we call netstat without ‘-h’, the problem disappear:

```
[root@BSDRP]~# netstat -iw 1
            input        (Total)           output
   packets  errs idrops      bytes    packets  errs    bytes   colls
    564224 927744     0   33553432     564224     0   23068672   0
    564444 927822     0   33557933     564444     0   23069924   0
    564504 928024     0   33594449     564504     0   23062278   0
    564842 929645     0   33524492     564842     0   23064732   0
```

Now we can try to bench your servers for a router usage, like [Forwarding performance lab of a HP ProLiant DL360p Gen8 with 10-Gigabit with 10-Gigabit Chelsio T540-CR](forwarding-performance-lab-of-a-hp-proliant-dl360p-gen8-with-10-gigabit-with-10-gigabit-chelsio-t540-cr.md).

## Bench reproducibility and ministat

Once your test ready you need to run it multiple time without human interaction:

- Need to script the test like on the [FreeBSD performance regression lab](freebsd-performance-regression-lab.md), and publish the scripts used
- Doing multiples times and publishing the [ministat](https://www.freebsd.org/cgi/man.cgiquery=ministat) output
