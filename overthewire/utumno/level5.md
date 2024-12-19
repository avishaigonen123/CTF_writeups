# utumno level5 Solution

first we can see there is no protection, and also ASLR disabled.
![image](./images/level5_1.png)

in this level we do buffer overflow, but we also need to pass one check, this check:
![image](./images/level5_2.png)
check that the len of the buffer answer on specific rule.

here you can find the shellcode [shellcode.py](./general/shellcode.py)

this is the solution [level5.py](./scripts/level5/level5.py), you need to change the address of the shellcode based on the address of your environment variable.

![image](./images/level5_3.png)

**Flag:** ***`vY134qxapL`*** 