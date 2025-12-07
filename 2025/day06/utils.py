import re


class Solver:
    def __init__(self, lines):
        self.nums1 = []
        self.signs = re.findall(r"[\+*]", lines[-1])

        for i in range(len(lines)-1):
            nums1 = re.findall(r"\d+", lines[i])
            nums1 = list(map(lambda x: int(x), nums1))
            self.nums1.append(nums1)

        curr = ["" for _ in range(len(lines)-1)]
        self.num_strs = []
        for i in range(len(lines[0])):
            found_separator = True
            for j in range(len(lines)-1):
                if lines[j][i].isnumeric():
                    found_separator = False
                    break
            if found_separator:
                self.num_strs.append(curr)
                curr = ["" for _ in range(len(lines)-1)]
                continue
            for j in range(len(lines)-1):
                curr[j] += lines[j][i]
        self.num_strs.append(curr)

    def SolvePart1(self):
        sum = 0
        for i in range(len(self.nums1[0])):
            s = 0 if self.signs[i] == '+' else 1
            if self.signs[i] == '+':
                for j in range(len(self.nums1)):
                    s += self.nums1[j][i]
            elif self.signs[i] == '*':
                for j in range(len(self.nums1)):
                    s *= self.nums1[j][i]
            sum += s
        return sum

    def SolvePart2(self):
        sum = 0
        for num_str_i, item in enumerate(self.num_strs):
            nums = []
            for i in range(len(item[0])): # digit index
                n = ""
                for j in range(len(item)):
                    n += item[j][i]
                nums.append(int(n))
            s = 0 if self.signs[num_str_i] == '+' else 1
            if self.signs[num_str_i] == '+':
                for i in range(len(nums)):
                    s += nums[i]
            elif self.signs[num_str_i] == '*':
                for i in range(len(nums)):
                    s *= nums[i]
            sum += s
        return sum
