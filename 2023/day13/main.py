from utils import Mirror


with open("input", "r+") as file:
    lines = file.readlines()

##### Part 1 #####
mirror = Mirror(lines)
result = mirror.GetSumMirrors()
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
result = mirror.GetSumFixedMirrors()
print(f"[+] Answer of part 2: {result}")
