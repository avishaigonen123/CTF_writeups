---
layout: default
title: Aster
status: incomplete
---

## TL;DR



### Recon

we start with `rustscan`, using this command:
```bash
rustscan -a $target -- -sV -sC -oN nmap.txt -oX nmap.xml
```

![rustscan results](image.png)

we can see port `22` with ssh, port `80` with apache http server, port `1720` with unknown service, port `2000` with unknown service and port `5038` with asterisk
```bash
PORT     STATE SERVICE     REASON         VERSION                                                                                                            
22/tcp   open  ssh         syn-ack ttl 62 OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)                                                      
| ssh-hostkey: 
|   2048 fe:e3:52:06:50:93:2e:3f:7a:aa:fc:69:dd:cd:14:a2 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDEs6oKJb5SNNUczex8j97pL/V93XRaRytbAH7iR9pN0HbCmc2bD/Rg4IUuDArz4USY1G5aN0r+C3fcBSlmLWaqk+uzbNZFriELMcJPKa7tP7zx7o4TVMQDepvvcZUy9Z8QoA+n4cJYOjlldkWGq/dmsPQqBHDmHowxMauJkZxh2QVR0WpDZxcjbS26O8aC62QvT5ct9wgzBzD/dVV/SC3VH7sQOPsEFj+PHGoHrFz7MntxtRyR9Ujf+Dzbk2wnUVGrc6NZt8MV3vfo5nXjBRPTaIX6XNTijQxoj0/0NJ3YwntmHOQXaPu4++fzjP9cf4+r8PNppeKNYwWLRxzjnAiZ
|   256 9c:4d:fd:a4:4e:18:ca:e2:c0:01:84:8c:d2:7a:51:f2 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBPROPGV3YntCB4YEBuSk7u8qF0H9WxI9nTGbCJahJP4gJNcEj4uwn24Ep1eSs0kHxjFdri6+QQlPUygwRvAQqTs=
|   256 c5:93:a6:0c:01:8a:68:63:d7:84:16:dc:2c:0a:96:1d (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIPrB46mC2C71WGXfIc9TwwLWhC99D9M2IxUHbQCbH0vp
80/tcp   open  http        syn-ack ttl 62 Apache httpd 2.4.18 ((Ubuntu))
|_http-title: Aster CTF
|_http-server-header: Apache/2.4.18 (Ubuntu)
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
1720/tcp open  h323q931?   syn-ack ttl 62
2000/tcp open  cisco-sccp? syn-ack ttl 62
5038/tcp open  asterisk    syn-ack ttl 62 Asterisk Call Manager 5.0.2
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

I added `aster.thm` to my `/etc/hosts`

### ...

```py
import pyfiglet
o0OO00 = pyfiglet.figlet_format('Hello!!')
oO00oOo = '476f6f64206a6f622c2075736572202261646d696e2220746865206f70656e20736f75726365206672616d65776f726b20666f72206275696c64696e6720636f6d6d756e69636174696f6e732c20696e7374616c6c656420696e20746865207365727665722e'
OOOo0 = bytes.fromhex(oO00oOo)
Oooo000o = OOOo0.decode('ASCII')
if 0:
    (i1 * ii1IiI1i % OOooOOo) / I11i / o0O / IiiIII111iI
Oo = '476f6f64206a6f622072657665727365722c20707974686f6e206973207665727920636f6f6c21476f6f64206a6f622072657665727365722c20707974686f6e206973207665727920636f6f6c21476f6f64206a6f622072657665727365722c20707974686f6e206973207665727920636f6f6c21'
I1Ii11I1Ii1i = bytes.fromhex(Oo)
Ooo = I1Ii11I1Ii1i.decode('ASCII')
if 0:
    iii1I1I / O00oOoOoO0o0O.O0oo0OO0 + Oo0ooO0oo0oO.I1i1iI1i - II
print o0OO00
```

###

 Privilege Escalation to Root


