from utils import Hash


with open('input', 'r+') as file:
    line = file.read().strip()

##### Part 1 #####
hash = Hash(line)
result = hash.GetSumLineHash()
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####

print(f"[+] Answer of part 2: {result}")