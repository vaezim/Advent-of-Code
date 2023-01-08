from Monkey import Monkey
from math import ceil


with open('input.txt', 'r') as file:
    lines = file.readlines()

monkeyList = []
for m in range(ceil(len(lines)/7)): # number of monkeys
    idx = m
    desc = lines[m*7:(m+1)*7]
    # Getting Items list
    items = list(map(lambda x: int(x), desc[1][18:-1].split(', ')))
    # Operation
    op = desc[2][23]
    num = desc[2][25:-1]
    # Test
    testNum = int(desc[3][desc[3].index('by')+2:-1])
    # Next monkeys
    trueIdx, falseIdx = int(desc[4][-2]), int(desc[5][-2])
    # create a new Monkey
    newMonkey = Monkey(idx, items, testNum, trueIdx, falseIdx)
    newMonkey.defOp(op, num)
    monkeyList.append(newMonkey)

# Add monkey list to each monkey and get cM
cM = 1
for monkey in monkeyList:
    monkey.addMonkList(monkeyList)
    cM *= monkey.test
for monkey in monkeyList:
    monkey.commonMultiplier(cM)

# 20 Rounds (Uncomment for Part 1!)
#for i in range(20):
#    for monkey in monkeyList:
#        monkey.round()

inspections = [m.inspecNum for m in monkeyList]
inspections.sort(reverse=True)
print(f"Answer of Part 1: {inspections[0]*inspections[1]}")

# 10000 Rounds
for i in range(10000):
    for monkey in monkeyList:
        monkey.round()

inspections = [m.inspecNum for m in monkeyList]
inspections.sort(reverse=True)
print(f"Answer of Part 2: {inspections[0]*inspections[1]}")
