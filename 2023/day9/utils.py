class Glider:
    def __init__(self, text):
        self.seqs = self._GetSeqs(text)

    def GetSumNextVals(self):
        sum = 0
        for seq in self.seqs:
            sum += self._GetNextVal(seq)
        return sum

    def GetSumPrevVals(self):
        sum = 0
        for seq in self.seqs:
            sum += self._GetPrevVal(seq)
        return sum

    def _GetPrevVal(self, seq):
        first_elements = [seq[0]]
        while not self._IsAllZeros(seq):
            for i in range(len(seq)-1):
                seq[i] = seq[i+1] - seq[i]
            first_elements.append(seq[0])
            seq.pop()
        prev = 0
        for i in range(len(first_elements)-1,-1,-1):
            prev = first_elements[i] - prev
        return prev

    def _GetNextVal(self, seq):
        last_elements = []
        while not self._IsAllZeros(seq):
            for i in range(len(seq)-1):
                seq[i] = seq[i+1] - seq[i]
            last_elements.append(seq.pop())
        return sum(last_elements)

    def _IsAllZeros(self, seq):
        for n in seq:
            if n != 0:
                return False
        return True

    def _GetSeqs(self, text):
        seqs = []
        for line in text:
            nums = list(map(lambda x: int(x), line.split()))
            seqs.append(nums)
        return seqs