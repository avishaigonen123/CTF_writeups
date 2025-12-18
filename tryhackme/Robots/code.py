import hashlib

target = "dfb35334bf2a1338fa40e5fbb4ae4753"
username = 'rgiskard'

for i in range(10000):
    pwd = f"{username}{i:04d}"
    h = hashlib.md5(pwd.encode()).hexdigest()
    h = hashlib.md5(h.encode()).hexdigest()
    if h == target:
        print("FOUND:", pwd)
        break
