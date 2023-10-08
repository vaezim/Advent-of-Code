from hashlib import sha256


class Medicine:
    def __init__(self, replacements, initial):
        self.initial = initial
        self.reps = replacements
        self.hashset = set()
        self.RnMolecules = {}

    def GetNumUniqueMolecules(self):
        for rep in self.reps:
            self._AddMolecules(rep)
        return len(self.hashset)
    
    def GetMinNumReplacements(self):
        return self._Format()

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
    
    # Rn => (
    # Y  => ,
    # Ar => )
    def _Format(self):
        numChanges = 0
        duplicates = []
        #( , ) in reps
        for i, rep in enumerate(self.reps):
            self.reps[i][1] = self.reps[i][1].replace("Rn", '(').\
                                              replace("Y" , ',').\
                                              replace("Ar", ')')
            if rep[1] == rep[0]*2:
                duplicates.append(rep[0])
        # ( , ) in initial
        self.initial = self.initial.replace("Rn", '(').\
                                    replace("Y" , ',').\
                                    replace("Ar", ')')
        
        def ApplyReplacements():
            n = 0
            for i, rep in enumerate(self.reps):
                n += self.initial.count(rep[1])
                self.initial = self.initial.replace(rep[1], rep[0])
            return n
        def RemoveDuplications():
            n = 0
            for dup in duplicates:
                len1 = len(self.initial)
                self.initial = self.initial.replace(dup*2, dup)
                len2 = len(self.initial)
                n += (len2-len1)//2
            return n

        while self.initial != "e":
            while True:
                n = ApplyReplacements()
                if n == 0:
                    break
                numChanges += n
            while True:
                n = RemoveDuplications()
                if n == 0:
                    break
                numChanges += n
        
        return numChanges
    