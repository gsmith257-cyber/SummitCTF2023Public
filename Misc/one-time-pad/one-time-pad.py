import random

guide1 = random.randrange(0, 4294967295)
guide2 = random.randrange(0, 4294967295)
flag = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
pad = (guide1*guide2)**2
f = [ord(i) for i in flag]
cipher = []
for i in range(len(flag)):
    cipher.append(f[i] ^ int(str(pad)[i]))
print(cipher) # [80, 112, 107, 111, 111, 116, 66, 80, 67, 122, 118, 104, 105, 102, 51, 104, 44, 56, 116, 40, 110, 50, 117, 41, 125, 84, 113, 53, 51, 125, 41, 117, 104, 77, 108, 48, 101, 121]
