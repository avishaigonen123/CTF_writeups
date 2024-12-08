from pwn import *

PATH = '/behemoth/behemoth0'
password = "eatmyshorts"


p = process(PATH)
p.sendline(password.encode())
p.interactive()

p.close()
