from utils import HexPathFinder


with open('input', 'r+') as file:
    text = file.readline()

##### Part 1 #####
hex = HexPathFinder(text)
result = hex.GetShortestPathLength()
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
result = hex.GetFurthestDistance()
print(f"[+] Answer of part 2: {result}")
