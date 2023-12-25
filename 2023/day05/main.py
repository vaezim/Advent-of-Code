from utils import Gardener


with open('input', 'r+') as file:
    lines = file.readlines()

##### Part 1 #####
gardener = Gardener(lines)
result = gardener.GetMinSeedLocations()
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####

gardener.Test(2906961955, 2906961955+52237479)

# result = gardener.GetMinSeedRangeLocations()
print(f"[+] Answer of part 2: {result}")