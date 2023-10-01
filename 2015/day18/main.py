from utils import GameOfLife


with open("input", "r+") as file:
    lines = file.readlines()

##### Part 1 #####
grid = [[0] * 100 for _ in range(100)]
for i, line in enumerate(lines):
    for j in range(len(line)):
        if line[j] == "#":
            grid[i][j] = 1
gol = GameOfLife(grid)
steps = 100
result = gol.Simulate(steps)
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
gol2 = GameOfLife(grid)
result = gol2.Simulate2(steps)
print(f"[+] Answer of part 2: {result}")
