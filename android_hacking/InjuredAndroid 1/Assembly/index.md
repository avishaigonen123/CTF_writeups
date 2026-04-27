---
layout: default
title: Assembly
---
When we access the challenge, we can see this list:

![400](images/index.png)
I checked the source code of the `AssmebleActivity.java`:

![](images/index-1.png)

We can see here the `this.z`, which is used to display the encrypted list.

Let's check where it comes from:

![](images/index-2.png)

We can see this is native function from the file `libnative-lib.so`, let's load this file to *Ghidra*.

![](images/index-3.png)

The `win` string is very interesting, let's try it:

![400](images/index-4.png)