from utils import Aunt


with open('input', 'r+') as file:
    lines = file.readlines()

sender = {
    "children":     3,
    "cats":         7,
    "samoyeds":     2,
    "pomeranians":  3,
    "akitas":       0,
    "vizslas":      0,
    "goldfish":     5,
    "trees":        3,
    "cars":         2,
    "perfumes":     1
}

##### Part 1 #####
auntFinder = Aunt(sender)
for line in lines:
    words = line.strip().split()
    aunt = {
        words[2][:-1]: int(words[3][:-1]),
        words[4][:-1]: int(words[5][:-1]),
        words[6][:-1]: int(words[-1])
    }
    auntFinder.AddAunt(aunt)
result = auntFinder.FindSenderIndex()
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
result = auntFinder.FindSenderIndex(mode=2)
print(f"[+] Answer of part 2: {result}")
