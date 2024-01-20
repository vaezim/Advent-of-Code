from utils import Layout


with open("input", "r+") as file:
    lines = file.readlines()
lines = list(map(lambda x: x.strip(), lines))

##### Part 1 #####
layout = Layout(lines)
layout.CastRay()
result = 0
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####

print(f"[+] Answer of part 2: {result}")
