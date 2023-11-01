from utils import CheckSum


input = "01110110101001000"

##### Part 1 #####
disk_size = 272
checkSum = CheckSum(input, disk_size)
result = checkSum.GetCheckSum()
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
disk_size = 35651584
checkSum = CheckSum(input, disk_size)
result = checkSum.GetCheckSum()
print(f"[+] Answer of part 2: {result}")
