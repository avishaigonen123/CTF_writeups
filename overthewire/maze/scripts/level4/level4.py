import sys
from pwn import *

payload = b'#!./code\n'
payload += b'A'*(12-len(payload))

var_a4h = payload[7]*payload[8] 
payload += p32(var_a4h)

sys.stdout.buffer.write(payload)
