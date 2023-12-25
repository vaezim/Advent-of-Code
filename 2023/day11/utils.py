import copy

class Galaxy:
    def __init__(self, text):
        self.cosmos = self._ProcessText(text)
        self.emptyRows = self._GetEmptyRows()
        self.emptyCols = self._GetEmptyColumns()
        self.expanded = self._GetExpandedCosmos()
        self.galaxies = self._GetGalaxies()

    def GetSumDistances(self):
        S = 0
        for i in range(len(self.galaxies)):
            for j in range(i+1,len(self.galaxies)):
                S += self._GetDistance(self.galaxies[i], self.galaxies[j])
        return S
    
    def _GetGalaxies(self):
        galaxies = []
        for i in range(len(self.expanded)):
            for j in range(len(self.expanded[i])):
                if self.expanded[i][j] == 1:
                    galaxies.append((i,j))
        return galaxies

    def _GetDistance(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return abs(x1-x2) + abs(y1-y2)

    def _GetExpandedCosmos(self, size):
        expanded = []
        for i in range(len(self.cosmos)):
            row = []
            for j in range(len(self.cosmos[i])):
                row.append(self.cosmos[i][j])
                if j in self.emptyCols:
                    row.append(self.cosmos[i][j])
            expanded.append(row)
            if i in self.emptyRows:
                expanded.append(row.copy())
        return expanded

    def _ProcessText(self, text):
        cosmos = [[0] * len(text[0]) for _ in range(len(text))]
        for i in range(len(text)):
            for j in range(len(text[i])):
                if text[i][j] == '#':
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