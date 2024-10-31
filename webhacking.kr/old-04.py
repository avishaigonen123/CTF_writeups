import hashlib


with open("hash_dictionry.txt", 'w') as file:
    for i in range(10000000,99999999):
        data = (str(i)+"salt_for_you")
        hashed_data = data
        for num in range(500):  
            hashed_data = hashlib.sha1(hashed_data.encode()).hexdigest()
        file.write(f"{i}salt_for_you: {hashed_data}\n")
