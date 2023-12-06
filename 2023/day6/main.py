
with open("input", 'r') as f:
    lines = f.readlines()

##### Part 1 #####
times = list(map(lambda x: int(x), lines[0][lines[0].index(':')+1:].split()))
distance = list(map(lambda x: int(x), lines[1][lines[1].index(':')+1:].split()))

mult = 1
for i, time in enumerate(times):
    possible = 0
    for t in range(time+1):
        if t * (time - t) > distance[i]:
            possible += 1
    mult *= possible
print(f"[+] Answer of part 1: {mult}")

##### Part 2 #####
times = int(''.join([str(t) for t in times]))
distance = int(''.join([str(d) for d in distance]))

possible = 0
for t in range(times+1):
    if t * (times - t) > distance:
        possible += 1
print(f"[+] Answer of part 2: {possible}")