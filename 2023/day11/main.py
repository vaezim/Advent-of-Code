from utils import Galaxy


with open('input', 'r+') as file:
    lines = file.readlines()

##### Part 1 #####
galaxy = Galaxy(lines)
result = galaxy.GetSumDistances()
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####

print(f"[+] Answer of part 2: {result}")