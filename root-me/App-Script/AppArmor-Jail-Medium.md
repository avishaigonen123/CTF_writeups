---
layout: default
title: AppArmor-Jail-Medium
---
In this challenge we get this `AppArmor` config file:
```
#include <tunables/global>

profile docker_chall_medium flags=(attach_disconnected,mediate_deleted) {
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

	deny @{PROC}/* w, # deny write for all files directly in /proc (not in a subdir)
	# deny write to files not in /proc/<number>/** or /proc/sys/**
	deny @{PROC}/{[^1-9],[^1-9][^0-9],[^1-9s][^0-9y][^0-9s],[^1-9][^0-9][^0-9][^0-9]*}/** w,
	deny @{PROC}/sys/[^k]** w, # deny /proc/sys except /proc/sys/k* (effectively /proc/sys/kernel)
	deny @{PROC}/sys/kernel/{?,??,[^s][^h][^m]**} w, # deny everything except shm* in /proc/sys/kernel/
	deny @{PROC}/sysrq-trigger rwklx,
	deny @{PROC}/kcore rwklx,

	/usr/local/bin/sh px -> shprof2,
	deny /home/admin/** w,
	deny /home/admin/flag_here/flag.txt r,
}

profile shprof2 flags=(attach_disconnected,mediate_deleted) {
	#include <abstractions/base>
	#include <abstractions/bash>

	network,
	capability,
	mount,
	deny mount cgroup, # prevent container escape
	umount,
	file,
	signal (send,receive),

	deny /sys/[^f]*/** wklx,
	deny /sys/f[^s]*/** wklx,
	deny /sys/fs/[^c]*/** wklx,
	deny /sys/fs/c[^g]*/** wklx,
	deny /sys/fs/cg[^r]*/** wklx,
	deny /sys/firmware/** rwklx,
	deny /sys/kernel/security/** rwklx,

	deny @{PROC}/* w, # deny write for all files directly in /proc (not in a subdir)
	# deny write to files not in /proc/<number>/** or /proc/sys/**
	deny @{PROC}/{[^1-9],[^1-9][^0-9],[^1-9s][^0-9y][^0-9s],[^1-9][^0-9][^0-9][^0-9]*}/** w,
	deny @{PROC}/sys/[^k]** w, # deny /proc/sys except /proc/sys/k* (effectively /proc/sys/kernel)
	deny @{PROC}/sys/kernel/{?,??,[^s][^h][^m]**} w, # deny everything except shm* in /proc/sys/kernel/
	deny @{PROC}/sysrq-trigger rwklx,
	deny @{PROC}/kcore rwklx,

	/lib/x86_64-linux-gnu/ld-*.so mr,
	deny /home/admin/** w,
	deny /home/admin/flag_here/flag.txt r,
}
```

