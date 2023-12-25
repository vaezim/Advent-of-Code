class Pipes:
    def __init__(self, text):
        self.pipes = text
        self.S = self._GetSource()
        self.dst = None

    def _GetLoop(self):
        i, j = self.S
        while self.dst == None:
            pass

    def _GetSource(self):
        for i in range(len(self.pipes)):
            for j in range(len(self.pipes[i])):
                if self.pipes[i][j] == "S":
                    return (i,j)