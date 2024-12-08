from utils import Solver


with open('input', 'r+') as file:
    lines = file.readlines()
lines = list(map(lambda x: x.strip(), lines))

##### Part 1 #####
solver = Solver(lines)
result = solver.SolvePart1()
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
result = solver.SolvePart2()
print(f"[+] Answer of part 2: {result}")