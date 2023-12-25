from utils import LanternFish


with open('input', 'r+') as file:
    line = file.read().strip()

##### Part 1 #####
days = 80
fish_ages = list(map(lambda x: int(x), line.split(',')))
lf = LanternFish(fish_ages)
result = lf.GetFishNum(days)
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
days = 256
result = lf.GetFishNum(days)
print(f"[+] Answer of part 2: {result}")
