---
layout: default
title: SQL-injection-authentication-GBK
---

`GBQ` is a chinese two bytes encoding. 
Also, when I tried to conduct simple `sqli` it doesn't work, probably it uses `addslashes` or other php function to escape all dangerous characters.

Let's look in this table [table gbk](https://www.khngai.com/chinese/charmap/tblgbk.php?page=0).

The character `刓` has the this hex value `845C`.

Let's think what will happen if we will give this as input, remember that `5C` is the value of `\`.

What will happen if we give `刓'  ` as input?

The string will look like: 
```
select password from users where login='刓' ' ...
``` 
And after escaping: 
```
select password from users where login='刓\' ' ...
```

However, because it uses `gbk` encoding, so in the SQL server it will treat it as: (not real `?`, rather different char, but we doesn't care as long it's not `\` or `'`)
```
select password from users where login='?\\' ' ...
```
And then, we got `Sql Injection`!.

our final payload: 
```
刓' or 1=1 -- 
```

**Flag:** ***`iMDaFlag1337!`***
