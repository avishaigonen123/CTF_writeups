---
layout: default
title: old-48
---

# Webhacking old-48 Solution

in this challenge there is command injection. when we delete file, it runs this command: `rm -rf $filename`

so, we need to upload file with this name for example: `file;ls`. Then, when we delete the file, it'll show us the flag.


**Flag:** ***`FLAG{i_think_this_chall_is_cool}`*** 

