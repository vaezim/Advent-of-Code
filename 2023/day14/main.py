from utils import Beam
from copy import deepcopy


with open("input", "r+") as file:
    lines = file.readlines()

##### Part 1 #####
beam = Beam(lines)
tilted_north = beam.TiltNorth(deepcopy(beam.grid))
result = beam.GetTotalLoad(tilted_north)
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
spinned_grid = beam.SpinALot(deepcopy(beam.grid), 1000000000)
result = beam.GetTotalLoad(spinned_grid)
print(f"[+] Answer of part 2: {result}")
