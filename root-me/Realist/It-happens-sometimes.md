---
layout: default
title: It-happens-sometimes
---
We can see this home page.

![](It-happens-sometimes.png)

The mission is to access the administartion section of the website, I tried to go to `/admin`, and got this basic auth pop window:

![](It-happens-sometimes-1.png)

![](It-happens-sometimes-2.png)

I tried my luck with `HTTP Verb Tampering`, which means changing the http method in the request, and it worked

![](It-happens-sometimes-3.png)

The reason is because the developer didn't gave use case for this, he checks if this is `GET` or `POST`, and then send to authentication. Otherwise, he just pass it without auth.

The password is **0010110111101001**.
