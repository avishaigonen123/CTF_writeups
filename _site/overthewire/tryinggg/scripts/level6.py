import socket

HOST = '127.0.0.1'  
PORT = 1337         

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

while True:
    try:
        data = sock.recv(1024) 
        print(f"Received: {data.decode('utf-8')}")
        break
    except Exception as e:
        print(f"An error occurred: {e}")
