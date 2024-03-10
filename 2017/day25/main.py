from utils import Turing


with open('input', 'r+') as file:
    lines = file.readlines()

##### Part 1 #####
turing = Turing(lines)
result = turing.GetChecksum()
print(f"[+] Answer of part 1: {result}")
