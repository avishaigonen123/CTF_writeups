---
layout: default
title: Flag3 - Firebase Database
---

Let's first have a look at the challenge:

![400](images/index.png)

Inside the source code, we can see it tries to access the path `/secret`, on the remote firebase:

![](images/index-1.png)

Let's find the url of the firebase, located at `/values/strings.xml`

![](images/index-2.png)

So, the full url is `https://allsafe-8cef0.firebaseio.com/secret.json`

![](images/index-3.png)

