from utils import Generator


with open('input', 'r+') as file:
    lines = file.readlines()

##### Part 1 #####
saltA = int(lines[0].split()[-1])
saltB = int(lines[1].split()[-1])
gen = Generator(saltA, saltB)
result = gen.GetJudgeCount()  # takes 5~10 seconds
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
result = gen.GetJudgeCount2()
print(f"[+] Answer of part 2: {result}")