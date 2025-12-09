from math import sqrt


class Solver:
    def __init__(self, lines):
        self.points = [] # (x,y,z)
        self.circuits = [] # set(points)
        for line in lines:
            point = tuple(map(lambda x: int(x), line.split(',')))
            self.points.append(point)

    def SolvePart1(self):
        # Find distances of all pairs
        self.distances = []
        for i in range(len(self.points)):
            for j in range(i+1, len(self.points)):
                p1, p2 = self.points[i], self.points[j]
                distance = sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)
                self.distances.append((distance, p1, p2))
        self.distances.sort(key=lambda x: x[0])

        # Make top 1000 shortest connections
        for i in range(1000):
            p1, p2 = self.distances[i][1], self.distances[i][2]
            p1_circuit, p2_circuit = None, None
            for c_i, circuit in enumerate(self.circuits):
                if p1 in circuit:
                    p1_circuit = c_i
                if p2 in circuit:
                    p2_circuit = c_i
            if p1_circuit == None and p2_circuit == None:
                self.circuits.append({ p1, p2 })
            elif p1_circuit == None:
                self.circuits[p2_circuit].add(p1)
            elif p2_circuit == None:
                self.circuits[p1_circuit].add(p2)
            elif p1_circuit != p2_circuit:
                self.circuits[p1_circuit] = self.circuits[p1_circuit].union(self.circuits[p2_circuit])
                self.circuits.remove(self.circuits[p2_circuit])
        self.circuits.sort(key=lambda x: len(x), reverse=True)

        # Multiply top 3 longest circuits
        ans = 1
        for i in range(3):
            ans *= len(self.circuits[i])
        return ans

    def SolvePart2(self):
        # Make all shortest connections until all junctions are connected
        for i in range(len(self.distances)):
            p1, p2 = self.distances[i][1], self.distances[i][2]
            p1_circuit, p2_circuit = None, None
            for c_i, circuit in enumerate(self.circuits):
                if p1 in circuit:
                    p1_circuit = c_i
                if p2 in circuit:
                    p2_circuit = c_i
            if p1_circuit == None and p2_circuit == None:
                self.circuits.append({ p1, p2 })
            elif p1_circuit == None:
                self.circuits[p2_circuit].add(p1)
            elif p2_circuit == None:
                self.circuits[p1_circuit].add(p2)
            elif p1_circuit != p2_circuit:
                self.circuits[p1_circuit] = self.circuits[p1_circuit].union(self.circuits[p2_circuit])
                self.circuits.remove(self.circuits[p2_circuit])
            if len(self.circuits[0]) == len(self.points):
                return p1[0] * p2[0]
        return None
