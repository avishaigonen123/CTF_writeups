---
layout: default
title: LagerLounge
---

In this challenge I noticed that when we logged in as guest with the credentials:
```bash
guest:guestpass
```

There was session cookie that was set to
```bash
Cookie: session=Z3Vlc3Q=
```

Which after decoding gave me `guest`.

So, I simply encoded `admin` and sent the cookie:
```bash
Cookie: session=YWRtaW4=
```

![cookie](image.png)

we logged in as admin and got the flag:

![flag](image-6.png)

```bash
wscoil{--------------------}
```
