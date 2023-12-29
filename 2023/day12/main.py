from utils import Onsen


with open("input", "r+") as file:
    lines = file.readlines()

##### Part 1 #####
onsen = Onsen(lines)
result = onsen.GetSumCorrectArrangements()
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
result = onsen.GetSumCorrectArrangements(unfold=5)
print(f"[+] Answer of part 2: {result}")
