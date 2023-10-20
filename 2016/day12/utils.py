
class Assembly:
    def __init__(self):
        self.registers = {"a": 0, "b": 0, "c": 0, "d": 0}
        self.instructions = None

    def AddInstructions(self, instruction_list):
        self.instructions = instruction_list

    def Run(self):
        if self.instructions == None:
            print(f"[-] Instructions are empty.")
            return
        i = 0
        while i < len(self.instructions):
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
            i += 1
        
    def GetRegisters(self):
        return self.registers
    
    def _GetRegisterVal(self, reg):
        x = self.registers.get(reg)
        if x == None:
            x = int(reg)
        return x