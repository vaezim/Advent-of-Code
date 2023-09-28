from itertools import permutations

class Happiness:
    def __init__(self, happiness):
        self.happiness = happiness
        self.people = list(happiness.keys())

    def GetMaximumHappiness(self):
        Max = 0
        for p in permutations(self.people):
            Max = max(Max, self._GetHappiness(p))
        return Max

    def _GetHappiness(self, permutation):
        happiness = 0
        for i, person in enumerate(permutation):
            happiness += self.happiness[person][permutation[i-1]] + \
                         self.happiness[person][permutation[(i+1) % len(permutation)]]
        return happiness
    