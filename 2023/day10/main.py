from utils import Pipes

with open("input", "r+") as file:
    lines = file.readlines()

##### Part 1 #####
pipes = Pipes(lines)
result = pipes.GetFarthestPointInLoop()
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
result = pipes.GetLoopArea()
print(f"[+] Answer of part 2: {result}")
