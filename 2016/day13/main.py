#!/usr/bin/python3
from utils import Grid


# input
num = 1350
width, height = 50,50

##### Part 1 #####
grid = Grid(num)
grid.BuildGrid(width+1, height+1)
grid.SetDestination(31,39)
# grid.Disp()  # show grid
result = grid.FindShortestPath()
grid.Disp()  # show grid + shortest path
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
result = grid.GetLocationsCloserThan50()
print(f"[+] Answer of part 2: {result}")
