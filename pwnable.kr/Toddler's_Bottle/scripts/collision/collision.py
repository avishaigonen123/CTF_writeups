#!/usr/bin/python3 
import sys
import struct

def p32(x):
    return struct.pack("<I", x)

hashcode = 0x21DD09EC

junk = 0x01010101

payload = p32(junk)
payload += p32(junk)
payload += p32(junk)
payload += p32(junk)
payload += p32(hashcode - 4 * junk)

sys.stdout.buffer.write(payload)
