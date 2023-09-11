from itertools import permutations


class ShortestHamiltonian:
    def __init__(self, cities, distances):
        self.cities = cities
        self.distances = distances

    def GetShortestHamiltonianPath(self):
        min_path_len = float("inf")
        for perm in permutations(self.cities):
            path_len = self.GetPathDistance(perm)
            min_path_len = min(min_path_len, path_len)
        return min_path_len
    
    def GetLongestHamiltonianPath(self):
        max_path_len = float("-inf")
        for perm in permutations(self.cities):
            path_len = self.GetPathDistance(perm)
            max_path_len = max(max_path_len, path_len)
        return max_path_len

    def GetPathDistance(self, cities):
        path_len = 0
        for i in range(len(cities)-1):
            path_len += self.GetDistanceTwoCities(cities[i],cities[i+1])
        return path_len

    def GetDistanceTwoCities(self, city1, city2):
        if city1 == city2:
            return 0
        if self.distances.get((city1,city2)) != None:
            return self.distances[(city1,city2)]
        if self.distances.get((city2,city1)) != None:
            return self.distances[(city2,city1)]
        print(f"[-] Distance from {city1} to {city2} does not exist!")
        return -1
    