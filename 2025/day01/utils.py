from math import floor


class Solver:
    def __init__(self, lines):
        self.nums = []
        for l in lines:
            n = int(l[1:])
            if l[0] == 'L':
                n *= -1
            self.nums.append(n)

    def SolvePart1(self):
        count = 0
        curr = 50
        for n in self.nums:
            curr = (curr + n) % 100
            if curr == 0:
                count += 1
        return count

    def SolvePart2(self):
        count = 0
        curr = 50
        for n in self.nums:
            curr2 = curr + n
            count += abs(floor(curr / 100) - floor(curr2 / 100))
            curr = curr2 % 100
        return count
