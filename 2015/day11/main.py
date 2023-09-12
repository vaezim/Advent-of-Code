from utils import *


##### Part 1 #####
s = "cqjxjnds"
result = NextPassword(s)
while not IsValidPassword(result):
    result = NextPassword(result)
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
result = NextPassword(result)
while not IsValidPassword(result):
    result = NextPassword(result)
print(f"[+] Answer of part 2: {result}")
