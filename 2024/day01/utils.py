
class Lists:
    def __init__(self, lines):
        self.col1 = []
        self.col2 = []
        self.map2 = {}
        for line in lines:
            a, b = int(line.split()[0]), int(line.split()[1])
            self.col1.append(a)
            self.col2.append(b)
            if self.map2.get(b) == None:
                self.map2[b] = 1
            else:
                self.map2[b] += 1
        self.col1.sort()
        self.col2.sort()

    def GetSumDistances(self):
        sum = 0
        for i in range(len(self.col1)):
            sum += abs(self.col1[i] - self.col2[i])
        return sum
    
    def GetSimilarityScore(self):
        sum = 0
        for n in self.col1:
            if self.map2.get(n) != None:
                sum += (n * self.map2[n])
        return sum