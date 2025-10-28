---
layout: default
title: Imagery
---

### Recon

we start with `nmap`, using this command, i was needed to add `-Pn`, because otherwise `nmap` thinks the host is down:
```bash
nmap -p- -sVC --min-rate=10000 $target -oX nmap.xml -oN nmap.txt -Pn
```

However, the number of open ports is very delusive, so i tried several times and that's what i got:
```bash
┌──(agonen㉿kali)-[~/htb/Conversor]
└─$ nmap 10.10.11.88 -Pn 
Starting Nmap 7.95 ( https://nmap.org ) at 2025-10-28 00:57 IST
Nmap scan report for 10.10.11.88
Host is up (1.6s latency).
Not shown: 998 closed tcp ports (reset)
PORT     STATE SERVICE
22/tcp   open  ssh
8000/tcp open  http-alt
```

I can verify that there is `ssh` on port `22`, and also some http serve on port `8000`.

After more enhance scan on port `8000`:
```bash
┌──(agonen㉿kali)-[~/htb/Conversor]
└─$ nmap -p8000 -sVC --min-rate=10000 $target -Pn
Starting Nmap 7.95 ( https://nmap.org ) at 2025-10-28 01:03 IST
Nmap scan report for imagery.htb (10.10.11.88)
Host is up (0.57s latency).

PORT     STATE SERVICE VERSION
8000/tcp open  http    Werkzeug httpd 3.1.3 (Python 3.12.7)
|_http-title: Image Gallery
|_http-server-header: Werkzeug/3.1.3 Python/3.12.7
```

So, we'll add `imagery.htb` to `/etc/hosts`.
```bash
10.10.11.88     imagery.htb
```

### 

So, we'll start with dir enumeration and vhost enumeration.

### Privilege Escalation to Root


**User Flag:*****`b40abdfe23665f766f9c61ecba8a4c19`***

**Root Flag:*****`b40abdfe23665f766f9c61ecba8a4c19`***
