from Space import Cube, Grid3D


with open("input", 'r') as file:
    cubes = file.readlines()

Grid = Grid3D(20, 20, 20)

for cube in cubes:
    xyz = cube.strip().split(',')
    x, y, z = int(xyz[0]), int(xyz[1]), int(xyz[2])
    Grid.addCube(Cube(x, y, z))

print(f"Answer of Part 1: {Grid.getExposedSides()}")








print(f"Answer of Part 2: ")