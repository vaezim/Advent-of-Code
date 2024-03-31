from utils import Scheduler


with open("input", "r+") as file:
    lines = file.readlines()

##### Part 1 #####
scheduler = Scheduler(lines)
result = scheduler.GetSingleWorkerOrder()
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
result = scheduler.GetMultiWorkerOrder(num_workers=5)
print(f"[+] Answer of part 2: {result}")