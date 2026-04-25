---
layout: default
title: SSL Pinning Bypass
---
This challenge is about SSL Pinning Bypass, so I first searched for the string `ssl`, in the decompiled source code:

![](images/index.png)
We can see there is usage of some `SSLCertificate` package, let's go there