from utils import Bags


with open('input', 'r+') as file:
    lines = file.readlines()

##### Part 1 #####
bags = Bags(lines)
result = bags.GetNumBagsContainingShinyGold()
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
result = bags.GetNumBagsWithinShinyGold()
print(f"[+] Answer of part 2: {result}")