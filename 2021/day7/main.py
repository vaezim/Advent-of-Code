from utils import GetMigrationFuel1, GetMigrationFuel2


with open('input', 'r+') as file:
    points = file.read()

##### Part 1 #####
points = list(map(lambda x: int(x), points.split(',')))
min_fuel = float("inf")
for p in range(min(points), max(points)):
    min_fuel = min(min_fuel, GetMigrationFuel1(points, p))
print(f"[+] Answer of part 1: {min_fuel}")

##### Part 2 #####
min_fuel = float("inf")
for p in range(min(points), max(points)):
    min_fuel = min(min_fuel, GetMigrationFuel2(points, p))
print(f"[+] Answer of part 2: {min_fuel}")
