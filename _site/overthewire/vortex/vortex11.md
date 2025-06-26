---
layout: default
title: vortex11
---

# vortex level11 Solution

I've found that on the heap there is an address that it + 0x40 will be the address of `s`, so, we need to put there our exit plt and override it using shellcode address.

```py
% scripts/level11.py
```

![image](./images/level11.png)

**Flag:** ***`reDLd0Cai`***