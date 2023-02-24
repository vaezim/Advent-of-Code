from sys import setrecursionlimit


class Cube:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z
        self.exposed_sides = 6

class Grid3D:
    def __init__(self, X, Y, Z):
        setrecursionlimit(X*Y*Z)
        self.X, self.Y, self.Z = X, Y, Z
        self.grid = [[[None for _ in range(Z)] for _ in range(Y)] for _ in range(X)]

    def addCube(self, cube: Cube):
        x, y, z = cube.x, cube.y, cube.z
        self.grid[x][y][z] = cube
        # Checking all sides
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

    def detectExteriorAirCubes(self):
        # Populating Boundary Cubes
        for i in range(self.X):
            for j in range(self.Y):
                self.grid[i][j][self.Z-1] = 0
        for i in range(self.X):
            for k in range(self.Z):
                self.grid[i][self.Y-1][k] = 0
        for j in range(self.Y):
            for k in range(self.Z):
                self.grid[self.X-1][j][k] = 0
        # DFS
        self.DFSExteriorAirCubes(self.X-2, self.Y-2, self.Z-2)

    def DFSExteriorAirCubes(self, x, y, z):
        if self.grid[x][y][z] != None: # if ==0 or ==<Cube>
            return
        self.grid[x][y][z] = 0
        # Checking all sides
        if x+1 < self.X: # top
            self.DFSExteriorAirCubes(x+1, y, z)
        if x-1 >= 0: # bottom
            self.DFSExteriorAirCubes(x-1, y, z)
        if y+1 < self.Y: # left
            self.DFSExteriorAirCubes(x, y+1, z)
        if y-1 >= 0: # right
            self.DFSExteriorAirCubes(x, y-1, z)
        if z+1 < self.Z: # front
            self.DFSExteriorAirCubes(x, y, z+1)
        if z-1 >= 0: # back
            self.DFSExteriorAirCubes(x, y, z-1)

    def getExteriorSides(self):
        self.detectExteriorAirCubes()
        result = 0
        for i in range(self.X):
            for j in range(self.Y):
                for k in range(self.Z):
                    if self.grid[i][j][k]:
                        result += self.countCubeExteriorSides(i,j,k)
        return result

    def countCubeExteriorSides(self, x, y, z):
        result = 0
        if x == 0: result += 1
        if y == 0: result += 1
        if z == 0: result += 1
        # Checking all sides
        if x+1 < self.X and self.grid[x+1][y][z] == 0: # top
            result += 1
        if x-1 >= 0 and self.grid[x-1][y][z] == 0: # bottom
            result += 1
        if y+1 < self.Y and self.grid[x][y+1][z] == 0: # left
            result += 1
        if y-1 >= 0 and self.grid[x][y-1][z] == 0: # right
            result += 1
        if z+1 < self.Z and self.grid[x][y][z+1] == 0: # front
            result += 1
        if z-1 >= 0 and self.grid[x][y][z-1] == 0: # back
            result += 1
        return result
        