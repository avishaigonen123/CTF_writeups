#!/usr/bin/python3
from pwn import *
import socket

HOST = 'vortex.labs.overthewire.org'
PORT = 5842

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((HOST, PORT))
print("Connection established.")

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
