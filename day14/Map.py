
class Map():
    def __init__(self, bluePrintText):
        self.source = (500,0)
        self.bP = self.parseBP(bluePrintText)
        self.borders = self.findBorders(self.bP)

        self.source = self.mapCoordinate(self.source)
        self.map = self.drawMap(self.borders, self.bP)

    def parseBP(self, bPtext):
        bP = []
        for line in bPtext.split('\n')[:-1]:
            line = line.strip().split(' -> ')
            path = list(map(lambda x: self.parseCoordinate(x), line))
            bP.append(path)
        return bP

    def traceSand(self, inplace=False): # inplace: update self.map or not
        # Returns the final location of the sand pepple. -1 if falls to the abyss
        pos = (self.source[0], self.source[1])
        while True:
            x, y = pos[0], pos[1]
            # Down
            if y+1 >= len(self.map): # Abyss
                return -1
            if self.map[y+1][x] == '.':
                pos = (x,y+1)
                continue

            # Down-Left
            if y+1 >= len(self.map) or x-1 < 0: # Abyss
                return -1
            if self.map[y+1][x-1] == '.':
                pos = (x-1,y+1)
                continue

            # Down-Right
            if y+1 >= len(self.map) or x+1 >= len(self.map[0]): # Abyss
                return -1
            if self.map[y+1][x+1] == '.':
                pos = (x+1,y+1)
                continue

            break # if position remains the same.
        if inplace:
            self.map[pos[1]][pos[0]] = 'o'

        return pos

    def drawMap(self, borders, bP):
        width, height = borders[1]-borders[0]+1, borders[3]-borders[2]+1
        _map = [['.']*width for _ in range(height)]
        _map[self.source[1]][self.source[0]] = '+' # source

        for i in range(len(bP)):
            for j in range(len(bP[i])-1): # excluding the last coor
                x1, y1 = self.mapCoordinate((bP[i][j][0], bP[i][j][1]))
                x2, y2 = self.mapCoordinate((bP[i][j+1][0], bP[i][j+1][1]))

                if x1 == x2:
                    for jj in range(min(y1,y2),max(y1,y2)+1): # y/x represents the line/column number.
                        _map[jj][x1] = '#'
                else:
                    for ii in range(min(x1,x2),max(x1,x2)+1):
                        _map[y1][ii] = '#'
        return _map

    def countSands(self):
        sandNum = 0
        for line in self.map:
            sandNum += line.count('o')
        return sandNum

    def printMap(self):
        for line in self.map:
            print(''.join(line))
        print()

    def parseCoordinate(self, coor):
        coor = coor.split(',')
        x, y = int(coor[0]), int(coor[1])
        return (x,y)

    def findBorders(self, bP): # find the borders of the blueprint
        left, right = float('inf'), 0
        up, down = float('inf'), 0
        for i in range(len(bP)):
            for j in range(len(bP[i])):
                coor = bP[i][j]
                left = min(left, coor[0])
                right = max(right, coor[0])
                up = min(up, coor[1])
                down = max(down, coor[1])
        # Sand source at (500,0)
        left = min(left, self.source[0])
        right = max(right, self.source[0])
        up = min(up, self.source[1])
        down = max(down, self.source[1])
        return [left, right, up, down]

    def mapCoordinate(self, coor):
        x, y = coor[0],coor[1]
        return (x-self.borders[0], y-self.borders[2]) # -= left | -= up
        