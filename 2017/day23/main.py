from utils import Assembly


with open("input", "r+") as file:
    lines = file.readlines()

##### Part 1 #####
ass = Assembly(lines)
result = ass.GetNumMulCalls()
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
"""
Go to [prog.py]
"""
print(f"[+] Answer of part 2: {}")
