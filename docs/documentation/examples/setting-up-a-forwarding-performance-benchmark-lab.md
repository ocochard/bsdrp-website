---
title: Setting up a forwarding performance benchmark lab
description: How to build a forwarding performance benchmark lab with BSDRP
---
## Benchmark methodology

Before starting a router benchmark, here are some RFCs to read:

- Benchmarking Terminology for Network Interconnection Devices: [RFC1242](https://tools.ietf.org/html/rfc1242)
- Benchmarking Methodology for Network Interconnect Devices: [RFC2544](http://www.ietf.org/rfc/rfc2544.txt) (notice usage of pool 198.18.0.0/15)
- Terminology for Forwarding Information Base (FIB) based Router Performance: [RFC3222](http://tools.ietf.org/html/rfc3222)
- IPv6 Benchmarking Methodology for Network Interconnect Devices: [RFC5180](https://tools.ietf.org/html/rfc5180) (notice usage of pool 2001:0002::/48) for IPv6
- Applicability Statement for RFC 2544: Use on Production Networks Considered Harmful [RFC6815](https://tools.ietf.org/html/rfc6815)

We will start with a simpler lab by focusing on a wire-speed (line-rate) packet generator. We do not cover firewall benchmarks ([RFC3511](https://www.ietf.org/rfc/rfc3511.txt)), but there is [a VPN benchmark lab](setting-up-a-vpn-ipsec-gre-etc-performance-benchmark-lab.md).

Reading the [FreeBSD forwarding performance](../technical-docs/performance.md) page is a good start too.

A wire-speed packet generator should be able to generate the [maximum number of smallest packets per second on the tested media](http://www.cisco.com/web/about/security/intelligence/network_performance_metrics.html). This is about 1.488 Mpps on a Gigabit lab (since we avoid packet fragmentation, 1 packet = 1 frame) and 14.88 Mpps on a 10-Gigabit lab.

## Simplified methodology

The method used here is to benchmark only the "worst" case by generating:

1.  Only the smallest packets (20 bytes for IPv4, 40 bytes for IPv6). Generating packets with only 1 byte of payload, using the padding feature, is another option.
2.  Offered load equal to the maximum line rate of the medium (similar to a denial-of-service attack).

The value of interest is the maximum forwarding rate measured at the receiving side, ignoring dropped packets.

Once this "worst-case" value is obtained, it is possible to estimate the expected throughput (in bit/s) by using the [Internet Mix](https://en.wikipedia.org/wiki/Internet_Mix) packet size distribution.

## Diagram

To cross-check the packet counters, we connect the devices to a non-blocking switch that has its own traffic counters.

The same device can be used for packet generator and receiver:

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

or using two different devices for packet generator and receiver:

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

Or, for a lab without a switch, the same device acts as both packet generator and receiver:

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

The switch configuration needs some care:

- The device used as "packet receiver" does not emit any packet, so the switch cannot learn its MAC address and would broadcast the traffic to all ports. We need to disable MAC-address aging or configure a static MAC entry on the switch.
- The switch must also be configured not to send unwanted frames (spanning tree, keepalive, CDP, etc.) that would skew the counters.
- Allowing Ethernet flow control is not a good idea (it is always better to drop some packets and let TCP windowing slow down the connection), and it is even worse when building a high-speed packet generator.

### Disabling Spanning Tree

Disable STP (if you know what you are doing) on the VLAN or interfaces used for the bench.

#### Cisco switch

```
no spanning-tree vlan 2
no spanning-tree vlan 3
```

#### Juniper switch

```
set protocols rstp interface xe0/0/0 disable
```

### MAC-address table aging or static MAC

Disable MAC-address-table aging, or configure a static MAC entry (this avoids the need to ping before starting the test to populate the dynamic MAC table):

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

Disable CDP, LLDP, DTP, keep-alive, and flow control on all ports connected to the testers and the DUT. Reduce the load-interval for statistics calculation to the minimum (30 seconds here).

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

NICs supported by [netmap](http://www.freebsd.org/cgi/man.cgiquery=netmap) are mandatory on the server used as packet generator/receiver: Chelsio (the best one!) and Intel (em, ixgbe). RealTek (re) NICs are supported but should be avoided at all cost.

### Static ARP

It is better to avoid ARP resolution on the packet generator:

```
sysrc static_arp_pairs="tester2 dut"
sysrc static_arp_tester2="1.1.1.1 00:1b:21:d5:66:0e"
sysrc static_arp_dut="2.2.2.3 00:0e:0c:de:45:de"
service static_arp start
```

### NIC driver tuning

#### Disabling flow control

This step depends on the NIC used. igb(4) uses this:

```
cat >> /etc/sysctl.conf <EOF
dev.igb.0.fc=0
dev.igb.1.fc=0
dev.igb.2.fc=0
dev.igb.3.fc=0
EOF
```

#### Unleashing the power of the NIC chipset

By default FreeBSD uses conservative driver values, but BSDRP raises them ([source of benchmarks](forwarding-performance-lab-of-an-ibm-system-x3550-m3-with-intel-82580.md#igb4-driver-tuning-with-82546gb)).

For example, for em(4) or igb(4) drivers:

- Disable the limit on the maximum number of received packets processed at a time:
    - `hw.em|igb.rx_process_limit`: 100 -> -1
- Increase the number of transmit and receive descriptors per queue to their maximum:
    - `hw.em|igb.txd`: 1024 -> 2048
    - `hw.em|igb.rxd`: 1024 -> 2048
- Increase the maximum number of interrupts generated per second:
    - `hw.igb.max_interrupt_rate`: 8000 -> 16000

If you understand all the parameters in [Interrupt Moderation with Intel GbE Controllers](http://www.intel.com/content/dam/doc/application-note/gbe-controllers-interrupt-moderation-appl-note.pdf), you can try tuning them too.

## Testing the packet generator and receiver

We need to learn how to use the packet generator/receiver and discover its limits.

### Diagram

```
+------------------+      +-----------------+
| Packet generator |=====>| Packet receiver |
+------------------+      +-----------------+
```

### Preparation

Before starting, if you did not configure a static MAC entry on the switch or static ARP on the generator, ping between the devices to force each one to emit at least one packet.

Then clear the counters on the switch:

```
switch#clear counters
Clear "show interface" counters on all interfaces [confirm] <enter>
```

### netmap pkt-gen


!!! warning
    You need a [patched version of netmap pkt-gen](https://github.com/ocochard/BSDRP/blob/master/BSDRP/patches/ports.pkt-gen.patch) because the hardware CRC checksum is disabled on Intel NICs in netmap mode (Chelsio NICs do not have this limitation), and to fix the range bug.


We need to generate:

- Multi-flow traffic (important to exercise NIC multi-queue features), meaning multiple source and destination IP addresses.
- The smallest Ethernet frame size (64 bytes including CRC).

Here is an example for:

- 2000 flows, using a source IP range of 198.18.0.1-198.18.0.100 and destination 198.19.0.1-198.19.0.20.
- The source and destination UDP port are both 2000 (it is important to specify both ports to avoid port number 0, which is filtered by pf).
- The destination MAC address must be given.
- One billion packets (10-Gigabit Ethernet links are fast).
- A 4-second timer to let the link come up (pkt-gen brings the link down/up).
- 60-byte Ethernet frames (pkt-gen does not include the 4-byte CRC).

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

It sends at about 12.4 Mpps (the line rate is 14.8 Mpps).

### Don't use `netstat -h` on FreeBSD older than 11-head r287593

During the tests, we hit a problem with netstat.

The receiver measures about 565 Kpps:

```
main_thread [1078] 564842 pps (565406 pkts in 1000998 usec)
main_thread [1078] 564443 pps (565009 pkts in 1001002 usec)
main_thread [1078] 564822 pps (565387 pkts in 1001000 usec)
main_thread [1078] 565082 pps (565647 pkts in 1001000 usec)
main_thread [1078] 565139 pps (565704 pkts in 1000999 usec)
main_thread [1078] 565122 pps (565686 pkts in 1000998 usec)
main_thread [1078] 564752 pps (565318 pkts in 1001002 usec)
```

Now check the router stats:

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

The router shows a forwarding rate of 552 Kpps, a 10 Kpps gap between the receiver and the router stats.

Check the switch stats to break the tie:

```
switch#sh int GigabitEthernet 1/0/6 | i output rate
  30 second output rate 289701000 bits/sec, 565821 packets/sec
```

The switch stats confirm the 565 Kpps received.

There was a problem with FreeBSD self-counters that misses about 10 Kpps in this case. Fortunately a contributor gave me a hint: 564842 / 1024 = 551.6 Kpps. The [netstat `-h` (human-readable) flag has a bug that converts 1k packets/errors into 1024 packets/errors](http://www.freebsd.org/cgi/query-pr.cgipr=183598) (fixed in 11-head r287593).

If we call netstat without `-h`, the problem disappears:

```
[root@BSDRP]~# netstat -iw 1
            input        (Total)           output
   packets  errs idrops      bytes    packets  errs    bytes   colls
    564224 927744     0   33553432     564224     0   23068672   0
    564444 927822     0   33557933     564444     0   23069924   0
    564504 928024     0   33594449     564504     0   23062278   0
    564842 929645     0   33524492     564842     0   23064732   0
```

Now you can benchmark your servers for router use, like in the [forwarding performance lab of an HP ProLiant DL360p Gen8 with 10-Gigabit Chelsio T540-CR](forwarding-performance-lab-of-a-hp-proliant-dl360p-gen8-with-10-gigabit-with-10-gigabit-chelsio-t540-cr.md).

## Bench reproducibility and ministat

Once your test is ready, you need to run it multiple times without human interaction:

- Script the test like the [FreeBSD performance regression lab](freebsd-performance-regression-lab.md), and publish the scripts used.
- Run it multiple times and publish the [ministat](https://www.freebsd.org/cgi/man.cgiquery=ministat) output.
