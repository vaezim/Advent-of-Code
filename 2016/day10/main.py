from utils import Bot


with open('input', 'r+') as file:
    lines = file.readlines()

##### Part 1 #####
bot = Bot()
while True:
    for i, line in enumerate(lines):
        bot.ProcessInstruction(line, i)
    if bot.AreBotsEmpty():
        break
result = bot.GetResult1()
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
result = bot.outputs[0] * bot.outputs[1] * bot.outputs[2]
print(f"[+] Answer of part 2: {result}")
