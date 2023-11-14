class Generator:
    def __init__(self, saltA, saltB):
        self.saltA = saltA
        self.saltB = saltB
        self.factorA = 16807
        self.factorB = 48271
        self.rem = 2147483647

    def GetJudgeCount(self):
        a = self.saltA
        b = self.saltB
        count = 0
        for _ in range(4 * 10**7):
            count += self._Match(a, b)
            a = (a * self.factorA % self.rem)
            b = (b * self.factorB % self.rem)
        return count
    
    def GetJudgeCount2(self):
        a = self.saltA
        b = self.saltB
        count = 0
        for _ in range(5 * 10**6):
            count += self._Match(a, b)
            a = (a * self.factorA % self.rem)
            while a % 4 != 0:
                a = (a * self.factorA % self.rem)
            b = (b * self.factorB % self.rem)
            while b % 8 != 0:
                b = (b * self.factorB % self.rem)
        return count

    def _Match(self, a, b):
        bin_a = bin(a)[2:].zfill(16)
        bin_b = bin(b)[2:].zfill(16)
        return bin_a[-16:] == bin_b[-16:]


if __name__ == "__main__":
    gen = Generator(65, 8921)
    print(gen.GetJudgeCount())
    print(gen.GetJudgeCount2())