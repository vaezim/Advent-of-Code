from utils import GetTravelledDistance


with open('input', 'r+') as file:
    lines = file.readlines()

##### Part 1 #####
totalTime = 2503
deers = []
travelledDistances = []
for line in lines:
    words = line.strip().split()
    deers.append(list(map(lambda x: int(x), [words[3], words[6], words[13]])))
for deer in deers:
    travelledDistances.append(GetTravelledDistance(deer[0],deer[1],deer[2],totalTime))
result = max(travelledDistances)
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
deerPoints = [0] * len(deers)
travelledDistances = [0] * len(deers)
for t in range(1,totalTime+1):
    for i, d in enumerate(deers):
        travelledDistances[i] = GetTravelledDistance(d[0],d[1],d[2],t)
    M = max(travelledDistances)
    for i in range(len(deers)):
        if travelledDistances[i] == M:
            deerPoints[i] += 1
result = max(deerPoints)
print(f"[+] Answer of part 2: {result}")
