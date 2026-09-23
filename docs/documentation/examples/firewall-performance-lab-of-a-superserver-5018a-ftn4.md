---
title: Firewall performance lab of a SuperServer 5018A-FTN4
description: Impact of pf, ipfw and ipf on the forwarding performance of an 8-core Atom C2758 at 2.4 GHz, measured with two different 10-Gigabit NICs
---
## Hardware detail

This lab tests a [SuperMicro](https://www.supermicro.com/en/products/system/1U/5018/SYS-5018A-FTN4.cfm) [SuperServer 5018A-FTN4](superserver-5018a-ftn4.md):

- Intel Rangeley: [Atom C2758 (8 cores) at 2.4 GHz](https://ark.intel.com/content/www/us/en/ark/products/77988/intel-atom-processor-c2758-4m-cache-2-40-ghz.html)
- 16 GB of RAM
- Two 10-Gigabit NICs, benchmarked separately:
    - Dual-port Chelsio T520-SO (`cxgbe`, `cxl` interfaces)
    - Dual-port Intel 82599 (`ixgbe`, `ix` interfaces)

Both runs use BSDRP 2.3 (FreeBSD 16-CURRENT n313366) with the GENERIC
kernel.

## Lab set-up

For more information about the full setup of this lab: [Setting up a forwarding performance benchmark lab](setting-up-a-forwarding-performance-benchmark-lab.md) (switch configuration, etc.).

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

The generator **MUST** generate lots of small IP flows (multiple source/destination IP addresses and/or UDP src/dst ports).

Here is an example for generating 2000 IPv4 flows (100 destination IP addresses x 20 source IP addresses) with a Chelsio NIC:

```
pkt-gen -i vcxl0 -f tx -n 1000000000 -l 60 -d 198.19.10.1:2000-198.19.10.100 -D 00:07:43:2e:e5:90 -s 198.18.10.1:2000-198.18.10.20 -w 4 -p 2
```

And the same with IPv6 flows (minimum frame size of 62 here):

```
pkt-gen -f tx -i vcxl0 -n 1000000000 -l 62 -6 -d "[2001:2:0:8010::1]-[2001:2:0:8010::64]" -D 00:07:43:2e:e5:90 -s "[2001:2:0:10::1]-[2001:2:0:10::14]" -S 00:07:43:2e:e4:72 -w 4 -p 2
```


!!! warning
    This version of pkt-gen has been improved with IPv6 support, software checksum, and optional unit normalization. See [BSDRP's patch to netmap pkt-gen](https://raw.githubusercontent.com/ocochard/BSDRP/master/BSDRPcur/patches/freebsd.pkt-gen.ae-ipv6.patch).

The receiver will use this command:

```
pkt-gen -i vcxl1 -f rx -w 4
```

## Configuration and tuning

[DUT configurations repository](https://github.com/ocochard/netbenches/tree/master/Atom_C2758_8Cores)

Per-NIC tuning applied during the runs:

- Chelsio T520-SO: `cxgbe` TOE/RDMA/iSCSI/FCoE capabilities disabled, pause frames off.
- Intel 82599: `tx_abdicate` enabled, 1024 tx/rx descriptors, flow control disabled.

## Results

Traffic load is 14.88 Mpps (10-Gigabit line rate with 60 B frames), which
is about 3x what this Atom can forward, so every number below is the DUT's
own ceiling and not a generator limit. Each data point is the median of 5
iterations, with a reboot between each.

### Median throughput, both NICs

Values in Mpps.

| Configuration  | Chelsio inet4 | Intel inet4 | Chelsio inet6 | Intel inet6 |
|----------------|---------------|-------------|---------------|-------------|
| forwarding     | 5.56          | 4.73        | 5.07          | 3.07        |
| ipf-stateful   | 0.64          | 0.66        | 0.88          | 0.81        |
| ipf-stateless  | 1.09          | 1.06        | 1.06          | 0.96        |
| ipfw-stateful  | 3.20          | 2.78        | 2.85          | 1.77        |
| ipfw-stateless | 4.04          | 3.49        | 3.88          | 2.36        |
| pf-stateful    | 1.70          | 1.80        | 1.69          | 1.22        |
| pf-stateless   | 1.39          | 1.55        | 1.29          | 1.05        |

### Observations

**Firewall ranking is the same on both NICs.** ipfw is the fastest of the
three, stateless around 26 to 27% below plain forwarding. pf sits in the
middle. ipf is the slowest, with ipf-stateful dropping 86 to 88% from plain
forwarding.

**The NIC matters far more for inet6 than for inet4.** On IPv4 the two
cards land within about 15% of each other, and pf is even slightly faster on
the Intel 82599. On IPv6 the Chelsio leads by 61 to 65% in the forwarding
and ipfw configurations. The IPv6 forwarding path is the part that is
sensitive to the driver here.

**pf-stateful is faster than pf-stateless** on both NICs (+22.9% inet4 on
the Chelsio, +16.6% on the Intel). This is not noise: the pf data points
have the tightest spreads in both runs. The usual explanation is that the
`no state` ruleset is evaluated in full for every packet, while a stateful
match short-circuits on the state table.

**ipf-stateful is the one configuration where inet6 beats inet4** on both
NICs (+37% on the Chelsio, +22% on the Intel). State lookup dominates that
configuration, so the larger IPv6 header stops being the limiting factor.

!!! note
    The fast configurations are the noisy ones. On the Chelsio run,
    `forwarding` and the `ipfw-*` points have spreads of 8 to 16%, while the
    pf and ipf points stay under 3%. Treat the top of the table as less
    precise than the bottom.

### Full result sets

Both runs, including the graphs, the min/max bars, the hwpmc flamegraphs and
the per-version deltas, are published in the netbenches repository:

- [Chelsio T520-SO](https://github.com/ocochard/netbenches/tree/master/Atom_C2758_8Cores/Chelsio_T520-SO/firewalls/results/fbsd16-n313366.BSDRP.2.3)
- [Intel 82599](https://github.com/ocochard/netbenches/tree/master/Atom_C2758_8Cores/Intel_82599/firewalls/results/fbsd16-n313366.BSDRP.2.3)
