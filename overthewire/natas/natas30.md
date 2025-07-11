---
layout: default
title: natas30
---

I searched in google and faced some interesting results.
[sqli in quote perl function](https://security.stackexchange.com/a/175872)

Basiccaly, that's what it says:

> You see, param is context-sensitive. In scalar context, if the parameter has a single value (name=foo), it returns that value, and if the parameter has multiple values (name=foo&name=bar) it returns an arrayref. In list context, it returns a list of values, whether there are zero, one, or many. The argument list of a method (such as quote) is a list context. That means that someone using your app can cause quote to receive two values, and quote's optional second argument is an SQL data type that the first argument should be treated as. If the data type is a non-string type like NUMERIC, then quote will pass its first argument through without any quoting. This constitutes an opportunity for SQL injection. 
([is-perl-function-dbh-quote-still-secure](https://stackoverflow.com/a/40275686))

So, we'll supply this: 
`username='natas31'+--&username=4&password=pass`

Then, it will interpret username as `'natas31' --`, and then when it'll run the query
`Select * FROM users where username ='natas31' -- password ='pass'`
However, the `--` will comment the rest of the query...

**Flag:** ***`m7bfjAHpJmSYgQWWeqRE2qVBuMiRNq0y`*** 