---
layout: default
title: level23
---

In this challenge there is a maze we need to solve and reach the cell where it holds `E`.

However, as we can see, there is no such cell:
```php
// $this->maze[$this->max_x-2][$this->max_y-1] = 'E';                   # There is no exit! Muhahahah

```

So, we the code we gives going through this `checkCode`:
```php
function checkCode($code) {
    $whitelist = array(" solve", " foreach", " if", ">print_maze", ">move", ">is_wall");
    $blacklist = array("`", "include", "require", "\/\/", "#");
    $code = preg_replace("/(\s|\r|\n|\t)/", " ", $code);  # remove whitespaces
    preg_match_all("/(.(\w|_|#|[\x7f-\xff]|}|\/|\])+)[\s\t\r\n]*\(/", $code, $f);

    for ($i=0; $i<count($f[0]); $i++) {  # check if functions are in the whitelist
        $function = $f[1][$i];
        if (!in_array($function, $whitelist)) {
            return true;
        }
    }
    foreach ($blacklist as $b) {  # baclisted functions
        if(preg_match("/($b)/i", $code, $m)) {
            return true;
        }
    }
    for ($i=0; $i<strlen($code); $i++) {
        if (ord($code[$i])>0x7e || ord($code[$i])<0x20) {  # only printable chars
            return true;
        }
    }

    return false;
}
```

And after, is going to eval
```php
eval("class Player {\n$code\n}");
```

The problem is that we can use only specific functions. In addition, it blacklist `require` and `include`.

We need to somehow escape the sandbox, and read `$flag` which is found in `flag.php`. 

Other method will be is to execute the `flag()` function, the problem is we can't use functions which isn't one of: `array(" solve", " foreach", " if", ">print_maze", ">move", ">is_wall");`



**Flag:** ***`WEBSEC{}`*** 
