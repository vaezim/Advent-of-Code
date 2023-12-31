import threading
from time import sleep
from queue import Queue


class Program:
    def __init__(self, pid, cpu, instructions):
        self.pid = pid
        self.cpu = cpu
        self.num_sent_msg = 0
        self.msg_queue = Queue()
        self.waiting_2_rcv = False
        self.registers = {"p": pid}
        self.instructions = instructions

    def Run(self):
        i = 0
        while i < len(self.instructions):
            # Parse instruction line
            inst, reg = self.instructions[i][0], self.instructions[i][1]
            if reg.isalpha() and self.registers.get(reg) == None:
                self.registers[reg] = 0
            if len(self.instructions[i]) == 3:
                val = self._GetVal(self.instructions[i][2])
            # Execute
            if inst == "snd":
                self._Snd(self.registers[reg])
            elif inst == "rcv":
                rcv_val = self._Rcv()
                self.registers[reg] = rcv_val
            elif inst == "set":
                self.registers[reg] = val
            elif inst == "add":
                self.registers[reg] += val
            elif inst == "mul":
                self.registers[reg] *= val
            elif inst == "mod":
                self.registers[reg] = self.registers[reg] % val
            elif inst == "jgz" and self._GetVal(reg) > 0:
                i += val
                continue
            i += 1

    def _Snd(self, val):
        self.cpu.GetProgram(int(not self.pid)).msg_queue.put(val)
        self.num_sent_msg += 1

    def _Rcv(self):
        self.waiting_2_rcv = True
        while self.msg_queue.empty():
            continue
        self.waiting_2_rcv = False
        return self.msg_queue.get()

    def _GetVal(self, X):
        if X.isalpha():
            if self.registers.get(X) == None:
                self.registers[X] = 0
            return self.registers[X]
        return int(X)


class CPU:
    def __init__(self, lines):
        self.programs = {}
        self.registers = {}
        self.played_sounds = []
        self.instructions = self._Process(lines)

    def Recover(self):
        i = 0
        while i < len(self.instructions):
            # Parse instruction line
            inst, reg = self.instructions[i][0], self.instructions[i][1]
            if self.registers.get(reg) == None:
                self.registers[reg] = 0
            if len(self.instructions[i]) == 3:
                val = self._GetVal(self.instructions[i][2])
            # Execute
            if inst == "snd":
                self.played_sounds.append(self.registers[reg])
            elif inst == "rcv" and self.registers[reg] != 0:
                return self.played_sounds[-1]
            elif inst == "set":
                self.registers[reg] = val
            elif inst == "add":
                self.registers[reg] += val
            elif inst == "mul":
                self.registers[reg] *= val
            elif inst == "mod":
                self.registers[reg] = self.registers[reg] % val
            elif inst == "jgz" and self._GetVal(reg) > 0:
                i += val
                continue
            i += 1

    def RunTwoPrograms(self):
        # Create two programs
        p0 = Program(0, self, self.instructions)
        p1 = Program(1, self, self.instructions)
        self.programs[0] = p0
        self.programs[1] = p1
        # Start a thread for each
        t0 = threading.Thread(target=p0.Run)
        t1 = threading.Thread(target=p1.Run)
        t0.start()
        t1.start()
        # Wait until a deadlock is reached
        sleep(3)
        return p1.num_sent_msg

    def GetProgram(self, pid):
        return self.programs[pid]

    def _GetVal(self, X):
        if X.isalpha():
            if self.registers.get(X) == None:
                self.registers[X] = 0
            return self.registers[X]
        return int(X)

    def _Process(self, lines):
        instructions = []
        for line in lines:
            tokens = line.split()
            instructions.append(tuple(tokens))
        return instructions
