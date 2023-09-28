
def GetTravelledDistance(speed: int, travelTime: int, restTime: int, totalTime: int) -> int:
    cycle = travelTime + restTime
    numCycles = totalTime // cycle
    remaining = totalTime % cycle
    return numCycles * (speed*travelTime) + min(remaining, travelTime) * speed

if __name__ == "__main__":
    speed = 14
    travelTime = 10
    restTime = 127
    totalTime = 1000
    print(GetTravelledDistance(speed,travelTime,restTime,totalTime))
