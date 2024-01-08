from collections import defaultdict


class Manhattan:
    def __init__(self, text):
        self.points = self._Process(text)
        self.width, self.height = self._GetGridSize()

    def GetRegionSize(self):
        region_size = 0
        for i in range(self.width):
            for j in range(self.height):
                if self._SumDists((i,j)) < 10000:
                    region_size += 1
        return region_size

    def _SumDists(self, p):
        sum_dist = 0
        for point in self.points:
            sum_dist += self._Dist(p,point)
        return sum_dist

    def GetLargestArea(self):
        self.area_map1 = defaultdict(lambda : 1)  # point => area_size
        self.area_map2 = defaultdict(lambda : 1)  # point => area_size
        self._GetAreaMapInGrid((0,0,self.width,self.height), self.area_map1)
        self._GetAreaMapInGrid((-1,-1,self.width+1,self.height+1), self.area_map2)
        largest_area = 0
        for point in self.points:
            if self.area_map1[point] != self.area_map2[point]:
                continue
            largest_area = max(largest_area, self.area_map1[point])
        return largest_area

    def _GetAreaMapInGrid(self, grid: tuple, area_map: map):
        for i in range(grid[0], grid[2]):
            for j in range(grid[1], grid[3]):
                if (i,j) in self.points:
                    continue
                point = self._GetNearestPointTo((i,j))
                if point != None:
                    area_map[point] += 1
    
    def _GetNearestPointTo(self, p: tuple):
        nearest = []
        nearest_dist = float("inf")
        for point in self.points:
            dist = self._Dist(point, p)
            if dist == nearest_dist:
                nearest.append(point)
            if dist < nearest_dist:
                nearest_dist = dist
                nearest.clear()
                nearest.append(point)
        if len(nearest) == 1:
            return nearest[0]
        return None
    
    def _Dist(self, p1, p2):
        return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

    def _GetGridSize(self):
        width, height = 0, 0
        for point in self.points:
            width = max(width, point[0])
            height = max(height, point[1])
        return (width+1, height+1)

    def _Process(self, text):
        points = []
        for line in text:
            points.append((int(line.split(',')[0]), int(line.split(',')[1])))
        return set(points)