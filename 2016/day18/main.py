from utils import TrapFinder


first_row = "^^^^......^...^..^....^^^.^^^.^.^^^^^^..^...^^...^^^.^^....^..^^^.^.^^...^.^...^^.^^^.^^^^.^^.^..^.^"

##### Part 1 #####
tf = TrapFinder(first_row)
result = tf.GenerateRows(40)
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
result = tf.GenerateRows(400000)
print(f"[+] Answer of part 2: {result}")
