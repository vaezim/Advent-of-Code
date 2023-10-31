from hashlib import md5

class KeyGenerator:
    def __init__(self, salt: str) -> None:
        self.salt = salt
        self.hashes = []

    def Get64thKey(self, strech: bool = False):
        self._GenerateHashes(50000, strech)
        foundNum = 0
        for index in range(len(self.hashes)-1000):
            foundNum += self._IsKey(index)
            if foundNum == 64:
                return index
        return -1 * foundNum

    def _IsKey(self, index: int):
        triple = self._ContainsTriple(self.hashes[index])
        if not triple:
            return False
        for i in range(index+1,index+1001):
            if self._ContainsFiveple(self.hashes[i], triple[0]):
                return True
        return False
    
    def _ContainsTriple(self, s: str) -> bool:
        for i in range(len(s)-2):
            if s[i] == s[i+1] == s[i+2]:
                return s[i:i+3]
        return False
        
    def _ContainsFiveple(self, s: str, c: str) -> bool:
        for i in range(len(s)-5):
            if c == s[i] == s[i+1] == s[i+2] == s[i+3] == s[i+4]:
                return True
        return False
    
    def _GenerateHashes(self, num: int, strech: bool = False):
        self.hashes.clear()
        for i in range(num):
            s = self.salt+str(i)
            if strech:
                for _ in range(2016):
                    s = md5(s.encode()).hexdigest()
            self.hashes.append(md5(s.encode()).hexdigest())


if __name__ == "__main__":
    salt = "abc"
    key_gen = KeyGenerator(salt)
    print("Part 1:", key_gen.Get64thKey())
    print("Part 2:", key_gen.Get64thKey(strech=True))
