import requests


URL = "https://webhacking.kr/challenge/web-37/"
SESSION_ID = "1234"
cookies = {'PHPSESSID':SESSION_ID}

params ={'mode':'auth'}
while True:
    response = requests.get(URL, params=params, cookies=cookies)

    print(response.text)

