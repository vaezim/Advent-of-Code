from math import lcm


class Desert:
    def __init__(self, text: list):
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
        A_nodes = self._GetANodes()
        A_nodes_cycles = []
        for node in A_nodes:
            A_nodes_cycles.append(self._GetANodeCycle(node)[0])
        return lcm(*A_nodes_cycles)

    def _GetANodeCycle(self, A_node):
        Z_steps = []
        curr = A_node
        hashes = set()
        step = 0
        while True:
            i = step % len(self.dirs)
            H = self._Hash(curr, i)
            if H in hashes:
                break
            hashes.add(H)
            if self.dirs[i] == "L":
                curr = self.nodes[curr][0]
            else:
                curr = self.nodes[curr][1]
            step += 1
            if curr[-1] == "Z":
                Z_steps.append(step)
        return Z_steps

    def _Hash(self, node, i):
        return f"{node}{i}"

    def _GetANodes(self):
        a_nodes = []
        for node in self.nodes:
            if node[-1] == "A":
                a_nodes.append(node)
        return a_nodes

    def _GetNodes(self, text):
        nodes = {}
        for line in text:
            tokens = line.split()
            nodes[tokens[0]] = (tokens[2][1:-1], tokens[3][:-1])
        return nodes
