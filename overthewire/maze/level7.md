# maze level7 Solution

i decompiled maze 6, here you can see the source code.

![image](./images/level7_1.png)

in this challenge we use buffer overflow to override the file.
we make our own File* struct, and put there in the write buffer our address, the address of the exit function in plt, and then we'll write there the shellcode.

* this is a regular FILE* struct, when we open `file` for writing.
* the words i marked are: *_IO_write_base*, *_IO_write_ptr*, *_IO_write_end*
![image](./images/level7_2.png)

* we need to find the address of exit in the plt record
![image](./images/level7_3.png)
![image](./images/level7_4.png)
so, the address of exit function in plt is `0x0804b208`

* we need to inject our shellcode and find its address, we need to find the address of our malware FILE* struct.
![image](./images/level7_5.png)
we can see that the address of shellcode is `0xffffd204` and address of our malware FILE* struct `0xffffd158`

for summary, we need to find this values:
```
FILE_struct_address  = 0xffffd158
plt_exit_address = 0x0804b208
shellcode_address = 0xffffd204
```
the code can be found here [level7.py](./scripts/level7.py)

![image](./images/level7_6.png)

s**Flag:** ***`B6XkM3Syq6`*** 
