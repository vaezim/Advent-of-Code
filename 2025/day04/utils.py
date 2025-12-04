class Solver:
    def __init__(self, lines):
        self.grid = list(map(lambda x: list(x), lines))

    def _FindNumberOfAdjacentPapers(self, i, j):
        count = 0
        adjacents = [
            (-1,-1), (-1,0), (-1,1),
            (0,-1),          (0,1),
            (1,-1),  (1,0),  (1,1)
        ]
        for a in adjacents:
            i2, j2 = i + a[0], j + a[1]
            if 0 <= i2 < len(self.grid) and 0 <= j2 < len(self.grid[0]):
                count += (self.grid[i2][j2] == '@')
        return count

    def SolvePart1(self):
        count = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                if self.grid[i][j] == '@' and self._FindNumberOfAdjacentPapers(i,j) < 4:
                    count += 1
        return count

    def SolvePart2(self):
        count = 0
        while True:
            removed_one = False
            for i in range(len(self.grid)):
                for j in range(len(self.grid[0])):
                    if self.grid[i][j] == '@' and self._FindNumberOfAdjacentPapers(i,j) < 4:
                        count += 1
                        self.grid[i][j] = '.'
                        removed_one = True
            if not removed_one:
                break
        return count
