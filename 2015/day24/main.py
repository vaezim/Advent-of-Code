from utils import Santa


with open("input", "r+") as file:
    lines = file.readlines()

##### Part 1 #####
santa = Santa(list(map(lambda x: int(x), lines)), num_groups=3)
result = santa.GetIdealConfigQE()
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
santa = Santa(list(map(lambda x: int(x), lines)), num_groups=4)
result = santa.GetIdealConfigQE()
print(f"[+] Answer of part 2: {result}")
