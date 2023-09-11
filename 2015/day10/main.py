from utils import NextLookSayNum


n = "1113122113"

##### Part 1 #####
for _ in range(40):
    n = NextLookSayNum(n)
print(f"[+] Answer of part 1: {len(n)}")

##### Part 2 #####
for _ in range(10):
    n = NextLookSayNum(n)
print(f"[+] Answer of part 2: {len(n)}")
