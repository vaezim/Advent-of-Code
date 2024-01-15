from utils import Capsule


with open("input", "r+") as file:
    lines = file.readlines()

##### Part 1 #####
capsule = Capsule(lines)
result = capsule.GetDisksAllignedTime()
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
capsule.disks.append((11, 0))
result = capsule.GetDisksAllignedTime()
print(f"[+] Answer of part 2: {result}")
