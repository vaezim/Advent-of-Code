from utils import Joltage


with open("input", "r+") as file:
    lines = file.readlines()

##### Part 1 #####
jolt = Joltage(lines)
result = jolt.Get1JoltTimes3JoltDiffs()
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
result = jolt.GetNumArrangements()
print(f"[+] Answer of part 2: {result}")
