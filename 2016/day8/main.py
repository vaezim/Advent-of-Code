import numpy as np


with open('input', 'r+') as file:
    lines = file.readlines()

##### Part 1 #####
width, height = 50, 6
screen = np.zeros((height, width))
for line in lines:
    tokens = line.split()
    if tokens[0] == "rect":
        w, h = int(tokens[1].split('x')[0]), int(tokens[1].split('x')[1])
        screen[0:h-1,]

result = screen.sum()
print(f"Answer of part 1: {result}")

##### Part 2 #####

print(f"Answer of part 2: {result}")
