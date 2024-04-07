import re

class Sky:
    def __init__(self, text):
        self.points = list()
        self.velocities = list()
        self._ProcessText(text)

    def AreAllStarsInGrid(self, size):
        for p in self.points:
            x, y = p[0], p[1]
            if abs(x) > size//2 or abs(y) > size//2:
                return False
        return True

    def Disp(self, size):
        grid = [[' ' for _ in range(size)] for _ in range(size)]
        for p in self.points:
            x, y = p[0], p[1]
            if abs(x) < size//2 and abs(y) < size//2:
                grid[-y+size//2][x+size//2] = '*'
        for row in grid:
            print(''.join(row))

    def Time(self, seconds=1):
        for i, point in enumerate(self.points):
            point[0] += self.velocities[i][0] * seconds
            point[1] += self.velocities[i][1] * seconds

    def _ProcessText(self, text):
        for line in text:
            nums = re.findall(r"-?\d+", line)
            nums = list(map(lambda x: int(x), nums))
            self.points.append([nums[0],nums[1]])
            self.velocities.append((nums[2],nums[3]))