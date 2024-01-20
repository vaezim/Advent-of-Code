from utils import Hamilton


with open("input", "r+") as file:
    lines = file.readlines()

##### Part 1 #####
hamilton = Hamilton(lines)
result = hamilton.GetShortestHamiltonianPath()
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
result = hamilton.GetShortestHamiltonianPathFromZeroToZero()
print(f"[+] Answer of part 2: {result}")
