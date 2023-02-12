
class Shape():
    def __init__(self):
        self.shapes = []
        self.populateShapes()

    def populateShapes(self):
        # Shapes start from x = 2
        s1 = [[0,2], [0,3], [0,4], [0,5]] # -
        s2 = [[0,3], [1,2], [1,3], [1,4], [2,3]] # +
        s3 = [[0,2], [0,3], [0,4], [1,4], [2,4]] # L
        s4 = [[0,2], [1,2], [2,2], [3,2]] # |
        s5 = [[0,2], [0,3], [1,2], [1,3]] # .
        self.shapes.append(s1)
        self.shapes.append(s2)
        self.shapes.append(s3)
        self.shapes.append(s4)
        self.shapes.append(s5)

        