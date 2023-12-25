from utils import ApplyLights1, ApplyLights2


with open('input', 'r+') as file:
    lines = file.readlines()

##### Part 1 #####
grid = [[0]*1000 for _ in range(1000)];
for line in lines:
    ApplyLights1(line, grid)
result = sum([sum(grid[i]) for i in range(len(grid))])

print(f"Answer of part 1: {result}")

##### Part 2 #####
grid = [[0]*1000 for _ in range(1000)];
for line in lines:
    ApplyLights2(line, grid)
result = sum([sum(grid[i]) for i in range(len(grid))])

print(f"Answer of part 2: {result}")
