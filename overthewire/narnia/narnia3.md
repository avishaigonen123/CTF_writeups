---
layout: default
title: narnia3
---



first we can see it doesn't have ASLR and run protection.
![alt text](./images/level3_1.png)

we will use our shellcode [shellcode.py](./general/shellcode.py) and store it in environment variable, then we will find the address of the environment variable using [get_address.c](./general/get_address.c)

using the script we saw we override the return address after 132, so let's insert the address of our environment variable. 

![alt text](./images/level3_2.png)


**Flag:** ***`2xszzNl6uG`*** 
