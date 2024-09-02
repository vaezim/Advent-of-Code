from utils import Airplane


with open('input', 'r+') as file:
    lines = file.readlines()
    lines = list(map(lambda x: list(x.strip()), lines))

##### Part 1 #####
airplane = Airplane(lines)
result = airplane.GetNumOccupiedSeatsAfterStabalizing(mode=1)
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
result = airplane.GetNumOccupiedSeatsAfterStabalizing(mode=2)
print(f"[+] Answer of part 2: {result}")