from utils import KeyGenerator


salt = "ihaygndm"

##### Part 1 #####
key_generator = KeyGenerator(salt)
result = key_generator.Get64thKey()
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
result = key_generator.Get64thKey(strech=True)
print(f"[+] Answer of part 2: {result}")
