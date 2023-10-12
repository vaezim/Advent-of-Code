
class CodeGenerator:
    def __init__(self):
        self.firstCode = 20151125
        self.lastCode = 20151125

    def GetCode(self, row, col):
        self.lastCode = self.firstCode
        code_diag = row + col - 1
        code_index = ((code_diag-1) * (code_diag) // 2) + col
        for _ in range(code_index-1):
            self.lastCode = self._NextCode()
        return self.lastCode

    def _NextCode(self):
        return (self.lastCode * 252533) % 33554393
    

if __name__ == "__main__":
    generator = CodeGenerator()
    print(generator.GetCode(1,1))
    print(generator.GetCode(1,2))
    print(generator.GetCode(1,3))
    print(generator.GetCode(6,6))
