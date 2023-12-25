class Hash:
    def __init__(self, line):
        self.line = line

    def GetSumLineHash(self):
        sum = 0
        words = self.line.strip().split(',')
        for w in words:
            sum += self._Hash(w)
        return sum

    def _Hash(self, s):
        curr = 0
        for c in s:
            curr += ord(c)
            curr = (17 * curr) % 256
        return curr
    

if __name__ == "__main__":
    hash = Hash("rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7")
    print(hash.GetSumLineHash())