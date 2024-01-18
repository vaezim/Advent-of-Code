class Assembly:
    def __init__(self, instructions):
        self.registers = {"a": 0, "b": 0, "c": 0, "d": 0}
        self.instructions = list(map(lambda x: x.strip().split(), instructions))

    def SetRegister(self, reg, val):
        if self.registers.get(reg) != None:
            self.registers[reg] = val

    def Run(self):
        if self.instructions == None:
            print(f"[-] Instructions are empty.")
            return
        instructions = self.instructions[:]
        i = 0
        while i < len(instructions):
            words = instructions[i]
            cmd = words[0]

            # Part 2 optimization
            if i == 5:  # skip lines 6-10
                self.registers["a"] += self.registers["c"] * self.registers["d"]
                self.registers["c"] = 0
                self.registers["d"] = 0
                i = 10
                continue

            # Commands
            if cmd == "cpy":
                if self.registers.get(words[-1]) != None:
                    self.registers[words[-1]] = self._GetRegisterVal(words[1])
            elif cmd == "inc":
                if self.registers.get(words[1]) != None:
                    self.registers[words[1]] += 1
            elif cmd == "dec":
                if self.registers.get(words[1]) != None:
                    self.registers[words[1]] -= 1
            elif cmd == "jnz":
                x = self._GetRegisterVal(words[1])
                if x != 0:
                    i += self._GetRegisterVal(words[-1])
                    continue
            elif cmd == "tgl":
                x = self._GetRegisterVal(words[1])
                translations = {
                    "inc": "dec",
                    "dec": "inc",
                    "tgl": "inc",
                    "jnz": "cpy",
                    "cpy": "jnz",
                }
                if i + x < len(instructions):
                    instructions[i + x][0] = translations[instructions[i + x][0]]
            i += 1

    def _GetRegisterVal(self, reg):
        x = self.registers.get(reg)
        if x == None:
            x = int(reg)
        return x


if __name__ == "__main__":
    with open("test", "r") as file:
        lines = file.readlines()
    ass = Assembly(lines)
    ass.Run()
    print(ass.registers["a"])
