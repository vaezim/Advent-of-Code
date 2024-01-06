class Atari:
    def __init__(self, text):
        self.instructions = self._Process(text)

    def RunFixedProgram(self):
        for i in range(len(self.instructions)):
            inst = self.instructions[i][0]
            if inst == "acc":
                continue
            if inst == "jmp":
                self.instructions[i][0] = "nop"
            elif inst == "nop":
                self.instructions[i][0] = "jmp"
            curropted = self._IsCurropted(self.instructions)
            if curropted != False:
                return curropted
            self.instructions[i][0] = inst

    def _IsCurropted(self, instructions):
        visited = set()
        acc = 0
        i = 0
        while i < len(instructions):
            if i in visited:
                return False
            visited.add(i)
            inst, num = instructions[i][0], instructions[i][1]
            if inst == "acc":
                acc += num
            elif inst == "jmp":
                i += num
                continue
            i += 1
        return acc

    def RunNoCycle(self):
        acc = 0
        visited = set()
        i = 0
        while i not in visited:
            visited.add(i)
            inst, num = self.instructions[i][0], self.instructions[i][1]
            if inst == "acc":
                acc += num
            elif inst == "jmp":
                i += num
                continue
            i += 1
        return acc

    def _Process(self, text):
        instructions = []  # [[instruction, num], ...]
        for line in text:
            instructions.append([line.split()[0], int(line.split()[1])])
        return instructions