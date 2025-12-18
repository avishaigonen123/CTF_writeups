import string

charset = string.ascii_letters + string.digits
secret = "0522202f33600b013a371412191537255e0e3f2010041f67223d26143c16231e146436231222263e"
xored_flag = bytes.fromhex(secret)

# known plaintext
plain = "THM{"

# recover first 4 key bytes
key = [None]*5
for i in range(4):
    key[i] = chr(xored_flag[i] ^ ord(plain[i]))

print("Recovered first 4 chars of key:", "".join(key[:4]))

# brute force only the 5th character
for k4 in charset:
    key[4] = k4
    key_str = ''.join(key)

    flag = ""
    for i in range(len(xored_flag)):
        flag += chr(xored_flag[i] ^ ord(key_str[i % 5]))

    if flag.startswith("THM{") and flag.endswith("}"):
        print("\nFound key:", key_str)
        print("Decoded flag:", flag)
        break
