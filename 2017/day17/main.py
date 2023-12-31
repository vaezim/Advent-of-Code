from utils import SpinLock


step_size = 380

##### Part 1 #####
spinlock = SpinLock(step_size)
result = spinlock.CreateBuffer1()
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
result = spinlock.CreateBuffer2()
print(f"[+] Answer of part 2: {result}")
