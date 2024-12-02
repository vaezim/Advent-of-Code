from utils import Solver


with open('input', 'r+') as file:
    lines = file.readlines()

##### Part 1 #####
solver = Solver(lines)
result = solver.GetNumSafeReports()
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
result = solver.GetNumSafeReportsWithErrorCorrection()
print(f"[+] Answer of part 2: {result}")