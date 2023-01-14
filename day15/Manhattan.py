
class Manhattan():
    def __init__(self, Sensors, Beacons):
        self.sensors = Sensors
        self.beacons = Beacons
        self.radius_list = self.getRadiusList()
        self.left, self.right = self.getXBorders()

    def distance(self, loc1, loc2):
        return abs(loc2[0]-loc1[0]) + abs(loc2[1]-loc1[1])
        
    def getRadiusList(self):
        radius_list = []
        for i in range(len(self.sensors)):
            radius_list.append(
                self.distance(self.sensors[i], self.beacons[i]))
        return radius_list

    def getXBorders(self):
        left_border = float('inf')
        right_border = -float('inf')
        for i, sensor in enumerate(self.sensors):
            radius = self.radius_list[i]
            left_border = min(sensor[0]-radius, left_border)
            right_border = max(sensor[0]+radius, right_border)
        return [left_border, right_border]

    def findCoveringSensor(self, loc):
        for i, sensor in enumerate(self.sensors):
            if self.distance(loc, sensor) <= self.radius_list[i]:
                return sensor
        return -1

    def getCoveredPointsInLine(self, y): # e.g. line at y = 100
        covered_points = set()

        for i, sensor in enumerate(self.sensors): # find the covering areas of every sensor at y
            # The point right under/above this sensor at y
            curr = [sensor[0], y]
            # Go left
            while self.distance(sensor, curr) <= self.radius_list[i]:
                covered_points.add(tuple(curr))
                curr[0] -= 1
            # Go right
            curr = [sensor[0], y]
            while self.distance(sensor, curr) <= self.radius_list[i]:
                covered_points.add(tuple(curr))
                curr[0] += 1

        # Remove already existing beacons
        for beacon in self.beacons:
            if beacon in covered_points:
                covered_points.remove(beacon)

        return len(covered_points)

    # Part 2: 0 <= x,y <= 4000000
    # Uses a different approach to find uncovered locations
    def findUncoveredPoints(self):
        bound = 4000000

        # An uncovered point has to be on the
        # boundaries of sensor coverage area
        for i, sensor in enumerate(self.sensors):
            print(f"Sensor {i+1}/{len(self.sensors)}: R = {self.radius_list[i]}")
            for point in self.getSensorBoundary(sensor, self.radius_list[i]):
                if 0 <= point[0] <= bound and 0 <= point[1] <= bound:
                    if self.findCoveringSensor(point) == -1:
                        return point

    def getSensorBoundary(self, sensor, radius): # generator function (iterable)
        top = [sensor[0], sensor[1]+radius+1]
        bottom = [sensor[0], sensor[1]-radius-1]
        left = [sensor[0]-radius-1, sensor[1]]
        right = [sensor[0]+radius+1, sensor[1]]

        # top -> right
        curr = top.copy()
        for _ in range(radius+1):
            yield curr
            curr[0] += 1
            curr[1] -= 1
        # right -> bottom
        curr = right.copy()
        for _ in range(radius+1):
            yield curr
            curr[0] -= 1
            curr[1] -= 1
        # bottom -> left
        curr = bottom.copy()
        for _ in range(radius+1):
            yield curr
            curr[0] -= 1
            curr[1] += 1
        # left -> top
        curr = left.copy()
        for _ in range(radius+1):
            yield curr
            curr[0] += 1
            curr[1] += 1
            