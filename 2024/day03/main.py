from utils import Solver


with open('input', 'r+') as file:
    text = file.read()

##### Part 1 #####
solver = Solver(text)
result = solver.SolvePart1()
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
result = solver.SolvePart2()
print(f"[+] Answer of part 2: {result}")