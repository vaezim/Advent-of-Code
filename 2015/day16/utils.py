
class Aunt:
    def __init__(self, sender: dict):
        self.sender = sender
        self.aunts = []

    def AddAunt(self, aunt: dict):
        self.aunts.append(aunt)

    def FindSenderIndex(self, mode=1):
        maxScore = 0
        maxIndex = -1
        for i, aunt in enumerate(self.aunts):
            if mode == 1:
                score = self.GetCorrelationScore1(aunt)
            elif mode == 2:
                score = self.GetCorrelationScore2(aunt)
            if score > maxScore:
                maxScore = score
                maxIndex = i+1
        return maxIndex

    def GetCorrelationScore1(self, aunt: dict):
        score = 0
        for attr in aunt.keys():
            score += aunt[attr] == self.sender[attr]
        return score

    def GetCorrelationScore2(self, aunt: dict):
        score = 0
        for attr in aunt.keys():
            if attr == "cats" or attr == "trees":
                score += aunt[attr] > self.sender[attr]
            elif attr == "pomeranians" or attr == "goldfish":
                score += aunt[attr] < self.sender[attr]
            else:
                score += aunt[attr] == self.sender[attr]
        return score
    