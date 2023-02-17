import re
from Manhattan import Manhattan


with open('input.txt', 'r') as file:
    lines = file.readlines()

##### Part 1 #####
Sensors = []
Beacons = []
for line in lines:
    coors = re.findall(r'[-]?\d+', line)
    Sensors.append((int(coors[0]), int(coors[1])))
    Beacons.append((int(coors[2]), int(coors[3])))

man = Manhattan(Sensors, Beacons)
print(man.getCoveredPointsInLine(y=2000000)) # runtime: <1min

##### Part 2 #####
isolated_point = man.findUncoveredPoints() # runtime: <10min
print(isolated_point[0]*4000000 + isolated_point[1])
