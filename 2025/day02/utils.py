class Solver:
    def __init__(self, lines):
        self.ranges = []
        for l in lines[0].split(','):
            a = int(l[:l.index('-')])
            b = int(l[l.index('-')+1:])
            self.ranges.append((a,b))

    def _IsInvalid1(self, a):
        str_a = str(a)
        if len(str_a) % 2 == 0 and str_a[:len(str_a)//2] == str_a[len(str_a)//2:]:
            return True
        return False
    
    def _IsInvalid2(self, a):
        str_a = str(a)
        for r in range(1,len(str_a)):
            if len(str_a) % r != 0:
                continue
            curr = str_a[:r]
            isInvalid = True
            for i in range(0, len(str_a), r):
                if str_a[i:i+r] != curr:
                    isInvalid = False
                    break
            if isInvalid:
                return True
        return False

    def SolvePart1(self):
        sum = 0
        for r in self.ranges:
            for i in range(r[0], r[1]+1):
                if self._IsInvalid1(i):
                    sum += i
        return sum

    def SolvePart2(self):
        sum = 0
        for r in self.ranges:
            for i in range(r[0], r[1]+1):
                if self._IsInvalid2(i):
                    sum += i
        return sum
