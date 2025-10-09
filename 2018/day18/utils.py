from copy import deepcopy
from collections import defaultdict

class Land:
    def __init__(self, lines):
        for i in range(len(lines)):
            lines[i] = list(lines[i])
        self.initial_land = deepcopy(lines)
        self.land = lines

    def Reset(self):
        self.land = self.initial_land

    def PassNMinutes(self, n):
        index_map = defaultdict(list)
        for i in range(n):
            self._Pass1Minute()
            ans = self.GetNumTrees() * self.GetNumLumberyards()
            index_map[ans].append(i)
            if i > 1000: break
        if n < 1000: return
        # After about 500 minutes the shape of the
        # land gets repeated every [period] minutes
        max_key, max_len = 0, 0
        for i in index_map:
            if len(index_map[i]) > max_len:
                max_key, max_len = i, len(index_map[i])
        indexes = index_map[max_key]
        period = indexes[1] - indexes[0]
        self.Reset()
        # Once we get to the minute with shape [max_key]
        # the shape is repeated every [period] minutes
        # so we just need to run (n - max_key) % period minutes more
        for _ in range(indexes[0]):
            self._Pass1Minute()
        n -= indexes[0]
        for _ in range(n % period):
            self._Pass1Minute()

    def GetNumTrees(self):
        count = 0
        for i in range(len(self.land)):
            for j in range(len(self.land[i])):
                if self.land[i][j] == '|':
                    count += 1
        return count

    def GetNumLumberyards(self):
        count = 0
        for i in range(len(self.land)):
            for j in range(len(self.land[i])):
                if self.land[i][j] == '#':
                    count += 1
        return count

    def _Pass1Minute(self):
        new_land = deepcopy(self.land)
        for i in range(len(self.land)):
            for j in range(len(self.land[i])):
                if self.land[i][j] == '.' and self._GetNumAdjacentOf(i, j, '|') >= 3:
                    new_land[i][j] = '|'
                elif self.land[i][j] == '|' and self._GetNumAdjacentOf(i, j, '#') >= 3:
                    new_land[i][j] = '#'
                elif self.land[i][j] == '#' and (self._GetNumAdjacentOf(i, j, '#') == 0 or self._GetNumAdjacentOf(i, j, '|') == 0):
                    new_land[i][j] = '.'
        self.land = new_land

    def _GetNumAdjacentOf(self, i, j, c):
        adjucent = []
        M, N = len(self.land), len(self.land[0])
        dirs = [(-1,-1), (-1,0), (-1,1),
                (0,-1),          (0,1),
                (1,-1),  (1,0),  (1,1)]
        for di, dj in dirs:
            i2, j2 = i + di, j + dj
            if 0 <= i2 < M and 0 <= j2 < N:
                adjucent.append(self.land[i2][j2])
        return adjucent.count(c)
