from queue import Queue


class Solver:
    def __init__(self, lines):
        self.zones = []
        self.grid = lines
        self.visited = set()
        self.M = len(self.grid)
        self.N = len(self.grid[0])

        for i in range(self.M):
            for j in range(self.N):
                if (i,j) not in self.visited:
                    zone = self._ZoneBFS(i,j)
                    self.zones.append(zone)

    def SolvePart1(self):
        ans = 0
        for zone in self.zones:
            area = len(zone)
            perimeter = self._GetPerimiter(zone)
            ans += area * perimeter
        return ans

    def SolvePart2(self):
        ans = 0
        for zone in self.zones:
            area = len(zone)
            perimeter = self._GetNumSides(zone)
            ans += area * perimeter
        return ans

    def _GetPerimiter(self, zone):
        perimeter = 0
        for p in zone:
            perimeter += self._GetNumNeighbors(zone, p[0], p[1])
        return perimeter

    def _GetNumNeighbors(self, zone, i, j):
        count = 4
        if (i > 0) and ((i-1,j) in zone): count -= 1
        if (i < self.M-1) and ((i+1,j) in zone): count -= 1
        if (j > 0) and ((i,j-1) in zone): count -= 1
        if (j < self.N-1) and ((i,j+1) in zone): count -= 1
        return count

    def _GetNumSides(self, zone):
        sides = 0
        for p in zone:
            sides += self._GetNumPointies(zone, p[0], p[1])
        return sides

    def _GetNumPointies(self, zone, i, j):
        count = 0
        if ((i-1,j-1) not in zone and ((i-1,j) in zone and (i,j-1) in zone)) or\
           ((i-1,j-1) in zone and ((i-1,j) not in zone and (i,j-1) not in zone)) or\
           ((i-1,j-1) not in zone and (i-1,j) not in zone and (i,j-1) not in zone): count += 1
        if ((i-1,j+1) not in zone and ((i-1,j) in zone and (i,j+1) in zone)) or\
           ((i-1,j+1) in zone and ((i-1,j) not in zone and (i,j+1) not in zone)) or\
           ((i-1,j+1) not in zone and (i-1,j) not in zone and (i,j+1) not in zone): count += 1
        if ((i+1,j+1) not in zone and ((i+1,j) in zone and (i,j+1) in zone)) or\
           ((i+1,j+1) in zone and ((i+1,j) not in zone and (i,j+1) not in zone)) or\
           ((i+1,j+1) not in zone and (i+1,j) not in zone and (i,j+1) not in zone): count += 1
        if ((i+1,j-1) not in zone and ((i+1,j) in zone and (i,j-1) in zone)) or\
           ((i+1,j-1) in zone and ((i+1,j) not in zone and (i,j-1) not in zone)) or\
           ((i+1,j-1) not in zone and (i+1,j) not in zone and (i,j-1) not in zone): count += 1
        return count

    def _ZoneBFS(self, x, y):
        zone = set()
        zone.add((x,y))
        self.visited.add((x,y))
        flower = self.grid[x][y]

        queue = Queue()
        queue.put((x,y))

        while not queue.empty():
            point = queue.get()
            zone.add(point)
            i, j = point

            # Up
            if (i > 0) and (self.grid[i-1][j] == flower) and ((i-1,j) not in self.visited):
                self.visited.add((i-1,j))
                queue.put((i-1,j))
            # Down
            if (i < self.M-1) and (self.grid[i+1][j] == flower) and ((i+1,j) not in self.visited):
                self.visited.add((i+1,j))
                queue.put((i+1,j))
            # Left
            if (j > 0) and (self.grid[i][j-1] == flower) and ((i,j-1) not in self.visited):
                self.visited.add((i,j-1))
                queue.put((i,j-1))
            # Right
            if (j < self.N-1) and (self.grid[i][j+1] == flower) and ((i,j+1) not in self.visited):
                self.visited.add((i,j+1))
                queue.put((i,j+1))

        return zone