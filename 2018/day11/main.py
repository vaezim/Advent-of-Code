from utils import Fuel

serial_number = 3463

##### Part 1 #####
F = Fuel(serial_number)
result = F.GetMaxTotalPowerCoordinates()
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
result = F.GetMaxTotalPowerCoordinates2()
print(f"[+] Answer of part 2: {result}")