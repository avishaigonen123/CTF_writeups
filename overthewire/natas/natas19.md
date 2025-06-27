---
layout: default
title: natas19
---



This challenge is almost the same as the previous challenge, the only difference is that the cookie now is `hex(session-admin)`
in this challenge we know there is a session for the admin, and the sessions can be detected using the cookie. so, let's brute force those 640 options until finding the session of the admin.

this is the source code [level19]
```python
{% include_relative scripts/level19.py %}
```



**Flag:** ***`p5mCvP7GS2K6Bmt3gqhM2Fc1A5T8MVyw`*** 