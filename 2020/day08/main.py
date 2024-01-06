from utils import Atari


with open("input", "r+") as file:
    lines = file.readlines()

##### Part 1 #####
atari = Atari(lines)
result = atari.RunNoCycle()
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
result = atari.RunFixedProgram()
print(f"[+] Answer of part 2: {result}")
