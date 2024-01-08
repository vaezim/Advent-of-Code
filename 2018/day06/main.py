from utils import Manhattan


with open("input", "r+") as file:
    lines = file.readlines()

##### Part 1 #####
man = Manhattan(lines)
result = man.GetLargestArea()
print(f"Answer of part 1: {result}")

##### Part 2 #####
result = man.GetRegionSize()
print(f"Answer of part 2: {result}")
