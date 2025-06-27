---
layout: default
title: mistake
---



in this challenge the error lies in the fact it reads the password from stdin, because the compare happens before the assignment when it opens the password file for reading.

```python
{% include_relative scripts/mistake/mistake.py %}
```


![image](./images/mistake.png)

**Flag:** ***`Mommy, the operator priority always confuses me :(`***
