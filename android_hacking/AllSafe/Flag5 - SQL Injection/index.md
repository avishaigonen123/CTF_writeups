---
layout: default
title: Flag5 - SQL Injection
---

Let's first have a look at the challenge:

![400](images/index.png)

It tried this payload as username `a' or '1'='1' -- -`:

![400](images/index-1.png)
We can see we actually got logged in as `admin`, and got the password which looks like some hash.

