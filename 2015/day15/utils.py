
class Ingred:
    def __init__(self):
        self.ingreds = []

    def AddIngred(self, ingred: tuple):
        self.ingreds.append(ingred)

    def FindMaximumScore(self):
        maxScore = 0
        for x1 in range(101):
            for x2 in range(101 - x1):
                for x3 in range(101 - x1 - x2):
                    x4 = 100 - x1 - x2 - x3
                    score = self._CalcScore([x1,x2,x3,x4])
                    maxScore = max(maxScore, score)
        return maxScore
    
    def FindMaximumScoreLimitedCal(self):
        maxScore = 0
        for x1 in range(101):
            for x2 in range(101 - x1):
                for x3 in range(101 - x1 - x2):
                    x4 = 100 - x1 - x2 - x3
                    if self._CalcCalories([x1,x2,x3,x4]) == 500:
                        score = self._CalcScore([x1,x2,x3,x4])
                        maxScore = max(maxScore, score)
        return maxScore

    def _CalcScore(self, xList):
        score = 1
        for attr in range(len(self.ingreds[0])-1):
            attrScore = 0
            for i in range(len(self.ingreds)):
                attrScore += xList[i] * self.ingreds[i][attr]
            score *= max(0, attrScore)
            if score == 0:
                return 0
        return score

    def _CalcCalories(self, xList):
        score = 0
        for i in range(len(self.ingreds)):
            score += self.ingreds[i][-1] * xList[i]
        return score

if __name__ == "__main__":
    ing = Ingred()
    ing.AddIngred((-1,-2,6,3,8))
    ing.AddIngred((2,3,-2,-1,3))

    print(ing.FindMaximumScore())
    print(ing.FindMaximumScoreLimitedCal())
    