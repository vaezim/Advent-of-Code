from utils import Carts


with open('input', 'r+') as file:
    lines = file.readlines()
lines = list(map(lambda x: list(x.strip('\n')), lines))

##### Part 1 #####
carts = Carts(lines)
result = carts.GetFirstCrash()
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
result = carts.GetLastRemainingCart()
print(f"[+] Answer of part 2: {result}")