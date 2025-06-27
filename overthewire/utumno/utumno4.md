---
layout: default
title: utumno4
---



first we can see there is no protection, and also ASLR disabled.
![image](./images/level4_1.png)

in this level we do buffer overflow, but we also need to pass one check, this check:
![image](./images/level4_2.png)
check that the len of the buffer answer on specific rule.

here you can find the shellcode [shellcode.py](./general/shellcode.py)

```py
{% include_relative scripts/level4/level4.py %}
```
, you need to change the address of the shellcode based on the address of your environment variable.

![image](./images/level4_3.png)

**Flag:** ***`vY134qxapL`*** 
