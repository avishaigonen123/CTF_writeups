# Bandit Level 21 Solution

```
bandit20@bandit:~$ cd $(mktemp -d)
bandit20@bandit:/tmp/tmp.Ym77rUbO5F$ cat > my_script.sh
#!/bin/bash

while true; do
        cat /etc/bandit_pass/bandit20 | nc -l localhost 1900
done
^C
bandit20@bandit:/tmp/tmp.Ym77rUbO5F$ chmod +x my_script.sh
bandit20@bandit:/tmp/tmp.Ym77rUbO5F$ ./my_script.sh &
[1] 50989
bandit20@bandit:/tmp/tmp.Ym77rUbO5F$ ~/suconnect 1900
Read: 0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO
Password matches, sending next password
EeoULMCra2q0dSkYj561DX7s1CpBuOBt
```

**Flag:** ***`EeoULMCra2q0dSkYj561DX7s1CpBuOBt`*** 

