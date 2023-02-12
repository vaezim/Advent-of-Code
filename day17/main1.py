from itertools import cycle
from copy import deepcopy
from Shape import Shape
import numpy as np
import utils


def sink(chamber, _shape, _top_level):
    # initial placement
    shape = deepcopy(_shape)
    for dot in shape:
        dot[0] += top_level + 3

    # sinking
    while True:
        jet = next(jets)
        mover = dirs[jet] # function pointer
        mover(chamber, shape)
        if not utils.checkMoveDown(chamber, shape):
            break

    # final placement & finding top_level
    new_top_level = utils.addShape2Chamber(chamber, shape, top_level)
    return new_top_level


with open("input", 'r') as file:
    jets = cycle(file.readline().strip())

dirs = {'>': utils.checkMoveRight, '<': utils.checkMoveLeft} # values: function pointer

height = 10000
chamber = np.zeros((height,7), dtype=np.int32)
top_level = 0

shapes_obj = Shape()
shapes = cycle(shapes_obj.shapes)

for _ in range(2022):
    top_level = sink(chamber, next(shapes), top_level)

print(f"Answer of Part 1: {top_level}")
