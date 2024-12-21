class Solver:
    def __init__(self, lines):
        self.memoization = {}
        self.sentences = lines[2:]
        self.words = lines[0].split(", ")

    def SolvePart1(self):
        numPossible = 0
        for sentence in self.sentences:
            if self._CountPossibleWays(sentence) > 0:
                numPossible += 1
        return numPossible

    def SolvePart2(self):
        numWays = 0
        for sentence in self.sentences:
            numWays += self._CountPossibleWays(sentence)
        return numWays

    def _CountPossibleWays(self, sentence):
        # Memoization
        if self.memoization.get(sentence) != None:
            return self.memoization[sentence]
        # Recursion
        count = 0
        for word in self.words:
            if len(word) > len(sentence): continue
            if sentence == word:
                count += 1
                continue
            if sentence[:len(word)] == word:
                count += self._CountPossibleWays(sentence[len(word):])
        self.memoization[sentence] = count
        return count
