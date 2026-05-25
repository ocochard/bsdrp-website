---
title: FreeBSD performance regression lab
description: FreeBSD performance regression testing lab
---
## Concepts

This article presents the method used for spotting some performance regression problem during the evolution of FreeBSD code (regarding different svn numbers).

Here is an example of a final bench graphic measuring the impact of forwarding performance: ![freebsd-performance-regression-lab-example-graph-pps.png](../../assets/images/documentation/examples/freebsd-performance-regression-lab-example-graph-pps.png)

This method follow these steps:

1.  A lab of one or more servers is set-up. [On this example, 2 servers were used](forwarding-performance-lab-of-a-hp-proliant-dl360p-gen8-with-10-gigabit-with-10-gigabit-chelsio-t540-cr.md): one traffic generator/receiver, one device under test (DUT).
2.  A [BSDRP sub-project folder is created](https://github.com/ocochard/BSDRP/tree/master/TESTING): This project configure a minimal (for rapid compilation) nanobsd image.
3.  A first [script generate lot's of nanobsd image regarding a list of FreeBSD code SVN revision number](https://github.com/ocochard/BSDRP/blob/master/tools/bisection-gen.sh)
4.  [Different configuration sets to be tested a created](https://github.com/ocochard/netbenches/tree/master/Xeon_E5-2697Av4_16Cores-Mellanox_ConnectX-4/firewalls/configs). The example given use 3 tests: One with forwarding, a second with a minimal ipfw configuration and a third with a minimal pf configuration
5.  A second [script will run the test and collect data](https://github.com/ocochard/netbenches/blob/master/scripts/bench-lab.sh) (by sending ssh commands to the lab servers). This order are followed:
    1.  Upgrading the server to the nanobsd release to be tested;
    2.  ..Uploading the configuration set to be tested (in this example: forwarding-only, ipfw or pf) & reboot the DUT;
    3.  ….Start the bench test and collecting the result;
    4.  ….Reboot the DUT;
    5.  ….Loop 5 times (for having usable [ministat](http://www.freebsd.org/cgi/man.cgiquery=ministat) datas);
    6.  ..Loop to next configuration set;
    7.  Loop to next nanobsd release
6.  [A third script filter the raw output of each tests](https://github.com/ocochard/netbenches/blob/master/scripts/bench-lab-ministat.sh) (heavy dependent of the tool used during the bench) and generate synthesis data files for each Revision-number/configuration-sets pairs.

## Physical lab

The physical lab used by BSDRP targets forwarding network speed. And for this purpose it’s composed of minimum 3 servers and 1 switches, and maximum 4 servers and 2 switchs. Common to all these setups:

- The controller server that runs the bench script;
- The admin switch (send SSH commands)

Specific:

- One server with netmap compliant NIC for being used as packet generator/receiver
- One server as DUT
- And for network crypto (IPSec, OpenVPN) bench, a referent server
- A dedicated switch with ([with specific configuration for not polluting packet counters](setting-up-a-forwarding-performance-benchmark-lab.md#switch-configuration)). Useful for double-checking NIC drivers statistics against the switch statistics

### 2 nodes lab examples

#### simplest lab

This simple lab is great for benching 10Gigabit performance without the need of 10Gigabit switch:

![bsdrp_simple_2_node_bench_lab.png](../../assets/images/documentation/examples/bsdrp_simple_2_node_bench_lab.png)

#### with switch lab

This simple lab is usefull for cross-checking NIC statistics counters with switch statistics counters:

![bsdrp_switched_2_node_bench_lab.png](../../assets/images/documentation/examples/bsdrp_switched_2_node_bench_lab.png)

### 3 nodes lab example

This is the setup used for a VPN benchmark:

![bsdrp_vpn_3_node_bench_lab.png](../../assets/images/documentation/examples/bsdrp_vpn_3_node_bench_lab.png)

## Generating FreeBSD nanobsd images

The objective is to generate BSDRP nanobsd images regarding a list of FreeBSD’s code SVN revision number.

You need to [download BSDRP source code](../technical-docs.md#getting-bsdrp-source-code) on a FreeBSD machine.

Then you have to create or customize a BSDRP project for obtaining a small image: Try to remove maximum [FreeBSD options](http://svnweb.freebsd.org/base/head/tools/build/options/) and no ports for improving the image generation speed. The BSDRP’s [TESTING project](https://github.com/ocochard/BSDRP/tree/master/TESTING) is a good example for this step.

Take care of the kernel configuration file: the head branch can impose kernel configuration parameters incompatible between different code revisions. The best method for avoiding this incompatibility is to start the kernel configuration by “include GENERIC” and adding or removing (nooptions XXX, nodevice XXX) unwanted parts. Refer the [kernel configuration file used for BSDRP regression bench lab](https://github.com/ocochard/BSDRP/blob/master/TESTING/kernels/amd64) as an example.

Once your BSDRP bench-project ready, edit the script [tools/bisection-gen.sh](https://github.com/ocochard/BSDRP/blob/master/tools/bisection-gen.sh)for adapting the project basic configuration (PROJECT name, CONSOLE type, ARCH) and filling all SVN revision numbers (SVN_REV_LIST), then start the image generation script (from the top level directory of BSDRP source code):

```
root@dev:/usr/local/BSDRP # mkdir -p /root/benchs/nanobsd
root@dev:/usr/local/BSDRP # tools/bisection-gen.sh /root/benchs/nanobsd
Building image matching revision 257506...done
Building image matching revision 257657...done
Building image matching revision 257715...done
All images were put in /root/benchs/nanobsd
```

At the end, you will find all the nanobsd images in your selected directory.

You can find an example of finals images generated here: <http://dev.bsdrp.net/benchs/265145-274745/nanobsd.images/>

## Configuration sets

The creation of different configuration sets is pretty simple: just create a main folder and inside this folder, creating different folder for each configuration sets.

Inside each configuration sets folder will be placed the configuration files that need override default parameters.

Here is a very simple example regarding [igb NIC drivers tuning benchs](forwarding-performance-lab-of-an-ibm-system-x3550-m3-with-intel-82580.md#igb4-drivers-tunning-with-82546gb) were differents parameters in /boot/loader.conf.local were tested.

We want 3 configuration sets:

- First called “xd1024.proc_lim-1”
- Second called “xd2048.proc_lim-1”
- Third called “xd4096.proc_lim-1”

<!-- -->

```
mkdir -p /root/benchs/configurations/xd1024.proc_lim-1/boot
cat > /root/benchs/configurations/xd1024.proc_lim-1/boot/loader.conf.local <<EOF
hw.igb.rxd="1024"
hw.igb.txd="1024"
hw.igb.rx_process_limit="-1"
EOF
mkdir -p /root/benchs/configurations/xd2048.proc_lim-1/boot
cat > /root/benchs/configurations/xd2048.proc_lim-1/boot/loader.conf.local <<EOF
hw.igb.rxd="2048"
hw.igb.txd="2048"
hw.igb.rx_process_limit="-1"
EOF
mkdir -p /root/benchs/configurations/xd4096.proc_lim-1/boot
cat > /root/benchs/configurations/xd4096.proc_lim-1/boot/loader.conf.local <<EOF
hw.igb.rxd="4096"
hw.igb.txd="4096"
hw.igb.rx_process_limit="-1"
EOF
```

## Testing Lab

Start by configuring all servers, and the DUT with the configurations parameters common to all configuration sets (but remember that files in configuration sets will totally overwrite existing file). Install your ssh public-key on each servers for permitting bench script to automatically connect to them.

There are 2 examples of configuration files available for a bench lab:

- [bench-lab-2nodes.config](https://github.com/ocochard/netbenches/blob/master/AMD_GX-412TC_4Cores_Intel_i210AT/bench-lab-2nodes.config)
- [bench-lab-3nodes.config](https://github.com/ocochard/netbenches/blob/master/AMD_GX-412TC_4Cores_Intel_i210AT/bench-lab-3nodes.pkt.config)

Put on one of these files, all the IP adresses, testing command lines, etc corresponding to your bench test.

Then start [bench-lab.sh](https://github.com/ocochard/netbenches/blob/master/scripts/bench-lab.sh) with some parameters. Then start it:

```
./bench-lab.sh -f bench-lab-parameters-file -c configuration-sets-dir -i nanobsd-images-dir -n iteration -d benchs-results-dir -r my@email.org
```

And here is an example:

```
olivier@lame4:~/netbenches/Xeon_E5-2650-8Cores-Chelsio_T540-CR % ../scripts/bench-lab.sh -f bench-lab-2nodes.config -i /root/images.2017/ -c forwarding-pf-ipfw/config
s/ -p ../pktgen.configs/dualstack-2k/ -d forwarding-pf-ipfw/results/fbsd.2017/ -r olivier@FreeBSD.org
BSDRP automatized upgrade/configuration-sets/benchs script

This script will start 210 bench tests using:
 - Multiples images to test: yes
 - Multiples configuration-sets to test: yes
 - Multiples pkt-gen configuration to test: yes
 - Number of iteration for each set: 5
 - Results dir: forwarding-pf-ipfw/results/fbsd.2017/

Do you want to continue ? (y/n): y
Testing ICMP connectivity to each devices:
  192.168.1.8...OK
  192.168.1.8...OK
  192.168.1.10...OK
Testing SSH connectivity with key to each devices:
  192.168.1.8...OK
  192.168.1.8...OK
  192.168.1.10...OK
Starting the benchs
Start firmware image set: /root/images.2017//BSDRP-311014-upgrade-amd64-serial.img.xz
Upgrading...done
Rebooting 192.168.1.10 and waiting device return online...done
Start configuration set: forwarding
Uploading cfg forwarding-pf-ipfw/configs//forwarding to 192.168.1.10
Rebooting 192.168.1.10 and waiting device return online...done
Start pkt-gen set: ../pktgen.configs/dualstack-2k//inet4
Start bench serie bench.311014.forwarding.inet4.1
Waiting for end of bench 1/210...done
Rebooting 192.168.1.10 and waiting device return online...done
Start bench serie bench.311014.forwarding.inet4.2
Waiting for end of bench 2/210...done
Rebooting 192.168.1.10 and waiting device return online...done
Start bench serie bench.311014.forwarding.inet4.3
Waiting for end of bench 3/210...done
Rebooting 192.168.1.10 and waiting device return online...done
Start bench serie bench.311014.forwarding.inet4.4
Waiting for end of bench 4/210...done
Rebooting 192.168.1.10 and waiting device return online...done
Start bench serie bench.311014.forwarding.inet4.5
Waiting for end of bench 5/210...done
Rebooting 192.168.1.10 and waiting device return online...done
Start pkt-gen set: ../pktgen.configs/dualstack-2k//inet6
Start bench serie bench.311014.forwarding.inet6.1
Waiting for end of bench 6/210...done
Rebooting 192.168.1.10 and waiting device return online...done
Start bench serie bench.311014.forwarding.inet6.2
Waiting for end of bench 7/210...done
Rebooting 192.168.1.10 and waiting device return online...done
Start bench serie bench.311014.forwarding.inet6.3
Waiting for end of bench 8/210...done
Rebooting 192.168.1.10 and waiting device return online...done
Start bench serie bench.311014.forwarding.inet6.4
Waiting for end of bench 9/210...done
Rebooting 192.168.1.10 and waiting device return online...done
Start bench serie bench.311014.forwarding.inet6.5
Waiting for end of bench 10/210...done
Rebooting 192.168.1.10 and waiting device return online...done
Start configuration set: ipfw-statefull
Uploading cfg forwarding-pf-ipfw/configs//ipfw-statefull to 192.168.1.10
Rebooting 192.168.1.10 and waiting device return online...done
...
Rebooting DUT and waiting device return online...done
Waiting for end of bench 209/210...done
Rebooting DUT and waiting device return online...done
Waiting for end of bench 210/210...done
All bench tests were done, results in forwarding-pf-ipfw/results/fbsd.2017/
```

## Results generation

Once bench finished, there are lot’s of raw result files with these names:

- bench.NANOBSD-SVN.CONFIGURATION-SETS.info: Give resumed information about the nanobsd image and configuration set name used
- bench.NANOBSD-SVN.CONFIGURATION-SETS.ITERATION.receiver: raw output of the ssh session on the receiver
- bench.NANOBSD-SVN.CONFIGURATION-SETS.ITERATION.sender: raw output of the ssh session on the sender

Here is [an example of these raw results](https://github.com/ocochard/netbenches/blob/master/AMD_GX-412TC_4Cores_Intel_i210AT/bench-lab-2nodes.config).

These raw results, closely dependents of the bench tool used, need to be filtered (and synthesized) in a usable data file.

BSDRP use the script [bench-lab-ministat.sh](https://github.com/ocochard/netbenches/blob/master/scripts/bench-lab-ministat.sh) for filtering netmap pkt-gen output with a first pass of ministat and generate a list of files named SVN-REV.CONFIG-SETS-NAME that include N line of result (with N=number of test iterations) and gnuplot.data file.
