from filesystem import File, Dir
from sys import exit

root = Dir('/')
curr_dir = root
small_dirs = []

with open('input.txt', 'r') as f:
	while True:
		line = f.readline()
		if line == '\n': break
		line = line.strip().split(' ')
		
		if line[0] == '$': # command
			if line[1] == 'cd': # change current directory
				new_dir = line[-1]
				if new_dir == '..':
					curr_dir = curr_dir.parent
					continue

				try:
					curr_dir = curr_dir.getChild(new_dir)
					continue
				except:
					print(f"Directory at line {i} not found!")
					print(curr_dir.name)
					print(new_dir)
					exit()
					
			if line[1] == 'ls': # list directory
				continue

		elif line[0] == 'dir': # directory
			dir_name = line[-1]
			child = Dir(dirname=dir_name, parent=curr_dir)
			curr_dir.addChild(child)
			continue

		else: # file
			size, filename = int(line[0]), line[1]
			file = File(filename, size)
			curr_dir.addFile(file)

def traverse1(node):
	if node.getSize() <= 100000:
		small_dirs.append(node)
	if not node.children: return
	for c in node.children:
		traverse1(c)
traverse1(root)

res = 0
for node in small_dirs:
	res += node.getSize()
print(f"Solution of Part 1: {res}")


needed_space = 30000000 - (70000000 - root.getSize())
print(f"{needed_space} space is needed.")

curr = root
def traverse2(node):
	global curr
	if needed_space <= node.getSize() < curr.getSize():
		curr = node
	if not node.children: return
	for c in node.children:
		traverse2(c)

traverse2(root)

print(f"Solution of Part 2: {curr.name, curr.getSize()}")