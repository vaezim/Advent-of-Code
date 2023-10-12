from utils import CodeGenerator


with open('input', 'r+') as file:
    words = file.read().strip().split()

##### Part 1 #####
row = int(words[-3][:-1])
col = int(words[-1][:-1])
generator = CodeGenerator()
result = generator.GetCode(row, col)
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####

print(f"[+] Answer of part 2: {result}")
