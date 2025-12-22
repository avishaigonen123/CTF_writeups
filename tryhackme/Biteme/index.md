---
layout: default
title: Biteme
status: incomplete
---

## TL;DR



### Recon

we start with `rustscan`, using this command:
```bash
rustscan -a $target -- -sV -sC -oN nmap.txt -oX nmap.xml
```

![rustscan](image.png)

we can see port `22` with ssh and port `80` with apache http server.
```bash
PORT   STATE SERVICE REASON         VERSION                                                                                                      
22/tcp open  ssh     syn-ack ttl 62 OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)                                                
| ssh-hostkey:                                                                                                                                   
|   3072 0d:e2:ab:3b:9a:34:2d:5b:09:bc:98:cd:8c:51:c6:7c (RSA)                                                                                   
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDBF63d7UcJ3yea5pRwsnwaNNuUNVSI/L/+F8BXQMfz7k1SjOzTSehdN8fW7Y9SVKa1pPOKmh53nGusKFMokdSTp2N2z25vqYP0J0kuct1
PZbzVZpWWu6wwoRrPUwIhxtXot4Suw8meD02G2ukieq2Go6A+5v9ElhvxsVCmxwSX/H+DvgYhnkUGuzoGckrIMY0dApjgihR4UnNk59vqv8NWp+RglFwDt0LlHix9fboAyoR0qgx1Y1mCI1Tg
iUw3yYhGhtXZDruRW03hk53jKPxEfuZ1Rq4ljU2AubmH73KXBQZLiAbGTamA3xq+uA5qo0xn2eA3+D2z7VMSR7kluEex75khWmOEU6/muCSpLGLnKSX018MELiZMYIV2nnZl99VaC+EvgSCyl
BMThjxYxQsxdA6ipzHLNNW8UfjlfDSuIWwtiuQdAFyINFIDBu+6Js4MsTBadDCCsRxAC2EX9dzc8iNhSb/g4+RremDSfh6t310jSBaHt5HBcxClRASZ6+c=                          
|   256 58:50:80:5f:b3:33:5a:57:02:76:23:f2:51:d0:9a:ef (ECDSA)                                                                                  
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBFLHyA/XcqqBl7UHDm/zLsMXDvZrupF0wkjjzBWksryC8isfpb+U0BeUXSDenJZDrVMZDsl
TOWvrEe4+EUY4J40=                                                                                                                                
|   256 62:35:31:88:13:12:e6:18:5d:00:28:d6:29:ec:3e:62 (ED25519)                                                                                
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIG09zzUM+JTAleiwfr708OWaRkIucheTz4/v+bt/n7B3                                                               
80/tcp open  http    syn-ack ttl 62 Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Apache2 Ubuntu Default Page: It works
| http-methods: 
|_  Supported Methods: GET POST OPTIONS HEAD
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

### ...

we start with enumerating endpoints using `ffuf`:
```bash
┌──(agonen㉿kali)-[~/thm/Bitme]
└─$ ffuf -u 'http://biteme/FUZZ' -w /usr/share/SecLists/Discovery/Web-Content/common.txt -e .txt,.php,.xml -fc 403

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://biteme/FUZZ
 :: Wordlist         : FUZZ: /usr/share/SecLists/Discovery/Web-Content/common.txt
 :: Extensions       : .txt .php .xml 
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
 :: Filter           : Response status: 403
________________________________________________

console                 [Status: 301, Size: 302, Words: 20, Lines: 10, Duration: 77ms]
index.html              [Status: 200, Size: 10918, Words: 3499, Lines: 376, Duration: 73ms]
```

![ffuf](image-1.png)

Next, we can go to `console` and find this login portal:

![login portal](image-2.png)

We can see this snippet in the source code:
```js
<script>
      function handleSubmit() {
        eval(function(p,a,c,k,e,r){e=function(c){return c.toString(a)};if(!''.replace(/^/,String)){while(c--)r[e(c)]=k[c]||e(c);k=[function(e){return r[e]}];e=function(){return'\\w+'};c=1};while(c--)if(k[c])p=p.replace(new RegExp('\\b'+e(c)+'\\b','g'),k[c]);return p}('0.1(\'2\').3=\'4\';5.6(\'@7 8 9 a b c d e f g h i... j\');',20,20,'document|getElementById|clicked|value|yes|console|log|fred|I|turned|on|php|file|syntax|highlighting|for|you|to|review|jason'.split('|'),0,{}))
        return true;
      }
    </script>
```
I didn't deobfuscate this, but it still looks like this message:
```bash
fred I turned on php file syntax highlighting for you to review jason
```

Inside the official documentation [https://www.php.net/manual/en/function.highlight-file.php](https://www.php.net/manual/en/function.highlight-file.php), I find this:

>  Many servers are configured to automatically highlight files with a phps extension. For example, example.phps when viewed will show the syntax highlighted source of the file. To enable this, add this line to the httpd.conf: 

Okay, let's try to get the source code, for example, `index.phps`:


### Privilege Escalation to Root


