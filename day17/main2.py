from itertools import cycle
from copy import deepcopy
from Shape import Shape
import numpy as np
import utils
import re


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

def findRepetitions(string):
    r = re.compile(r"(.+?)\1+")
    for match in r.finditer(string):
        if len(match.group(0)) > 100:
            return match.group(0)

with open("input", 'r') as file:
    jets = cycle(file.readline().strip())

dirs = {'>': utils.checkMoveRight, '<': utils.checkMoveLeft} # values: function pointer

height = 1000000
chamber = np.zeros((height,7), dtype=np.int32)
top_level = 0

shapes_obj = Shape()
shapes = cycle(shapes_obj.shapes)

level_diffs = []

for _ in range(33000):
    new_level = sink(chamber, next(shapes), top_level)
    level_diffs.append(new_level-top_level)
    top_level = new_level

string = ''.join(map(str, level_diffs))
cycle = findRepetitions(string)
repetition_len = len(cycle)//2
print(f"Repetition Length = {repetition_len}")
assert cycle[:repetition_len] == cycle[repetition_len:], "Not a Cycle!"

nums = list(map(int, list(cycle[:repetition_len])))
result = sum(nums) * (1000000000000 // repetition_len)
nums = list(map(int, list(cycle[:1000000000000%repetition_len])))
result += sum(nums)

print(f"Answer of Part 2: {result}")
