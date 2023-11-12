from utils import ProgramMgr


with open('input', 'r+') as file:
    lines = file.readlines()

##### Part 1 #####
manager = ProgramMgr(lines)
result = manager.GetNumProgramContainingId(id=0)
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
result = manager.GetNumGroups()
print(f"[+] Answer of part 2: {result}")
