from utils import Decompressor


with open('input', 'r+') as file:
    text = file.readline().strip()

##### Part 1 #####
decomp = Decompressor()
result = len(decomp.Decompress(text))
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
result = decomp.Decompress2Len(text)
print(f"[+] Answer of part 2: {result}")
