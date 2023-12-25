class Desert:
    def __init__(self, text):
        self.dirs = text[0].strip()
        self.nodes = self._GetNodes(text[2:])

    def GetNumSteps(self):
        curr = "AAA"
        steps = 0
        while curr != "ZZZ":
            i = steps % len(self.dirs)
            steps += 1
            if self.dirs[i] == "L":
                curr = self.nodes[curr][0]
            else:
                curr = self.nodes[curr][1]
        return steps
    
    def GetNumGhostSteps(self):
        curr = self._GetANodes()
        steps = 0
        while not self._AreAllEndingInZ(curr):
            i = steps % len(self.dirs)
            steps += 1
            for n in range(len(curr)):
                if self.dirs[i] == "L":
                    curr[n] = self.nodes[curr[n]][0]
                else:
                    curr[n] = self.nodes[curr[n]][1]

            print(steps, [i*curr[n].endswith("Z") for n in range(len(curr))])
                
        return steps

    def _GetANodes(self):
        a_nodes = []
        for node in self.nodes:
            if node[-1] == "A":
                a_nodes.append(node)
        return a_nodes
    
    def _AreAllEndingInZ(self, nodes):
        for n in nodes:
            if n[-1] != "Z":
                return False
        return True

    def _GetNodes(self, text):
        nodes = {}
        for line in text:
            tokens = line.split()
            nodes[tokens[0]] = (tokens[2][1:-1], tokens[3][:-1])
        return nodes