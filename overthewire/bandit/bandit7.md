# Bandit Level 7 Solution

```
bandit6@bandit:~$ ls -l $(find / -type f -size 33c 2> /dev/null) | grep "bandit7 * bandit6"
ls: cannot access '/home/bandit2/spaces': No such file or directory
ls: cannot access 'in': No such file or directory
ls: cannot access 'this': No such file or directory
ls: cannot access 'filename': No such file or directory
-rw-r----- 1 bandit7     bandit6     33 Sep 19 07:08 /var/lib/dpkg/info/bandit7.password
bandit6@bandit:~$ cat /var/lib/dpkg/info/bandit7.password
morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj
```

**Flag:** ***`morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj`*** 

