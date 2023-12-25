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
        for i in range(h):
            for j in range(w):
                screen[i][j] = 1
    elif tokens[1] == "row":
        row = int(tokens[2][2:])
        screen[row] = np.roll(screen[row], int(tokens[-1]))
    elif tokens[1] == "column":
        col = int(tokens[2][2:])
        screen[:,col] = np.roll(screen[:,col], int(tokens[-1]))
result = int(screen.sum())
print(f"Answer of part 1: {result}")

##### Part 2 #####
for row in screen:
    for c in row:
        if int(c) == 1:
            print("0", end="")
        else:
            print(" ", end="")
    print()
