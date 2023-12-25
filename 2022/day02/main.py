
shapes = {'X': 1, 'Y': 2, 'Z': 3}
points = {'A X': 3, 'B Y': 3, 'C Z': 3,
          'A Z': 0, 'B X': 0, 'C Y': 0,
          'A Y': 6, 'B Z': 6, 'C X': 6}
with open('input.txt', 'r+') as file:
    hands = file.readlines()

res = 0
for h in hands:
    res += points[h[:-1]]
    res += shapes[h[:-1][-1]]

print(f'Answer of part 1: {res}')

points = {'X': 0, 'Y': 3, 'Z': 6}
strats = {'X': {'A': 3, 'B': 1, 'C': 2},
          'Y': {'A': 1, 'B': 2, 'C': 3},
          'Z': {'A': 2, 'B': 3, 'C': 1}}

res = 0
for h in hands:
    res += points[h[-2]]
    res += strats[h[-2]][h[0]]

print(f'Answer of part 2: {res}')
