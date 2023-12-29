import math
from copy import deepcopy


class Mirror:
    def __init__(self, text=""):
        self.grids = None
        if len(text):
            self.grids = self._GetGrids(text)

    def GetSumMirrors(self):
        sum = 0
        for grid in self.grids:
            hor = self._FindHorMirror(grid)
            if hor != None:
                sum += 100 * hor
                continue
            ver = self._FindVerMirror(grid)
            if ver != None:
                sum += ver
                continue
            print("No mirror found!")
            print(grid)
            return None
        return sum

    def GetSumFixedMirrors(self):
        sum = 0
        for grid in self.grids:
            mirror = self._FindFixedMirror(grid)
            sum += mirror
        return sum

    def _FindFixedMirror(self, grid):
        initial_grid = deepcopy(grid)
        # Horizontal
        hor_smudges = self._GetHorSmudge(grid)
        for smudge in hor_smudges:
            grid = deepcopy(initial_grid)
            p1, p2 = smudge[0], smudge[1]
            grid[p1[0]][p1[1]] = grid[p2[0]][p2[1]]
            mirror = (p1[0] + p2[0]) / 2
            if self._IsHorMirror(grid, mirror):
                return math.ceil(mirror) * 100
            grid = deepcopy(initial_grid)
            grid[p2[0]][p2[1]] = grid[p1[0]][p1[1]]
            mirror = (p1[0] + p2[0]) / 2
            if self._IsHorMirror(grid, mirror):
                return math.ceil(mirror) * 100
        # Vertical
        ver_smudges = self._GetVerSmudge(grid)
        for smudge in ver_smudges:
            grid = deepcopy(initial_grid)
            p1, p2 = smudge[0], smudge[1]
            grid[p1[0]][p1[1]] = grid[p2[0]][p2[1]]
            mirror = (p1[1] + p2[1]) / 2
            if self._IsVerMirror(grid, mirror):
                return math.ceil(mirror)
            grid = deepcopy(initial_grid)
            grid[p2[0]][p2[1]] = grid[p1[0]][p1[1]]
            mirror = (p1[1] + p2[1]) / 2
            if self._IsVerMirror(grid, mirror):
                return math.ceil(mirror)
        return None

    def _IsHorMirror(self, grid, mirror):
        for i in range(len(grid)):
            if math.floor(mirror) - i < 0 or math.ceil(mirror) + i >= len(grid):
                break
            if grid[math.floor(mirror) - i] != grid[math.ceil(mirror) + i]:
                return False
        return True

    def _IsVerMirror(self, grid, mirror):
        cols = []
        for j in range(len(grid[0])):
            col = [grid[i][j] for i in range(len(grid))]
            cols.append("".join(col))
        return self._IsHorMirror(cols, mirror)

    def _GetHorSmudge(self, grid):
        all_opposites = []  # [(),()]
        for mirror in [0.5 + j for j in range(len(grid) - 1)]:
            opposites = []
            for i in range(len(grid)):
                if math.floor(mirror) - i < 0 or math.ceil(mirror) + i >= len(grid):
                    break
                opp_list = self._GetOppositeList(
                    grid[math.floor(mirror) - i], grid[math.ceil(mirror) + i]
                )
                for j in opp_list:
                    opposites.append(
                        [(math.floor(mirror) - i, j), (math.ceil(mirror) + i, j)]
                    )
            if len(opposites) == 1:
                all_opposites.extend(deepcopy(opposites))
        return all_opposites

    def _GetVerSmudge(self, grid):
        cols = []
        for j in range(len(grid[0])):
            col = [grid[i][j] for i in range(len(grid))]
            cols.append("".join(col))
        hor_smudges = self._GetHorSmudge(cols)
        ver_smudges = []
        for smudge in hor_smudges:
            ver_smudges.append(
                [(smudge[0][1], smudge[0][0]), (smudge[1][1], smudge[1][0])]
            )
        return ver_smudges

    def _GetOppositeList(self, s1, s2):
        opp_list = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                opp_list.append(i)
        return opp_list

    def _FindHorMirror(self, grid):
        for mirror in [0.5 + j for j in range(len(grid) - 1)]:
            IS_MIRROR = True
            for i in range(len(grid)):
                if math.floor(mirror) - i < 0 or math.ceil(mirror) + i >= len(grid):
                    break
                if grid[math.floor(mirror) - i] != grid[math.ceil(mirror) + i]:
                    IS_MIRROR = False
                    break
            if IS_MIRROR:
                return math.ceil(mirror)
        return None

    def _FindVerMirror(self, grid):
        cols = []
        for j in range(len(grid[0])):
            col = [grid[i][j] for i in range(len(grid))]
            cols.append("".join(col))
        for mirror in [0.5 + j for j in range(len(cols) - 1)]:
            IS_MIRROR = True
            for i in range(len(cols)):
                if math.floor(mirror) - i < 0 or math.ceil(mirror) + i >= len(cols):
                    break
                if cols[math.floor(mirror) - i] != cols[math.ceil(mirror) + i]:
                    IS_MIRROR = False
                    break
            if IS_MIRROR:
                return math.ceil(mirror)
        return None

    def _GetGrids(self, text):
        grids = []
        grid = []
        for line in text:
            if line == "\n":
                grids.append(grid.copy())
                grid.clear()
                continue
            grid.append(list(line.strip()))
        if len(grid):
            grids.append(grid)
        return grids

    def _Disp(self, grid):
        for line in grid:
            print("".join(line))


if __name__ == "__main__":
    mirror = Mirror()
    grid = [
        "#...##..#",
        "#...##..#",
        "..######.",
        ".#.###..#",
        "#...####.",
        ".#..###..",
        "#....#..#",
        "#.#.#....",
        "####..#.#",
        "####..#.#",
        "#.#.#....",
        "#....#..#",
        ".#..###..",
        "#...####.",
        ".#.###..#",
        "..#####..",
        "#...##..#",
    ]
    grid = list(map(lambda x: list(x), grid))
    print(mirror._GetHorSmudge(grid))
    print(mirror._GetVerSmudge(grid))
    print(mirror._FindFixedMirror(grid))
