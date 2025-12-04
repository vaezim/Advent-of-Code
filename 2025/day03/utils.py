class Solver:
    def __init__(self, lines):
        self.lines = lines
    
    def _FindLargestNDigits(self, line, N):
        digits = list(map(lambda x: int(x), list(line)))
        indices = []
        curr = 0
        for n in range(N, 0, -1):
            search_space = digits[curr:len(digits)-n+1]
            max_index = search_space.index(max(search_space)) + curr
            curr = max_index
            indices.append(curr)
            curr += 1
        output = ""
        for i in indices:
            output += str(digits[i])
        return int(output)

    def SolvePart1(self):
        sum = 0
        for line in self.lines:
            sum += self._FindLargestNDigits(line, 2)
        return sum

    def SolvePart2(self):
        sum = 0
        for line in self.lines:
            sum += self._FindLargestNDigits(line, 12)
        return sum
