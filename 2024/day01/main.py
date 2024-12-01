from utils import Lists


with open('input', 'r+') as file:
    lines = file.readlines()

##### Part 1 #####
lists = Lists(lines)
result = lists.GetSumDistances()
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
result = lists.GetSimilarityScore()
print(f"[+] Answer of part 2: {result}")