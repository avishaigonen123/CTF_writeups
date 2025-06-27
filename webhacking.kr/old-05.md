---
layout: default
title: old-05
---

# webhacking old-05 Solution

as we can see, the login page redirects us to `./mem/login.php`. so, there might be also `./mem/join.php`. we will go there:
```https://webhacking.kr/challenge/web-05/mem/join.php``` 

in this page there is js obfuscated, let's use some online tool like https://beautifier.io/ and achieve more nice looking code. 
here is the source code: [old-05]
```scripts/old-05.js
{% include_relative scripts/old-05.js %}
```



after research the code, we come to conclusion that there need to be a cookie with the name `oldzombie`, and also, we need to set the param `mode` to 1.
so, `https://webhacking.kr/challenge/web-05/mem/join.php?mode=1`

now, let's add this user:
username: ` admin`
password: `123`

i added space in purpose, this is part of the challenge.
finally, let's go back to the login page and insert those credentials.