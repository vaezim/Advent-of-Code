# https://stackoverflow.com/questions/5084801/manhattan-distance-between-tiles-in-a-hexagonal-grid

class HexPathFinder:
    def __init__(self, text: str):
        self.pos = [0,0]
        self.path = None
        self.text = text
        self.dirMap = {
            "n":    self._n,
            "s":    self._s,
            "ne":   self._ne,
            "nw":   self._nw,
            "se":   self._se,
            "sw":   self._sw
        }

    def GetShortestPathLength(self):
        self.pos = [0,0]
        self.path = self.text.strip().split(',')
        for step in self.path:
            self.dirMap[step]()
        return self._GetDistance(self.pos, [0,0])
    
    def GetFurthestDistance(self):
        self.pos = [0,0]
        self.path = self.text.strip().split(',')
        maxDist = 0
        for step in self.path:
            self.dirMap[step]()
            maxDist = max(maxDist, self._GetDistance(self.pos, [0,0]))
        return maxDist

    def _GetDistance(self, p1, p2):
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        if dx * dy > 0:
            return abs(dx + dy)
        return max(abs(dx), abs(dy))

    def _n(self):   self.pos[1] += 1
    def _s(self):   self.pos[1] -= 1
    def _ne(self):  self.pos[0] += 1
    def _sw(self):  self.pos[0] -= 1
    def _se(self):
        self.pos[0] += 1
        self.pos[1] -= 1
    def _nw(self):
        self.pos[0] -= 1
        self.pos[1] += 1