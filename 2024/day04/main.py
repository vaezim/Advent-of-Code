from utils import Solver


with open('input', 'r+') as file:
    text = file.readlines()
text = list(map(lambda x: x.strip(), text))

##### Part 1 #####
solver = Solver(text)
result = solver.SolvePart1()
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
result = solver.SolvePart2()
print(f"[+] Answer of part 2: {result}")
