from utils import Solver


with open('input', 'r+') as file:
    lines = file.readlines()

##### Part 1 #####
solver = Solver(lines)
result = solver.SolvePart1()
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
result = solver.SolvePart2()
print(f"[+] Answer of part 2: {result}")