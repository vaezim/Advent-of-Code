from utils import StreamParser


with open('input', 'r+') as file:
    text = file.read().strip()

##### Part 1 #####
sp = StreamParser(text)
result = sp.GetGroupScore()
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
result = sp.GetNumGarbage()
print(f"[+] Answer of part 2: {result}")