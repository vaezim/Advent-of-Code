from string import ascii_lowercase

class Dance:
    def __init__(self, length, text):
        self.length = length
        self.dancers = ascii_lowercase[:length]
        self.moves = self._ParseText(text)

    def Dance(self):
        dancers = list(self.dancers)
        for move in self.moves:
            type = move[0]
            if type == "s":
                num = int(move[1:])
                dancers = dancers[-num:] + dancers[:-num]
            elif type == "x":
                slash = move.index('/')
                A, B = int(move[1:slash]), int(move[slash+1:])
                tmp = dancers[A]
                dancers[A] = dancers[B]
                dancers[B] = tmp
            elif type == "p":
                slash = move.index('/')
                A, B = dancers.index(move[1:slash]), dancers.index(move[slash+1:])
                tmp = dancers[A]
                dancers[A] = dancers[B]
                dancers[B] = tmp
        return ''.join(dancers)
    
    def DanceRepeat(self, num):
        visited = set()
        for i in range(num):
            if self.dancers in visited:
                break
            visited.add(self.dancers)
            self.dancers = self.Dance()
        self.dancers = ascii_lowercase[:self.length]
        for _ in range(num % len(visited)):
            self.dancers = self.Dance()
        return self.dancers

    def _ParseText(self, text: str):
        return text.split(',')


if __name__ == "__main__":
    text = """s1,x3/4,pe/b"""
    dance = Dance(5, text)
    print(dance.Dance())
    print(dance.DanceRepeat(10**9))