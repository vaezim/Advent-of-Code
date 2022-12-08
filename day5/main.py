
crates = []
for _ in range(9):
	crates.append([])
idxs = [1, 5, 9, 13, 17, 21, 25, 29, 33]

with open('input.txt', 'r+') as file:
	while True:
		line = file.readline()
		if line == '\n': break

		if '[' in line:
			for i, idx in enumerate(idxs):
				if line[idx] != ' ':
					crates[i].append(line[idx])
	for c in crates:
		c.reverse()

	# Moves start from here
	while True:
		line = file.readline()
		if len(line) < 5: break

		line = line[:-1].split(' ')
		num, src, dst = int(line[1]), int(line[3])-1, int(line[5])-1
		
		tmp = crates[src][-num:]
		tmp.reverse()
		crates[src] = crates[src][:-num]
		crates[dst].extend(tmp)

res = ''
for c in crates:
	if c:
		res += c[-1]
print(res)