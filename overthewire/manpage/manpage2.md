---
layout: default
title: manpage2
---



in this level we can exploit the fact it leaves the file open, and also we can execute our code using the last line that reruns the file, with `excel`.

```python
{% include_relative scripts/shellcode.py %}
```
<!--
 ```c
{% include_relative scripts/level2/level2.c %}
```
```c
{% include_relative scripts/level2/read_pass.c %}
```
 -->

```python
{% include_relative scripts/shellcode.py %}
```

![image](./images/level2.png)

**Flag:** ***`uAcGloJt0Q`*** 
