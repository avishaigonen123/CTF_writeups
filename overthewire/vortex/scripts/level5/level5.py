import itertools
import string
from hashlib import md5
import time


desired_hash = b"\x15\x5f\xb9\x5d\x04\x28\x7b\x75\x7c\x99\x6d\x77\xb5\xea\x51\xf7"

# Check if a given password matches the desired hash
def checkguess(password):
    guess_hash = md5(password.encode()).digest()
    return guess_hash == desired_hash


print("Brute-forcing started...")
start = time.time()

cnt = 0
for guess in itertools.product('r' + string.ascii_letters+string.digits, repeat=5):
    cnt += 1
    if checkguess(''.join(guess)):
        print("Password is: {0}".format(''.join(guess)))
        break
    if cnt % 10000000 == 0:
        print("Checked {0} passwords, guess is {1}".format(cnt, ''.join(guess)))

end = time.time()
print("Brute-forcing ended...")

print("Time taken: {0:.2f} seconds".format(end - start))
