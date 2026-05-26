---
title: Frequently Asked Questions (FAQ)
description: Frequently Asked Questions
---
## What is the difference between BSDRP and OPNsense or pfSense?

1.  BSDRP focuses on routing, not firewalling. If you are looking for a firewall, or for sharing your internet access, use [pfSense](http://www.pfsense.com/), [OPNsense](https://opnsense.org/), [SmallWall](http://smallwall.org/), or [t1n1wall](http://t1n1wall.com/) instead.
2.  BSDRP does not have a web GUI. It is configured from a CLI only (like Cisco or Juniper), or through an API such as NETCONF (planned feature).
3.  BSDRP is not intended for home use; it targets company use cases (a small ISP, for example).

## What about routing performance?

It depends on your hardware: ![](https://raw.githubusercontent.com/ocochard/netbenches/master/synthesis/hardware.png)

- A 4-core Atom with a multi-queue-aware NIC is the minimum for a line-rate gigabit router (1.48 Mpps at the smallest packet size).
- An 8-core Atom is not enough for full-duplex 10 Gigabit (10 Gbps receiving + 10 Gbps transmitting = 20 Gbps) with IMIX packet size distribution.
- An 8-core Xeon is enough for a 10 Gb line-rate router (14.8 Mpps).

## What about firewall performance?

### 10 Gb/s hardware

![](https://raw.githubusercontent.com/ocochard/netbenches/master/synthesis/10G/hardware.png)

### 40 Gb/s hardware

A server sized for 40 Gb/s of bidirectional traffic can almost sustain IPFW in stateless mode, but neither pf nor ipf: ![](https://raw.githubusercontent.com/ocochard/netbenches/master/synthesis/40G/hardware.png)

## What about IPsec performance?

It depends on the hardware and the crypto algorithms in use: ![](https://raw.githubusercontent.com/ocochard/netbenches/master/synthesis/ipsec.png)

## How do the different VPN solutions compare?

![](https://raw.githubusercontent.com/ocochard/netbenches/master/synthesis/VPNs-Atom_C2758.png)

## Can I install BSDRP on a MIPS or ARM device (RouterStation, D-Link, etc.)?

BSDRP targets x86 architectures only.

[ZRouter.org](http://zrouter.org/) targets ARM and MIPS architectures.

The open technical issues for ARM/MIPS support in BSDRP are:

1.  Modifying the bootloader from FreeBSD user space (to change the boot partition), so the active partition can be switched after an upgrade.
2.  A bootloader with a minimal boot-partition selection screen, so the user can revert to the previous version if a new install has serious problems.

## Can you add squid/apache/BitTorrent server/subversion/MySQL/etc. to BSDRP?

Features unrelated to routing will not be added to the BSDRP base ([but installing and removing FreeBSD packages is still possible](end-users-docs.md#system)).

## Where is the forum?

No forum is planned.
