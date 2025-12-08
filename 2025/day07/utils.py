class Solver:
    def __init__(self, lines):
        self.memo = {}
        self.lines = list(map(lambda x: list(x), lines))

    def SolvePart1(self):
        count = 0
        self.lines[0][self.lines[0].index('S')] = '|'
        for i in range(1, len(self.lines)):
            for j in range(len(self.lines[0])):
                if self.lines[i-1][j] != '|': continue
                if self.lines[i][j] == '.':
                    self.lines[i][j] = '|'
                elif self.lines[i][j] == '^':
                    count += 1
                    self.lines[i][j-1] = '|'
                    self.lines[i][j+1] = '|'
        return count

    def _FindNumTimelines(self, i, j):
        if i == len(self.lines) - 1 and self.lines[i][j] == '|':
            return 1
        if self.memo.get((i,j)) != None:
            return self.memo[(i,j)]
        if self.lines[i][j] == '|':
            return self._FindNumTimelines(i+1, j)
        if self.lines[i][j] == '^':
            result = self._FindNumTimelines(i+1, j-1) + self._FindNumTimelines(i+1, j+1)
            self.memo[(i,j)] = result
            return result

    def SolvePart2(self):
        return self._FindNumTimelines(0, self.lines[0].index('|'))
