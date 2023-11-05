from utils import Assembly


with open('input', 'r+') as file:
    lines = file.readlines()

##### Part 1 #####
ass = Assembly(lines)
result = ass.FindLowestClockMakerNum()
print(f"[+] Answer of part 1: {result}")