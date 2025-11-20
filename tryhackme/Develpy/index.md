---
layout: default
title: Develpy
---

## TL;DR



### Recon

we start with `nmap`, using this command:
```bash
nmap -p- -sVC --min-rate=10000 $target -oX nmap.xml -oN nmap.txt -Pn
```

![nmap results](image.png)

We can see port `22` with ssh, and port `10000` with some strange service.

```bash
PORT      STATE SERVICE           VERSION                                                                                                                    
22/tcp    open  ssh               OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)                                                               
| ssh-hostkey:                                                                                                                                               
|   2048 78:c4:40:84:f4:42:13:8e:79:f8:6b:e4:6d:bf:d4:46 (RSA)                                                                                               
|   256 25:9d:f3:29:a2:62:4b:24:f2:83:36:cf:a7:75:bb:66 (ECDSA)                                                                                              
|_  256 e7:a0:07:b0:b9:cb:74:e9:d6:16:7d:7a:67:fe:c1:1d (ED25519)                                                                                            
10000/tcp open  snet-sensor-mgmt?                                                                                                                            
| fingerprint-strings:                                                                                                                                       
|   DNSVersionBindReqTCP, GetRequest, NULL:                                                                                                                  
|     Private 0days                                                                                                                                          
|     Please enther number of exploits to send??:                                                                                                            
|   GenericLines:                                                                                                                                            
|     Private 0days                                                                                                                                          
|     Please enther number of exploits to send??: Traceback (most recent call last):                                                                         
|     File "./exploit.py", line 6, in <module>                                                                                                               
|     num_exploits = int(input(' Please enther number of exploits to send??: '))                                                                             
|     File "<string>", line 0                                                                                                                                
|     SyntaxError: unexpected EOF while parsing                                                                                                              
|   HTTPOptions, RTSPRequest:                                                                                                                                
|     Private 0days                                                                                                                                          
|     Please enther number of exploits to send??: Traceback (most recent call last):                                                                         
|     File "./exploit.py", line 6, in <module>                                                                                                               
|     num_exploits = int(input(' Please enther number of exploits to send??: '))                                                                             
|     File "<string>", line 1, in <module>                                                                                                                   
|_    NameError: name 'OPTIONS' is not defined                         
```

### a

We can check what there is behind port `10000`. when we execute:
```bash
nc $target 10000
```
it asks:
```bash
Please enther number of exploits to send??:
```

Then, we give some number, and it looks like pinging behind the scenes.

![port 10000 nc](image-1.png)

I tried to give something else, like `'`, and it crashed. We can see the error message:
```py
File "./exploit.py", line 6, in <module>
    num_exploits = int(input(' Please enther number of exploits to send??: '))
``` 

![crashing](image-2.png)

...


### Privilege Escalation to Root


