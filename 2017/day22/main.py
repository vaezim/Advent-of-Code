from utils import Worm


with open("input", "r+") as file:
    lines = file.readlines()

##### Part 1 #####
worm = Worm(lines)
result = worm.GetNumInfectingBursts1(10_000)
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
result = worm.GetNumInfectingBursts2(10_000_000)
print(f"[+] Answer of part 2: {result}")
