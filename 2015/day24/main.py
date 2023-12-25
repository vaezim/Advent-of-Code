from utils import Santa


with open('input', 'r+') as file:
    lines = file.readlines()

##### Part 1 #####
packages = list(map(lambda x: int(x), lines))
santa = Santa(packages)
result = santa.GetIdealConfigQE()
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####

print(f"[+] Answer of part 2: {result}")
