---
title: Frequently Asked Questions (FAQ)
description: Frequently Asked Questions
---
## What’s the difference between BSDRP and OPNsense or pfSense ?

1.  The main goal of BSDRP is not firewalling but routing. If you are looking for a firewall, or for sharing your Internet access, don’t use BSDRP but use [pfSense](http://www.pfsense.com/), [OPNsense](https://opnsense.org/), [SmallWall](http://smallwall.org/) or [t1n1wall](http://t1n1wall.com/), instead.
2.  BSDRP doesn’t have a Web GUI: It’s to be configured from a CLI only (like Cisco/Juniper), or by an API (like netconf) \[planned feature\]
3.  BSDRP is not intended for home use but for company use (small ISP as example).

## What’s about the routing performance ?

It depends on your hardware: ![](https://raw.githubusercontent.com/ocochard/netbenches/master/synthesis/hardware.png)

- 4 cores Atom with with multi-queue aware NIC is the minimum for a line-rate gigabit router (1.48Mpps of smallest packet size).
- 8 core Atom not enough for the minimum for a 10Gigabit Full-Duplex (10Gbps receiving + 10Gbps transmitting = 20Gbps) with IMIX packet size distribution
- 8 core Xeon is enough for a 10Gb line-rate router (14.8Mpps)

## What’s about the firewall performance ?

### 10Gb/s hardware

![](https://raw.githubusercontent.com/ocochard/netbenches/master/synthesis/10G/hardware.png)

### 40Gb/s hardware

A server designed to support 40Gb/s of bidirectional traffic could almost support IPFW in stateless mode but not pf neither ipf: ![](https://raw.githubusercontent.com/ocochard/netbenches/master/synthesis/40G/hardware.png)

## What’s about IPSec performance ?

It depends of your hardware and crypto algorithms used: ![](https://raw.githubusercontent.com/ocochard/netbenches/master/synthesis/ipsec.png)

## What’s about different VPN performance ?

![](https://raw.githubusercontent.com/ocochard/netbenches/master/synthesis/VPNs-Atom_C2758.png)

## Can I install BSDRP on a MIPS or ARM device (RouterStation, D-Link, etc..) ?

BSDRP targets x86 architectures only.

[ZRouter.org](http://zrouter.org/) targets ARM and MIPS architectures.

The technical issues regarding the support of ARM/MIPS architectures with BSDRP are:

1.  Be able to modify the bootloader (for changing the boot-partition) from the FreeBSD user space: Permit to switch the active partition after an upgrade
2.  Having a bootloader that support a minimum boot-partition selection screen: Permit to revert-back to the previous version if the new installed version has major problem.

## Can you add squid/apache/BitTorrent server/subversion/MySQL/etc. to BSDRP ?

All features not related to routing will not be added into the base of BSDRP ([but installing or removing FreeBSD packages is still possible](end-users-docs.md#system)).

## Where is the forum ?

No forum planned..
