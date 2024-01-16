import re


class FileSystem:
    def __init__(self, nodes_info):
        self.width = 0
        self.height = 0
        self.nodes = {}  # (x,y) --> [Size, Used, Avail, Use%]
        self._ProcessNodesInfo(nodes_info)

    def GetNumViablePairs(self):
        viable_num = 0
        for key1 in self.nodes.keys():
            for key2 in self.nodes.keys():
                viable_num += self._IsViablePair(key1, key2)
        return viable_num

    def _ProcessNodesInfo(self, nodes_info):
        for i in range(2, len(nodes_info)):
            info = nodes_info[i]
            x = int(info[info.index('x')+1 : info.index('y')-1])
            y = int(info[info.index('y')+1 : info.index(' ')])
            size, used, avail = tuple(list(map(lambda x: int(x), re.findall(r" (\d+)T", info))))
            use = int(re.findall(r" (\d+)%", info)[0])
            self.nodes[(x,y)] = [size, used, avail, use]
            self.width = max(self.width, x)
            self.height = max(self.height, y)
        self.width += 1
        self.height += 1

    def _IsViablePair(self, n1, n2):  # (x1,y1), (x2,y2)
        if self.nodes[n1][1] == 0:  # Used
            return False
        if n1[0] == n2[0] and n1[1] == n2[1]:
            return False
        if self.nodes[n1][1] > self.nodes[n2][2]:
            return False
        return True
    
    def DispToFile(self, filename):
        s = ""
        for j in range(self.height):
            for i in range(self.width):
                if i == 0 and j == 0:
                    s += "T "
                    continue
                if j == 0 and i == self.width-1:
                    s += "X "
                    continue
                if self.nodes[(i,j)][1] == 0:
                    s += "O "
                elif self.nodes[(i,j)][1] > 400:
                    s += "| "
                else:
                    s += ". "
            s += "\n"
        with open(filename, 'w') as f:
            f.write(s)