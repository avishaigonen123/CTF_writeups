# vortex level8 Solution

in this level we can use buffer overflow to inject our code
![image](./images/level8_1.png).

the safe function below:
![image](./images/level8_2.png).

while the unsafe function:
![image](./images/level8_3.png).

as you can see we can use buffer overflow to inject our code, however, the code drops our privileges before execute the unsafe function. 

we will modify the `plt_print` and then, in the safe code which runs with the higher privileges, we will execute our shellcode.

this will be our shellcode that'll be in the return address of the unsafe function:
```
mov eax, plt_printf_address
mov ebx, shellcode_address
mov [eax], ebx

push 1
pop eax 
int 0x80  => exit()
```

so, we only need to find `plt_printf_address` and `shellcode_address`, and put them in the code [shellcode.py](./scripts/level8/shellcode.py)

after generating the shellcode, we need to modify the address of the shellcode and put it in the return address of the unsafe function, which will do using [level8.py](./scripts/level8/level8.py).
so, modify `shellcode_address`, and execute those lines:

![image](./images/level8_4.png).

**Flag:** ***`hCuwrgfqn`***