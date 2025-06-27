---
layout: default
title: natas16
---



here we inject this payload: 
`$(grep -E ^{password} /etc/natas_webpass/natas17)African`.
if the password is in the file, so the word ??African won't be in the dictionary.
here we do brute force, the source code is here [level16]
```python
{% include_relative scripts/level16.py %}
```



**Flag:** ***`EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC`*** 