---
layout: default
title: maze7
---



we will exploit the line marked, and override the ret-address by giving value of 0x44 in the size, while the ret-address is at 0x40.
![image](./images/level7_1.png)

in the payload all the staff is \x00, with one exception, when we pass arg4 which contains the size.
we do it using buffer overflow 
![image](./images/level7_2.png)

i marked important values: arg1, arg2, arg3, arg4, fd. (in this order), so we can see that *arg4* is found after *46 bytes*.
![image](./images/level7_3.png)

 
now, all left is to create your shellcode in environment variable and put the address in the code, in `shellcode_address`.
```python
{% include_relative scripts/level7/level7.py %}
```


![image](./images/level7_4.png)

**Flag:** ***`eQdZB1qy6L`*** 
