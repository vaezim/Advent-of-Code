from utils import Image


with open('input', 'r+') as file:
    line = file.readline().strip()

##### Part 1 #####
image = Image(line)
result = image.GetPart1()
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
result = image.GetPart2() # HFYAK
print(f"[+] Answer of part 2: {result}")