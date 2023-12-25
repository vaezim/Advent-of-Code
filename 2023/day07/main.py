from utils import Cards


with open('input', 'r+') as file:
    lines = file.readlines()

##### Part 1 #####
cards = Cards(lines)
result = cards.GetTotalWinnings()
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
result = cards.GetTotalWinnings2()
print(f"[+] Answer of part 2: {result}")