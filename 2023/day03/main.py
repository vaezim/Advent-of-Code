from utils import Engine


with open('input', 'r+') as file:
    lines = file.readlines()

##### Part 1 #####
engine = Engine(lines)
result = engine.GetSumPartNumbers()
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
result = engine.GetSumGearRatios()
print(f"[+] Answer of part 2: {result}")