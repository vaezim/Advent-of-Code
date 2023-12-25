from utils import Game


with open('input', 'r+') as file:
    lines = file.readlines()

##### Part 1 #####
game = Game([12, 13, 14])  # [red, green, blue]
game.ParseGames(lines)
result = game.GetSumPossibleGameIds()
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
result = game.GetSumMinPower()
print(f"[+] Answer of part 2: {result}")