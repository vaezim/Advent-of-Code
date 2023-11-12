from utils import Grid


salt = "nbysizxe"

##### Part 1 #####
grid = Grid(salt)
result = grid.GetNumOnes()
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
result = grid.GetNumRegions()
print(f"[+] Answer of part 2: {result}")
