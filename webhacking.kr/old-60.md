---
layout: default
title: old-60
---

# Webhacking old-60 Solution

this challenge is based on race condition, and also on the fact that you can talk on two different PHP sessions by changing your cookie.

this are the two source codes:
[old-60_1]
```scripts/old-60_1.py
{% include_relative scripts/old-60_1.py %}
```

[old-60_2]
```scripts/old-60_2.py
{% include_relative scripts/old-60_2.py %}
```


they are mainly the same, the only difference it the `PHPSESSID`
