import sys

NOP_SLIDE = 50

# print = lambda *args, **kwargs: None # override print function


# Shellcode in Python
# write(1, "HelloKitty", 11)
shellcode = (


    # mov	ecx,msg		; message to write
    b"\x31\xd2"  # xor edx, edx
    b"\x52"      # push edx, which is \0
    b"\x68\x69\x74\x74\x79"      # push "itty"
    b"\x68\x6c\x6c\x6f\x4b"      # push "lloK"
    b"\x68\x0a\x0a\x48\x65"      # push "He"
    b"\x83\xc4\x02" #  add esp, 2 
    b"\x89\xe1"  # mov ecx, esp (now ecx contains: "HelloKitty",\x00)

    # mov	ebx,1		; file descriptor (stdout)
    b"\x6a\x01"  # push 1
    b"\x5b"      # pop ebx

    # mov	edx,12		; message length (+1s)
    b"\x6a\x0c"  # push 11, in this challange i mustn't use '0xb'
    b"\x5a"      # pop edx
    
    # mov	eax,4		; system call number (sys_write)
    b"\x6a\x04"  # push 4
    b"\x58"      # pop eax (sys_write)
    # int 0x80
    b"\xcd\x80"  # int 0x80 (write(1, "HelloKitty", 11))

    # mv eax, 1         ; system call number (sys_exit)
    b"\x6a\x01"  # push 1
    b"\x58"      # pop eax (sys_exit)
    # int 0x80
    b"\xcd\x80"  # int 0x80 (exit())



)

# Print shellcode details
print("Shellcode code is:")
print("write(1, \"HelloKitty\", 11)")

# Print shellcode with NOP slide
print("\nShellcode as formatted string:")

# Add NOP slide (\x90) before shellcode
nop_slide = b"\x90" * NOP_SLIDE
formatted_shellcode = nop_slide + shellcode

# Convert to formatted string
print("".join(f"\\x{byte:02x}" for byte in formatted_shellcode))

# Print shellcode in hex format
print("\nShellcode in hex format:")
print("".join(f"{byte:02x}" for byte in formatted_shellcode))

# Calculate shellcode length
print(f"\nLength of shellcode is {len(formatted_shellcode)} bytes")

# sys.stdout.buffer.write(formatted_shellcode)
