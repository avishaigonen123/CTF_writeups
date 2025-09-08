---
layout: default
title: hell_fire
---

In this challenge we can use `Blind SQL injection`, by giving this query
```sql
?order=IF(substr(id,1,1)='a',0,1)
```
and viewing the way the tables get sorted.

the source code is here:
```python
{% include_relative scripts/hell_fire.py %}
```

From some reason, it doesn't manage to find the `i` inside `admin`, so i inserted it manually, with `initial_flag` parameter in the code.

**Password:** ***`admin_secure_email@emai1.com`*** 
