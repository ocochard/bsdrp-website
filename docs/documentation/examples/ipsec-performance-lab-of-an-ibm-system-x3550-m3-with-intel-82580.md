---
title: IPsec performance lab of an IBM System x3550 M3 with Intel 82580
description: IPsec performance lab of a quad-core Xeon 2.13 GHz and quad-port Gigabit Intel 82580
---
## Hardware detail

This lab tests an [IBM System x3550 M3](ibm-system-x3550-m3.md) with **quad** cores (Intel Xeon L5630 2.13 GHz, hyper-threading disabled) and a quad-port 82580 NIC connected to the PCI-Express bus.

This CPU includes AES-NI: AES-CBC, AES-XTS, AES-GCM, AES-ICM.

## Method used

The benchmarking method used here is detailed in [Setting up a VPN IPSec, GRE, etc... performance benchmark lab](setting-up-a-vpn-ipsec-gre-etc-performance-benchmark-lab.md).

### Diagram

```
+---------------------+   +-------------------------------------+    +----------------------------------------+
|          R1         |   |             IBM x3550 M3            |    |                     R3                 |
|   Packet generator  |   |           Device under Test         |    |              IPSec endpoint            |
|     and receiver    |   |                                     |    |                 (AES-NI)               |
|                     |   |                                     |    |                                        |
|igb2: 198.18.0.201/24|=>=| igb2: 198.18.0.202/24               |    |                                        |
|       2001:2::201/64|   | 2001:2::202/64                      |    |                                        |
|    00:1b:21:d4:3f:2a|   | 00:1b:21:d3:8f:3e                   |    |                                        |
|                     |   |                                     |    |                                        |
|                     |   |               igb3: 198.18.1.202/24 |==>=| igb2: 198.18.1.203/24                  |
|                     |   |                  2001:2:0:1::202/64 |    |    2001:2:0:1::203/64                  |
|                     |   |                   00:1b:21:d3:8f:3f |    |     00:1b:21:c4:95:7a                  |
|                     |   |                                     |    |                                        |
|                     |   |              static routes          |    |             static routes              |
|                     |   |     198.19.0.0/16 => 198.18.1.203   |    |     198.19.0.0/16 => 198.19.0.201      |
|                     |   |     198.18.0.0/16 => 198.18.0.201   |    |     198.18.0.0/16 => 198.18.1.202      |
|                     |   |       2001:2::/49 => 2001:2::201    |    |       2001:2::/49 => 2001:2:0:1::202   |
|                     |   |2001:2:0:8000::/49 => 2001:2:0:1::203|    | 2001:2:0:8000::/49=>2001:2:0:8000::201 |
|                     |   |                                     |    |                                        |
|igb3: 198.19.0.201/24|   |                                     |    |         igb3: 198.19.0.203/24          |
|2001:2:0:8000::201/64|   |                                     |    |         2001:2:0:8000::203/64          |
|   00:1b:21:d4:3f:2b |   |                                     |    |          00:1b:21:c4:95:7b             |
+---------------------+   +-------------------------------------+    +----------------------------------------+
          ||                                                                           ||
      ==================================<============================================
```

## Devices configuration

Almost the same as the forwarding performance lab, but with fastforwarding disabled (not compatible with IPsec).

### R2 (DUT)

Disable fastforwarding (not compatible with IPsec), then configure IP addresses, routes, and static IPsec.

/etc/rc.conf:

```
# IPv4 router
gateway_enable="YES"
ifconfig_igb2="198.18.0.202/24 -tso4 -tso6 -lro"
ifconfig_igb3="198.18.1.202/24 -tso4 -tso6 -lro"
static_routes="generator receiver"
route_generator="-net 198.18.0.0/16 198.18.0.201"
route_receiver="-net 198.19.0.0/16 198.18.1.203"
static_arp_pairs="receiver generator"
static_arp_generator="198.18.0.201 00:1b:21:d4:3f:2a"
static_arp_receiver="198.18.1.203 00:1b:21:c4:95:7a"

# IPv6 router
ipv6_gateway_enable="YES"
ipv6_activate_all_interfaces="YES"
ifconfig_igb2_ipv6="inet6 2001:2::202 prefixlen 64"
ifconfig_igb3_ipv6="inet6 2001:2:0:1::202 prefixlen 64"
ipv6_static_routes="generator receiver"
ipv6_route_generator="2001:2:: -prefixlen 49 2001:2::201"
ipv6_route_receiver="2001:2:0:8000:: -prefixlen 49 2001:2:0:1::203"
static_ndp_pairs="receiver generator"
static_ndp_generator="2001:2::201 00:1b:21:d4:3f:2a"
static_ndp_receiver="2001:2:0:1::203 00:1b:21:c4:95:7a"

# Enabling IPSec
ipsec_enable="YES"

# Enabling AES-NI
kld_list="aesni"
```

/etc/ipsec.conf

```
flush;
spdflush;
spdadd 198.18.0.0/16 198.19.0.0/16 any -P out ipsec esp/tunnel/198.18.1.202-198.18.1.203/require;
spdadd 198.19.0.0/16 198.18.0.0/16 any -P in ipsec esp/tunnel/198.18.1.203-198.18.1.202/require;
add 198.18.1.203 198.18.1.202 esp 0x1000 -E aes-gcm-16 "12345678901234567890";
add 198.18.1.202 198.18.1.203 esp 0x1001 -E aes-gcm-16 "12345678901234567890";
spdadd 2001:2::/49 2001:2:0:8000::/49 any -P out ipsec esp/tunnel/2001:2:0:1::202-2001:2:0:1::203/require;
spdadd 2001:2:0:8000::/49 2001:2::/49 any -P in ipsec esp/tunnel/2001:2:0:1::203-2001:2:0:1::202/require;
add 2001:2:0:1::203 2001:2:0:1::202 esp 0x1002 -E aes-gcm-16 "12345678901234567890";
add 2001:2:0:1::202 2001:2:0:1::203 esp 0x1003 -E aes-gcm-16 "12345678901234567890";
```

### R3 (reference)

Disable fastforwarding (not compatible with IPsec), then configure IP addresses, routes, and static IPsec:

```
# IPv4 router
gateway_enable="YES"
ifconfig_igb2="inet 198.18.1.203/24"
ifconfig_igb3="inet 198.19.0.203/24"

static_routes="generator receiver"
route_generator="-net 198.18.0.0/16 198.18.1.202"
route_receiver="-net 198.19.0.0/16 198.19.0.201"
static_arp_pairs="receiver generator"
static_arp_generator="198.18.1.202 00:1b:21:d3:8f:3f"
static_arp_receiver="198.19.0.201 00:1b:21:d4:3f:2b"

# IPv6 router
ipv6_gateway_enable="YES"
ipv6_activate_all_interfaces="YES"
ifconfig_igb2_ipv6="inet6 2001:2:0:1::203 prefixlen 64"
ifconfig_igb3_ipv6="inet6 2001:2:0:8000::203 prefixlen 64"

ipv6_static_routes="generator receiver"
ipv6_route_generator="2001:2:: -prefixlen 49 2001:2:0:1::202"
ipv6_route_receiver="2001:2:0:8000:: -prefixlen 49 2001:2:0:8000::201"
static_ndp_pairs="receiver generator"
static_ndp_generator="2001:2:0:1::202 00:1b:21:d3:8f:3f"
static_ndp_receiver="2001:2:0:8000::201 00:1b:21:d4:3f:2b"

# Enabling IPSec
kld_list="aesni"
ipsec_enable="YES"
```

/etc/ipsec.conf:

```
flush;
spdflush;
spdadd 198.18.0.0/16 198.19.0.0/16 any -P in ipsec esp/tunnel/198.18.1.202-198.18.1.203/require;
spdadd 198.19.0.0/16 198.18.0.0/16 any -P out ipsec esp/tunnel/198.18.1.203-198.18.1.202/require;
add 198.18.1.203 198.18.1.202 esp 0x1000 -E aes-gcm-16 "12345678901234567890";
add 198.18.1.202 198.18.1.203 esp 0x1001 -E aes-gcm-16 "12345678901234567890";
spdadd 2001:2::/49 2001:2:0:8000::/49 any -P in ipsec esp/tunnel/2001:2:0:1::202-2001:2:0:1::203/require;
spdadd 2001:2:0:8000::/49 2001:2::/49 any -P out ipsec esp/tunnel/2001:2:0:1::203-2001:2:0:1::202/require;
add 2001:2:0:1::203 2001:2:0:1::202 esp 0x1002 -E aes-gcm-16 "12345678901234567890";
add 2001:2:0:1::202 2001:2:0:1::203 esp 0x1003 -E aes-gcm-16 "12345678901234567890";
```

## IPsec benchmark "equilibrium throughput" method

Once that is done, we use a fast method to measure the "IPsec equilibrium throughput" of the DUT.

From the packet generator/receiver, a simple script that uses netmap-pktgen will do the job:

```
[root@pkt-gen]~# equilibrium -u -4 -d 00:1b:21:d3:8f:3e -t igb2 -r igb3
Benchmark tool using equilibrium throughput method
- Benchmark mode: Bandwitdh (bps) for VPN gateway
- UDP load = 500B, IPv4 packet size=528B, Ethernet frame size=542B
- Link rate = 1000 Mb/s
- Tolerance = 0.01
Iteration 1
  - Offering load = 500 Mb/s
  - Step = 250 Mb/s
  - Measured forwarding rate = 500 Mb/s
Iteration 2
  - Offering load = 750 Mb/s
  - Step = 250 Mb/s
  - Trend = increasing
  - Measured forwarding rate = 750 Mb/s
Iteration 3
  - Offering load = 1000 Mb/s
  - Step = 250 Mb/s
  - Trend = increasing
  - Warning: Generated only 959Mb/s in place of 1000Mb/s
  - Measured forwarding rate = 872 Mb/s
Iteration 4
  - Offering load = 875 Mb/s
  - Step = 125 Mb/s
  - Trend = decreasing
  - Measured forwarding rate = 872 Mb/s
Iteration 5
  - Offering load = 937 Mb/s
  - Step = 62 Mb/s
  - Trend = increasing
  - Measured forwarding rate = 872 Mb/s
Iteration 6
  - Offering load = 906 Mb/s
  - Step = 31 Mb/s
  - Trend = decreasing
  - Measured forwarding rate = 872 Mb/s
Iteration 7
  - Offering load = 891 Mb/s
  - Step = 15 Mb/s
  - Trend = decreasing
  - Measured forwarding rate = 872 Mb/s
Estimated Equilibrium Ethernet throughput= 872 Mb/s (maximum value seen: 872 Mb/s)
```

IPsec overhead prevents us from reaching 1 Gb/s of clear traffic across an encrypted 1 Gb/s link (974 Mb/s seems to be the maximum in our case), but we reach about 872 Mb/s!

### Encryption algorithms

![Impact of IPSec encryption algorithms on 4 cores Xeon 2.13GHz with Intel 82580 NIC](../../assets/images/documentation/examples/ipsec-ibm3550-fbsd11.0.png)
