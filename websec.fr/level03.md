---
layout: default
title: level03
---

In this challenge, we use the fact someone wrote `fa1se` instead of `false`, and by this exploit the vulnerability that can be shown here
[null vulnerability in password verify php](https://github.com/nette/security/issues/14#issuecomment-80114475), and also here [more detailed](https://github.com/php/php-src/security/advisories/GHSA-h746-cjrr-wfmr).

this is the source code
```php
$h2 = password_hash (sha1($_POST['c'], fa1se), PASSWORD_BCRYPT);

    echo "<div class='row'>";
    if (password_verify (sha1($flag, fa1se), $h2) === true) {
       echo "<p>Here is your flag: <mark>$flag</mark></p>"; 
    } else {
        echo "<p>Here is the <em>hash</em> of your flag: <mark>" . sha1($flag, false) . "</mark></p>";
    }
```

As you can see, he wrote `fa1se` twice, and this means that the `sha1` function returns *raw* bytes, while in the third occournce of `sha1`, he wrote `false`, in this returns the hash in hex. This it the hash of the flag we got: `7c00249d409a91ab84e3f421c193520d9fb3674b`.

As we can see, the second byte is null, so, if we will manage to create some password, that it looks like `7c00....`, we can bypass the check!
Here is a little PoC i made, [online PoC](https://3v4l.org/lHtim).

Our short python script:
```py
{% include_relative scripts/level03.py %}
```

The password we will input is: `CWM`

**Flag:** ***`WEBSEC{Please_Do_not_combine_rAw_hash_functions_mi}`*** 
