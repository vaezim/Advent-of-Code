
class Cube:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        self.exposed_sides = 6

class Grid3D:
    def __init__(self, X, Y, Z):
        self.X, self.Y, self.Z = X, Y, Z
        self.grid = [[[None for _ in range(Z)] for _ in range(Y)] for _ in range(X)]

    def addCube(self, cube: Cube):
        x, y, z = cube.x, cube.y, cube.z
        self.grid[x][y][z] = cube
        # Checking all surfaces for neighbor cubes
        if x+1 < self.X and self.grid[x+1][y][z] != None: # top
            cube.exposed_sides -= 1
            self.grid[x+1][y][z].exposed_sides -= 1
        if x-1 >= 0 and self.grid[x-1][y][z] != None: # bottom
            cube.exposed_sides -= 1
            self.grid[x-1][y][z].exposed_sides -= 1
        if y+1 < self.Y and self.grid[x][y+1][z] != None: # left
            cube.exposed_sides -= 1
            self.grid[x][y+1][z].exposed_sides -= 1
        if y-1 >= 0 and self.grid[x][y-1][z] != None: # right
            cube.exposed_sides -= 1
            self.grid[x][y-1][z].exposed_sides -= 1
        if z+1 < self.Z and self.grid[x][y][z+1] != None: # front
            cube.exposed_sides -= 1
            self.grid[x][y][z+1].exposed_sides -= 1
        if z-1 >= 0 and self.grid[x][y][z-1] != None: # back
            cube.exposed_sides -= 1
            self.grid[x][y][z-1].exposed_sides -= 1

    def getExposedSides(self):
        result = 0
        for i in range(self.X):
            for j in range(self.Y):
                for k in range(self.Z):
                    if self.grid[i][j][k] != None:
                        result += self.grid[i][j][k].exposed_sides
        return result
        