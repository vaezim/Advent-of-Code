class Round:
    def __init__(self, lengths):
        self.curr = 0
        self.skip_size = 0
        self.lengths = lengths
        self.arr = list(range(256))

    def Round(self):
        for length in self.lengths:
            end = (self.curr + length - 1) % len(self.arr)
            if length > 0:
                self._ReverseSublist(self.curr, end)
            self.curr = (self.curr + self.skip_size + length) % len(self.arr)
            self.skip_size += 1
    
    def Reset(self):
        self.arr = list(range(len(self.arr)))
        self.curr = 0
        self.skip_size = 0

    def _ReverseSublist(self, start, end):
        if start <= end:
            sublist = self.arr[start:end+1]
            sublist.reverse()
            for i in range(start,end+1):
                self.arr[i] = sublist[i-start]
        else:
            sublist = self.arr[start:] + self.arr[:end+1]
            sublist.reverse()
            for i in range(start,len(self.arr)):
                self.arr[i] = sublist[i-start]
            for i in range(end+1):
                self.arr[i] = sublist[len(self.arr)-start+i]
    

class KnotHash:
    def RunRound(self, lengths, num=1):
        r = Round(lengths)
        r.Reset()
        for _ in range(num):
            r.Round()
        return r.arr
    
    def GetHash(self, text):
        lengths = []
        # Ascii lengths
        for c in text:
            lengths.append(ord(c))
        lengths.extend([17, 31, 73, 47, 23])
        # 64 rounds of hash
        arr = self.RunRound(lengths, num=64)
        # XOR
        xor_list = []
        for i in range(16):
            sublist = arr[i*16:(i+1)*16]
            xor_list.append(self._ListXOR(sublist))
        # Hex representation
        hex_str = ""
        for n in xor_list:
            h = hex(n)[2:]
            if len(h) == 1:
                h = "0" + h
            hex_str += h
        return hex_str

    def _ListXOR(self, arr):
        res = arr[0]
        for i in range(1,len(arr)):
            res = res ^ arr[i]
        return res


class Grid:
    def __init__(self, salt):
        self.salt = salt
        self.grid = []
        self.hasher = KnotHash()
        self._CreateGrid()

    def GetNumOnes(self):
        return sum([sum(x) for x in self.grid])
    
    def GetNumRegions(self):
        num_regions = 0
        self.visited = set()  # tuple (x,y)
        for i in range(128):
            for j in range(128):
                if self.grid[i][j] == 0 or (i,j) in self.visited:
                    continue
                self._DFS((i,j))
                num_regions += 1
        return num_regions

    def _DFS(self, point):
        x, y = point[0], point[1]
        self.visited.add(point)
        if x > 0 and (x-1,y) not in self.visited and self.grid[x-1][y] == 1:
            self._DFS((x-1,y))
        if x < 127 and (x+1,y) not in self.visited and self.grid[x+1][y] == 1:
            self._DFS((x+1,y))
        if y > 0 and (x,y-1) not in self.visited and self.grid[x][y-1] == 1:
            self._DFS((x,y-1))
        if y < 127 and (x,y+1) not in self.visited and self.grid[x][y+1] == 1:
            self._DFS((x,y+1))

    def _CreateGrid(self):
        for i in range(128):
            text = self.salt + "-" + str(i)
            bin_str = self._GetBinStr(self.hasher.GetHash(text))
            self.grid.append(list(map(lambda x: int(x), list(bin_str))))

    def _GetBinStr(self, hex: str):
        bin_str = ""
        for i in range(0, len(hex), 2):
            bin_str += bin(int(hex[i:i+2], 16))[2:].zfill(8)
        return bin_str


if __name__ == "__main__":
    grid = Grid("flqrgnkx")
    print(grid.GetNumOnes())
    print(grid.GetNumRegions())