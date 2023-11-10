from utils import KnotHash


with open('input', 'r+') as file:
    text = file.read().strip()
    lengths = list(map(lambda x: int(x), text.split(',')))

##### Part 1 #####
kh = KnotHash(256)
arr = kh.RunRound(lengths)
result = arr[0] * arr[1]
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
result = kh.GetHash(text)
print(f"[+] Answer of part 2: {result}")
