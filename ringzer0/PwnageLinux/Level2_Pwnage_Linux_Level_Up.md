---
layout: default
title: Level2_Pwnage_Linux_Level_Up
---



here we need to give username: `nobody`, password: `Ksdkjkk32avsh`, and then in the command we can overflow the user and put there `root`.

```python
{% include_relative scripts/level2.py %}
```


the file I created is `my_script.sh`, it contains this:
```
#!/bin/bash
pass=$(cat /home/level3/.pass)
echo "Passowrd is: $pass"
```


Notice that we can't use chmod, so i used this: 
`perl -e 'chmod 0755, "my_script.sh"'`

![image](./images/level2.png)

**Flag:** ***`b130hOOfGftXUfmRZlgD`***
