class Container:
    def __init__(self, containers, total):
        self.total = total
        self.containers = containers

    def GetNumCombs(self):
        num = 0
        for c in range(2 ** len(self.containers)):
            b = bin(c)[2:][::-1]
            S = 0
            for i in range(len(b)):
                S += int(b[i]) * self.containers[i]
            num += S == self.total
        return num

    def GetMinNumCombs(self):
        M = self._GetMinComb()
        num = 0
        for c in range(2 ** len(self.containers)):
            b = bin(c)[2:][::-1]
            S = 0
            for i in range(len(b)):
                S += int(b[i]) * self.containers[i]
            if S == self.total and b.count("1") == M:
                num += 1
        return num

    def _GetMinComb(self):
        M = float("inf")
        for c in range(2 ** len(self.containers)):
            b = bin(c)[2:][::-1]
            S = 0
            for i in range(len(b)):
                S += int(b[i]) * self.containers[i]
            if S == self.total:
                M = min(M, b.count("1"))
        return M


if __name__ == "__main__":
    containers = [20, 15, 10, 5, 5]
    total = 25
    cont = Container(containers, total)
    print(cont.GetNumCombs())
    print(cont.GetMinNumCombs())
