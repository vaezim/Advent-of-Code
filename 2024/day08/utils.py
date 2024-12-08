class Solver:
    def __init__(self, lines):
        self.grid = lines
        self.m = len(lines)
        self.n = len(lines[0])
        self.nodes = self._ParseAntennas()

    def SolvePart1(self):
        antinodes = set()
        for n in self.nodes:
            nodes = self.nodes[n]
            for i in range(len(nodes)):
                for j in range(i+1,len(nodes)):
                    n1, n2 = nodes[i], nodes[j]
                    anti1 = (2*n2[0]-n1[0],2*n2[1]-n1[1])
                    anti2 = (2*n1[0]-n2[0],2*n1[1]-n2[1])
                    if 0 <= anti1[0] < self.m and 0 <= anti1[1] < self.n:
                        antinodes.add(anti1)
                    if 0 <= anti2[0] < self.m and 0 <= anti2[1] < self.n:
                        antinodes.add(anti2)
        return len(antinodes)

    def SolvePart2(self):
        antinodes = set()
        for n in self.nodes:
            nodes = self.nodes[n]
            for i in range(len(nodes)):
                for j in range(i+1,len(nodes)):
                    n1, n2 = nodes[i], nodes[j]
                    dx, dy = n1[0]-n2[0], n1[1]-n2[1]
                    x, y = n1[0], n1[1]
                    while 0 <= x < self.m and 0 <= y < self.n:
                        antinodes.add((x,y))
                        x += dx
                        y += dy
                    x, y = n1[0], n1[1]
                    while 0 <= x < self.m and 0 <= y < self.n:
                        antinodes.add((x,y))
                        x -= dx
                        y -= dy
        return len(antinodes)

    def _ParseAntennas(self):
        nodes = {}
        for i in range(self.m):
            for j in range(self.n):
                c = self.grid[i][j]
                if c == '.': continue
                if nodes.get(c) == None:
                    nodes[c] = []
                nodes[c].append((i,j))
        return nodes
