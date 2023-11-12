from utils import FireWall


with open('input', 'r+') as file:
    lines = file.readlines()

##### Part 1 #####
firewall = FireWall(lines)
result = firewall.GetSeverity()
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
result = firewall.GetLeastDelay()  # takes 10 seconds
print(f"[+] Answer of part 2: {result}")