import requests
import time


URL = "https://webhacking.kr/challenge/web-19/"
SESSION_ID = "123"
cookies = {'PHPSESSID':SESSION_ID}
# params ={'val':"b UNION database()", 'answer':''}
# while True:
filename = "asd"*1000
files = {'up':(f'{filename}','jn')}
# files['upfile'] = "hello:("

response = requests.post(URL, files=files, cookies=cookies)
print(response.text)

