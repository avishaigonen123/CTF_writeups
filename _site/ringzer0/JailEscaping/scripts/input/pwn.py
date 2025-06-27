#!/usr/bin/python3
import subprocess
import sys

program = "/tmp/input_sol/input"

process = subprocess.Popen(program, stdin=subprocess.PIPE)

# Example: Send input to the program if necessary

# seed = b"your_input_here\n"
# process.stdin.write(seed)
# process.stdin.flush()
# Wait for the program to finish and capture the output
# stdout, _ = process.communicate()  # Capture the output and error

# Output results
# print(stdout.decode(errors="replace"))  # Decode the output (handling errors gracefully)

input()
sys.stderr.buffer.write(b"\x00\x0a\x02\xff")

process.stdin.write(b"\x00\x0a\x00\xff")
process.stdin.flush()

# sys.stderr.buffer.flush()

# x = input()

# process.kill()  # Kill the process after completing
