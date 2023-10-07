from hashlib import sha256


class Medicine:
    def __init__(self, replacements, initial):
        self.initial = initial
        self.reps = replacements
        self.hashset = set()

    def GetNumUniqueMolecules(self):
        for rep in self.reps:
            self._AddMolecules(rep)
        return len(self.hashset)

    def _AddMolecules(self, rep):
        rep1, rep2 = rep[0], rep[1]
        rep1len = len(rep1)
        rep1idx = -1
        while True:
            rep1idx = self.initial.find(rep1, rep1idx+1)
            if rep1idx == -1:
                return
            tmpStr = self.initial[:rep1idx] + rep2 + self.initial[rep1idx+rep1len:]
            H = sha256(tmpStr.encode())
            self.hashset.add(H.digest())
    