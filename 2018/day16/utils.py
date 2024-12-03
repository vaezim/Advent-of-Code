from copy import deepcopy

class Solver:
    def __init__(self, lines, program):
        self.registers = [0, 0, 0, 0]
        self.samples = self._ParseLines(lines)
        self.program = self._ParseProgram(program)
        self.op_codes = {
            "_addr": self._addr,
            "_addi": self._addi,
            "_mulr": self._mulr,
            "_muli": self._muli,
            "_banr": self._banr,
            "_bani": self._bani,
            "_borr": self._borr,
            "_bori": self._bori,
            "_setr": self._setr,
            "_seti": self._seti,
            "_gtir": self._gtir,
            "_gtri": self._gtri,
            "_gtrr": self._gtrr,
            "_eqir": self._eqir,
            "_eqri": self._eqri,
            "_eqrr": self._eqrr,
        }
        self.op_ids = [None] * len(self.op_codes)
        self.found_op_set = set()

    def CountNumSamplesBehavingLikeThreeOrMoreOpCodes(self):
        count = 0
        for sample in self.samples:
            possible_ops = []
            a, b, c = sample[1][1], sample[1][2], sample[1][3]
            for op_code in self.op_codes:
                self.registers = deepcopy(sample[0])
                self.op_codes[op_code](a, b, c)
                if self.registers == sample[2]:
                    possible_ops.append(op_code)
            if len(possible_ops) >= 3:
                count += 1
        return count

    def RunProgram(self):
        while not self._IsSolved():
            for sample in self.samples:
                possible_ops = []
                id, a, b, c = sample[1][0], sample[1][1], sample[1][2], sample[1][3]
                for op_code in self.op_codes:
                    if op_code in self.found_op_set:
                        continue
                    self.registers = deepcopy(sample[0])
                    self.op_codes[op_code](a, b, c)
                    if self.registers == sample[2]:
                        possible_ops.append(op_code)
                if len(possible_ops) == 1 and self.op_ids[id] == None:
                    self.op_ids[id] = possible_ops[0]
                    self.found_op_set.add(possible_ops[0])
        self.registers = [0, 0, 0, 0]
        for instruction in self.program:
            id, a, b, c = instruction[0], instruction[1], instruction[2], instruction[3]
            self.op_codes[self.op_ids[id]](a, b, c)
        return self.registers[0]

    def _IsSolved(self):
        for item in self.op_ids:
            if item == None:
                return False
        return True

    def _addr(self, a, b, c):
        self.registers[c] = self.registers[a] + self.registers[b]
    def _addi(self, a, b, c):
        self.registers[c] = self.registers[a] + b
    def _mulr(self, a, b, c):
        self.registers[c] = self.registers[a] * self.registers[b]
    def _muli(self, a, b, c):
        self.registers[c] = self.registers[a] * b
    def _banr(self, a, b, c):
        self.registers[c] = self.registers[a] & self.registers[b]
    def _bani(self, a, b, c):
        self.registers[c] = self.registers[a] & b
    def _borr(self, a, b, c):
        self.registers[c] = self.registers[a] | self.registers[b]
    def _bori(self, a, b, c):
        self.registers[c] = self.registers[a] | b
    def _setr(self, a, b, c):
        self.registers[c] = self.registers[a]
    def _seti(self, a, b, c):
        self.registers[c] = a
    def _gtir(self, a, b, c):
        if a > self.registers[b]:
            self.registers[c] = 1
        else:
            self.registers[c] = 0
    def _gtri(self, a, b, c):
        if self.registers[a] > b:
            self.registers[c] = 1
        else:
            self.registers[c] = 0
    def _gtrr(self, a, b, c):
        if self.registers[a] > self.registers[b]:
            self.registers[c] = 1
        else:
            self.registers[c] = 0
    def _eqir(self, a, b, c):
        if a == self.registers[b]:
            self.registers[c] = 1
        else:
            self.registers[c] = 0
    def _eqri(self, a, b, c):
        if self.registers[a] == b:
            self.registers[c] = 1
        else:
            self.registers[c] = 0
    def _eqrr(self, a, b, c):
        if self.registers[a] == self.registers[b]:
            self.registers[c] = 1
        else:
            self.registers[c] = 0

    def _ParseLines(self, lines):
        test = []
        samples = []
        for i, line in enumerate(lines):
            line = line.strip()
            if i % 4 == 0:
                before = line[9:-1]
                before = list(map(lambda x: int(x), before.split(", ")))
                test.append(before)
            elif i % 4 == 1:
                op = list(map(lambda x: int(x), line.split()))
                test.append(op)
            elif i % 4 == 2:
                after = line[9:-1]
                after = list(map(lambda x: int(x), after.split(", ")))
                test.append(after)
            else:
                samples.append(deepcopy(test))
                test.clear()
        return samples

    def _ParseProgram(self, lines):
        program = []
        for line in lines:
            line = line.strip()
            nums = list(map(lambda x: int(x), line.split()))
            program.append(nums.copy())
        return program
