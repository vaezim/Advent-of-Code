from utils import IsNice1, IsNice2

with open("input") as file:
    lines = file.readlines()

##### Part 1 #####
nice_count = 0
for s in lines:
    nice_count += IsNice1(s)
print(f"Answer of part 1: {nice_count}")

##### Part 2 #####
nice_count = 0
for s in lines:
    nice_count += IsNice2(s)
print(f"Answer of part 2: {nice_count}")
