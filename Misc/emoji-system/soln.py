#!/usr/bin/env python3

from pwn import *
from z3 import *
import re

# Create regex to extract variables from the program
reg = re.compile(r'\((?P<c1>-?[0-9]+)\s*\*\s*(?P<v1>[^\x00-\x7F]+)\)\s*\+\s*\((?P<c2>-?[0-9]+)\s*\*\s*(?P<v2>[^\x00-\x7F]+)\)\s*\+\s*\((?P<c3>-?[0-9]+)\s*\*\s*(?P<v3>[^\x00-\x7F]+)\)\s*\=\s*(?P<ans>-?[0-9]+)')

# Connect to localhost on port 1337
p = remote('localhost', 1337)

# Skip the first line of input
p.recvline()

# Create a z3 solver
s = Solver()

# Read the next three lines of input
for i in range(3):
    line = p.recvline()
    m = reg.match(line.decode())
    if m is None:
        print("Error: Could not parse input")
        exit()
    else:
        c1 = int(m.group('c1'))
        c2 = int(m.group('c2'))
        c3 = int(m.group('c3'))
        ans = int(m.group('ans'))

        # Make v1, v2, and v3 into variables in z3
        v1 = Int('v1')
        v2 = Int('v2')
        v3 = Int('v3')

        # Create equation using the constants and variables
        s.add(c1 * v1 + c2 * v2 + c3 * v3 == ans)

# Create a dictionary of the variables and their values
vars = {'v1': 0, 'v2': 0, 'v3': 0}

# Print out each solved variable in the solver
assert(s.check() == sat)
for v in s.model():
    # Set the dictionary value to the variable value
    vars[v.name()] = s.model()[v].as_long()

# Send the answers back to the binary
p.sendline(str(vars['v1']).encode())
p.sendline(str(vars['v2']).encode())
p.sendline(str(vars['v3']).encode())

# Read the rest of the output and print it out
print(p.recvall().decode())