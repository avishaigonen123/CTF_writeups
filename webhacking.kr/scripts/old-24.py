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

response = requests.post(URL,data=data, cookies=cookies)
print(response.text)

    
