---
layout: default
title: Resources
---
First, this is the challenge:

![400](images/index.png)
This is the code of the `submitFlag` function: 

![](images/index-1.png)

We can see it compare the string we input, with the value of the key `cmVzb3VyY2VzX3lv`.

We can find the value inside `res/values/strings.xml`:

![](images/index-2.png)

So, the flag is: **`F1ag_thr33`**.

Another way will be to use `frida`, same as we did [Login](../Login/index.md)