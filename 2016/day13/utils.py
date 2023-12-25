class Grid:
    def __init__(self, num):
        self.num = num
        self.grid = None
        self.source = (1,1)
        self.destination = None
        self.visited = set()
        self.shortest_path = {self.source}

    def BuildGrid(self, width, height):
        self.grid = [[0]*width for _ in range(height)]
        for i in range(height):
            for j in range(width):
                if self._IsWall(i,j):
                    self.grid[i][j] = 1
        return self.grid
    
    def SetDestination(self, x, y):
        self.destination = (x,y)
        self.shortest_path.add(self.destination)

    def FindShortestPath(self):
        if self.destination == None or self.grid == None:
            return -1
        self.visited.clear()
        return self._FindShortestPath(self.source)
    
    def GetLocationsCloserThan50(self):
        close_points = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                self.SetDestination(i,j)
                # Code Here #
        return close_points
    
    def Disp(self):
        if self.grid == None:
            print("[-] Grid is None")
            return
        print('   ',end="")
        for j in range(len(self.grid[0])):
            print(j//10,end="")
        print()
        print('   ',end="")
        for j in range(len(self.grid[0])):
            print(j%10, end="")
        print()
        for i in range(len(self.grid)):
            if i < 10:
                print(' ',end="")
            print(i,end=" ")
            for j in range(len(self.grid[i])):
                if (i,j) in self.shortest_path:
                    print('O',end="")
                elif self.grid[i][j] == 0:
                    print('.',end="")
                else:
                    print('#',end="")
            print()
        print()

    def _GetPolynomial(self, x, y):
        # x*x + 3*x + 2*x*y + y + y*y
        return x**2 + 3*x + 2*x*y + y + y**2 + self.num

    def _IsWall(self, x, y):
        poly = self._GetPolynomial(x, y)
        binary = bin(poly)
        return binary.count('1') % 2 == 1
    
    def _FindShortestPath(self, src):
        x, y = src[0], src[1]
        if self.grid[x][y] == 1:
            return float("inf")
        self.visited.add((x,y))

        # Base Case
        if x == self.destination[0] and y == self.destination[1]:
            self.visited.remove((x,y))
            return 0
        
        paths = [float("inf")] * 4
        locations = [(x,y-1), (x,y+1), (x-1,y), (x+1,y)]
        # left
        if y-1 >= 0 and self.grid[x][y-1] == 0 and (x,y-1) not in self.visited:
            paths[0] = self._FindShortestPath((x,y-1))
        # right
        if y+1 < len(self.grid[0]) and self.grid[x][y+1] == 0 and (x,y+1) not in self.visited:
            paths[1] = self._FindShortestPath((x,y+1))
        # top
        if x-1 >= 0 and self.grid[x-1][y] == 0 and (x-1,y) not in self.visited:
            paths[2] = self._FindShortestPath((x-1,y))
        # bottom
        if x+1 < len(self.grid) and self.grid[x+1][y] == 0 and (x+1,y) not in self.visited:
            paths[3] = self._FindShortestPath((x+1,y))

        M = min(paths)
        if M != float("inf"):
            self.shortest_path.add(locations[paths.index(M)])
        self.visited.remove((x,y))

        return 1 + M


if __name__ == "__main__":
    grid = Grid(10)
    grid.BuildGrid(20,20)
    grid.SetDestination(7,4)
    print(grid.FindShortestPath())
    grid.Disp()
