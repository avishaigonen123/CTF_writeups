import requests

url = "https://webhacking.kr/challenge/js-2/?getFlag"

response = requests.get(url)                                

print(response.text)

    