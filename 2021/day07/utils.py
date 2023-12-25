
def GetMigrationFuel1(points: list, dest: int):
    fuel = 0
    for p in points:
        fuel += abs(dest - p)
    return fuel

def GetMigrationFuel2(points: list, dest: int):
    fuel = 0
    for p in points:
        fuel += abs(dest - p) * (abs(dest - p) + 1) // 2
    return fuel

if __name__ == "__main__":
    print(GetMigrationFuel1([1,2,3], 5))
    print(GetMigrationFuel2([1,2,3], 5))