---
layout: default
title: level21
---

It looks like `encryption` CTF. 
This function seams the be vulnerable, i saw `mcrypt_encrypt` is depricated, maybe this PoC is relevant [PoC: Attack Against PHP Crypto](https://gist.github.com/defuse/0822a9c6d70ab4939c95)
```php
function create_cookies($username,$password,$key) {
    $iv = mcrypt_create_iv (16, MCRYPT_RAND);
    $plain = 'user/pass:' . $username . '/' . $password;

    $session = bin2hex ($iv).bin2hex (mcrypt_encrypt (MCRYPT_RIJNDAEL_128, $key, $plain, MCRYPT_MODE_CBC, $iv));
    setcookie ("session", $session, time () + 60*1000*15);  // cookies are valid for 15 minutes
}
```


**Flag:** ***`WEBSEC{}`*** 
