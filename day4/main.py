
with open('input.txt', 'r+') as file:
	ranges = file.readlines()

ranges = [c[:-1].split(',') for c in ranges]

overlap = 0
for r in ranges:
	r1, r2 = r[0], r[1]
	r1L, r1R = int(r1.split('-')[0]), int(r1.split('-')[1])
	r2L, r2R = int(r2.split('-')[0]), int(r2.split('-')[1])

	if (r1L <= r2L and r1R >= r2R) or (r2L <= r1L and r2R >= r1R):
		overlap += 1

print(f"Answer of part 1: {overlap}")

overlap = 0
for r in ranges:
	r1, r2 = r[0], r[1]
	r1L, r1R = int(r1.split('-')[0]), int(r1.split('-')[1])
	r2L, r2R = int(r2.split('-')[0]), int(r2.split('-')[1])

	if r1L <= r2L:
		if r1R >= r2L:
			overlap += 1
			continue
	if r2L <= r1L:
		if r2R >= r1L:
			overlap += 1
			continue

print(f"Answer of part 2: {overlap}")

