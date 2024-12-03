from utils import Solver


with open('input1', 'r+') as file:
    lines1 = file.readlines()
with open('input2', 'r+') as file:
    lines2 = file.readlines()

##### Part 1 #####
solver = Solver(lines1, lines2)
result = solver.CountNumSamplesBehavingLikeThreeOrMoreOpCodes()
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
result = solver.RunProgram()
print(f"[+] Answer of part 2: {result}")