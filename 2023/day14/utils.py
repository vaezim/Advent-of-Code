import copy

class Beam:
    def __init__(self, text):
        self.grid = self._ProcessText(text)

    def GetTotalNorthLoad(self):
        tilted_north = self._TiltNorth()
        total_load = 0
        for i in range(len(tilted_north)):
            line = tilted_north[i]
            num_rocks = line.count('O')
            total_load += (num_rocks * (len(tilted_north)-i))
        return total_load

    def _TiltNorth(self):
        grid = copy.deepcopy(self.grid)
        for i, line in enumerate(grid):
            if i == 0: continue
            for j, c in enumerate(line):
                if c != 'O': continue
                grid[i][j] = '.'
                down = i
                while grid[down-1][j] == '.':
                    down -= 1
                    if down == 0: break
                grid[down][j] = 'O'
        return grid

    def Print(self, grid):
        for line in grid:
            print(''.join(line))

    def _ProcessText(self, text):
        grid = [list(line.strip()) for line in text]
        return grid