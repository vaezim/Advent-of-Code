
with open('input.txt', 'r') as file:
    nums = file.readlines()

nums = list(map(lambda x:int(x.strip()), nums))

##### Part 1 #####
increases = 0
for i in range(1,len(nums)):
    increases += nums[i] > nums[i-1]

print(increases)

##### Part 2 #####
increases = 0
for i in range(3, len(nums)):
    increases += nums[i] > nums[i-3]

print(increases)
