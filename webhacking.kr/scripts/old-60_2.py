import requests
# import hashlib
import time


URL = "https://webhacking.kr/challenge/web-37/"
SESSION_ID = "1234"
cookies = {'PHPSESSID':SESSION_ID}
params ={'mode':'auth'}

while True:

    response = requests.get(URL, cookies=cookies)
    print(response.text)

