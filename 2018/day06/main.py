from utils import ManhattanDist


with open('input', 'r+') as file:
    lines = file.readlines()
points = []
for line in lines:
    point = (int(line.split(',')[0]),
             int(line.split(',')[1]))
    points.append(point)

##### Part 1 #####
grid_width = 400
grid1 = [[[-1,float("inf")]]*grid_width for _ in range(grid_width)]
grid2 = [[[-1,float("inf")]]*(grid_width+2) for _ in range(grid_width+2)]

for i in range(len(grid1)):
    for j in range(len(grid1[0])):
        for p, point in enumerate(points):
            manhattan_dist = ManhattanDist((i,j),point)
            if manhattan_dist == grid1[i][j][1]:
                break
            if manhattan_dist < grid1[i][j][1]:
                grid1[i][j][1] = manhattan_dist
                grid1[i][j][0] = p

for i in range(len(grid2)):
    for j in range(len(grid2[0])):
        for p, point in enumerate(points):
            manhattan_dist = ManhattanDist((i-1,j-1),point)
            if manhattan_dist == grid2[i][j][1]:
                break
            if manhattan_dist < grid2[i][j][1]:
                grid2[i][j][1] = manhattan_dist
                grid2[i][j][0] = p

distances1 = [0]*len(points)
distances2 = [0]*len(points)
for i in range(len(grid1)):
    for j in range(len(grid1[0])):
        if grid1[i][j][0] != -1:
            distances1[grid1[i][j][0]] += 1
for i in range(len(grid2)):
    for j in range(len(grid2[0])):
        if grid2[i][j][0] != -1:
            distances2[grid2[i][j][0]] += 1

result = 0
for i in range(len(points)):
    if distances1[i] == distances2[i]:
        result = max(result, distances1[i])

print(f"Answer of part 1: {result}")

##### Part 2 #####

print(f"Answer of part 2: {result}")
