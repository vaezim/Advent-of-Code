class CPU:
    def __init__(self):
        self.registers = {}
        self.max = 0

    def ParseInstruction(self, line: str):
        tokens = line.split()

        # register names
        reg_name = tokens[0]
        cond_reg_name = tokens[4]
        if self.registers.get(reg_name) == None:
            self.registers[reg_name] = 0
        if self.registers.get(cond_reg_name) == None:
            self.registers[cond_reg_name] = 0

        # condiction
        condition = False
        cond_num = int(tokens[-1])
        cond_operator = tokens[-2]
        if cond_operator == "<":
            condition = self.registers[cond_reg_name] < cond_num
        elif cond_operator == "<=":
            condition = self.registers[cond_reg_name] <= cond_num
        elif cond_operator == ">":
            condition = self.registers[cond_reg_name] > cond_num
        elif cond_operator == ">=":
            condition = self.registers[cond_reg_name] >= cond_num
        elif cond_operator == "==":
            condition = self.registers[cond_reg_name] == cond_num
        elif cond_operator == "!=":
            condition = self.registers[cond_reg_name] != cond_num

        # operation
        if not condition:
            return
        if tokens[1] == "dec":
            self.registers[reg_name] -= int(tokens[2])
        elif tokens[1] == "inc":
            self.registers[reg_name] += int(tokens[2])
        self.max = max(self.max, self.registers[reg_name])
