---
layout: default
title: HTTP-Directory-indexing
---

I first checked the source code and found this line:
`<!-- include("admin/pass.html") -->`
So, i tried to go there, and got this:
```
Got a rick rolled? ;)
Don't worry, you're not the last :p

Just search
```

From the name of the level, I guessed directory indexing is enabled, let's try to go to `http://challenge01.root-me.org/web-serveur/ch4/admin/`.
There, we can see a directory `backup`, and in this directory, we can find `admin.txt`, which has this:
`Password: LINUX`

**Flag:** ***`LINUX`***
