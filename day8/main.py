
with open('input.txt', 'r') as file:
	text = file.readlines()

nums = []
for line in text:
	nums.append( list(map(lambda x: int(x), line.strip())) )

W, H = len(nums), len(nums[0])
visited = set()

# Left side
for i in range(W):
	curr = -1
	for j in range(H):
		if nums[i][j] > curr:
			curr = nums[i][j]
			visited.add((i,j))

# Right side
for i in range(W):
	curr = -1
	for j in range(H):
		if nums[i][H-j-1] > curr:
			curr = nums[i][H-j-1]
			visited.add((i,H-j-1))

# Top side
for j in range(H):
	curr = -1
	for i in range(W):
		if nums[i][j] > curr:
			curr = nums[i][j]
			visited.add((i,j))

# Bottom side
for j in range(H):
	curr = -1
	for i in range(W):
		if nums[W-i-1][j] > curr:
			curr = nums[W-i-1][j]
			visited.add((W-i-1,j))

print(f"Solution of Part 1: {len(visited)}")