import re

class Solver:
    def __init__(self, text):
        self.text = text
        self.pattern = r"mul\(\d{1,3},\d{1,3}\)"

    def SolvePart1(self):
        sum = 0
        for mul in re.findall(self.pattern, self.text):
            a = int(mul[4:mul.index(',')])
            b = int(mul[mul.index(',')+1:-1])
            sum += a*b
        return sum
    
    def SolvePart2(self):
        sum = 0
        muls = re.findall(self.pattern, self.text)
        mul_indices = list(re.finditer(self.pattern, self.text))
        dos = list(re.finditer(r"do\(\)", self.text))
        donts = list(re.finditer(r"don't\(\)", self.text))
        spots = [0] * len(self.text)
        for item in dos:
            spots[item.start()] = 1
        for item in donts:
            spots[item.start()] = -1
        for i, mul in enumerate(muls):
            a = int(mul[4:mul.index(',')])
            b = int(mul[mul.index(',')+1:-1])
            index = mul_indices[i].start()
            while index >= 0 and spots[index] == 0:
                index -= 1
            if spots[index] != -1:
                sum += a*b
        return sum
