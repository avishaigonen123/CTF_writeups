---
layout: default
title: natas27
---

As we can see, the username size is 64 chars.
```sql
CREATE TABLE `users` (
  `username` varchar(64) DEFAULT NULL,
  `password` varchar(64) DEFAULT NULL
);
```

When we create user, it checks whether i give spaces at the begin \ end
```php
if($usr != trim($usr)) {
        echo "Go away hacker";
        return False;
    }
```

And if not, it'll insert the username and password, but with `substr` of 64 chars 
```php
$user=mysqli_real_escape_string($link, substr($usr, 0, 64));    
```

By this way, we can insert for example:
`'natas28'` + `' '`*57 + `'a'`, which after `substr` leave us with `natas28` and a lot of spaces... however, this is the same as `natas28`. 
Then, we manage to inject our own user `natas28`, with blank password for example, and then when asking for `natas28` + `' '`*57, we get the flag :)  

It works because the check using `trim` working only in `createUser` and not in `checkCredentials`


**Flag:** ***`1JNwQM1Oi6J6j1k49Xyw7ZN6pXMQInVj`*** 