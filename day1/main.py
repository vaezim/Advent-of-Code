import heapq

with open('input.txt', 'r+') as file:
	calories = file.readlines()

elves = []
curr = 0
for c in calories:
	if c == '\n':
		elves.append(curr)
		curr = 0
		continue
	curr += int(c[:-1])

print(f'Answer of part 1: {max(elves)}')

heapq.heapify(elves)
ans = sum(heapq.nlargest(3,elves))

print(f'Answer of part 2: {ans}')
