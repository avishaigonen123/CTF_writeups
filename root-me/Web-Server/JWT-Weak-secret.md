---
layout: default
title: JWT-Weak-secret
---

This is our access_token: `eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJyb2xlIjoiZ3Vlc3QifQ.4kBPNf7Y6BrtP-Y3A-vQXPY9jAh_d0E6L4IUjL65CvmEjgdTZyr2ag-TM-glH6EYKGgO3dBYbhblaPQsbeClcw`

We run this bruteforce command:
```
hashcat -a 0 -m 16500 eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJyb2xlIjoiZ3Vlc3QifQ.4kBPNf7Y6BrtP-Y3A-vQXPY9jAh_d0E6L4IUjL65CvmEjgdTZyr2ag-TM-glH6EYKGgO3dBYbhblaPQsbeClcw /usr/share/seclists/Passwords/scraped-JWT-secrets.txt
```

And after seconds, we get the super secret key which is `lol`.
![FINAL](./images/JWT-Weak-secret_FINAL.png)

**Flag:** **_`PleaseUseAStrongSecretNextTim`_**
