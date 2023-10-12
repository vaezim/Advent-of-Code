from utils import Computer


with open('input', 'r+') as file:
    lines = file.readlines()

##### Part 1 #####
computer = Computer()
computer.AddInstructions(lines)
computer.Run()
result = computer.registers["b"]
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
computer.registers["a"] = 1
computer.registers["b"] = 0
computer.Run()
result = computer.registers["b"]
print(f"[+] Answer of part 2: {result}")
