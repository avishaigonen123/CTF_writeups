---
layout: default
title: behemoth9
---



```python
{% include_relative general/shellcode.py %}
```

we need to find the address of the env variable.

```c
{% include_relative general/get_address.c %}
```
    
```python
{% include_relative scripts/level2.py %}
```

**Flag:** ***`IxPJbQtH8q`*** 
