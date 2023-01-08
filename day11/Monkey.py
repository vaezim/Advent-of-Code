from queue import deque


class Monkey():
    def __init__(self, idx, items, testNum, trueIdx, falseIdx):
        self.idx = idx
        self.items = deque(items)
        self.op = None # op is a lambda function
        self.test = testNum
        self.trueMonk = trueIdx
        self.falseMonk = falseIdx
        self.monkList = None
        self.inspecNum = 0
        self.cM = None

    def addMonkList(self, monkList):
        self.monkList = monkList

    def commonMultiplier(self, cM):
        self.cM = cM

    def addItem(self, item):
        self.items.append(item % self.cM)

    def round(self):
        while len(self.items):
            item = self.items.popleft()
            worry = self.op(item) # Add [// 3] for Part 1!
            if worry % self.test == 0:
                tM = self.monkList[self.trueMonk]
                tM.addItem(worry)
            else:
                fM = self.monkList[self.falseMonk]
                fM.addItem(worry)
            self.inspecNum += 1

    def defOp(self, op, num):
        if op == '*':
            if num == 'old':
                self.op = lambda x: x**2
            else:
                self.op = lambda x: x*int(num)
        elif op == '+':
            if num == 'old':
                self.op = lambda x: x*2
            else:
                self.op = lambda x: x+int(num)

    def printMonkey(self):
        print(f"Monkey {self.idx}")
        print(self.items, self.test, self.trueMonk, self.falseMonk)
        