class Xmas:
    def __init__(self, text):
        self.nums = list(map(lambda x: int(x.strip()), text))
        self.anomaly = None

    def GetEncryptionWeakness(self):
        i, j, Sum = 0, 0, self.nums[0]
        while Sum != self.anomaly and i <= j:
            if Sum < self.anomaly:
                j += 1
                Sum += self.nums[j]
            else:
                Sum -= self.nums[i]
                i += 1
        nums = self.nums[i:j+1]
        return min(nums) + max(nums)

    def GetAnomaly(self):
        for i in range(len(self.nums)):
            if self._IsAnomaly(i):
                self.anomaly = self.nums[i]
                return self.nums[i]

    def _IsAnomaly(self, index):
        if index < 25:
            return False
        num = self.nums[index]
        possible_nums = set(self.nums[index-25:index])
        for n in possible_nums:
            if num-n in possible_nums:
                return False
        return True