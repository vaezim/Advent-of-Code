from copy import deepcopy


class GameOfLife:
    def __init__(self, grid):
        self.grid = grid

    def Simulate(self, steps):
        for _ in range(steps):
            self._Step()
        S = 0
        M, N = len(self.grid), len(self.grid[0])
        for i in range(M):
            for j in range(N):
                S += self.grid[i][j]
        return S

    def _Step(self):
        grid = deepcopy(self.grid)
        M, N = len(self.grid), len(self.grid[0])
        for i in range(M):
            for j in range(N):
                numOnNeighbors = self._GetNumOnNeighbors(i, j)
                if self.grid[i][j] == 0 and numOnNeighbors == 3:
                    grid[i][j] = 1
                elif self.grid[i][j] == 1 and not (
                    numOnNeighbors == 2 or numOnNeighbors == 3
                ):
                    grid[i][j] = 0
        self.grid = grid

    def Simulate2(self, steps):
        M, N = len(self.grid), len(self.grid[0])
        self.grid[0][0] = 1
        self.grid[0][N - 1] = 1
        self.grid[M - 1][0] = 1
        self.grid[M - 1][N - 1] = 1
        for _ in range(steps):
            self._Step2()
        S = 0
        for i in range(M):
            for j in range(N):
                S += self.grid[i][j]
        return S

    def _Step2(self):
        grid = deepcopy(self.grid)
        M, N = len(self.grid), len(self.grid[0])
        restricted = [(0, 0), (0, N-1), (M-1, 0), (M-1, N-1)]
        for i in range(M):
            for j in range(N):
                if (i,j) in restricted:
                    continue
                numOnNeighbors = self._GetNumOnNeighbors(i, j)
                if self.grid[i][j] == 0 and numOnNeighbors == 3:
                    grid[i][j] = 1
                elif self.grid[i][j] == 1 and not (
                    numOnNeighbors == 2 or numOnNeighbors == 3
                ):
                    grid[i][j] = 0
        self.grid = grid

    def _GetNumOnNeighbors(self, i, j):
        num = 0
        M, N = len(self.grid), len(self.grid[0])
        neighbors = [
            (i - 1, j),
            (i - 1, j - 1),
            (i - 1, j + 1),
            (i + 1, j),
            (i + 1, j - 1),
            (i + 1, j + 1),
            (i, j - 1),
            (i, j + 1),
        ]
        for n in neighbors:
            if 0 <= n[0] < M and 0 <= n[1] < N:
                num += self.grid[n[0]][n[1]]
        return num
    