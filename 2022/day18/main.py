from Space import Cube, Grid3D


with open("input", 'r') as file:
    cubes = file.readlines()

grid_size = 25
Grid = Grid3D(grid_size, grid_size, grid_size)

for cube in cubes:
    xyz = cube.strip().split(',')
    x, y, z = int(xyz[0]), int(xyz[1]), int(xyz[2])
    Grid.addCube(Cube(x, y, z))

exposedSides = Grid.getExposedSides()
print(f"Answer of Part 1: {exposedSides}")

exteriorSides = Grid.getExteriorSides()
print(f"Answer of Part 2: {exteriorSides}")
