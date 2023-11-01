class CheckSum:
    def __init__(self, input, disk_size):
        self.input = input
        self.disk_size = disk_size

    def GetCheckSum(self):
        output = self.input
        while len(output) < self.disk_size:
            output = self._GetDragonCurve(output)
        output = output[:self.disk_size]
        return self._GetCheckSum(output)

    def _GetDragonCurve(self, s: str):
        b = list(s[::-1])
        for i in range(len(b)):
            if b[i] == '0':
                b[i] = '1'
            elif b[i] == '1':
                b[i] = '0'
        return s + '0' + ''.join(b)
    
    def _GetCheckSum(self, s: str):
        while len(s) % 2 == 0:
            checkSum = ""
            for i in range(0, len(s), 2):
                if s[i] == s[i+1]:
                    checkSum += "1"
                else:
                    checkSum += "0"
            s = checkSum
        return s
    

if __name__ == "__main__":
    checkSum = CheckSum(input="10000", disk_size=20)
    print(checkSum._GetDragonCurve("1"))
    print(checkSum._GetCheckSum("110010110100"))
    print(checkSum.GetCheckSum())