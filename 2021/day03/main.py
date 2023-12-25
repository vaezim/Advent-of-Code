
def findMostCommon(nums, index):
    ones = 0
    for n in nums:
        if n[index] == '1':
            ones += 1
    if ones > len(nums)/2:
        return '1'
    elif ones < len(nums)/2:
        return '0'
    else:
        return -1

with open('input.txt', 'r') as file:
    lines = file.readlines()
lines = [line.strip() for line in lines]

##### Part 1 #####
most_common = [0]*len(lines[0])
for line in lines:
    for i in range(len(line)):
        if line[i] == '1': # Counting the number of ones
            most_common[i] += 1

gamma = ''
for i in range(len(most_common)):
    if most_common[i] >= len(lines)//2:
        gamma += '1'
    else:
        gamma += '0'

gamma = int(gamma, 2)
epsilon = (2**len(most_common)-1) - gamma
print(gamma * epsilon)

##### Part 2 #####

# Oxygen
curr_list = lines.copy()
next_list = []
for i in range(len(lines[0])):
    most_common = findMostCommon(curr_list, i)
    if most_common == -1:
        most_common = '1'

    for num in curr_list:
        if num[i] == most_common:
            next_list.append(num)
    if len(next_list) == 1:
        oxygen = int(next_list[0], 2)
        break

    curr_list = next_list.copy()
    next_list.clear()

# CO2
curr_list = lines.copy()
next_list = []
for i in range(len(lines[0])):
    most_common = findMostCommon(curr_list, i)
    if most_common == -1:
        most_common = '1'
    least_common = str(int(not bool(int(most_common))))

    for num in curr_list:
        if num[i] == least_common:
            next_list.append(num)
    if len(next_list) == 1:
        carbon = int(next_list[0], 2)
        break

    curr_list = next_list.copy()
    next_list.clear()

print(oxygen * carbon)
