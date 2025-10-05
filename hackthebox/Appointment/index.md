---
layout: default
title:  Appointment 
---

first, we'll start with the `nmap`:
```bash
nmap -p- -sVC --min-rate=10000 $target
```

As we can see, the only open port is `80`.

![nmap](image.png)

We can see there is an *apache* server on this port, and it serves a page that its title is `login`, so it's probably some sort of login page.
```
PORT      STATE    SERVICE VERSION
80/tcp    open     http    Apache httpd 2.4.38 ((Debian))
|_http-server-header: Apache/2.4.38 (Debian)
|_http-title: Login
```



**Flag:*****`b40abdfe23665f766f9c61ecba8a4c19`***
