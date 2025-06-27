---
layout: default
title: maze0
---



in this level we exploit race condition.
first it checks access to a file, and then change to higher privileges and print the content of the file. 
so, we will link it to maze0 privilege, and before it opens the file for reading, we'll change to maze1 privilege.

```sh
{% include_relative scripts/level0/link_script.sh %}
```


```sh
{% include_relative scripts/level0/run_script.sh %}
```


then, we'll run this
```
./link_script.sh &
./run_script.sh | grep -av "maze0"
```

![image](./images/level1.png)

**Flag:** ***`kfL7RRfpkY`*** 
