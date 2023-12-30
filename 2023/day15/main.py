from utils import HashMap


with open("input", "r+") as file:
    line = file.read().strip()

##### Part 1 #####
hash = HashMap(line)
result = hash.GetSumLineHash()
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
result = hash.GetBoxesFocusPower()
print(f"[+] Answer of part 2: {result}")
