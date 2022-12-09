
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

def scenicScore(tree):
	x, y = tree[0], tree[1]
	res = 1
	# down
	i = 1
	while x+i < H and nums[x+i][y] < nums[x][y]:
		if x+i == H-1:
			break
		i += 1
	res *= i
	# top
	i = 1
	while 0 <= x-i and nums[x-i][y] < nums[x][y]:
		if 0 == x-i:
			break
		i += 1
	res *= i
	# left
	i = 1
	while 0 <= y-i and nums[x][y-i] < nums[x][y]:
		if 0 == y-i:
			break
		i += 1
	res *= i
	# right
	i = 1
	while y+i < W and nums[x][y+i] < nums[x][y]:
		if y+i == W-1:
			break
		i += 1
	res *= i
	return res

print(scenicScore((1,1)))

MAX = 0
for i in range(1,W-1):
	for j in range(1,H-1):
		MAX = max(MAX, scenicScore((i,j)))

print(f"Solution of Part 2: {MAX}")
