#!/usr/bin/python3
import subprocess
import sys
import time

program = "/home/lotto/lotto"

process = subprocess.Popen(program, stdin=subprocess.PIPE)

for i in range(1,46):

    submit = bytes([i] * 6)
    print("\ni = {}\n".format(i))
    input()
    
    process.stdin.write(b'1')
    process.stdin.flush()

    process.stdin.write(submit)
    process.stdin.flush()
