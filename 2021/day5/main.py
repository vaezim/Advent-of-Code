from utils import draw_line, draw_diagonal


with open("input") as file:
    lines = file.readlines()

src_points = []
dst_points = []

for line in lines:
    p1, p2 = line.split()[0], line.split()[-1]
    xy1, xy2 = p1.split(','), p2.split(',')
    src_points.append(( int(xy1[0]), int(xy1[1]) ))
    dst_points.append(( int(xy2[0]), int(xy2[1]) ))

width, height = 0, 0
for i in range(len(src_points)):
    width, height = max(width, src_points[i][0], dst_points[i][0]),\
                    max(height, src_points[i][1], dst_points[i][1])
width += 1
height += 1

vent_map = [[0]*height for _ in range(width)]

##### Part 1 #####
for i in range(len(src_points)):
    draw_line(src_points[i], dst_points[i], vent_map)

dangerous_count = 0
for i in range(width):
    for j in range(height):
        dangerous_count += (vent_map[i][j] >= 2)

print(f"Answer of part 1: {dangerous_count}")

##### Part 2 #####
for i in range(len(src_points)):
    draw_diagonal(src_points[i], dst_points[i], vent_map)

dangerous_count = 0
for i in range(width):
    for j in range(height):
        dangerous_count += (vent_map[i][j] >= 2)

print(f"Answer of part 2: {dangerous_count}")
