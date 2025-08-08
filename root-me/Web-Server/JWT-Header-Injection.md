---
layout: default
title: JWT-Header-Injection
---

Here we can get this `jwt token`, with contain the payload of `Trinity`.
```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiVHJpbml0eSIsIm1lc3NhZ2UiOiJXYWtlIHVwIE5lbywgZm9sbG93IHRoZSB3aGl0ZSByYWJiaXQuIiwiaWF0IjoxNjc2NjM3ODMyfQ.eYekblLchhHS8F9kMjW6F9oiBIC0wlHmPHR1jiw-rD4JoQ8gpgih5RlonFBKVoippF12zRJIgAs8yGUkBMYHSQ
```

The name of the lab suggests this is `header injection` attack, when I inject the key the server would verify with, and then can send whatever payload I want.

So, first let's create our pair of `RSA256` kets
As you can see, it uses `RSA` inside `JWT editor` tab.
![jwt editor](./images/JWT-Header-Injection_jwt_editor.png)

Then, we will change to `New` and choose the attack of `Embedded JWK`
![jwt attack](./images/JWT-Header-Injection_attack.png)

And this is the flag we got
![FINAL](./images/JWT-Header-Injection_FINAL.png)

**Flag:** **_`RM{N3v3r_All0w_UnTrusTed_K3ys}`_**
