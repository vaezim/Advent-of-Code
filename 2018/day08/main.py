from utils import Tree


with open('input', 'r+') as file:
    line = file.readline()

##### Part 1 #####
tree = Tree(line)
result = tree.GetSumMetadata()
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
result = tree.GetRootNodeValue()
print(f"[+] Answer of part 2: {result}")