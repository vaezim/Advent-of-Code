from copy import deepcopy


class Beam:
    def __init__(self, text=""):
        self.grid = None
        if len(text):
            self.grid = self._ProcessText(text)

    def GetTotalLoad(self, grid):
        total_load = 0
        for i in range(len(grid)):
            line = grid[i]
            num_rocks = line.count('O')
            total_load += (num_rocks * (len(grid)-i))
        return total_load

    def SpinALot(self, grid, cycles):
        initial_grid = deepcopy(grid)
        visited = {}
        period = None
        visited_grid_index = None

        # Find period
        for i in range(1, cycles+1):
            grid = self.Spin(grid)
            hash = self._GetHash(grid)
            if hash in visited:
                visited_grid_index = visited[hash]
                period = i - visited_grid_index
                print(f"[*] Already visited grid {visited_grid_index} after {i} spins")
                break
            visited[hash] = i

        # Optimize
        grid = deepcopy(initial_grid)
        for _ in range(visited_grid_index):
            grid = self.Spin(grid)
        periodic_cycle_num = ((cycles - visited_grid_index) // period)*period + visited_grid_index
        for _ in range(cycles - periodic_cycle_num):
            grid = self.Spin(grid)
        return grid

    def Spin(self, grid):
        grid = self.TiltNorth(grid)
        grid = self.TiltWest(grid)
        grid = self.TiltSouth(grid)
        grid = self.TiltEast(grid)
        return grid

    def TiltNorth(self, grid):
        for i, line in enumerate(grid):
            if i == 0: continue
            for j, c in enumerate(line):
                if c != 'O': continue
                grid[i][j] = '.'
                up = i
                while grid[up-1][j] == '.':
                    up -= 1
                    if up == 0: break
                grid[up][j] = 'O'
        return grid
    
    def TiltSouth(self, grid):
        for i in range(len(grid)-2,-1,-1):
            line = grid[i]
            for j, c in enumerate(line):
                if c != 'O': continue
                grid[i][j] = '.'
                down = i
                while grid[down+1][j] == '.':
                    down += 1
                    if down == len(grid)-1: break
                grid[down][j] = 'O'
        return grid

    def TiltEast(self, grid):
        for j in range(len(grid[0])-2,-1,-1):
            col = [grid[x][j] for x in range(len(grid))]
            for i, c in enumerate(col):
                if c != 'O': continue
                grid[i][j] = '.'
                right = j
                while grid[i][right+1] == '.':
                    right += 1
                    if right == len(grid)-1: break
                grid[i][right] = 'O'
        return grid
    
    def TiltWest(self, grid):
        for j in range(1, len(grid[0])):
            col = [grid[x][j] for x in range(len(grid))]
            for i, c in enumerate(col):
                if c != 'O': continue
                grid[i][j] = '.'
                left = j
                while grid[i][left-1] == '.':
                    left -= 1
                    if left == 0: break
                grid[i][left] = 'O'
        return grid

    def Print(self, grid):
        for line in grid:
            print(''.join(line))
        print()

    def _GetHash(self, grid):
        return ''.join([''.join(line) for line in grid])

    def _ProcessText(self, text):
        grid = [list(line.strip()) for line in text]
        return grid
    

if __name__ == "__main__":
    beam = Beam()
    grid = ["O....#....",
            "O.OO#....#",
            ".....##...",
            "OO.#O....O",
            ".O.....O#.",
            "O.#..O.#.#",
            "..O..#O..O",
            ".......O..",
            "#....###..",
            "#OO..#....",]
    grid = list(map(lambda x: list(x), grid))
    grid = beam.Spin(grid, 3)
    beam.Print(grid)