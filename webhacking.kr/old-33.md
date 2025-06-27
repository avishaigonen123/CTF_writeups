---
layout: default
title: old-33
---

# Webhacking old-33 Solution


this challange will be long, each time you will need to do something different until you finish it.
1. `https://webhacking.kr/challenge/bonus-6/?get=hehe`
2. ...


there are bunch of levels, i've got no time to explain all. you can see the solution in the source code:
[old-33]
```scripts/old-33.py
{% include_relative scripts/old-33.py %}
```



in the last stage, you need to run this, and the go to the URL+what the script prints
```
<?php
$ip = 'YOUR IP';
for($i=0;$i<=strlen($ip);$i++) $ip=str_replace($i,ord($i),$ip);
$ip=str_replace(".","",$ip);
$ip=substr($ip,0,10);
$answer = $ip*2;
$answer = $ip/2;
$answer = str_replace(".","",$answer);

echo "answerip/{$answer}_{$ip}.php"

?>
```


(this works for me, assume we don't have the same ip it won't work for you)
`https://webhacking.kr/challenge/bonus-6/answerip/28287759875_5657551975.php`

