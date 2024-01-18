from utils import Assembly


with open("input", "r+") as file:
    lines = file.readlines()

##### Part 1 #####
a = 7
ass = Assembly(lines)
ass.SetRegister("a", a)
ass.Run()
result = ass.registers["a"]
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
a = 12
ass = Assembly(lines)
ass.SetRegister("a", a)
ass.Run()
result = ass.registers["a"]
print(f"[+] Answer of part 2: {result}")
