---
layout: default
title: level16
---

In this challenge we need to somehow achieve same `HMAC` from one of the list, and then achieve our `RCE` using the `eval`.

This is the relevant code:
```php
$hmac = hash_hmac ('md5', $flag, $t);
$hmac1 = "b48dad7ab306a220186e32e27c3d600c";  // sample 1
$hmac2 = "0f8f2139cbdc4319a0c27d10dbea021a";  // sample 2
$hmac3 = "bab3493782947288bd5bce96f658066c";  // sample 3

if ($n > 64) {  /* Please don't kill the box. */
    $text = "The number <strong>$n</strong> is too big.";
} elseif (in_array ($hmac,  [$hmac1, $hmac2, $hmac3])) {
        $prime_test = '
        $primes = "<code>fib($n)</code> and <code>fib($n+2)</code> are <strong>not</strong> relative primes.";
        if (gcd (fib ($n), fib ($n+2) ) != 1 ) /* Check if F_N and F_(N+2) are relative primes. */
        {
            $primes = "<code>fib($n)</code> and <code>fib($n+2)</code> <strong>are</strong> relative primes.";
            $primes .= "<br><br>";
            $primes .= "Here is your flag: <mark>" . $flag . "</mark>";
        }';
    eval ($t . $prime_test);
}
```

As you can see in this line, it uses `$t` which is the input, as the key, while the `$flag` is the message.
In addition, it uses `md5` which has collisions.
```php
$hmac = hash_hmac ('md5', $flag, $t);
```

Now, I believe there is some attack, I've found this blog:
https://dankaminsky.com/2015/05/07/the-little-mac-attack/

and also this paper:
[The Dangerous Message/Key Swap in HMAC](https://cascade-conference.org/Paper/CASCADE25/final-versions/cascade2025-cycleB/cascade2025b-final15.pdf)

Just need to analyze it and use it.

**Flag:** ***`PLACE_HOLDER`*** 
