class Network:
    def __init__(self, lines) -> None:
        self.network = lines
        self.WIDTH, self.HEIGHT = len(self.network[0]), len(self.network)
        self.start = self._GetStartingPos()
        self.steps = 0

    def RoutePacket(self):
        letters = []
        curr, dir = self.start.copy(), "S"
        while True:
            x, y = curr[0], curr[1]
            line_type = self.network[x][y]
            if not self._CanContinue(curr, dir) or self.network[x][y] == " ":
                break
            if line_type.isalpha():
                letters.append(line_type)
            # Corners (+)
            if line_type == "+":
                if dir in "NS":
                    if y > 0 and self.network[x][y - 1] != " ":
                        dir = "W"
                        curr[1] -= 1
                    elif y < self.WIDTH - 1 and self.network[x][y + 1] != " ":
                        dir = "E"
                        curr[1] += 1
                elif dir in "EW":
                    if x > 0 and self.network[x - 1][y] != " ":
                        dir = "N"
                        curr[0] -= 1
                    elif x < self.HEIGHT - 1 and self.network[x + 1][y] != " ":
                        dir = "S"
                        curr[0] += 1
            # Straight lines or Letters
            else:
                if dir == "N" and x > 0:
                    curr[0] -= 1
                elif dir == "S" and x < self.HEIGHT - 1:
                    curr[0] += 1
                elif dir == "W" and y > 0:
                    curr[1] -= 1
                elif dir == "E" and y < self.WIDTH - 1:
                    curr[1] += 1
            self.steps += 1
        return "".join(letters)

    def GetNumSteps(self):
        return self.steps

    def _CanContinue(self, curr_pos, dir):
        x, y = curr_pos[0], curr_pos[1]
        if dir == "N":
            return x > 0
        if dir == "S":
            return x < (self.HEIGHT - 1)
        if dir == "W":
            return y > 0
        if dir == "E":
            return y < (self.WIDTH - 1)

    def _GetStartingPos(self):
        for i in range(self.HEIGHT):
            for j in range(self.WIDTH):
                if self.network[i][j] == "|":
                    return [i, j]
