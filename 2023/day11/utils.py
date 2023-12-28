import copy


class Galaxy:
    def __init__(self, text):
        self.cosmos = self._ProcessText(text)
        self.emptyRows = sorted(self._GetEmptyRows())
        self.emptyCols = sorted(self._GetEmptyColumns())
        self.galaxies = self._GetGalaxies()

    def GetSumDistances(self, expansion_size=1):
        S = 0
        for i in range(len(self.galaxies)):
            for j in range(i + 1, len(self.galaxies)):
                S += self._GetDistance(self.galaxies[i], self.galaxies[j], expansion_size)
        return S

    def _GetGalaxies(self):
        galaxies = []
        for i in range(len(self.cosmos)):
            for j in range(len(self.cosmos[i])):
                if self.cosmos[i][j] == 1:
                    galaxies.append((i, j))
        return galaxies

    def _GetDistance(self, p1, p2, expansion_size=1):
        x1, y1 = p1
        x2, y2 = p2
        expanded_row_num = self._GetListNumsInRange(self.emptyRows, min(x1,x2), max(x1,x2))
        expanded_col_num = self._GetListNumsInRange(self.emptyCols, min(y1,y2), max(y1,y2))
        return abs(x1 - x2) + abs(y1 - y2) + (expanded_col_num + expanded_row_num) * (expansion_size-1)

    def _GetListNumsInRange(self, arr, low, high):
        count = 0
        for n in arr:
            if n > high:
                return count
            if n >= low:
                count += 1
        return count

    def _ProcessText(self, text):
        cosmos = [[0] * len(text[0]) for _ in range(len(text))]
        for i in range(len(text)):
            for j in range(len(text[i])):
                if text[i][j] == "#":
                    cosmos[i][j] = 1
        return cosmos

    def _GetEmptyColumns(self):
        cols = []
        for j in range(len(self.cosmos[0])):
            S = 0
            for i in range(len(self.cosmos)):
                S += self.cosmos[i][j]
            if S == 0:
                cols.append(j)
        return cols

    def _GetEmptyRows(self):
        rows = []
        for i in range(len(self.cosmos)):
            if sum(self.cosmos[i]) == 0:
                rows.append(i)
        return rows
