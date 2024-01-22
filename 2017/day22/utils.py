class Worm:
    def __init__(self, grid):
        self.infected = set()
        self.node_states = {}  # States: Clean 0, Weak 1, Infected 2, Flagged, 3
        self.pos = [12, 12]
        self.dir = "U"
        self.dirs = ["U", "R", "D", "L"]
        self._Process(grid)

    def GetNumInfectingBursts1(self, burst_num):
        res = 0
        for _ in range(burst_num):
            res += self._Burst1()
        return res

    def GetNumInfectingBursts2(self, burst_num):
        self.dir = "U"
        self.pos = [len(self.grid) // 2, len(self.grid[0]) // 2]
        res = 0
        for _ in range(burst_num):
            res += self._Burst2()
        return res

    def _Burst2(self):
        INFECTED = False
        x, y = self.pos[0], self.pos[1]
        if (
            self.node_states.get((x, y)) == None or self.node_states[(x, y)] == 0
        ):  # Clean
            self.node_states[(x, y)] = 0
            self.dir = self.dirs[(self.dirs.index(self.dir) - 1)]
        else:
            state = self.node_states[(x, y)]
            if state == 1:  # Weak
                INFECTED = True
            elif state == 2:  # Infected
                self.dir = self.dirs[(self.dirs.index(self.dir) + 1) % len(self.dirs)]
            elif state == 3:  # Flagged
                self.dir = self.dirs[(self.dirs.index(self.dir) - 2)]
        self.node_states[(x, y)] = (self.node_states[(x, y)] + 1) % 4
        if self.dir == "U":
            self.pos[0] -= 1
        elif self.dir == "R":
            self.pos[1] += 1
        elif self.dir == "D":
            self.pos[0] += 1
        elif self.dir == "L":
            self.pos[1] -= 1
        return INFECTED

    def _Burst1(self):
        INFECTED = False
        x, y = self.pos[0], self.pos[1]
        if (x, y) in self.infected:
            self.dir = self.dirs[(self.dirs.index(self.dir) + 1) % len(self.dirs)]
            self.infected.remove((x, y))
        else:
            self.dir = self.dirs[(self.dirs.index(self.dir) - 1)]
            self.infected.add((x, y))
            INFECTED = True
        if self.dir == "U":
            self.pos[0] -= 1
        elif self.dir == "R":
            self.pos[1] += 1
        elif self.dir == "D":
            self.pos[0] += 1
        elif self.dir == "L":
            self.pos[1] -= 1
        return INFECTED

    def _Process(self, grid):
        self.grid = list(map(str.strip, grid))
        for i in range(len(self.grid)):
            for j in range(len(self.grid)):
                if self.grid[i][j] == "#":
                    self.infected.add((i, j))
                    self.node_states[(i, j)] = 2
        self.pos = [len(self.grid) // 2, len(self.grid[0]) // 2]
