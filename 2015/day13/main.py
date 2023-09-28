from utils import Happiness


with open('input', 'r+') as file:
    lines = file.readlines()

##### Part 1 #####
happiness = {}
for line in lines:
    words = line.split()
    name1, name2 = words[0], words[-1][:-1]
    points = int(words[3])
    if happiness.get(name1) == None:
        happiness[name1] = {}
    if words[2] == "lose":
        points *= -1
    happiness[name1][name2] = points

h = Happiness(happiness)
result = h.GetMaximumHappiness()
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
happiness["You"] = {}
for person in happiness:
    happiness[person]["You"] = 0
    happiness["You"][person] = 0

h = Happiness(happiness)
result = h.GetMaximumHappiness()
print(f"[+] Answer of part 2: {result}")
