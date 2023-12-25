from utils import FileSystem


with open('input', 'r+') as file:
    lines = file.readlines()

##### Part 1 #####
fs = FileSystem(lines)
result = fs.GetNumViablePairs()
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####

print(f"[+] Answer of part 2: {result}")
