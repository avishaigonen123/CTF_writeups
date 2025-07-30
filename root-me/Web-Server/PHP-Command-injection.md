---
layout: default
title: PHP-Command-injection
---

Here, i injected my command. i guess it do something like: `system('ping ' . '$user_input')`, so, i simply gave this as user_input: `127.0.0.1 && cat index.php`, and saw the password

Then, i saw this line in the resposne:
```php
$flag = "".file_get_contents(".passwd")."";
```

So, i sent this payload: `127.0.0.1 && cat .passwd` (to read the flag)

**Flag:** ***`S3rv1ceP1n9Sup3rS3cure`***
