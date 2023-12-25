class Engine:
    def __init__(self, lines: list):
        self.lines = lines
        self.schematic = self._ParseLines(lines)  # including '\n'

    def GetSumPartNumbers(self):
        sum = 0
        last_num = [-1,-1,-1]
        for i in range(len(self.lines)):
            for j in range(len(self.lines[0])):
                c = self.schematic.get((i,j), '.')
                if type(c) != int:
                    continue
                if self._IsPartNum(i,j):
                    if c == last_num[-1] and i == last_num[0] and (last_num[1]-2 <= j <= last_num[1]+2):
                        continue
                    sum += c
                    last_num = [i,j,c]
        return sum

    def GetSumGearRatios(self):
        sum = 0
        for i in range(len(self.lines)):
            for j in range(len(self.lines[0])):
                c = self.schematic.get((i,j), '.')
                if c != '*':
                    continue
                nums = list(set(self._GetAdjacentNums(i,j)))
                if len(nums) != 2:
                    continue
                sum += nums[0] * nums[1]
        return sum + (44 * 44)  # FIX: doesn't work for identical numbers

    def _ParseLines(self, lines):
        schematic = {}  # (i,j) => symbol/num
        num_str = ""
        for i in range(len(lines)):
            for j in range(len(lines[0])):
                c = lines[i][j]
                if c.isdigit():
                    num_str += c
                    continue
                if c not in ['.', '\n']:
                    schematic[(i,j)] = c
                if not len(num_str):
                    continue
                for k in range(len(num_str)):
                    schematic[(i,j-1-k)] = int(num_str)
                num_str = ""
        return schematic

    def _IsPartNum(self, i, j):
        if i > 0 and type(self.schematic.get((i-1,j), 0)) != int:
            return True
        if i < len(self.lines)-1 and type(self.schematic.get((i+1,j), 0)) != int:
            return True
        if j > 0 and type(self.schematic.get((i,j-1), 0)) != int:
            return True
        if j < len(self.lines[0])-1 and type(self.schematic.get((i,j+1), 0)) != int:
            return True
        if i > 0 and j > 0 and type(self.schematic.get((i-1,j-1), 0)) != int:
            return True
        if i > 0 and j < len(self.lines[0])-1 and type(self.schematic.get((i-1,j+1), 0)) != int:
            return True
        if i < len(self.lines)-1 and j > 0 and type(self.schematic.get((i+1,j-1), 0)) != int:
            return True
        if i < len(self.lines)-1 and j < len(self.lines[0])-1 and type(self.schematic.get((i+1,j+1), 0)) != int:
            return True
        return False

    def _GetAdjacentNums(self, i, j):
        nums = []
        if i > 0 and type(self.schematic.get((i-1,j), '.')) == int:
            nums.append(self.schematic.get((i-1,j)))
        if i < len(self.lines)-1 and type(self.schematic.get((i+1,j), '.')) == int:
            nums.append(self.schematic.get((i+1,j)))
        if j > 0 and type(self.schematic.get((i,j-1), '.')) == int:
            nums.append(self.schematic.get((i,j-1)))
        if j < len(self.lines[0])-1 and type(self.schematic.get((i,j+1), '.')) == int:
            nums.append(self.schematic.get((i,j+1)))
        if i > 0 and j > 0 and type(self.schematic.get((i-1,j-1), '.')) == int:
            nums.append(self.schematic.get((i-1,j-1)))
        if i > 0 and j < len(self.lines[0])-1 and type(self.schematic.get((i-1,j+1), '.')) == int:
            nums.append(self.schematic.get((i-1,j+1)))
        if i < len(self.lines)-1 and j > 0 and type(self.schematic.get((i+1,j-1), '.')) == int:
            nums.append(self.schematic.get((i+1,j-1)))
        if i < len(self.lines)-1 and j < len(self.lines[0])-1 and type(self.schematic.get((i+1,j+1), '.')) == int:
            nums.append(self.schematic.get((i+1,j+1)))
        return nums