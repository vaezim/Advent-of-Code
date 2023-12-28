from copy import deepcopy


class Pipes:
    def __init__(self, text):
        self.pipes = list(map(lambda x: list(x.strip()), text))
        self.S = self._GetSource()
        self.loop = None
        self.visited = set()
        self.outside_expanded_loop = set()  # Part 2
        self.expanded_pipes = None  # Part 2
        self.dir_funcs = {  # (dir, pipe) => next_node func
            ("U", "|"): lambda x: (x[0] - 1, x[1]),
            ("U", "F"): lambda x: (x[0], x[1] + 1),
            ("U", "7"): lambda x: (x[0], x[1] - 1),
            ("D", "|"): lambda x: (x[0] + 1, x[1]),
            ("D", "J"): lambda x: (x[0], x[1] - 1),
            ("D", "L"): lambda x: (x[0], x[1] + 1),
            ("L", "-"): lambda x: (x[0], x[1] - 1),
            ("L", "L"): lambda x: (x[0] - 1, x[1]),
            ("L", "F"): lambda x: (x[0] + 1, x[1]),
            ("R", "-"): lambda x: (x[0], x[1] + 1),
            ("R", "7"): lambda x: (x[0] + 1, x[1]),
            ("R", "J"): lambda x: (x[0] - 1, x[1]),
        }
        self.expanded_pipe_shapes = {
            "|": [[0, 1, 0], [0, 1, 0], [0, 1, 0]],
            "-": [[0, 0, 0], [1, 1, 1], [0, 0, 0]],
            "L": [[0, 1, 0], [0, 1, 1], [0, 0, 0]],
            "F": [[0, 0, 0], [0, 1, 1], [0, 1, 0]],
            "J": [[0, 1, 0], [1, 1, 0], [0, 0, 0]],
            "7": [[0, 0, 0], [1, 1, 0], [0, 1, 0]],
            "S": [[0, 0, 0], [0, 1, 0], [0, 0, 0]],
        }

    def GetFarthestPointInLoop(self):
        loop = self._GetLoop()
        loop_len = len(loop)
        return loop_len // 2

    def GetLoopArea(self):
        self._GetExpandedPipes()
        self.loop_set = set(self.loop)
        self._BFS()
        area = 0
        for i in range(len(self.pipes)):
            for j in range(len(self.pipes[0])):
                ii, jj = 3 * i + 1, 3 * j + 1
                if (ii, jj) not in self.outside_expanded_loop and (
                    i,
                    j,
                ) not in self.loop_set:
                    area += 1
        return area

    def _BFS(self):
        outside_expanded_loop = (0, 0)  # definitely outside expanded loop
        queue = [outside_expanded_loop]
        while len(queue):
            node = queue.pop()
            if node in self.outside_expanded_loop:
                continue
            ii, jj = node
            if self.expanded_pipes[ii][jj] == 1:
                continue
            if ii > 0:
                queue.append((ii - 1, jj))
            if ii < len(self.expanded_pipes) - 1:
                queue.append((ii + 1, jj))
            if jj > 0:
                queue.append((ii, jj - 1))
            if jj < len(self.expanded_pipes[0]) - 1:
                queue.append((ii, jj + 1))
            self.outside_expanded_loop.add(node)

    def _GetExpandedPipes(self):
        if self.expanded_pipes != None:
            return self.expanded_pipes
        loop = self._GetLoop()
        self.expanded_pipes = [
            [0] * (3 * len(self.pipes[0])) for _ in range(3 * len(self.pipes))
        ]
        for node in loop:
            self._FillExpandedPipes(node)
        return self.expanded_pipes

    def _FillExpandedPipes(self, node):
        i, j = node
        pipe = self.pipes[i][j]
        ii, jj = 3 * i + 1, 3 * j + 1
        mat = deepcopy(self.expanded_pipe_shapes[pipe])
        if pipe == "S":
            # Up
            if i > 0 and self.pipes[i - 1][j] in "|F7":
                mat[0][1] = 1
            # Down
            if i < len(self.pipes) - 1 and self.pipes[i + 1][j] in "|LJ":
                mat[2][1] = 1
            # Left
            if j > 0 and self.pipes[i][j - 1] in "-FL":
                mat[1][0] = 1
            # Right
            if j < len(self.pipes[0]) - 1 and self.pipes[i][j + 1] in "-J7":
                mat[1][2] = 1
        for i in range(3):
            for j in range(3):
                self.expanded_pipes[ii + i - 1][jj + j - 1] = mat[i][j]

    def _GetLoop(self):
        if self.loop != None:
            return self.loop
        loop = [self.S]
        curr = self._GetNextFromSource()
        loop.append(curr)
        while loop[-1] != self.S:
            next = self._GetNextFromPath(loop)
            loop.append(next)
        self.loop = loop
        return self.loop

    def _GetNextFromPath(self, path):
        prev, curr = path[-2], path[-1]
        i, j = curr
        curr_pipe = self.pipes[i][j]
        dir = self._GetDirection(prev, curr)
        dir_func = self.dir_funcs[(dir, self.pipes[i][j])]
        return dir_func(curr)

    def _GetNextFromSource(self):
        i, j = self.S
        # Up
        if i > 0 and self.pipes[i - 1][j] in "|F7":
            return (i - 1, j)
        # Down
        if i < len(self.pipes) - 1 and self.pipes[i + 1][j] in "|LJ":
            return (i + 1, j)
        # Left
        if j > 0 and self.pipes[i][j - 1] in "-FL":
            return (i, j - 1)
        # Right
        if j < len(self.pipes[0]) - 1 and self.pipes[i][j + 1] in "-J7":
            return (i, j + 1)
        return None

    def _GetDirection(self, prev, curr):
        i1, j1 = prev
        i2, j2 = curr
        if i1 == i2:
            if j2 == j1 - 1:
                return "L"
            if j2 == j1 + 1:
                return "R"
        if j1 == j2:
            if i2 == i1 - 1:
                return "U"
            if i2 == i1 + 1:
                return "D"
        return None

    def _GetSource(self):
        for i in range(len(self.pipes)):
            for j in range(len(self.pipes[i])):
                if self.pipes[i][j] == "S":
                    return (i, j)

    def _DispExpanded(self):
        for line in self.expanded_pipes:
            for c in line:
                if c == 0:
                    print(".", end="")
                else:
                    print("X", end="")
            print()
