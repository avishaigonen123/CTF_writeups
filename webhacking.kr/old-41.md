---
layout: default
title: old-41
---



first we will upload file with long filename, and see what happens: [old-41]
```py
{% include_relative scripts/old-41.py %}
```


```
<b>Warning</b>:  copy(./4b0e87fef7b5e8ba83894970c9806042e5d6ec9a/asdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasdasda in <b>/var/www/html/challenge/web-19/index.php</b> on line <b>21</b><br />
```

as we can see in the warning, this is the directory: `4b0e87fef7b5e8ba83894970c9806042e5d6ec9a`

let's go to this directory and enter random file:
`https://webhacking.kr/challenge/web-19/4b0e87fef7b5e8ba83894970c9806042e5d6ec9a/d`

**Flag:** ***`FLAG{error_msg_is_more_userful_than_you_think}`*** 

