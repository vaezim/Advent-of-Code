from queue import Queue
from itertools import permutations


class Hamilton:
    def __init__(self, text):
        self.grid = list(map(str.strip, text))
        self.nodes = self._GetNodes()  # node => (x,y)
        self.distances = {}  # (x1,y1,x2,y2) => dist
        self.visited = set()

    def GetShortestHamiltonianPath(self):
        nodes = self.nodes.keys()
        min_dist = float("inf")
        for perm in permutations(nodes):
            min_dist = min(min_dist, self._GetPermPathDistance(perm))
        return min_dist

    def GetShortestHamiltonianPathFromZeroToZero(self):
        nodes = list(self.nodes.keys())
        nodes.remove('0')
        min_dist = float("inf")
        for perm in permutations(nodes):
            new_perm = ['0']
            new_perm.extend(list(perm))
            new_perm.append('0')
            min_dist = min(min_dist, self._GetPermPathDistance(new_perm))
        return min_dist

    def _GetPermPathDistance(self, perm):
        dist = 0
        for i in range(len(perm)-1):
            dist += self._GetShortestDistance(self.nodes[perm[i]], self.nodes[perm[i+1]])
        return dist

    def _GetShortestDistance(self, node1, node2):
        x1, y1 = node1
        x2, y2 = node2
        if self.distances.get((x1,y1,x2,y2)) != None: return self.distances[(x1,y1,x2,y2)]
        if self.distances.get((x2,y2,x1,y1)) != None: return self.distances[(x2,y2,x1,y1)]
        self.visited.clear()
        Q = Queue()
        Q.put((x1,y1,0))
        while not Q.empty():
            x, y, dist = Q.get()
            if (x,y) in self.visited: continue
            self.visited.add((x,y))
            if x == x2 and y == y2:
                self.distances[(x1,y1,x2,y2)] = dist
                self.distances[(x2,y2,x1,y1)] = dist
                return dist
            if x > 0 and (x-1,y) not in self.visited and self.grid[x-1][y] != '#':
                Q.put((x-1,y,dist+1))
            if x < len(self.grid)-1 and (x+1,y) not in self.visited and self.grid[x+1][y] != '#':
                Q.put((x+1,y,dist+1))
            if y > 0 and (x,y-1) not in self.visited and self.grid[x][y-1] != '#':
                Q.put((x,y-1,dist+1))
            if y < len(self.grid[0])-1 and (x,y+1) not in self.visited and self.grid[x][y+1] != '#':
                Q.put((x,y+1,dist+1))
        return float("inf")

    def _GetNodes(self):
        nodes = {}
        for i, line in enumerate(self.grid):
            for j, c in enumerate(line):
                if c.isdigit():
                    nodes[c] = (i, j)
        return nodes


if __name__ == "__main__":
    grid = ["###########",
            "#0.1.....2#",
            "#.#######.#",
            "#4.......3#",
            "###########",]
    ham = Hamilton(grid)
    print(ham._GetShortestDistance((1,1),(1,2)))