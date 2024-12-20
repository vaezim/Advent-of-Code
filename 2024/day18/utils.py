from queue import Queue


class Solver:
    def __init__(self, lines):
        self.exit = (70, 70)
        self.m = self.exit[0] + 1
        self.n = self.exit[1] + 1
        self.first_bytes = 1024
        self.bytes = self._ParseBytes(lines)
        self.grid = [[0] * (self.n) for _ in range(self.m)]

    def SolvePart1(self):
        for i in range(self.first_bytes):
            byte = self.bytes[i]
            self.grid[byte[1]][byte[0]] = 1
        return self._BFS((0,0))

    def SolvePart2(self):
        for i in range(self.first_bytes, len(self.bytes)):
            byte = self.bytes[i]
            self.grid[byte[1]][byte[0]] = 1
            if self._BFS((0,0)) == 0:
                return byte

    def _BFS(self, start):
        Q = Queue()
        Q.put(start)
        visited = { (0,0) }
        distances = [[0] * (self.n) for _ in range(self.m)]
        while not Q.empty():
            p = Q.get()
            x, y = p
            # Up
            if x > 0 and self.grid[x-1][y] == 0 and (x-1,y) not in visited:
                distances[x-1][y] = distances[x][y] + 1
                Q.put((x-1,y))
                visited.add((x-1,y))
            # Down
            if x < self.m-1 and self.grid[x+1][y] == 0 and (x+1,y) not in visited:
                distances[x+1][y] = distances[x][y] + 1
                Q.put((x+1,y))
                visited.add((x+1,y))
            # Left
            if y > 0 and self.grid[x][y-1] == 0 and (x,y-1) not in visited:
                distances[x][y-1] = distances[x][y] + 1
                Q.put((x,y-1))
                visited.add((x,y-1))
            # Right
            if y < self.n-1 and self.grid[x][y+1] == 0 and (x,y+1) not in visited:
                distances[x][y+1] = distances[x][y] + 1
                Q.put((x,y+1))
                visited.add((x,y+1))
        return distances[self.exit[0]][self.exit[1]]

    def _ParseBytes(self, lines):
        _bytes = []
        for line in lines:
            b1 = int(line[:line.index(',')])
            b2 = int(line[line.index(',')+1:])
            _bytes.append((b1,b2))
        return _bytes