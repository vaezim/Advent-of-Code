from utils import Xmas


with open('input', 'r+') as file:
    lines = file.readlines()

##### Part 1 #####
xmas = Xmas(lines)
result = xmas.GetAnomaly()
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
result = xmas.GetEncryptionWeakness()
print(f"[+] Answer of part 2: {result}")