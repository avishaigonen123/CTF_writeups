---
layout: default
title: level21
---

It looks like `encryption` CTF. 

```php
function create_cookies($username,$password,$key) {
    $iv = mcrypt_create_iv (16, MCRYPT_RAND);
    $plain = 'user/pass:' . $username . '/' . $password;

    $session = bin2hex ($iv).bin2hex (mcrypt_encrypt (MCRYPT_RIJNDAEL_128, $key, $plain, MCRYPT_MODE_CBC, $iv));
    setcookie ("session", $session, time () + 60*1000*15);  // cookies are valid for 15 minutes
}
```

This function seams the be vulnerable, i saw `mcrypt_encrypt` is depricated, I'm quite sure this is the attack vector: [CBC bit flipping attack](https://masterpessimistaa.wordpress.com/2017/05/03/cbc-bit-flipping-attack/).

The idea i thought of is using this `flipping byte` method, to achieve `SQL Injection`, as you can see this is the source code:
```php
function auth($session, $key) {
    $iv = hex2bin (substr ($session, 0, 32));
    $ciphertext = hex2bin (substr ($session, 32));

    /* Strip the "\0" padding */
    $session = rtrim (mcrypt_decrypt (MCRYPT_RIJNDAEL_128, $key, $ciphertext, MCRYPT_MODE_CBC, $iv), "\0");

    if (strpos($session, ":") > 0 && substr ($session, 0, strlen ('user/pass')) === 'user/pass') {
        $session = explode (":", $session)[1];
        if (strpos ($session, "/") > 0) {
            list($username, $password) = explode("/", $session);
        } else {
            die("The session is corrupted!");
        }
    } else {
        die("The session is  corrupted!");
    }

    if (verify_credentials ($username, $password)) {
        return $username;
    } else {
        die ("Wrong login or password.!");
    }
}

function verify_credentials($username, $password) {
    global $aes_key;
    $pdo = new SQLite3 ('database.db', SQLITE3_OPEN_READONLY);

    $result = $pdo->query("SELECT * FROM users WHERE username='$username' AND password='$password';");
``` 

As you can see here, we can achieve `SQL Injection`:
```php
$result = $pdo->query("SELECT * FROM users WHERE username='$username' AND password='$password';");
```

I tried to build it using this code, I did manage to achieve `SQL Injection`, but I'm stuck on how to achieve `admin` exactly.

The problem is that we need the `\`, need to think more on this challenge... :|
```py
{% include_relative scripts/level21.py %}
```

**Flag:** ***`PLACE_HOLDER`*** 
