class Solver:
    def __init__(self, text):
        self.text = text

    def SolvePart1(self):
        count = 0
        for i in range(len(self.text)):
            for j in range(len(self.text[0])):
                count += self._CountXmasFromPoint(i,j)
        return count

    def _CountXmasFromPoint(self, x, y):
        count = 0
        m, n = len(self.text), len(self.text[0])
        if self.text[x][y] != 'X':
            return 0
        # Right
        if y <= n - 4 and self.text[x][y:y+4] == "XMAS":
            count += 1
        # Left
        if y >= 3 and self.text[x][y-3:y+1] == "SAMX":
            count += 1
        # Up
        if x >= 3 and self.text[x-1][y] == 'M' and self.text[x-2][y] == 'A' and self.text[x-3][y] == 'S':
            count += 1
        # Down
        if x <= m - 4 and self.text[x+1][y] == 'M' and self.text[x+2][y] == 'A' and self.text[x+3][y] == 'S':
            count += 1
        # NE
        if x >= 3 and y <= n - 4 and self.text[x-1][y+1] == 'M' and self.text[x-2][y+2] == 'A' and self.text[x-3][y+3] == 'S':
            count += 1
        # NW
        if x >= 3 and y >= 3 and self.text[x-1][y-1] == 'M' and self.text[x-2][y-2] == 'A' and self.text[x-3][y-3] == 'S':
            count += 1
        # SE
        if x <= m - 4 and y <= n - 4 and self.text[x+1][y+1] == 'M' and self.text[x+2][y+2] == 'A' and self.text[x+3][y+3] == 'S':
            count += 1
        # SW
        if x <= m - 4 and y >= 3 and self.text[x+1][y-1] == 'M' and self.text[x+2][y-2] == 'A' and self.text[x+3][y-3] == 'S':
            count += 1
        return count

    def SolvePart2(self):
        count = 0
        for i in range(1, len(self.text)-1):
            for j in range(1, len(self.text[0])-1):
                count += self._CountX_MasFromPoint(i,j)
        return count
    
    def _CountX_MasFromPoint(self, x, y):
        count = 1
        if self.text[x][y] != 'A':
            return 0
        a = self.text[x-1][y-1] + "A" + self.text[x+1][y+1]
        b = self.text[x-1][y+1] + "A" + self.text[x+1][y-1]
        if a not in ["MAS", "SAM"]:
            return 0
        if b not in ["MAS", "SAM"]:
            return 0
        return 1
