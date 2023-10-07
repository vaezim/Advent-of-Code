from utils import Medicine


with open('input', 'r+') as file:
    lines = file.readlines()

##### Part 1 #####
reps = []
for line in lines:
    if line == '\n':
        break
    words = line.strip().split()
    reps.append((words[0], words[2]))
initial = lines[-1].strip()
M = Medicine(replacements=reps, initial=initial)
result = M.GetNumUniqueMolecules()
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####

print(f"[+] Answer of part 2: {result}")
