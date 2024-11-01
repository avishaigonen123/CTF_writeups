# Bandit Level 6 Solution

## one solution:
```
bandit5@bandit:~/inhere$ cat $(find . -type f -size 1033c)
HWasnPhtq9AVKe0dmk45nxy20cvUa6EG
```

## second solution:
search for files with strings in the length of 32.

```
bandit5@bandit:~/inhere$ grep -rEa '^.{32}$' ./*
./maybehere07/.file2:HWasnPhtq9AVKe0dmk45nxy20cvUa6EG
```

**Flag:** ***`HWasnPhtq9AVKe0dmk45nxy20cvUa6EG`*** 

