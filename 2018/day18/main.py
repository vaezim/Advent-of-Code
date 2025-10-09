from utils import Land


with open('input', 'r+') as file:
    lines = file.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].strip()

##### Part 1 #####
land = Land(lines)
land.PassNMinutes(n=10)
result = land.GetNumLumberyards() * land.GetNumTrees()
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
land.Reset()
land.PassNMinutes(n=1_000_000_000)
result = land.GetNumLumberyards() * land.GetNumTrees()
print(f"[+] Answer of part 2: {result}")
