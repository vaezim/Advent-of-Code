from utils import RoomChecker

with open ("input") as file:
    lines = file.readlines()

##### Part 1 #####
id_sum = 0
north_pole_id = 0
for room in lines:
    room_id, is_northpole = RoomChecker(room.strip())
    id_sum += room_id
    if is_northpole:
        north_pole_id = room_id
print(f"Answer of of part 1: {id_sum}")

##### Part 2 #####
print(f"Answer of of part 2: {north_pole_id}")
