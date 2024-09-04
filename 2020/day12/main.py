from utils import Ship


with open('input', 'r+') as file:
    lines = file.readlines()
lines = list(map(lambda x: x.strip(), lines))

##### Part 1 #####
ship = Ship(lines)
result = ship.GetDestination()
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
result = ship.GetDestinationWithWaypoint()
print(f"[+] Answer of part 2: {result}")