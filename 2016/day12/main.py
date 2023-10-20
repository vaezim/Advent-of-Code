from utils import Assembly


with open('input', 'r+') as file:
    lines = file.readlines()

##### Part 1 #####
ass = Assembly()
ass.AddInstructions(lines)
ass.Run()
registers = ass.GetRegisters()
result = registers["a"]
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
ass = Assembly()
ass.registers["c"] = 1
ass.AddInstructions(lines)
ass.Run()
registers = ass.GetRegisters()
result = registers["a"]
print(f"[+] Answer of part 2: {result}")
