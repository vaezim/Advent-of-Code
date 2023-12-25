from utils import GetStringAndMemoryDiff, GetStringAndEncodedDiff


with open("input") as file:
    lines = file.readlines()

diff = 0
for line in lines:
    diff += GetStringAndMemoryDiff(line)
print(f"Answer of part 1: {diff}")

diff = 0
for line in lines:
    diff += GetStringAndEncodedDiff(line)
print(f"Answer of part 2: {diff}")
