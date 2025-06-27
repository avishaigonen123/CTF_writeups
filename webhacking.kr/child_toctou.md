---
layout: default
title: child_toctou
---

# webhacking child_toctou Solution

I've got the main idea, which is making my own server after 1 second that will point to "webhacking.kr" (use DNS somehow), and then open there the port 10020, and there i'll server `/cmd/api.txt`, where api.txt contain the command i want, in this case `cat flag.php`

i can use this: https://github.com/l4rzy/l4rzy.github.io/commit/0f9c7f5e53ac9693351bf6cdb955010748a5f19d, link for someone who solved this challange

here is the source code: [child_toctou]
```python
{% include_relative scripts/child_toctou.py %}
```


![example](./images/child_toctou.png)


**Flag:** ***``*** 
