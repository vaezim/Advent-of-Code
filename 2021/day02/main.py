
with open('input.txt', 'r') as file:
    lines = file.readlines()

##### Part 1 #####
x, depth = 0, 0
for line in lines:
    line = line.strip().split(' ')
    direc, length = line[0], int(line[1])
    if direc == 'forward':
        x += length
    elif direc == 'up':
        depth -= length
    elif direc == 'down':
        depth += length

print(x * depth)

##### Part 2 #####
x, depth, aim = 0, 0, 0
for line in lines:
    line = line.strip().split(' ')
    direc, length = line[0], int(line[1])
    if direc == 'forward':
        x += length
        depth += aim*length
    elif direc == 'up':
        aim -= length
    elif direc == 'down':
        aim += length

print(x * depth)
