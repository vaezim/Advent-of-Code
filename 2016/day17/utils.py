from hashlib import md5

class VaultFinder:
    def __init__(self, passcode):
        self.passcode = passcode
        self.grid = [[0] * 4 for _ in range(4)]
        self.visited_paths = set()

    def GetShortestPath(self):
        if len(self.visited_paths) == 0:
            self._SearchPaths()
        return min(list(self.visited_paths), key=lambda x: len(x))
    
    def GetLongestPath(self):
        if len(self.visited_paths) == 0:
            self._SearchPaths()
        return max(list(self.visited_paths), key=lambda x: len(x))

    def _SearchPaths(self, pos=[0,0], path=""):
        if pos == [len(self.grid)-1,len(self.grid[0])-1]:
            self.visited_paths.add(path)
            return
        open_doors = self._GetOpenDoors(pos, path)
        if sum(open_doors) == 0:
            return
        for i, n in enumerate(open_doors):
            if n == 0:
                continue
            if i == 0:  # U
                self._SearchPaths([pos[0]-1,pos[1]], path+"U")
            elif i == 1:  # D
                self._SearchPaths([pos[0]+1,pos[1]], path+"D")
            elif i == 2:  # L
                self._SearchPaths([pos[0],pos[1]-1], path+"L")
            elif i == 3:  # R
                self._SearchPaths([pos[0],pos[1]+1], path+"R")

    def _GetOpenDoors(self, pos, path):
        open_doors = [0]*4  # U, D, L, R
        open_chars = "bcdef"
        hash = md5((self.passcode + path).encode()).hexdigest()[:4]
        for i in range(len(open_doors)):
            char = hash[i]
            if char not in open_chars:
                continue
            if i == 0 and pos[0] > 0:  # U
                open_doors[i] = 1
            elif i == 1 and pos[0] < len(self.grid)-1:  # D
                open_doors[i] = 1
            elif i == 2 and pos[1] > 0:  # L
                open_doors[i] = 1
            elif i == 3 and pos[1] < len(self.grid[0])-1:  # R
                open_doors[i] = 1
        return open_doors
    
if __name__ == "__main__":
    passcode = "ihgpwlah"
    vf = VaultFinder(passcode)
    print(vf.GetShortestPath())
    print(len(vf.GetLongestPath()))

    passcode = "kglvqrro"
    vf = VaultFinder(passcode)
    print(vf.GetShortestPath())
    print(len(vf.GetLongestPath()))

    passcode = "ulqzkmiv"
    vf = VaultFinder(passcode)
    print(vf.GetShortestPath())
    print(len(vf.GetLongestPath()))
