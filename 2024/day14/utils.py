import re

class Solver:
    def __init__(self, lines):
        self.M = 101
        self.N = 103
        self.time = 100
        self.speeds = []
        self.locations = []
        self._ProcessRobots(lines)

    def SolvePart1(self):
        ans = 1
        grid = [[0] * self.M for _ in range(self.N)]
        for robot_idx in range(len(self.locations)):
            loc = self._RunRobot(robot_idx, self.time)
            grid[loc[1]][loc[0]] += 1

        Q1, Q2, Q3, Q4 = 0, 0, 0, 0
        for i in range(self.N // 2):
            # NW
            for j in range(self.M // 2):
                Q1 += grid[i][j]
            # NE
            for j in range(self.M // 2 + 1, self.M):
                Q2 += grid[i][j]
        for i in range(self.N // 2 + 1, self.N):
            # SW
            for j in range(self.M // 2):
                Q3 += grid[i][j]
            # SE
            for j in range(self.M // 2 + 1, self.M):
                Q4 += grid[i][j]
        ans *= Q1 * Q2 * Q3 * Q4
        return ans

    def SolvePart2(self):
        for time in range(1, 10_000):
            visited = set()
            for robot_idx in range(len(self.locations)):
                loc = self._RunRobot(robot_idx, time)
                if tuple(loc) in visited:
                    break
                visited.add(tuple(loc))
            if len(visited) == len(self.locations):
                return time

    def _RunRobot(self, robot_idx, time):
        speed = self.speeds[robot_idx]
        loc = self.locations[robot_idx].copy()
        loc[0] = (loc[0] + time * speed[0]) % self.M
        loc[1] = (loc[1] + time * speed[1]) % self.N
        return loc

    def _ProcessRobots(self, lines):
        for line in lines:
            nums = re.findall(r"-?\d+", line)
            self.speeds.append((int(nums[2]), int(nums[3])))
            self.locations.append([int(nums[0]), int(nums[1])])