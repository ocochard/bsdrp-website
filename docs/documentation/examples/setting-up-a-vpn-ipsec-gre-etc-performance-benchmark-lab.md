---
title: Setting-up a VPN (IPSec, GRE, etc…) performance benchmark lab
description: How to build a VPN (IPSec, GRE, etc…) performance benchmark lab with BSDRP
---
## Global concept

Benching forwarding performance is not simple, benching VPN (IPsec, GRE, etc…) is lot’s more complex.

- Methodology for Benchmarking IPsec Devices: [draft-ietf-bmwg-ipsec-meth-03](https://tools.ietf.org/html/draft-ietf-bmwg-ipsec-meth-03).
- [Methodology for Benchmarking IPsec Gateways](http://www.mecs-press.org/ijcnis/ijcnis-v4-n9/IJCNIS-V4-N9-1.pdf) (from Department of Telecommunications, Slovak University of Technology) that introduce the concept of equilibrium throughput.
- [Performance Analysis of VPN Gateways](https://www.net.in.tum.de/fileadmin/bibtex/publications/theses/2018-pudelko-vpn-performance.pdf) (Linux/DPDK/OpenVPN/WireGuard)

Equilibrium throughput is the highest forwarding rate of a device that is the same as offered load.

The concept is simple:

- Generating network load using 500 bytes UDP payload datagram (528 bytes IP packet);
- Using a hybrid step/binary search algorithm, it generate multiple load and search for the optimum load (when offered load = forwarded load) in minimum tries.

BSDRP includes a [shell script that use netmap-pkg for measuring the Equilibrium throughput](https://github.com/ocochard/BSDRP/blob/master/BSDRP/Files/usr/local/bin/equilibrium) that apply this concept:

- Use netmap’s pktgen in place of Iperf;
- Generate about 2000 flows (mix of different source & destination IP);
- Allow using 2 modes
  - The standard “IPSec Benchmark mode”, using 500 bytes UDP payload (by default, but configurable) and using equilibrium throughput unit in Mb/s (Ethernet link-level);
  - A specific “Router Benchmark mode”, using minimum 16 bytes UDP payload (default but configurable) and using equilibrium throughput unit in Kpp/s;
- Add some fixes to the official hybrid step/binary search algorithm.

## Diagram

### Logical

```
+-------------------+      +--------------------------------------+           +----------------------+
|                   |      |                                      |           |                      |
| Packet generator  |      |      Device under Test (DUT)         |           |   Device under Test  |
|  and receiver     |      |                                      |           |  (same as other DUT  |
|                   |      |                                      |           |  or a more powerful) |
|                   |      |                                      |           |                      |
|    Generating NIC |==>>==| incomming NIC          outgoing NIC  |===IPSec===| incommig NIC         |
|                   |      |                                      |           |                      |
|                   |      |                                      |           |                      |
|  Receiving NIC    |      |                                      |           |     outgoing NIC     |
+-------------------+      +--------------------------------------+           +----------------------+
          ||                                                                           ||
      ===========================<<<<<===============================================
```

### Physical

For cross-checking the packet counters, it’s possible to connect our devices to a non-blocking switch that have its own traffic counters.

```
+---------------------------+    +-------------------+     +-------------------+
| Packet generator/receiver |    | Device Under Test |     | Device Under Test |
+---------------------------+    +-------------------+     +-------------------+
         |          |                  |       |                  |      |
         |          |                  |       |                  |      |
+-----------------------------------------------------------------------------+
|         Non-blocking gigabit/tengigabit Ethernet switch with counters       |
+-----------------------------------------------------------------------------+
```

## Switch configuration

Same configuration as on [forwarding performance benchmark lab](setting-up-a-forwarding-performance-benchmark-lab.md)

## Configuring packet generator/receiver and DUT

A detailed example of configuration can be found on [IPSec performance lab of an IBM System x3550 M3 with Intel 82580](ipsec-performance-lab-of-an-ibm-system-x3550-m3-with-intel-82580.md).

We need to measure the performance of “Reference Device” by setting up a bench lab with 2 identical devices as DUT if possible. Or using a powerfull “reference” device if only one DUT is available.

If CPU supports [AES-NI feature](http://www.intel.com/content/dam/www/public/us/en/documents/white-papers/aes-ipsec-performance-linux-paper.pdf), the [aesni kernel module](https://www.freebsd.org/cgi/man.cgiquery=aesni&sektion=4) need to be loaded.

## IPSec bench “Equilibrium throughput” method

Once lab set, we can use the BSDRP tools “equilibrium” for using a fast method for measuring the “IPsec equilibrium throughput” of the DUT.

```
[root@packet-generator]/# equilibrium
Usage: ./equilibrium -d MAC-DEST -t TX-NIC -r RX-NIC [-l LINK-BIT-RATE -p -o TOLERANCE -s UDP-LOAD-SIZE]
 -d MAC :      Destination MAC of the Device Under Test (DUT)
 -h :          Display this usage message
 -l RATE :     Maximum link bit-rate in Mbit/s.
                  100 for a 100Mb/s link
                 1000 for a 1Gb/s link (default)
                10000 for a 10Gb/s link
                If option -p, this value is in Kilo packet-per-second
                Maximum link packet rate in Kpps (1 frame = 1 packet)
                  148 for a 100Mb/s link
                 1488 for a Gigabit link (default if -p)
                14880 for a 10Gb/s link
 -p :          Switch into Packet-per-second mode
                Input and displayed values unit change from Mb/s to Kpps
                Use this option for benching router in place of IPSec gateway
 -o TOLERANCE: Measure tolerance in %
                default value of 0.01 for 0.1%
 -t TX-NIC :   NIC used for sending load
 -r RX-NIC :   NIC used for receiving (and measuring) load
 -s LOAD  :    Size of the UDP load
                default: 500 in Mb/s, 18 in pps mode
                Minimum load for Ethernet: 18
Example: ./equilibrium -d 00:1b:21:d3:8f:3e -t igb2 -r igb3

[root@packet-generator]/# equilibrium -d 00:1b:21:d3:8f:3e -t igb2 -r igb3
Benchmark tool using equilibrium throughput method
- Mode: IPSec gateway benchmark
- UDP load = 500B, IP packet size=528B, Ethernet frame size=542B
- Link rate = 1000 Mb/s
- TOLERANCE = 0.01
Iteration 1
  - offering load = 500 Mb/s
  - STEP = 250 Mb/s
  - Measured forwarding rate = 500 Mb/s
Iteration 2
  - offering load = 750 Mb/s
  - STEP = 250 Mb/s
  - TREND = increasing
  - Measured forwarding rate = 750 Mb/s
Iteration 3
  - offering load = 1000 Mb/s
  - STEP = 250 Mb/s
  - TREND = increasing
  - Warning: Generated only 957Mb/s in place of 1000Mb/s
  - Measured forwarding rate = 871 Mb/s
Iteration 4
  - offering load = 875 Mb/s
  - STEP = 125 Mb/s
  - TREND = decreasing
  - Measured forwarding rate = 871 Mb/s
Iteration 5
  - offering load = 813 Mb/s
  - STEP = 62 Mb/s
  - TREND = decreasing
  - Measured forwarding rate = 813 Mb/s
Iteration 6
  - offering load = 844 Mb/s
  - STEP = 31 Mb/s
  - TREND = increasing
  - Measured forwarding rate = 844 Mb/s
Iteration 7
  - offering load = 859 Mb/s
  - STEP = 15 Mb/s
  - TREND = increasing
  - Measured forwarding rate = 859 Mb/s
Estimated Equilibrium link throughput= 859 Mb/s (maximum value seen: 871 Mb/s)
```
