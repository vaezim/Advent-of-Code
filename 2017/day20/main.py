from utils import GPU


with open("input", "r+") as file:
    lines = file.readlines()

##### Part 1 #####
gpu = GPU(lines)
result = gpu.GetClosestToCenterInLongRun()
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
result = gpu.SimulateCollision()
print(f"[+] Answer of part 2: {result}")
