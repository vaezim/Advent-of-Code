class Joltage:
    def __init__(self, text):
        self.nums = [0] + sorted(list(map(lambda x: int(x.strip()), text)))
        self.nums.append(self.nums[-1] + 3)
        self.DP = {}  # index => num_arrangements

    def GetNumArrangements(self):
        return self._GetNumArrangements(0)

    def _GetNumArrangements(self, index):
        if self.DP.get(index) != None:
            return self.DP[index]
        next_indices = []
        curr = self.nums[index]
        for i in range(index + 1, len(self.nums)):
            next = self.nums[i]
            if next > curr + 3:
                break
            next_indices.append(i)
        if not len(next_indices):
            self.DP[index] = 1
            return 1
        res = 0
        for next in next_indices:
            res += self._GetNumArrangements(next)
        self.DP[index] = res
        return res

    def Get1JoltTimes3JoltDiffs(self):
        one_diffs, three_diffs = 0, 0
        for i in range(len(self.nums) - 1):
            diff = self.nums[i + 1] - self.nums[i]
            if diff == 1:
                one_diffs += 1
            elif diff == 3:
                three_diffs += 1
        return one_diffs * three_diffs
