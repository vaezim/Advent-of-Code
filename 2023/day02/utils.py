class Game:
    def __init__(self, initial: list):
        self.initial = initial  # [red, green, blue]

    def ParseGames(self, lines):
        self.games = []
        for line in lines:
            line = line[line.index(':')+1:].strip()
            subsets = line.split(';')
            game = []
            for subset in subsets:
                cubes = [0, 0, 0]  # [red, green, blue]
                tokens = subset.strip().split()
                for i in range(len(tokens)//2):
                    color = tokens[2*i+1].strip(',')
                    num = int(tokens[2*i])
                    if color == "red":
                        cubes[0] = num
                    elif color == "green":
                        cubes[1] = num
                    elif color == "blue":
                        cubes[2] = num
                game.append(cubes)
            self.games.append(game)

    def GetSumPossibleGameIds(self):
        sum = 0
        for i, game in enumerate(self.games):
            possible = True
            for subset in game:
                if not self._IsPossibleSubset(subset):
                    possible = False
                    break
            if possible:
                sum += i+1
        return sum
    
    def GetSumMinPower(self):
        sum = 0
        for game in self.games:
            sum += self._GetMinPower(game)
        return sum

    def _IsPossibleSubset(self, subset):
        for i in range(3):
            if subset[i] > self.initial[i]:
                return False
        return True
    
    def _GetMinPower(self, game):
        cubes = [0, 0, 0]
        for subset in game:
            for i, cube in enumerate(subset):
                cubes[i] = max(cubes[i], cube)
        return cubes[0] * cubes[1] * cubes[2]