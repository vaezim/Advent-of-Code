from utils import Galaxy


with open("input", "r+") as file:
    lines = file.readlines()

##### Part 1 #####
galaxy = Galaxy(lines)
result = galaxy.GetSumDistances(expansion_size=2)
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
result = galaxy.GetSumDistances(expansion_size=1000000)
print(f"[+] Answer of part 2: {result}")
