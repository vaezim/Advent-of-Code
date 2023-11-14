from utils import Dance


with open('input', 'r+') as file:
    text = file.read().strip()

##### Part 1 #####
dance = Dance(16, text)
result = dance.Dance()
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
result = dance.DanceRepeat(10**9)
print(f"[+] Answer of part 2: {result}")