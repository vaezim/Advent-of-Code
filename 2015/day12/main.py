import re
import json
from utils import JsonParser


##### Part 1 #####
result = 0
lines = open("input.json", 'r').readlines()
for line in lines:
    nums = re.findall(r"-?\d+", line)
    result += sum(list(map(lambda x: int(x), nums)))
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
jsonData = json.loads(open("input.json", 'r').read())
jp = JsonParser(jsonData)
result = jp.GetNonRedNumSum()
print(f"[+] Answer of part 2: {result}")
