---
title: cloud-init
description: Provisioning a BSDRP instance at first boot with FreeBSD's nuageinit (NoCloud datasource)
---
BSDRP ships with FreeBSD's [`nuageinit(7)`](https://man.freebsd.org/cgi/man.cgi?query=nuageinit) enabled by default. `nuageinit` is FreeBSD's in-base re-implementation of a subset of [cloud-init](https://cloud-init.io/): on first boot it looks for a configuration datasource and applies user-provided cloud-config to the running system. This lets you ship a generic BSDRP image and have it configure itself (hostname, users, network, services, routing daemons) the first time it starts, with no console interaction.

This page walks through provisioning a BSDRP VM with the `NoCloud` datasource, which is the simplest path for self-hosted setups: you build a small disk image (ISO 9660 or VFAT) containing two files, attach it to the VM, and `nuageinit` does the rest.

## How nuage-init runs on BSDRP

`nuageinit` is enabled in `/etc/defaults/vendor.conf` (`nuageinit_enable="yes"`) and runs through three `firstboot` rc scripts:

- `nuageinit` runs before networking is up. It probes for a datasource (see below), mounts it, and processes the metadata and the static parts of the user-data (users, SSH keys, files to write).
- `nuageinit_post_net` runs after networking is up but before regular services. It applies anything that needed the network (for example, package installs).
- `nuageinit_user_data_script` runs near the end of the boot sequence and executes the `runcmd` commands and any raw user-data script.

Output from all three is appended to `/var/log/nuageinit.log` on the running system. Because they are `firstboot` scripts, they only run once: after the first successful boot, BSDRP removes the firstboot sentinel and subsequent boots skip them.

### Supported datasources

`nuageinit` auto-detects the datasource by probing, in this order:

1. A vfat or iso9660 volume labelled `config-2` (OpenStack ConfigDrive).
2. A vfat or iso9660 volume labelled `cidata` (NoCloud).
3. If the SMBIOS product string starts with `OpenStack`, the OpenStack metadata service at `http://169.254.169.254/openstack/latest/` is contacted over DHCP.

The NoCloud walkthrough below uses case 2.

## NoCloud walkthrough

The NoCloud datasource is a filesystem with up to two files at its root:

- `meta-data` (YAML, mandatory): instance identity. `nuageinit` aborts if the file is missing, but in practice the only key it consults from it is `local-hostname` (the canonical NoCloud field for the hostname; `hostname` is accepted as a fallback). The NoCloud spec also defines `instance-id`, but `nuageinit` ignores it - the firstboot sentinel takes care of "have I run before?".
- `user-data` (YAML, starting with the `#cloud-config` marker line, optional): what to configure. If absent (or empty), `nuageinit` only applies the hostname from `meta-data` and creates the default user, then exits.

You package them into a small disk image with the volume label `cidata`, then attach that image to the VM. The image can be either an ISO 9660 filesystem (typical with hypervisors that expose it as a CD-ROM) or a VFAT filesystem (convenient when attaching as a regular block device, which is what BSDRP's own bhyve lab script does).

### Building the seed image

Create a working directory with the two files:

```
mkdir -p seed
cat > seed/meta-data <<'EOF'
local-hostname: edge1
EOF

cat > seed/user-data <<'EOF'
#cloud-config
runcmd:
       - mount -uw /
       - mkdir -p /home/admin
       - cp /usr/share/skel/dot.profile /home/admin/.profile
       - cp /usr/share/skel/dot.shrc /home/admin/.shrc
       - chown -R admin:admin /home/admin
chpasswd:
  list: |
    root:password123
  expire: False
network:
  version: 2
  ethernets:
    vtnet0:
      dhcp4: true
write_files:
  - path: /etc/rc.conf
    content: |
     frr_enable=yes
    permissions: '0644'
users:
  - name: admin
    homedir: /home/admin
    gecos: Foo B. Bar
    sudo: ALL=(ALL) NOPASSWD:ALL
    plain_text_passwd: password321
```

Build the image. Two options work equally well for `nuageinit`; pick whichever is most convenient for your hypervisor.

ISO 9660, on FreeBSD with `makefs(8)` from base:

```
makefs -t cd9660 -o rockridge,label=cidata seed.iso seed
```

ISO 9660, on a host with `genisoimage` or `mkisofs`:

```
genisoimage -output seed.iso -volid cidata -joliet -rock seed
```

VFAT, on FreeBSD with `makefs(8)`. This is the format BSDRP's [`BSDRP-lab-bhyve.sh`](https://github.com/ocochard/BSDRP/blob/master/tools/BSDRP-lab-bhyve.sh) script generates, because the resulting image can be attached as a plain `virtio-blk` disk:

```
makefs -t msdos -o volume_label=cidata -o fat_type=12 -s 2m seed.img seed
```

The volume label must be exactly `cidata`, otherwise `nuageinit` will not pick it up.

### Attaching the seed image to the VM

Attach the seed image when you boot the BSDRP image. Whether you attach it as a CD-ROM or as a regular block device depends on the filesystem you chose: ISO 9660 is the obvious fit for a virtual CD-ROM, while a VFAT image can be plugged in as any other disk. The exact incantation depends on your hypervisor:

- **bhyve, ISO 9660 as CD-ROM**: add another `-s` slot with `ahci-cd,seed.iso`, alongside your BSDRP image device.
- **bhyve, VFAT as disk** (used by `BSDRP-lab-bhyve.sh`): add another `-s` slot with `virtio-blk,seed.img`.
- **QEMU/KVM, ISO 9660**: `-drive file=seed.iso,media=cdrom,readonly=on`.
- **VirtualBox**: add an additional optical drive on the VM's storage controller and mount `seed.iso`.
- **VMware**: add a CD/DVD drive backed by `seed.iso`.

Boot the VM. The first boot will take noticeably longer than a normal boot while `nuageinit` runs. After it finishes, you can SSH in with the `admin` user's key.

### Verifying the run

After the first boot, log in and check the log:

```
cat /var/log/nuageinit.log
```

If anything went wrong, the log usually points at the offending key or at the datasource not being found. Two common failure modes:

- **Volume label typo**: the image must be labelled `cidata` exactly. On the running system, `fstyp /dev/iso9660/CIDATA` (or `fstyp /dev/msdosfs/CIDATA` for a VFAT seed) confirms the label.
- **YAML indentation**: `user-data` is YAML, not free-form text. A misindented `users` block silently produces no users.

Because `firstboot` scripts only run once, fixing user-data and rebooting is not enough on its own: you also need to clear the firstboot sentinel (`/firstboot`) or rebuild the VM from a clean image.

## Supported cloud-config keys

The example above uses the keys you are most likely to need on a router: `users`, `chpasswd`, `network`, `write_files`, `runcmd`. FreeBSD's `nuageinit` implements a subset of upstream cloud-init's schema. For the authoritative list of supported keys and their exact semantics, see [`nuageinit(7)`](https://man.freebsd.org/cgi/man.cgi?query=nuageinit).

!!! note
    `nuageinit` is intentionally limited compared to upstream cloud-init. If you depend on a specific cloud-config key, check the man page before assuming it is supported.

## Acknowledgements

The original working recipe that this page is based on was contributed by Mark Saad via the [BSDRP mailing list](../community/mailing-lists.md) and published as [this gist](https://gist.github.com/failedrequest/b3e75c63e68b22cac10273b30d0b0ad3); the user-data above is adapted from that contribution.
