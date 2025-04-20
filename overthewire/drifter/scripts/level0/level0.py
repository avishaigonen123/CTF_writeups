# !/usr/bin/python3
from pwn import *
import socket
from arc4 import ARC4

HOST = 'drifter.labs.overthewire.org'
PORT = 1111


hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print(f"IP address: {ip_address}, Port: {PORT}")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((HOST, PORT))
print("Connection established.")


key = bytes(int(i) for i in ip_address.split('.')) + b'\x0b\x0b'
# print(f"Key: {key}")
arc4 = ARC4(key)

content = p32(1)*9# p32(0xdeadbeef) * 9
cipher = arc4.encrypt(content)
sock.send(cipher)

# print(cipher)
dat = sock.recv(4)
print(dat)
arc4 = ARC4(key)
res = arc4.decrypt(dat)
print(res)
print(int.from_bytes(res, 'little'))
'''
integers = []
for _ in range(4):
    dat = sock.recv(4)
    val = u32(dat)
    integers.append(val)

total = sum(integers)

print("Received integers:", integers)
sock.sendall(p64(total))
print(f"Data sent: {total}")
dat = sock.recv(1024)
print("Received data:", dat.decode())
'''