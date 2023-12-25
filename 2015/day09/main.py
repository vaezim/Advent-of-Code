from utils import ShortestHamiltonian


with open('input', 'r+') as file:
    lines = file.readlines()

##### Part 1 #####
distances = {} # (city1,city2) => distance
cities = set()
for line in lines:
    (src, _, dst, _, dist) = line.split()
    cities.add(src)
    cities.add(dst)
    distances[(src,dst)] = int(dist)
cities = list(cities)

sh = ShortestHamiltonian(cities, distances)
result = sh.GetShortestHamiltonianPath()
print(f"[+] Answer of part 1: {result}")

##### Part 2 #####
result = sh.GetLongestHamiltonianPath()
print(f"[+] Answer of part 2: {result}")
