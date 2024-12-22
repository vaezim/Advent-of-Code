import numpy as np
from math import modf
from copy import deepcopy


class Solver:
    def __init__(self, lines):
        self.A = []
        self.B = []
        self._ParseLinearSystem(lines)

    def SolvePart1(self):
        total = 0
        for i in range(len(self.A)):
            A = np.array(self.A[i])
            B = np.array(self.B[i])
            total += self._BruteForceSolver(A, B)
        return total

    def SolvePart2(self):
        count = 0
        for i in range(len(self.A)):
            A = np.array(self.A[i])
            B = np.array(self.B[i])
            B += 10000000000000
            if np.linalg.det(A) != 0:
                x = np.linalg.solve(A, B)
                button_a, button_b = round(x[0]), round(x[1])
                if (button_a * A[0][0] + button_b * A[0][1] == B[0]) and\
                   (button_a * A[1][0] + button_b * A[1][1] == B[1]):
                    count += (3*button_a + button_b)
        return count

    def _BruteForceSolver(self, A, B):
        price = 1_000_000
        for i in range(100):
            for j in range(100):
                b1 = A[0][0] * i + A[0][1] * j
                b2 = A[1][0] * i + A[1][1] * j
                if b1 == B[0] and b2 == B[1]:
                    price = min(price, 3*i+j)
        if price != 1_000_000: return price
        return 0

    def _ParseLinearSystem(self, lines):
        for i in range(len(lines)//4+1):
            l1, l2, l3 = lines[4*i], lines[4*i+1], lines[4*i+2]
            a11 = int(l1[l1.index("X+")+2:l1.index(',')])
            a12 = int(l1[l1.index("Y+")+2:])
            a21 = int(l2[l2.index("X+")+2:l2.index(',')])
            a22 = int(l2[l2.index("Y+")+2:])
            b1  = int(l3[l3.index("X=")+2:l3.index(',')])
            b2  = int(l3[l3.index("Y=")+2:])
            A = [[a11, a21], [a12, a22]]
            B = [b1, b2]
            self.A.append(deepcopy(A))
            self.B.append(deepcopy(B))