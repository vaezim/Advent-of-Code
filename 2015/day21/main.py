from utils import RPG


with open('input', 'r+') as file:
    lines = file.readlines()

##### Part 1 #####
enemy_stats = [int(lines[0].strip().split()[-1]),
               int(lines[1].strip().split()[-1]),
               int(lines[2].strip().split()[-1])]
rpg = RPG()
rpg.AddEnemyStats(enemy_stats)
result = rpg.GetMinGoldCost()
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
result = rpg.GetMaxGoldCost()
print(f"[+] Answer of part 2: {result}")
