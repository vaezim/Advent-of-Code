import hashlib

with open("input") as file:
    key = file.readline().strip()

##### Part 1 #####
i = 1
while True:
    string = key+str(i)
    digest = hashlib.md5(string.encode()).hexdigest()
    if digest.startswith("00000"):
        break
    i += 1

print(f"Answer of part 1: {i}")

##### Part 2 #####
i = 1
while True:
    string = key+str(i)
    digest = hashlib.md5(string.encode()).hexdigest()
    if digest.startswith("000000"):
        break
    i += 1

print(f"Answer of part 2: {i}")

