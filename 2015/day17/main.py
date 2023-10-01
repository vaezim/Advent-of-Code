from utils import Container


with open('input', 'r+') as file:
    line = file.read()

##### Part 1 #####
total = 150
containers = list(map(lambda x: int(x), line.strip().split('\n')))
cont = Container(containers, total)
result = cont.GetNumCombs()
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
result = cont.GetMinNumCombs()
print(f"[+] Answer of part 2: {result}")
