from itertools import permutations


class Scrambler:
    def __init__(self, operations: str):
        self.operations = operations

    def Scramble(self, s: str) -> str:
        s = list(s)
        for i, op in enumerate(self.operations):
            s = self._ApplyOperation(op.strip(), s)
            # print(i+1, ''.join(s))
        return ''.join(s)
    
    def Unscramble(self, s: str) -> str:
        letters = "abcdefgh"
        for perm in permutations(letters):
            password = list(perm)
            if self.Scramble(password) == s:
                return ''.join(password)

    def _ApplyOperation(self, op: str, s: list):
        words = op.split()
        if words[0] == "swap":
            if words[1] == "position":
                pos1, pos2 = int(words[2]), int(words[5])
                tmp = s[pos2]
                s[pos2] = s[pos1]
                s[pos1] = tmp
            elif words[1] == "letter":
                let1, let2 = words[2], words[5]
                for i in range(len(s)):
                    if s[i] == let1: s[i] = let2
                    elif s[i] == let2: s[i] = let1
        elif words[0] == "reverse":
            pos1, pos2 = int(words[2]), int(words[4])
            rev_str = s[pos1:pos2+1]
            rev_str.reverse()
            for i in range(pos1,pos2+1):
                s[i] = rev_str[i-pos1]
        elif words[0] == "rotate":
            if words[1] in ["left", "right"]:
                rot_size = int(words[2])
                if words[1] == "right":
                    rot_size = len(s) - rot_size
                s = s[rot_size:] + s[:rot_size]
            elif words[1] == "based":
                index = s.index(words[6])
                rot_size = len(s) - index + (len(s) - 1)
                if index >= 4:
                    rot_size += (len(s) - 1)
                rot_size = rot_size % len(s)
                s = s[rot_size:] + s[:rot_size]
        elif words[0] == "move":
            pos1, pos2 = int(words[2]), int(words[5])
            ch = s[pos1]
            s.pop(pos1)
            s.insert(pos2, ch)
        else:
            print(f"[-] Invalid operation: {op}")
        return s
    

if __name__ == "__main__":
    with open("test", 'r') as file:
        lines = file.readlines()
    scr = Scrambler(lines)
    print(scr.Scramble("abcde"))