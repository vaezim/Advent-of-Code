
class LanternFish:
    def __init__(self, fish_ages):
        self.fish_ages = fish_ages
        self.mem = {} # (age,days) => fishNum

    def _GetFishNum(self, age, days):
        if age >= days or days <= 0:
            return 1
        if self.mem.get((age, days)) != None:
            return self.mem[(age, days)]

        ans = self._GetFishNum(6, days - age - 1) + self._GetFishNum(8, days - age - 1)
        self.mem[(age, days)] = ans
        return ans
    
    def GetFishNum(self, days):
        ans = 0
        for age in self.fish_ages:
            ans += self._GetFishNum(age, days)
        return ans
    
if __name__ == "__main__":
    lf = LanternFish([3])
    print(lf.GetFishNum(10))
    print(lf.GetFishNum(11))
    print(lf.GetFishNum(20))