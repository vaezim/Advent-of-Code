from copy import deepcopy


class Solver:
    def __init__(self, lines):
        self.grid = [list(map(int, list(line))) for line in lines]
        self.m = len(self.grid)
        self.n = len(self.grid[0])

    def SolvePart1(self):
        count = 0
        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] == 0:
                    allTrails = self._FindallTrails((i,j))
                    uniqueNines = set()
                    for trail in allTrails:
                        uniqueNines.add(trail[-1])
                    count += len(uniqueNines)
        return count

    def SolvePart2(self):
        count = 0
        for i in range(self.m):
            for j in range(self.n):
                if self.grid[i][j] == 0:
                    allTrails = self._FindallTrails((i,j))
                    count += len(allTrails)
        return count

    def _FindallTrails(self, point):
        x, y = point
        allTrails = []
        self._DFS([(x,y)], set(), allTrails)
        return allTrails

    def _DFS(self, curr, visited, allTrails):
        x, y = curr[-1]
        val = self.grid[x][y]
        if val == 9:
            allTrails.append(deepcopy(curr))
            return
        # Up
        if (x > 0) and (self.grid[x-1][y] == val+1) and ((x-1,y) not in visited):
            curr.append((x-1,y))
            visited.add((x-1,y))
            self._DFS(curr, visited, allTrails)
            curr.pop()
            visited.remove((x-1,y))
        # Down
        if (x < self.m-1) and (self.grid[x+1][y] == val+1) and ((x+1,y) not in visited):
            curr.append((x+1,y))
            visited.add((x+1,y))
            self._DFS(curr, visited, allTrails)
            curr.pop()
            visited.remove((x+1,y))
        # Left
        if (y > 0) and (self.grid[x][y-1] == val+1) and ((x,y-1) not in visited):
            curr.append((x,y-1))
            visited.add((x,y-1))
            self._DFS(curr, visited, allTrails)
            curr.pop()
            visited.remove((x,y-1))
        # Right
        if (y < self.n-1) and (self.grid[x][y+1] == val+1) and ((x,y+1) not in visited):
            curr.append((x,y+1))
            visited.add((x,y+1))
            self._DFS(curr, visited, allTrails)
            curr.pop()
            visited.remove((x,y+1))
