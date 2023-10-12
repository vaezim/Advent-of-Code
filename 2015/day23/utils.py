
class Computer:
    def __init__(self):
        self.registers = {"a": 0, "b": 0}
        self.instructions = None

    def AddInstructions(self, instructions: list):
        self.instructions = instructions

    def Run(self):
        curr = 0
        while (0 <= curr < len(self.instructions)):
            instruction = self.instructions[curr]
            words = instruction.strip().split()
            cmd = words[0]
            if cmd == "hlf":
                self.registers[words[1]] /= 2
            elif cmd == "tpl":
                self.registers[words[1]] *= 3
            elif cmd == "inc":
                self.registers[words[1]] += 1
            elif cmd == "jmp":
                offset = int(words[1])
                curr += offset
                continue
            elif cmd == "jie":
                register = words[1][:-1]
                if self.registers[register] % 2 == 0:
                    offset = int(words[2])
                    curr += offset
                    continue
            elif cmd == "jio":
                register = words[1][:-1]
                if self.registers[register] == 1:
                    offset = int(words[2])
                    curr += offset
                    continue
            curr += 1