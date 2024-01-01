from utils import Network


with open("input", "r+") as file:
    lines = file.readlines()
lines = list(map(lambda x: x.strip("\n"), lines))

##### Part 1 #####
network = Network(lines)
result = network.RoutePacket()
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
result = network.GetNumSteps()
print(f"[+] Answer of part 2: {result}")
