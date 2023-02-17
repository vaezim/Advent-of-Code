from utils import isHorVer
from numpy import zeros


with open("input", 'r') as file:
    lines = file.readlines()

vents = []
width, height = 0, 0
for line in lines:
    head, tail = line.strip().split()[0], line.strip().split()[-1]
    head = (int(head[0]), int(head[-1]) )
    tail = (int(tail[0]), int(tail[-1]) )

    width, height = max(width, head[0], tail[0]), max(height, head[1], tail[1])
    vents.append((head,tail))

grid = zeros((height+1,width+1))

for vent in vents:
    head, tail = vent[0], vent[1]
    HorVer = isHorVer(vent)

    if HorVer == 'H':
        left, right = min(head[0],tail[0]), max(head[0],tail[0])
        for i in range(left,right+1):
            grid[head[1]][i] += 1
    elif HorVer == 'V':
        top, down = min(head[1],tail[1]), max(head[1],tail[1])
        for i in range(top,down+1):
            grid[i][head[0]] += 1
    else: # diagonal
        continue

##### Part 1 #####
overlaps = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] >= 2:
            overlaps += 1
print(f"Answer of part 1: {overlaps}")
