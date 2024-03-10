import re

class Turing:
    def __init__(self, lines):
        self.steps = None
        self.states = []

        self.pointer = 0
        self.curr_state = 0
        self.one_slots = set()

        self._ProcessLines(lines)

    def GetChecksum(self):
        for _ in range(self.steps):
            value = int(self.pointer in self.one_slots)
            for func in self.states[self.curr_state][value]:
                func[0](func[1])
        return len(self.one_slots)

    def _ProcessLines(self, lines: list):
        self.steps = int(re.findall(r"\d+", lines[1])[0])
        value = 0
        for line in lines[2:]:
            line = line.strip()
            if len(line) < 2:
                self.states.append([[],[]])
                continue
            if line.split()[0] == "In":
                continue
            if line[-1] == ':':
                value = int(line[-2])
            elif line.split()[1] == "Write":
                val = int(re.findall(r"\d", line)[0])
                self.states[-1][value].append((self._Write, val))
            elif line.split()[1] == "Move":
                val = 1 if line.split()[-1] == "right." else -1
                self.states[-1][value].append((self._Move, val))
            elif line.split()[1] == "Continue":
                val = ord(line[-2]) - ord('A')
                self.states[-1][value].append((self._ChangeState, val))

    def _Write(self, val):
        if val == 1:
            self.one_slots.add(self.pointer)
        elif self.pointer in self.one_slots:
            self.one_slots.remove(self.pointer)

    def _Move(self, val):
        if val == 1:
            self.pointer += 1
        else:
            self.pointer -= 1

    def _ChangeState(self, newState):
        self.curr_state = newState