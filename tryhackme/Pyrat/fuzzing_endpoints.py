#!/usr/bin/env python3
import socket

TARGET = "10.10.53.13"
PORT = 8000
WORDLIST_PATH = "/usr/share/SecLists/Discovery/Web-Content/common-api-endpoints-mazen160.txt"
SOCKET_TIMEOUT = 1.0

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(SOCKET_TIMEOUT)
try:
    s.connect((TARGET, PORT))
    i = 1
    with open(WORDLIST_PATH, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            word = line.strip()
            if not word:
                continue
            try:
                s.sendall((word + "\n").encode())
            except Exception:
                break
            try:
                data = s.recv(4096)  # read but do nothing with it
                if not (b"is not defined" in data or b"(<string>, line 1)" in data or data==b'\n'):
                    print(f"{word} -> {data.decode()}")
                if not data:
                    break
                if i%100 == 0:
                    print(i)
                i+=1
            except socket.timeout:
                pass
            except Exception:
                break
finally:
    try:
        s.close()
    except Exception:
        pass
