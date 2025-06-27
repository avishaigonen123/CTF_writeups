---
layout: default
title: bandit32
---




```
bandit31@bandit:~$ cd $(mktemp -d)
bandit31@bandit:/tmp/tmp.tKq7o6Kk2U$ git clone ssh://bandit31-git@localhost:2220/home/bandit31-git/repo

bandit31@bandit:/tmp/tmp.tKq7o6Kk2U$ cd repo
bandit31@bandit:/tmp/tmp.tKq7o6Kk2U/repo$ cat > key.txt
May I come in?
^C
bandit31@bandit:/tmp/tmp.tKq7o6Kk2U/repo$ cat README.md
This time your task is to push a file to the remote repository.

Details:
    File name: key.txt
    Content: 'May I come in?'
    Branch: master

bandit31@bandit:/tmp/tmp.tKq7o6Kk2U/repo$ git add -f *
bandit31@bandit:/tmp/tmp.tKq7o6Kk2U/repo$ git commit -m "my commit"
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
bandit31@bandit:/tmp/tmp.tKq7o6Kk2U/repo$ git push

...

remote: .oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.
remote:
remote: Well done! Here is the password for the next level:
remote: 3O9RfhqyAlVBEZpVb6LYStshZoqoSx5K
remote:
remote: .oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.
remote:
```


**Flag:** ***`3O9RfhqyAlVBEZpVb6LYStshZoqoSx5K`*** 

