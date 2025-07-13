---
layout: default
title: level09
---

Here we can upload our own `cache_file`, and then it being saved in `/tmp/hash`. We can calculate the hash, using `sha1(time())`, and by this way know where our payload will be.

Then, we can see it strip slashes from our file, and then eval'ing it.
```php
echo eval (stripcslashes (file_get_contents ($_GET['cache_file'])));
```

I created some payload in hex, and added more `\` before every slash, and by this way, after the removing the code will be running.

Our python script:
```py
{% include_relative scripts/level09.py %}
```

### For some reason, it doesn't working, i need to check why. I fill like the session create isn't working

**Flag:** ***`WEBSEC{}`*** 
