import re

with open('input', 'r+') as file:
    lines = file.readlines()

##### Part 1 #####
result = 0

for line in lines:
    digits = re.findall(r"\d", line)
    n = int(f"{digits[0]}{digits[-1]}")
    result += n

print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
result = 0

digit_str_map = {"one": 1, "two": 2, "three": 3,
                 "four": 4, "five": 5, "six": 6,
                 "seven": 7, "eight": 8, "nine": 9}

for line in lines:
    digits = {}
    for i, c in enumerate(line):
        if c.isdecimal():
            digits[i] = c
    for ds in digit_str_map:
        iters = list(re.finditer(ds, line))
        if len(iters) > 0:
            digits[iters[0].start()] = digit_str_map[ds]
            digits[iters[-1].start()] = digit_str_map[ds]
    first = digits[min(digits)]
    last = digits[max(digits)]
    n = int(f"{first}{last}")
    result += n

print(f"[+] Answer of part 2: {result}")