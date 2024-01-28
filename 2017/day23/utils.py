class Assembly:
    def __init__(self, text):
        self.lines = list(map(str.strip, text))
        self.registers = {
            "a": 0,
            "b": 0,
            "c": 0,
            "d": 0,
            "e": 0,
            "f": 0,
            "g": 0,
            "h": 0,
        }
        self.mul_calls = 0

    def GetNumMulCalls(self):
        self.mul_calls = 0
        self._Run()
        return self.mul_calls

    def _Run(self):
        i = 0
        while i < len(self.lines):
            tokens = self.lines[i].split()
            instruction = tokens[0]
            if instruction == "set":
                self.registers[tokens[1]] = self._GetVal(tokens[2])
            elif instruction == "sub":
                self.registers[tokens[1]] -= self._GetVal(tokens[2])
            elif instruction == "mul":
                self.mul_calls += 1
                self.registers[tokens[1]] *= self._GetVal(tokens[2])
            elif instruction == "jnz" and self._GetVal(tokens[1]) != 0:
                i += self._GetVal(tokens[2])
                continue
            i += 1

    def _GetVal(self, x):
        if self.registers.get(x) != None:
            return self.registers[x]
        return int(x)
