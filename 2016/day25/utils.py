
class Assembly:
    def __init__(self, instructions):
        self.registers = {"a": 0, "b": 0, "c": 0, "d": 0}
        self.instructions = instructions

    def FindLowestClockMakerNum(self):
        a = 0
        while True:
            signal = self.Run(100)
            if self._IsClockSignal(signal):
                return a
            self._ClearRegisters()
            a += 1
            self.registers["a"] = a

    def Run(self, transmission_length):
        if self.instructions == None:
            print(f"[-] Instructions are empty.")
            return
        i = 0
        transmissions = []
        while len(transmissions) < transmission_length:
            inst = self.instructions[i]
            words = inst.strip().split()
            cmd = words[0]
            if cmd == "cpy":
                self.registers[words[-1]] = self._GetRegisterVal(words[1])
            elif cmd == "inc":
                self.registers[words[1]] += 1
            elif cmd == "dec":
                self.registers[words[1]] -= 1
            elif cmd == "jnz":
                x = self._GetRegisterVal(words[1])
                if x != 0:
                    i += int(words[-1])
                    continue
            elif cmd == "out":
                transmissions.append(self._GetRegisterVal(words[1]))
            i += 1
        return transmissions
    
    def _IsClockSignal(self, signal):
        curr = signal[0]
        for n in signal:
            if n != curr:
                return False
            curr = int(not curr)
        return True
    
    def _GetRegisterVal(self, reg):
        x = self.registers.get(reg)
        if x == None:
            x = int(reg)
        return x
    
    def _ClearRegisters(self):
        for reg in self.registers.keys():
            self.registers[reg] = 0


if __name__ == "__main__":
    ass = Assembly("asd")
    print(ass._IsClockSignal([1,0,1,0]))
    print(ass._IsClockSignal([1,1,1,0]))
    print(ass._IsClockSignal([0,0,1,0]))
    print(ass._IsClockSignal([1,0,1,0,1,0,1,0,1,0,]))
    print(ass._IsClockSignal([1,0,1,0,1,0,1,0,1,0,0]))