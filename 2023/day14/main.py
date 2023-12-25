from utils import Beam


with open('input', 'r+') as file:
    lines = file.readlines()

##### Part 1 #####
beam = Beam(lines)
result = beam.GetTotalNorthLoad()
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####

print(f"[+] Answer of part 2: {result}")