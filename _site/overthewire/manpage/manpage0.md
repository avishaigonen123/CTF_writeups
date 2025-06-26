# manpage level0 Solution

in this level we exploit the fact it uses setuid32 bit, and not setuid16 bit. so, using the shellcode [shellcode.py](./scripts/level0/shellcode.py) and giving the right `shellcode_address` we can solve the stage, [level0.py](./scripts/level0/level0.py)

![image](./images/level0.png)

**Flag:** ***`oiRJLfkGyb`*** 
