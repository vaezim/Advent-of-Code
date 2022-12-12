
#################### Functions ####################

# Returns 1 if Head and Tail are within a 1x1 square, 0 otherwise.
def rel_dist(Head, Tail):
    hx, hy = Head[0], Head[1]
    tx, ty = Tail[0], Tail[1]
    return (abs(hx-tx)<=1 and abs(hy-ty)<=1)

# Returns the direction from loc1 to loc2 (must be within a 1x1 square) 
def find_direc(loc1, loc2):
    x1, y1, x2, y2 = loc1[0], loc1[1], loc2[0], loc2[1]
    if x1==x2 and y1==y2: return '.'
    if x1==x2:
        if y2-y1==1: return 'U'
        if y1-y2==1: return 'D'
    elif y1==y2:
        if x2-x1==1: return 'R'
        if x1-x2==1: return 'L'
    else:
        if x1-x2==1:
            if y1-y2==1: return 'LD'
            if y2-y1==1: return 'LU'
        if x2-x1==1:
            if y1-y2==1: return 'RD'
            if y2-y1==1: return 'RU'
    raise "Wrong Locations!"

# Moves Head in the <direc> direction. Tail is moved according to circumstances.
def move(Head, Tail, direc):
    Head0 = Head.copy() # copy! don't create a reference!
    motion = {'R':[1,0], 'L':[-1,0], 'U':[0,1], 'D':[0,-1],
              'LD':[-1,-1], 'LU':[-1,1], 'RD':[1,-1], 'RU':[1,1]}
    M = motion[direc]

    dist0 = rel_dist(Head, Tail)
    Head[0] += M[0]
    Head[1] += M[1]
    dist1 = rel_dist(Head, Tail)
    if dist1:
        return Head, Tail
    if len(direc)==1:
        return Head, Head0

    rel_pos = find_direc(Tail,Head0)
    M2 = motion[rel_pos]
    if len(rel_pos)==1:
        return Head, [Tail[0]+M[0],Tail[1]+M[1]]
    if len(rel_pos)==2:
        new_Tail = [Tail[0]+(M[0]+M2[0])//2,
                    Tail[1]+(M[1]+M2[1])//2]
        return Head, new_Tail

# Moves a rope with multiple knots in the <direc> direction
def move_rope(rope, direc):
    rope0 = rope.copy()
    knots = len(rope)
    for i in range(knots-1):
        rope[i], rope[i+1] = move(rope[i],rope[i+1],direc)
        if i==knots-2: break
        direc = find_direc(rope0[i+1],rope[i+1])
        if direc == '.': break
        rope[i+1] = rope0[i+1]
    return rope


#################### Part 1 ####################
Head = [0,0]
Tail = [0,0]
visited = set()
visited.add((0,0))

with open('input.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    motion = line.strip().split(' ')
    direc, steps = motion[0], int(motion[1])

    for _ in range(steps):
        Head, Tail = move(Head, Tail, direc)
        visited.add((Tail[0],Tail[1]))

print(f"Answer of Part 1: {len(visited)}")


#################### Part 2 ####################
knots = 10
rope = [[0,0] for _ in range(knots)]
visited = set()
visited.add((0,0))

with open('input.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    motion = line.strip().split(' ')
    direc, steps = motion[0], int(motion[1])

    for _ in range(steps):
        rope = move_rope(rope, direc)
        visited.add((rope[-1][0],rope[-1][1]))

print(f"Answer of Part 2: {len(visited)}")
