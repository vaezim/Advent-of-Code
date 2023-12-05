from utils import Card


with open('input', 'r+') as file:
    lines = file.readlines()

##### Part 1 #####
card = Card(lines)
result = card.GetTotalWorth()
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
result = card.GetCardNum()
print(f"[+] Answer of part 2: {result}")