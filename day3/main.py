
with open('input.txt', 'r+') as file:
	sacks = file.readlines()

total = 0
for items in sacks:
	items = items[:-1]
	h1 = set(items[:len(items)//2])
	h2 = set(items[len(items)//2:])
	common = None
	for i in h1:
		if i in h2:
			common = i
			break
	if common.islower():
		total += ord(common)-96
	else:
		total += ord(common)-38

print(f'Answer of part 1: {total}')

group = []
total = 0
for items in sacks:
	group.append(items)
	if len(group) == 3:
		h1 = set(group[0][:-1])
		h2 = set(group[1][:-1])
		h3 = set(group[2][:-1])
		common = None
		for i in h1:
			if i in h2:
				if i in h3:
					common = i
					break
		if not common.isalpha():
			print(group)
		if common.islower():
			total += ord(common)-96
		else:
			total += ord(common)-38
		group.clear()

print(f'Answer of part 2: {total}')