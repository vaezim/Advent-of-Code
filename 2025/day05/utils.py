class Solver:
    def __init__(self, lines):
        self.ids = []
        self.ranges = []
        for line in lines:
            if '-' in line:
                a, b = int(line[:line.index('-')]), int(line[line.index('-')+1:])
                self.ranges.append([a,b])
            elif len(line):
                self.ids.append(int(line))
        
        self.ranges.sort(key=lambda x: x[0])
        for i in range(len(self.ranges)-1):
            a1, b1 = self.ranges[i][0], self.ranges[i][1]
            for j in range(i+1, len(self.ranges)):
                a2, b2 = self.ranges[j][0], self.ranges[j][1]
                if b2 > b1: break
                self.ranges[j] = [0,0]
            for j in range(i+1, len(self.ranges)):
                a2, b2 = self.ranges[j][0], self.ranges[j][1]
                if a2 == 0: continue
                if a2 > b1: break
                self.ranges[j][0] = self.ranges[i][1]+1

    def SolvePart1(self):
        count = 0
        for id in self.ids:
            for range in self.ranges:
                if range[0] <= id <= range[1]:
                    count += 1
                    break
        return count

    def SolvePart2(self):
        sum = 0
        for range in self.ranges:
            a, b = range[0], range[1]
            if a == 0:
                continue
            sum += (b - a + 1)
        return sum
