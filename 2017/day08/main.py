from utils import CPU


with open('input', 'r+') as file:
    lines = file.readlines()

##### Part 1 #####
cpu = CPU()
for line in lines:
    cpu.ParseInstruction(line=line)
result = max(cpu.registers.values())

print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
result = cpu.max

print(f"[+] Answer of part 2: {result}")
