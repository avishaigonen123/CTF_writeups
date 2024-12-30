import requests
import base64
from urllib.parse import unquote, quote
import binascii


def string_to_hex(s):
    return ''.join(format(ord(char), '02x') for char in s)

# def check_session(i):
URL = "http://natas28.natas.labs.overthewire.org"
auth_username = "natas28"
auth_password = "1JNwQM1Oi6J6j1k49Xyw7ZN6pXMQInVj"
headers = {"authorization": 'Basic {0}'.format(base64.b64encode((auth_username + ':' + auth_password).encode('utf8')).decode())}
data = {'query':''}


# first get the fake line, for afterwards
data['query'] = 'programmers'
response = requests.post(URL,data=data, headers=headers, allow_redirects=False)
param = response.headers.get('Location').split('=')[1]
response = requests.post(URL,data=data, headers=headers)
print(response.text)
