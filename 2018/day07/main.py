from utils import Steps


with open("test", "r+") as file:
    lines = file.readlines()

##### Part 1 #####
steps = Steps(lines)
result = steps.GetStepSequence()
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
result = steps.RunTwoWorkers()
print(f"[+] Answer of part 2: {result}")
