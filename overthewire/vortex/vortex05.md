---
layout: default
title: vortex5
---



in this challenge we run brute force on md5, which approved to be vulnerable to collision attack.

```python
{% include_relative scripts/level5/level5.py %}
```
, which will do the brute force for us.

example output:
```
Brute-forcing started...
Password is: rlTf6
Brute-forcing ended...
Time taken: 4.70 seconds
```
so, the password is: `rlTf6`

![image](./images/level5.png)

**Flag:** ***`heo3EbnS9`***