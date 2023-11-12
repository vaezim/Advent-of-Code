class FireWall:
    def __init__(self, layers: str):
        self.layers = {}  # depth => range
        self._ParseLayers(layers)
        self.layer_num = max(self.layers.keys())

    def GetSeverity(self, delay=0):
        severity = 0
        for t in range(self.layer_num+1):
            if self.layers.get(t) == None:
                continue
            r = self.layers[t]
            if self._GetScannerDepth(t+delay, r) == 0:
                severity += t * r
                self.caught = True
        return severity

    def GetLeastDelay(self):
        delay = 0
        while True:
            self.caught = False
            self.GetSeverity(delay)
            if self.caught == False:
                return delay
            delay += 1

    def _GetScannerDepth(self, t, range):
        t = t % (2*(range-1))
        if t < range:
            return t
        return range - (t % range + 1)

    def _ParseLayers(self, text: str):
        for line in text:
            depth = int(line[:line.index(':')])
            range = int(line[line.index(':')+1:].strip())
            self.layers[depth] = range


if __name__ == "__main__":
    layers = """
            0: 3
            1: 2
            4: 4
            6: 4
    """
    firewall = FireWall(layers.strip().split('\n'))
    print(firewall.GetSeverity())
    print(firewall.GetLeastDelay())