from queue import Queue

class Grid:
    def __init__(self, num, width, height):
        self.num = num
        self.grid = self._BuildGrid(width, height)
        self.source = (1,1)
        self.destination = None
        self.visited = set()
        self.all_shortest_paths = [[float("inf")]*len(self.grid) for _ in range(len(self.grid[0]))]

    def _BuildGrid(self, width, height):
        self.grid = [[0]*width for _ in range(height)]
        for i in range(height):
            for j in range(width):
                if self._IsWall(i,j):
                    self.grid[i][j] = 1
        return self.grid
    
    def SetDestination(self, x, y):
        self.destination = (x,y)

    def FindShortestPath(self):
        self._FindAllShortestPaths()
        return self.all_shortest_paths[self.destination[0]][self.destination[1]]
    
    def GetLocationsCloserThan50(self):
        close_points = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == 0 and self.all_shortest_paths[i][j] <= 50:
                    close_points += 1
        return close_points
    
    def _FindAllShortestPaths(self):
        queue = Queue()
        queue.put((self.source, 0))
        while not queue.empty():
            item = queue.get()
            node, length = item[0], item[1]
            self.all_shortest_paths[node[0]][node[1]] = length
            self.visited.add(node)
            x, y = node
            # Up
            if x > 0 and self.grid[x-1][y] == 0 and (x-1,y) not in self.visited:
                queue.put(((x-1,y), length+1))
            # Down
            if x < len(self.grid)-1 and self.grid[x+1][y] == 0 and (x+1,y) not in self.visited:
                queue.put(((x+1,y), length+1))
            # Left
            if  y > 0 and self.grid[x][y-1] == 0 and (x,y-1) not in self.visited:
                queue.put(((x,y-1), length+1))
            # Right
            if  y < len(self.grid[0])-1 and self.grid[x][y+1] == 0 and (x,y+1) not in self.visited:
                queue.put(((x,y+1), length+1))

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
                if self.grid[i][j] == 0:
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


if __name__ == "__main__":
    grid = Grid(10, 20, 20)
    grid.SetDestination(7,4)
    print(grid.FindShortestPath())
