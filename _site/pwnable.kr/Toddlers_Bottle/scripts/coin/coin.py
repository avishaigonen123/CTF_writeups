from pwn import *
import re

def check(p, left, right):
    payload=  " ".join(map(str, range(left,right))) + '\n'
    p.send(payload)
    answer = p.recv().decode()
    if "Correct" in answer:
        print("coin is {}\n".format(payload))
        return -1

    answer_int = int(answer)
    # if answer_int==9:
    #     # p.send(payload)
    return answer_int/10 < (right-left)    

# Connection details
# host = 'pwnable.kr'
host = 'localhost'
port = 9007

# context.log_level = 'debug'

# Establish a remote connection
p = remote(host, port)

# p.recvuntil('- Ready? starting in 3 sec... -')
# p.recv() # get all begin data

# line = p.recv() # N=734 C=10

# # Regular expression to extract N and C values
# match = re.search(r'N=(\d+)\s+C=(\d+)', line.decode())

# if not match:
#     print("Could not extract N and C values from the received data.")
#     exit(1)

# N = int(match.group(1))  # Extract the first group (N)
# C = int(match.group(2))  # Extract the second group (C)
# # print(f"N={N}, C={C}")
# print("N={0}, C={1}".format(N,C))

# low = 0
# big = N
# binary search algorithm

p.recv() # get all begin data
# p.recv()

while True:
    line = p.recv() # N=734 C=10
    
    if "flag" in line.decode():
        print(line.decode())
        break

    # Regular expression to extract N and C values
    match = re.search(r'N=(\d+)\s+C=(\d+)', line.decode())

    if not match:
        print("Could not extract N and C values from the received data.")
        exit(1)

    N = int(match.group(1))  # Extract the first group (N)
    C = int(match.group(2))  # Extract the second group (C)

    print("N={0}, C={1}".format(N,C))
    left, right = 0, N - 1  # Initialize the search bounds
    
    while left <= right:
        mid = (left + right) / 2  # Find the midpoint
        res = check(p, left, mid)
        if res==-1: # Found first coin
            break 
        elif res==1: # Target in in left half
            right = mid+1
        else: # Target in right half
            left = mid



p.close()
# p.sendline('15')
# p.recv()
# p.sendline('92')

#  p.log("send values")

