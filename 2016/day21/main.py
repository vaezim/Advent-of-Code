from utils import Scrambler

password = "abcdefgh"
with open("input", 'r') as file:
    lines = file.readlines()

##### Part 1 #####
scr = Scrambler(lines)
result = scr.Scramble(password)
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
scrambled = "fbgdceah"
result = scr.Unscramble(scrambled)
print(f"[+] Answer of part 2: {result}")
