---
layout: default
title: Level3_Pwnage_Linux_Level_Up
---

# Level3 Pwnage Linux Level Up Solution


It doesn't put NULL after the strncat, so, we can manipulate it to make buffer overflow and then override the ret-address.
```python
{% include_relative scripts/level3.py %}
```



![image](./images/level3.png)

**Flag:** ***`VHDY2pdYVyXi08kupbos`***
