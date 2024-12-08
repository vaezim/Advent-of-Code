def ternary (n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))

class Solver:
    def __init__(self, lines):
        self.nums = []
        self.values = []
        self._ProcessLines(lines)

    def SolvePart1(self):
        sum = 0
        for i in range(len(self.values)):
            val = self.values[i]
            nums = self.nums[i]
            if self._IsPossible(val, nums, part=1):
                sum += val
        return sum

    def SolvePart2(self):
        sum = 0
        for i in range(len(self.values)):
            val = self.values[i]
            nums = self.nums[i]
            if self._IsPossible(val, nums, part=2):
                sum += val
        return sum

    def _IsPossible(self, val, nums, part):
        if part == 1:
            N = 2 ** (len(nums)-1)
        else:
            N = 3 ** (len(nums)-1)
        for i in range(N):
            if part == 1:
                _val = self._GenerateVal1(i, nums)
            else:
                _val = self._GenerateVal2(i, nums)
            if val == _val:
                return True
        return False

    def _GenerateVal1(self, index, nums):
        binary = bin(index)[2:].zfill(len(nums)-1)
        val = nums[0]
        for i, b in enumerate(binary):
            if b == '0':
                val += nums[i+1]
            else:
                val *= nums[i+1]
        return val

    def _GenerateVal2(self, index, nums):
        base3 = ternary(index)
        base3 = base3.zfill(len(nums)-1)
        val = nums[0]
        for i, b in enumerate(base3):
            if b == '0':
                val += nums[i+1]
            elif b == '1':
                val *= nums[i+1]
            else:
                val = int(f"{val}{nums[i+1]}")
        return val

    def _ProcessLines(self, lines):
        for line in lines:
            self.values.append(int(line[:line.index(':')]))
            nums = line[line.index(':')+1:].strip().split()
            nums = list(map(lambda x: int(x), nums))
            self.nums.append(nums.copy())
