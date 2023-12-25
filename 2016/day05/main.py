import hashlib
import os

with open("input") as file:
    key = file.readline().strip()

##### Part 1 #####
i = 0
password = ""
print(f"Finding password for key = {key}")
for _ in range(8):
    while True:
        i += 1
        string = key+str(i)
        digest = hashlib.md5(string.encode()).hexdigest()
        if digest.startswith("00000"):
            print(f"One letter found: {digest[5]}")
            password += digest[5]
            break

part1 = password
print(f"Answer of part 1: {part1}")

##### Part 2 #####
i=0
password = ['_']*8
print(f"Password: {' '.join(password)}")
while True:
    i += 1
    string = key+str(i)
    digest = hashlib.md5(string.encode()).hexdigest()
    if digest.startswith("00000"):
        idx = digest[5]
        if idx.isalpha(): continue
        idx = int(idx)

        if idx >= len(password) or password[idx] != '_': continue
        password[idx] = digest[6]

        os.system('clear')
        print(f"Password: {' '.join(password)}")

        if password.count('_') == 0:
            break

print(f"Answer of part 1: {part1}")
print(f"Answer of part 2: {''.join(password)}")
