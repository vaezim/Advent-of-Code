from Compare import compare, comparator
from functools import cmp_to_key


with open('input.txt', 'r') as file:
    lines = file.readlines()

##### Part 1 #####
inOrderNum = 0

for i in range(len(lines)//3):
    # Try parsing the lines instead of using eval()
    left = eval(lines[i*3].strip())
    right = eval(lines[i*3+1].strip())

    if compare(left, right):
        inOrderNum += (i+1)

print(inOrderNum)

##### Part 2 #####
new_lines = [[[2]], [[6]]]
for line in lines:
    if line != '\n':
        new_lines.append(eval(line))

new_lines.sort(key=cmp_to_key(comparator), reverse=True)
first, second = new_lines.index([[2]])+1, new_lines.index([[6]])+1
print(first * second)
