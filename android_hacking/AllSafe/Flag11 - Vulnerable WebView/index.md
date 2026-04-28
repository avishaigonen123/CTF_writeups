---
layout: default
title: Flag11 - Vulnerable WebView
---

Let's first have a look at the challenge:

![400](images/index.png)

For the first task, let's try to give xss payload, like `<script>alert()</script>`:

![400](images/index-1.png)

Let's try to access some file, using `file:///etc/hosts`:

![400](images/index-2.png)

It worked because there are so many flags that are set to true:

![](images/index-3.png)

