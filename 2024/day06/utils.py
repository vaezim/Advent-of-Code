class Solver:
    def __init__(self, lines):
        self.grid = list(map(lambda x: list(x), lines))
        self.guard = self._FindGuard()
        self.covered_grid = [[0] * len(self.grid[0]) for _ in range(len(self.grid))]
        self.covered_grid[self.guard[0]][self.guard[1]] = 1
        self.dirs = [[-1,0], [0,1], [1,0], [0,-1]]

    def SolvePart1(self):
        self._WalkGuard()
        count = 0
        for i in range(len(self.covered_grid)):
            for j in range(len(self.covered_grid[0])):
                count += self.covered_grid[i][j]
        return count

    def SolvePart2(self):
        count = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] != '.': continue
                self.grid[i][j] = '#'
                if self._IsInLoop():
                    count += 1
                self.grid[i][j] = '.'
        return count

    def _IsInLoop(self):
        limit = 100_000
        return self._WalkGuard(limit)

    def _WalkGuard(self, limit=float("inf")):
        dir = 0
        steps = 0
        i, j = self.guard
        m, n = len(self.grid), len(self.grid[0])
        while i > 0 and i < m-1 and j > 0 and j < n-1 and steps <= limit:
            dir_i, dir_j = self.dirs[dir][0], self.dirs[dir][1]
            while self.grid[i+dir_i][j+dir_j] != '#':
                i += dir_i
                j += dir_j
                steps += 1
                self.covered_grid[i][j] = 1
                if i == 0 or i == m-1 or j == 0 or j == n-1:
                    break
            dir = (dir + 1) % len(self.dirs)
        return steps > limit

    def _FindGuard(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == '^':
                    return (i,j)
