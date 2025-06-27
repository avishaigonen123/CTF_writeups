---
layout: default
title: utumno3
---



first we can see there is no protection, and also ASLR disabled.
![image](./images/level3_1.png)

i decompiled the file using ghidra, and find out that we can manipulate our input in order to override the return address to our shellcode address. 
![image](./images/level3_2.png)

```python
{% include_relative scripts/level3/shellcode.py %}
```
, that runs: `execve('/bin/cat','/tmp/passwwd')`

```python
{% include_relative scripts/level3/level3.py %}
```
, you need to change the address of the shellcode based on the address of your environment variable.

also, you need to run this command: `ln -sf /etc/utumno_pass/utumno4 /tmp/passwwd`


![image](./images/level3_3.png)

**Flag:** ***`qHWLExh7C5`*** 
