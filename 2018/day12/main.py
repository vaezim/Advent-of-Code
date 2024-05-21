from utils import Plants


with open('input', 'r+') as file:
    lines = file.readlines()

##### Part 1 #####
plants = Plants(lines)
result = plants.Pass20Generations()
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
result = plants.Pass50BillionGenerations()
print(f"[+] Answer of part 2: {result}")