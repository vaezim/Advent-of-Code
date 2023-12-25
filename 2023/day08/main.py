from utils import Desert


with open('input', 'r+') as file:
    lines = file.readlines()

##### Part 1 #####
desert = Desert(lines)
result = desert.GetNumSteps()
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
result = desert.GetNumGhostSteps()
print(f"[+] Answer of part 2: {result}")