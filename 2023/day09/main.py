from utils import Glider


with open('input', 'r+') as file:
    lines = file.readlines()

##### Part 1 #####
glider = Glider(lines)
result = glider.GetSumNextVals()
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
glider = Glider(lines)
result = glider.GetSumPrevVals()
print(f"[+] Answer of part 2: {result}")