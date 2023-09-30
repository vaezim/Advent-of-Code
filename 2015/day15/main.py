from utils import Ingred


with open('input', 'r+') as file:
    lines = file.readlines()

##### Part 1 #####
ing = Ingred()
for line in lines:
    words = line.strip().split()
    ingred = (
        int(words[2][:-1]),
        int(words[4][:-1]),
        int(words[6][:-1]),
        int(words[8][:-1]),
        int(words[-1])
    )
    ing.AddIngred(ingred)
result = ing.FindMaximumScore()
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
result = ing.FindMaximumScoreLimitedCal()
print(f"[+] Answer of part 2: {result}")
