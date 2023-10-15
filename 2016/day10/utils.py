
class Bot:
    def __init__(self):
        self.bots = {}  # bot number => [low, high]
        self.outputs = {}
        self.processedInstructions = set()  # instruction index
        self.result1 = None

    def AddVal(self, bot, val=None):
        if self.bots.get(bot) == None:
            self.bots[bot] = []
        if val != None:
            self.bots[bot].append(val)

    def ProcessInstruction(self, inst, inst_index):
        if inst_index in self.processedInstructions:
            return
        words = inst.strip().split()
        if words[0] == "value":
            val, bot = int(words[1]), int(words[-1])
            self.AddVal(bot, val)
        else:  # bot ... gives ...
            bot = int(words[1])
            self.AddVal(bot=bot)
            if len(self.bots[bot]) < 2:
                return
            low, high = min(self.bots[bot]), max(self.bots[bot])

            #################################
            ##### Change for your input #####
            #################################
            if low == 17 and high == 61:
                self.result1 = bot

            low_type, low_to = words[5], int(words[6])
            high_type, high_to = words[-2], int(words[-1])

            if low_type == "bot":
                self.AddVal(bot=low_to, val=low)
            else:  # output
                self.outputs[low_to] = low
            if high_type == "bot":
                self.AddVal(bot=high_to, val=high)
            else:  # output
                self.outputs[high_to] = high
            self.bots[bot].clear()
        self.processedInstructions.add(inst_index)

    def AreBotsEmpty(self):
        for bot in self.bots.keys():
            if len(self.bots[bot]) > 0:
                return False
        return True

    def GetResult1(self):
        return self.result1


if __name__ == "__main__":
    bot = Bot()
    text =  """ value 5 goes to bot 2
            bot 2 gives low to bot 1 and high to bot 0
            value 3 goes to bot 1
            bot 1 gives low to output 1 and high to bot 0
            bot 0 gives low to output 2 and high to output 0
            value 2 goes to bot 2 """
    
    for line in text.split('\n'):
        bot.ProcessInstruction(line)

    print(bot.bots)
    print(bot.outputs)