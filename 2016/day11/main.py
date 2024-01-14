from utils import min_moves_to_top_level, parse_floors


with open("input", "r+") as file:
    text = file.read()

##### Part 1 #####
result = min_moves_to_top_level(parse_floors(text))
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
floors = parse_floors(text)
floors[0] = floors[0].union(
    [
        ("elerium", "generator"),
        ("elerium", "microchip"),
        ("dilithium", "generator"),
        ("dilithium", "microchip"),
    ]
)
result = min_moves_to_top_level(floors)
print(f"[+] Answer of part 2: {result}")
