class Onsen:
    def __init__(self, text=[]):
        self.text = list(map(lambda x: x.strip(), text))
        self.springs = self._GetSprings()
        self.arrangements = self._GetArrangements()
        self.DP = {}

    def GetSumCorrectArrangements(self, unfold=1):
        sum = 0
        for i in range(len(self.springs)):
            ans = self._GetNumCorrectArrangements('?'.join([self.springs[i]]*unfold), self.arrangements[i]*unfold)
            sum += ans
        return sum

    def _GetNumCorrectArrangements(self, spring, arr):
        # Base cases
        spring = spring.strip('.')
        if len(arr) == 0:
            return int('#' not in spring)
        if len(spring) == 0:
            return int(len(arr) == 0)
        # DP
        state = (spring, tuple(arr))
        if self.DP.get(state) != None:
            return self.DP[state]
        # Recursion
        res = 0
        # (first => '.')
        if spring[0] == '?':
            res += self._GetNumCorrectArrangements(spring[1:], arr)
        # (first => '#')
        if spring[0] in "?#":
            if arr[0] <= len(spring) and '.' not in spring[:arr[0]] and (len(spring) == arr[0] or spring[arr[0]] != '#'):
                res += self._GetNumCorrectArrangements(spring[arr[0]+1:], arr[1:])
        self.DP[state] = res
        return res

    def _IsCorrectArrangement(self, spring, arr):
        curr = 0
        spring_arr = []
        for n in spring:
            if n == ".":
                if curr > 0:
                    spring_arr.append(curr)
                curr = 0
                continue
            if n == "#":
                curr += 1
        if curr > 0:
            spring_arr.append(curr)
        return spring_arr == arr

    def _GetSprings(self):
        springs = []
        for line in self.text:
            springs.append(line.split()[0])
        return springs

    def _GetArrangements(self):
        arrangements = []
        for line in self.text:
            s = line.split()[1].split(",")
            s = list(map(lambda x: int(x), s))
            arrangements.append(s)
        return arrangements


if __name__ == "__main__":
    onsen = Onsen()
    print(onsen._GetNumCorrectArrangements(".??..??...?##.", [1,1,3]))
    print(onsen.DP)