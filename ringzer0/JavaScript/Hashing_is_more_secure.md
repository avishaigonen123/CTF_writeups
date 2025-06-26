---
layout: default
title: Hashing_is_more_secure
---

# Hashing is more secure Solution

here we got the hash `b89356ff6151527e89c4f3e3d30c8e6586c63962`.
i used hashcat to crack this using bruteforce:
`hashcat -m 100 -a 3 "b89356ff6151527e89c4f3e3d30c8e6586c63962" --show`

we got this password: `adminz`

**Flag:** ***`FLAG-bXNsYg9tLCaIX6h1UiQMmMYB`***
