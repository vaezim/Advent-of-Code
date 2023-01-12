from Map import Map


with open('input.txt', 'r') as file:
    bluePrintText = file.read()

##### Part 1 #####
m = Map(bluePrintText)
# m.printMap()

is_abyss = 0
while is_abyss != -1:
    is_abyss = m.traceSand(inplace=True)
# m.printMap()

sand_num = m.countSands()
print(f"Answer of Part 1: {sand_num}")

##### Part 2 #####
left, right, down = m.borders[0], m.borders[1], m.borders[3]
width = right-left
floor_level = down + 2

# create the new blueprint with the added floor.
# increase the width coefficient if sand still falls to the abyss.
bluePrintText += f"{left-2*width},{floor_level} -> {right+2*width},{floor_level}\n"

m2 = Map(bluePrintText)

is_source = 0
while is_source != m2.source:
    is_source = m2.traceSand(inplace=True)

sand_num = m2.countSands()
print(f"Answer of Part 2: {sand_num}")
