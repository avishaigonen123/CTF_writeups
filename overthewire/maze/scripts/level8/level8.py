#!/usr/bin/python3
import socket

HOST = '127.0.0.1'
PORT = 1337

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.bind((HOST, PORT))

while True:
    try:
        sock.connect((HOST, PORT))  
        sock.send('god'.encode())

        print("Connection established")
        # data = sock.recv(1024)
        # print(f"Received: {data.decode('utf-8')}")
        break
    except Exception as e:
        pass
    # print(f"An error occurred: {e}")
