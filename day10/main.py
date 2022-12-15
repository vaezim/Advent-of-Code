
#################### Part 1 ####################

def get_strength(cycle, X):
    if cycle in [20,60,100,140,180,220]:
        return cycle*X
    return 0

with open('input.txt', 'r') as file:
    lines = file.readlines()

cycle = 0
X = 1
strengths = 0

for line in lines:
    line = line.strip().split(' ')

    if line[0] == 'noop':
        cycle += 1
        strengths += get_strength(cycle, X)

    elif line[0] == 'addx':
        cycle += 1
        strengths += get_strength(cycle, X)

        cycle += 1
        strengths += get_strength(cycle, X)
        X += int(line[1])

print(f"Answer of Part 1: {strengths}")

#################### Part 2 ####################

def draw(screen, cycle, X):
    rows = screen.split('\n')
    if len(rows[-1]) == 40:
        screen += '\n'
    pos = cycle % 40
    if pos in [X-1,X,X+1]:
        screen += '#'
    else:
        screen += '.'
    return screen

with open('input.txt', 'r') as file:
    lines = file.readlines()

cycle = 0
screen = ''
X = 1

for line in lines:
    line = line.strip().split(' ')

    if line[0] == 'noop':
        screen = draw(screen, cycle, X)
        cycle += 1

    elif line[0] == 'addx':
        screen = draw(screen, cycle, X)
        cycle += 1
        screen = draw(screen, cycle, X)
        cycle += 1
        X += int(line[1])

print(f"Answer of Part 2:")
print(screen)
# ZFBFHGUP