from Path import Path


with open('input.txt', 'r') as file:
    lines = file.readlines()
_map = [list(line.strip()) for line in lines]

# Find initial position (S)
for i, line in enumerate(lines):
    if 'S' in line:
        init_pos = [i,line.index('S')]
        # Replace 'S' with its height ('a')
        _map[init_pos[0]][init_pos[1]] = 'a'
        break

# Find final position (E)
for i, line in enumerate(lines):
    if 'E' in line:
        final_pos = [i,line.index('E')]
        # Replace 'E' with its height ('z')
        _map[final_pos[0]][final_pos[1]] = 'z'
        break

##### Part 1 #####
pathFinder = Path(_map, init_pos, final_pos)
sP = pathFinder.globalShortestPath()
print(sP)

##### Part 2 #####
all_sP = pathFinder.discovered
min_sP = float('inf')

for i in range(len(_map)):
    for j in range(len(_map[0])):
        if _map[i][j] == 'a':
            min_sP = min(min_sP, all_sP[i][j])
print(min_sP)
