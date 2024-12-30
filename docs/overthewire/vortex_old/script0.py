import socket
import struct
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 5842
host = 'vortex.labs.overthewire.org'

s.connect((host,port))
print("socket successfuly connected")

integers = []
for _ in range(4):
  data = s.recv(4)
  val = struct.unpack('<I', data)[0]
  integers.append(val)
total = sum(integers)
print("Received integers:", integers)
print("Sum of integers:", total)

# Send the result back
s.sendall(struct.pack("<I", total))

# Receive username and password
content = s.recv(1024).decode()

print(content)
