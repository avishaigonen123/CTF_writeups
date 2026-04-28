---
layout: default
title: Flag4 - Insecure Shared Preferences
---

Let's first have a look at the challenge:

![400](images/index.png)

When we look at the code, we can see it saves the credentials in none encrypted shared preferences:

![](images/index-1.png)

We can find this file in the internal storage of the application, the filename is `user.xml`:

![](images/index-2.png)

