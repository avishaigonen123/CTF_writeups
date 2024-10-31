import socket

sock = socket.socket()
sockets = []
host = "127.0.0.1"
port = 10000
for i in range(1000):
    sockets.append(socket.socket())
    sockets[i].bind((host, port+i))
    sockets[i].listen()

for i in range(1000):
    client, addr = sockets[i].accept()
    print(f"Connected by {addr}")
    print(client.recv(100))
    