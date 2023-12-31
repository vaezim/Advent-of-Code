from utils import CPU


with open("input", "r+") as file:
    lines = file.readlines()

##### Part 1 #####
cpu = CPU(lines)
result = cpu.Recover()
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
result = cpu.RunTwoPrograms()
print(f"[+] Answer of part 2: {result}")
