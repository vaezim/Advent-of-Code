
class Solver:
    def __init__(self, lines):
        self.reports = []
        for line in lines:
            nums = list(map(lambda x: int(x), line.split()))
            self.reports.append(nums)

    def GetNumSafeReports(self):
        count = 0
        for nums in self.reports:
            if self._IsSafe(nums):
                count += 1
        return count

    def GetNumSafeReportsWithErrorCorrection(self):
        count = 0
        for nums in self.reports:
            if self._IsSafeWithCorrection(nums):
                count += 1
        return count

    def _IsSafe(self, nums):
        slope = 'i'
        if nums[1] < nums[0]:
            slope = 'd'
        for i in range(len(nums)-1):
            d = nums[i+1] - nums[i]
            if abs(d) < 1 or abs(d) > 3:
                return False
            if slope == 'i' and d < 0:
                return False
            if slope == 'd' and d > 0:
                return False
        return True
    
    def _IsSafeWithCorrection(self, nums):
        if self._IsSafe(nums):
            return True
        for i in range(len(nums)):
            new_nums = [nums[j] for j in range(len(nums)) if i != j]
            if self._IsSafe(new_nums):
                return True
        return False