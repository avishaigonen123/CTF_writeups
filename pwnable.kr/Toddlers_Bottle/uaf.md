---
layout: default
title: uaf
---



here we exploit the fact we delete Man and Woman, and manage to put our code inside the grave of Man and Woman.
Then, when we'll call it's introduce function, it will execute shell.

```python
{% include_relative scripts/uaf/payload.py %}
```


we will give as input this values:
```
3 (for free)
2 (for put our payload once)
2 (for put our payload twice)
1 (for calling "introduce")
```

![image](./images/uaf.png)

**Flag:** ***`yay_f1ag_aft3r_pwning`***
