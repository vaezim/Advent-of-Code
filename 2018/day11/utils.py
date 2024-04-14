class Fuel:
    def __init__(self, serial):
        self.serial = serial
        self.cell_power_map = dict()
        self.grid = [[0] * 300 for _ in range(300)]
        self._FillGrid()

    def GetMaxTotalPowerCoordinates(self) -> tuple:
        Max, max_x, max_y = 0, 0, 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                cell_power = self._GetCellPower(i,j)
                if cell_power > Max:
                    Max = cell_power
                    max_x = j+1
                    max_y = i+1
        return max_x, max_y

    def GetMaxTotalPowerCoordinates2(self) -> tuple:
        Max, x, y, size = 0, 0, 0, 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                for s in range(1,len(self.grid)):
                    cell_power = self._GetCellPower2(i,j,s)
                    if cell_power > Max:
                        Max = cell_power
                        x, y, size = j+1, i+1, s
        return (x, y, size)

    def _GetCellPower2(self, i, j, size):
        # Memoization
        memo = self.cell_power_map.get((i,j,size))
        if memo != None:
            return memo
        # Check boundaries
        if size == 0:
            return 0
        if max(i+size-1,j+size-1) >= len(self.grid):
            return -1
        # Sub-cell with size=size-1
        cell_power = self._GetCellPower2(i,j,size-1)
        for k in range(size):
            cell_power += self.grid[i+size-1][j+k]
        for k in range(size):
            cell_power += self.grid[i+k][j+size-1]
        cell_power -= self.grid[i+size-1][j+size-1]
        self.cell_power_map[(i,j,size)] = cell_power
        return cell_power

    def _GetCellPower(self, i, j):
        if i >= len(self.grid)-2 or j >= len(self.grid[0])-2:
            return 0
        return self.grid[i][j] + self.grid[i][j+1] + self.grid[i][j+2] + \
               self.grid[i+1][j] + self.grid[i+1][j+1] + self.grid[i+1][j+2] + \
               self.grid[i+2][j] + self.grid[i+2][j+1] + self.grid[i+2][j+2]

    def _FillGrid(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                self.grid[i][j] = self._GetPower(j+1,i+1)

    def _GetPower(self, i, j):
        rack_id = i + 10
        power = rack_id * j
        power += self.serial
        power *= rack_id
        power = power % 1000
        power = power // 100
        power -= 5
        return power