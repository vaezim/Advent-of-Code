from copy import deepcopy


class Airplane:
    def __init__(self, text):
        self.original_grid = text
        self.grid = deepcopy(text)

    def GetNumOccupiedSeatsAfterStabalizing(self, mode):
        last_val = None
        num_reps = 0
        self.grid = deepcopy(self.original_grid)
        while num_reps < 10:
            self._Tick(mode)
            val = self._GetNumOccupiedSeats()
            if last_val != val:
                last_val = val
                num_reps = 0
            else:
                num_reps += 1
        return last_val

    def _Tick(self, mode):
        temp_grid = deepcopy(self.grid)
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                c = self.grid[i][j]
                if c == '.':
                    continue
                if mode == 1:
                    n = self._GetNumAdjacentOccupiedSeats(i, j)
                else:
                    n = self._GetNumAdjacentOccupiedSeatsMode2(i, j)
                if c == 'L' and n == 0:
                    temp_grid[i][j] = '#'
                elif c == '#':
                    if (mode == 1 and n >= 4) or (mode == 2 and n >= 5):
                        temp_grid[i][j] = 'L'
        self.grid = temp_grid

    def _GetNumAdjacentOccupiedSeats(self, i, j):
        empty = 8
        if i > 0:
            empty -= (self.grid[i-1][j] == '#')
            if j > 0:
                empty -= (self.grid[i-1][j-1] == '#')
            if j < len(self.grid[i])-1:
                empty -= (self.grid[i-1][j+1] == '#')
        if i < len(self.grid)-1:
            empty -= (self.grid[i+1][j] == '#')
            if j > 0:
                empty -= (self.grid[i+1][j-1] == '#')
            if j < len(self.grid[i])-1:
                empty -= (self.grid[i+1][j+1] == '#')
        if j > 0:
            empty -= (self.grid[i][j-1] == '#')
        if j < len(self.grid[i])-1:
            empty -= (self.grid[i][j+1] == '#')
        return 8 - empty

    def _GetNumAdjacentOccupiedSeatsMode2(self, ii, jj):
        empty = 8
        for i in range(ii-1, -1, -1):
            if self.grid[i][jj] != '.':
                if self.grid[i][jj] == '#':
                    empty -= 1
                break
        for i in range(ii+1, len(self.grid)):
            if self.grid[i][jj] != '.':
                if self.grid[i][jj] == '#':
                    empty -= 1
                break
        for j in range(jj-1, -1, -1):
            if self.grid[ii][j] != '.':
                if self.grid[ii][j] == '#':
                    empty -= 1
                break
        for j in range(jj+1, len(self.grid[ii])):
            if self.grid[ii][j] != '.':
                if self.grid[ii][j] == '#':
                    empty -= 1
                break
        i = ii
        j = jj
        while i > 0 and j > 0:
            i -= 1
            j -= 1
            if self.grid[i][j] != '.':
                if self.grid[i][j] == '#':
                    empty -= 1
                break
        i = ii
        j = jj
        while i > 0 and j < len(self.grid[0])-1:
            i -= 1
            j += 1
            if self.grid[i][j] != '.':
                if self.grid[i][j] == '#':
                    empty -= 1
                break
        i = ii
        j = jj
        while i < len(self.grid)-1 and j > 0:
            i += 1
            j -= 1
            if self.grid[i][j] != '.':
                if self.grid[i][j]  == '#':
                    empty -= 1
                break
        i = ii
        j = jj
        while i < len(self.grid)-1 and j < len(self.grid[0])-1:
            i += 1
            j += 1
            if self.grid[i][j] != '.':
                if self.grid[i][j]  == '#':
                    empty -= 1
                break
        return 8 - empty

    def _GetNumOccupiedSeats(self):
        count = 0
        for row in self.grid:
            count += row.count('#')
        return count
    
    def _Print(self):
        for row in self.grid:
            print(''.join(row))
        print("\n\n")