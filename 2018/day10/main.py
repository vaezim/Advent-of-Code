from utils import Sky

with open('input', 'r+') as file:
    lines = file.readlines()

##### Part 1, 2 #####
sky = Sky(lines)
time = 0
size = 400
while True:
    sky.Time()
    time += 1
    print(f"Time = {time}")
    if sky.AreAllStarsInGrid(size):
        sky.Disp(size)
        input()