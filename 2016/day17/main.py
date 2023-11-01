from utils import VaultFinder


passcode = "pgflpeqp"

##### Part 1 #####
vf = VaultFinder(passcode)
result = vf.GetShortestPath()
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
result = len(vf.GetLongestPath())
print(f"[+] Answer of part 2: {result}")
