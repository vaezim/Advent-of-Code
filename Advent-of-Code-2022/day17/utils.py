import numpy as np


def addShape2Chamber(chamber, shape, top_level):
    for dot in shape:
        chamber[dot[0],dot[1]] = 1

    top_level = max(top_level, 0)
    while np.any(chamber[top_level,:]):
        top_level += 1
    return top_level

def canMoveRight(chamber, shape):
    W, H = chamber.shape[1], chamber.shape[0]
    for dot in shape:
        x, y = dot[0], dot[1]
        if y == W-1 or chamber[x,y+1] == 1:
            return False
    return True

def canMoveLeft(chamber, shape):
    W, H = chamber.shape[1], chamber.shape[0]
    for dot in shape:
        x, y = dot[0], dot[1]
        if y == 0 or chamber[x,y-1] == 1:
            return False
    return True

def canMoveDown(chamber, shape):
    for dot in shape:
        x, y = dot[0], dot[1]
        if x == 0 or chamber[x-1,y] == 1:
            return False
    return True

def checkMoveRight(chamber, shape):
    if not canMoveRight(chamber, shape):
        return False
    for dot in shape:
        dot[1] += 1
    return True

def checkMoveLeft(chamber, shape):
    if not canMoveLeft(chamber, shape):
        return False
    for dot in shape:
        dot[1] -= 1
    return True

def checkMoveDown(chamber, shape):
    if not canMoveDown(chamber, shape):
        return False
    for dot in shape:
        dot[0] -= 1
    return True
    