---
title: Forwarding performance lab of an IBM eServer 306m with Intel 82546GB
description: Forwarding performance lab of an one core IBM server and dual-port gigabit Intel NIC
---
## Hardware detail

This lab tests an [IBM eServer xSeries 306m](ibm-eserver-xseries-306m.md) with **one** core (Intel Pentium 4 at 3.00 GHz, hyper-threading disabled) and a dual-port 82546GB NIC connected to the PCI-X bus. Overloading a one-core server should be easy.

## Lab set-up

The lab is detailed here: [Setting up a forwarding performance benchmark lab](setting-up-a-forwarding-performance-benchmark-lab.md).

BSDRP-amd64 v1.4 (FreeBSD 9.1) is used on the router.

### Diagram

```
+-------------------+      +----------------------------------------+      +-------------------+
| Packet generator  |      |            Device under Test           |      |  Packet receiver  |
|    em0: 2.2.2.2   |=====>| em1: 2.2.2.3              em0: 1.1.1.3 |=====>|    em0: 1.1.1.1   |
| 00:1b:21:d5:66:15 |      | 00:0e:0c:de:45:df    00:0e:0c:de:45:de |      | 00:1b:21:d5:66:0e |
+-------------------+      +----------------------------------------+      +-------------------+
```

The generator will use this command:

```
pkt-gen -i em0 -t 0 -l 42 -d 1.1.1.1 -D 00:0e:0c:de:45:df -s 2.2.2.2 -w 10
```

The receiver will use this command:

```
pkt-gen -i em0 -w 10
```

## Configuring

For this small lab, we will configure the router.

### Disabling Ethernet flow control

First, disable Ethernet flow control:

```
echo "hw.em.0.fc=0" >> /etc/sysctl.conf
echo "hw.em.1.fc=0" >> /etc/sysctl.conf
sysctl hw.em.0.fc=0
sysctl hw.em.1.fc=0
```

### Static ARP entries

Here is the modified value of the default BSDRP /etc/rc.conf for static ARP:

```
ifconfig_em0="inet 1.1.1.3/24"
ifconfig_em1="inet 2.2.2.3/24"
static_arp_pairs="receiver generator"
static_arp_receiver="1.1.1.1 00:1b:21:d5:66:0e"
static_arp_generator="2.2.2.2 00:1b:21:d5:66:15"
```

## em(4) driver tuning with 82546GB

### Default FreeBSD values

Default FreeBSD NIC parameters are used for this first test.

Edit BSDRP /boot/loader.conf.local and comment out all NIC tuning, then reboot.

```
[root@BSDRP]~# sysctl hw.em.
hw.em.rx_process_limit: 100
hw.em.txd: 1024
hw.em.rxd: 1024
```

The generator will push packets at 1.4 Mpps:

```
root@generator:~ # pkt-gen -i em0 -t 0 -l 42 -d 1.1.1.1 -D 00:0e:0c:de:45:df -s 2.2.2.2 -w 10
main [832] ether_aton(00:0e:0c:de:45:df) gives 0x800f9b292
main [900] map size is 334980 Kb
main [922] mmapping 334980 Kbytes
Sending on em0: 1 queues, 1 threads and 1 cpus.
2.2.2.2 -> 1.1.1.1 (00:1b:21:d5:66:15 -> 00:0e:0c:de:45:df)
main [975] Wait 10 secs for phy reset
main [977] Ready...
sender_body [479] start
main [1085] 1405293 pps
main [1085] 1406363 pps
main [1085] 1406409 pps
main [1085] 1406509 pps
main [1085] 1406560 pps
main [1085] 1406439 pps
main [1085] 1405242 pps
...
```

Meanwhile, the receiver shows this:

```
root@receiver:~ # pkt-gen -i em0 -w 10
main [900] map size is 334980 Kb
main [922] mmapping 334980 Kbytes
Receiving from em0: 1 queues, 1 threads and 1 cpus.
main [975] Wait 10 secs for phy reset
main [977] Ready...
receiver_body [621] waiting for initial packets, poll returns 0 0
main [1085] 0 pps
receiver_body [621] waiting for initial packets, poll returns 0 0
main [1085] 0 pps
main [1085] 159098 pps
main [1085] 400260 pps
main [1085] 400247 pps
...
main [1085] 400198 pps
main [1085] 400287 pps
main [1085] 400240 pps
main [1085] 400235 pps
main [1085] 400245 pps
main [1085] 400232 pps
main [1085] 215381 pps
main [1085] 0 pps
Received 30859400 packets, in 77.13 seconds.
Speed: 400.07Kpps.
```

Receiver results in Kpps for 5 tests (with a reboot between them):

```
400.15
400.10
400.09
399.88
399.93
```

The receiver measures 400 Kpps.

Now check the router stats:

```
[root@BSDRP]~# netstat -ihw 1
            input        (Total)           output
   packets  errs idrops      bytes    packets  errs      bytes colls
      387k  983k     0        22M       387k     0        15M     0
      389k  981k     0        22M       389k     0        16M     0
      390k  982k     0        22M       390k     0        16M     0
      390k  982k     0        22M       390k     0        16M     0
      390k  983k     0        22M       390k     0        16M     0
      390k  979k     0        22M       390k     0        16M     0
      390k  982k     0        22M       390k     0        16M     0
      390k  982k     0        22M       390k     0        16M     0
      390k  983k     0        22M       390k     0        16M     0
[root@BSDRP]~# vmstat -i | head -1 ; vmstat -i | grep em
interrupt                          total       rate
irq17: em0 bge1                  2555941       2745
irq18: em1 uhci2                 2555879       2745
[root@BSDRP]~# top -nCHSIzs1
last pid:  1334;  load averages:  0.00,  0.02,  0.05  up 0+00:15:38    10:17:26
76 processes:  2 running, 58 sleeping, 16 waiting

Mem: 9984K Active, 8432K Inact, 64M Wired, 17M Buf, 894M Free
Swap:

  PID USERNAME PRI NICE   SIZE    RES STATE    TIME    CPU COMMAND
    0 root     -92    0     0K   176K -        9:30 93.65% kernel{em1 taskq}
    0 root     -92    0     0K   176K -        0:27  3.76% kernel{em0 taskq}
   11 root     -92    -     0K   256K WAIT     0:07  0.68% intr{irq17: em0 bge1}
   11 root     -92    -     0K   256K WAIT     0:06  0.59% intr{irq18: em1 uhci2}

[root@BSDRP]~# vmstat -z | head -1 ; vmstat -z | grep -i mbuf
ITEM                   SIZE  LIMIT     USED     FREE      REQ FAIL SLEEP
mbuf_packet:            256,      0,    1024,     128,263652366,   0,   0
mbuf:                   256,      0,       1,     137,     137,   0,   0
mbuf_cluster:          2048, 262144,    1152,       6,    1152,   0,   0
mbuf_jumbo_page:       4096,  12800,       0,       0,       0,   0,   0
mbuf_jumbo_9k:         9216,   6400,       0,       0,       0,   0,   0
mbuf_jumbo_16k:       16384,   3200,       0,       0,       0,   0,   0
mbuf_ext_refcnt:          4,      0,       0,       0,       0,   0,   0
```

The router is still very responsive, but it shows a forwarding rate of 390 Kpps. The receiver measured 400 Kpps, so there is a 10 Kpps gap between them.

We need to check the switch stats to break the tie:

```
switch>sh int Gi0/10
GigabitEthernet0/10 is up, line protocol is up
  Hardware is Gigabit Ethernet, address is 000c.307c.208a (bia 000c.307c.208a)
  Description: Receiver-em0
  MTU 1500 bytes, BW 1000000 Kbit, DLY 10 usec,
     reliability 255/255, txload 52/255, rxload 1/255
  (etc...)
  30 second input rate 0 bits/sec, 0 packets/sec
  30 second output rate 204464000 bits/sec, 399348 packets/sec
```

Switch stats confirm the 400 Kpps figure: there is a problem with FreeBSD self-counters, which miss about 10 Kpps in this case.


!!! note
    We need to use the receiver stats, not the router stats.


### Default BSDRP values

BSDRP NIC parameters are used for this test:

- The maximum number of received packets to process at a time is increased to 500
- The number of transmit/receive descriptors per queue is increased to its maximum (4096)

<!-- -->

```
[root@BSDRP]~# sysctl hw.em.
hw.em.rx_process_limit: 500
hw.em.txd: 4096
hw.em.rxd: 4096
```

Receiver results in Kpps for 5 tests (with a reboot between them):

```
405.29
405.23
406.25
405.20
404.98
```

Throughput increases to 405 Kpps: a small 5 Kpps gain.

Some router counters:

```
[root@BSDRP]~# vmstat -i | head -1 ; vmstat -i | grep em
interrupt                          total       rate
irq17: em0 bge1                   181885        301
irq18: em1 uhci2                  181884        301

[root@BSDRP]~# top -nCHSIzs1
last pid:  1344;  load averages:  0.00,  0.05,  0.07  up 0+00:10:19    10:31:13
76 processes:  2 running, 58 sleeping, 16 waiting

Mem: 9976K Active, 8300K Inact, 85M Wired, 17M Buf, 873M Free
Swap:

  PID USERNAME PRI NICE   SIZE    RES STATE    TIME    CPU COMMAND
    0 root     -92    0     0K   176K -        3:39 93.07% kernel{em1 taskq}
    0 root     -92    0     0K   176K -        0:11  4.20% kernel{em0 taskq}

[root@BSDRP]~# vmstat -z | head -1 ; vmstat -z | grep -i mbuf
ITEM                   SIZE  LIMIT     USED     FREE      REQ FAIL SLEEP
mbuf_packet:            256,      0,    8704,     512,110372794,   0,   0
mbuf:                   256,      0,       1,     128,     135,   0,   0
mbuf_cluster:          2048, 262144,    9216,       6,    9216,   0,   0
mbuf_jumbo_page:       4096,  12800,       0,       0,       0,   0,   0
mbuf_jumbo_9k:         9216,   6400,       0,       0,       0,   0,   0
mbuf_jumbo_16k:       16384,   3200,       0,       0,       0,   0,   0
mbuf_ext_refcnt:          4,      0,       0,       0,       0,   0,   0
```

The server is still very responsive.

There is no IRQ storm and no mbuf problem: it is the em taskq that consumes all the CPU resources.

### Removing rx limit

For this test, we completely disable the maximum number of received packets processed at a time (-1):

```
[root@BSDRP]~# sysctl hw.em.
hw.em.rx_process_limit: -1
hw.em.txd: 4096
hw.em.rxd: 4096
```

Receiver results in Kpps for 5 tests (with a reboot between them):

```
410.52
409.65
410.31
408.92
410.52
```

Performance increases to 410 Kpps (a 10 Kpps gain over the default value, and a 5 Kpps gain over the tuned-but-still-limited value).

Now check the router stats:

```
[root@BSDRP3]~# vmstat -i | head -1 ; vmstat -i | grep em
interrupt                          total       rate
irq17: em0 bge1                    81956         84
irq18: em1 uhci2                   81928         84
[root@BSDRP3]~# top -nCHSIzs1
last pid:  1343;  load averages:  3.05,  2.29,  1.49  up 0+00:19:57    10:56:06
80 processes:  5 running, 59 sleeping, 16 waiting

Mem: 10M Active, 8348K Inact, 93M Wired, 17M Buf, 865M Free
Swap:

  PID USERNAME PRI NICE   SIZE    RES STATE    TIME    CPU COMMAND
    0 root     -92    0     0K   176K -       17:02 100.00% kernel{em1 taskq}
```

The router is very slow to respond, almost unusable. Receiving packets consumes all its CPU.


!!! note
    Disabling the limit on the maximum number of received packets processed at a time is a bad idea on this server.


### Results

Ministat graphs:

```
x hw.em.txd-rxd=1024.hw.em.rx_proc_lim=100
+ hw.em.txd-rxd=4096.hw.em.rx_proc_lim=500
* hw.em.txd-rxd=4096.hw.em.rx_proc_lim=-1
+----------------------------------------------------------------------------------------------------+
|x x                                              +                                                * |
|x x                                            + ++       +                        *      *     * * |
||AM                                           |__M_A___|                              |______A__M__||
+----------------------------------------------------------------------------------------------------+
    N           Min           Max        Median           Avg        Stddev
x   5        399.88        400.15        400.09        400.03    0.11768602
+   5        404.98        406.25        405.23        405.39     0.4948232
Difference at 95.0% confidence
        5.36 +/- 0.524533
        1.3399% +/- 0.131123%
        (Student's t, pooled s = 0.359653)
*   5        408.92        410.52        410.31       409.984    0.69363535
Difference at 95.0% confidence
        9.954 +/- 0.725551
        2.48831% +/- 0.181374%
        (Student's t, pooled s = 0.497484)
```

## Firewall impact

### IPFW

Test the impact of enabling a simple IPFW rule:

```
cat > /etc/ipfw.rules <<'EOF'
#!/bin/sh
fwcmd="/sbin/ipfw"
# Flush out the list before we begin.
${fwcmd} -f flush
${fwcmd} add 3000 allow ip from any to any
'EOF'

echo 'firewall_enable="YES"' >> /etc/rc.conf
echo 'firewall_script="/etc/ipfw.rules"  >> /etc/rc.conf
```

Receiver results in Kpps for 5 tests (with a reboot between them):

```
320.63
320.13
320.79
320.18
320.52
```

Throughput is reduced to 320 Kpps: enabling ipfw has an impact of about 80 Kpps on this server. The router still responds perfectly on the CLI.

### PF

```
cat >/etc/pf.conf <<'EOF'
set skip on lo0
pass
'EOF'

echo 'pf_enable="YES"' >> /etc/rc.conf
```

Receiver results in Kpps for 5 tests (with a reboot between them):

```
272.40
274.78
272.56
275.65
274.51
```

A very big performance impact here. Drops to 274 Kpps and the router is not responsive at all: if the watchdog is enabled, it will trigger a reboot of the router.

### Results

Ministat graphs:

```
x ipfw
+ pf
+----------------------------------------------------------------------------------------------------+
|+                                                                                                 xx|
|+   ++ +                                                                                          xx|
||__AM_|                                                                                           A||
+----------------------------------------------------------------------------------------------------+
    N           Min           Max        Median           Avg        Stddev
x   5        320.13        320.79        320.52        320.45    0.28644371
+   5         272.4        275.65        274.51        273.98     1.4337538
Difference at 95.0% confidence
        -46.47 +/- 1.50781
        -14.5015% +/- 0.47053%
        (Student's t, pooled s = 1.03385)
```
