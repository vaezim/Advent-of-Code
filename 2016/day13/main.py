#!/usr/bin/python3
from utils import Grid


# input
num = 1350
width, height = 50,50

##### Part 1 #####
grid = Grid(num, 50, 50)
# grid.Disp()
grid.SetDestination(31,39)
result = grid.FindShortestPath()
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
result = grid.GetLocationsCloserThan50()
print(f"[+] Answer of part 2: {result}")
