from utils import FileSystem


with open("input", "r+") as file:
    lines = file.readlines()

##### Part 1 #####
fs = FileSystem(lines)
result = fs.GetNumViablePairs()
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
fs.DispToFile("filesystem.fs")
result = 256  # Do it by hand !!! #
print(f"[+] Answer of part 2: {result}")
