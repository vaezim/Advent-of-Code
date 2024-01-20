class Fractal:
    def __init__(self, lines) -> None:
        self.rules = self._Process(lines)

    def GetNumOnPixels(self):
        pass

    def _FindCorrespondingRule(self, grid):
        pass

    def _Process(self, lines):
        rules = {}  # (.../...) => (.../.../...)
        for line in lines:
            src, dst = line.split(" => ")[0].strip(), line.split(" => ")[1].strip()
            rules[tuple(src.split("/"))] = tuple(dst.split("/"))
        return rules
    