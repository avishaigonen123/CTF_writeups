---
layout: default
title: tiny_easy
---



in this challenge, we spam the stack with our shellcode, and hope that in arg1 we'll put address that'll fall exactly on NOP bytes, and by this way execute our shellcode.

```python
{% include_relative scripts/tiny_easy/tiny_easy.py %}
```


![image](./images/tiny_easy.png)

**Flag:** ***`What a tiny task :) good job!`***
