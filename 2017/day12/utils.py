class Program:
    def __init__(self, id: int, neighbors: list):
        self.neighbors = set(neighbors)
        self.neighbors.add(id)

class ProgramMgr:
    def __init__(self, pipes: str):
        self.programs = {}  # dict: program id => program object
        self._ParsePipes(pipes)

    def GetNumProgramContainingId(self, id):
        num = 0
        for id1 in self.programs:
            num += self._AreNeighbors(id1, id)
        return num
    
    def GetNumGroups(self):
        num = 0
        visited = set()
        for id in self.programs:
            if id in visited: continue
            stack = [id]
            while len(stack):
                id1 = stack.pop()
                if id1 in visited: continue
                visited.add(id1)
                program = self.programs[id1]
                for neighbor in program.neighbors: stack.append(neighbor)
            num += 1
        return num

    def _ParsePipes(self, pipes: str):
        for line in pipes:
            line = line.strip()
            id = int(line[:line.index('<')])
            neighbors = list(map(lambda x: int(x), line[line.index('>')+1:].split(', ')))
            self.programs[id] = Program(id, neighbors)
    
    def _AreNeighbors(self, id1, id2):
        stack = [id1]
        visited = set()
        while len(stack):
            id = stack.pop()
            if id in visited: continue
            program = self.programs[id]
            if id2 in program.neighbors: return True
            visited.add(id)
            for neighbor in program.neighbors: stack.append(neighbor)
        return False


if __name__ == "__main__":
    pipes = """
        0 <-> 2
        1 <-> 1
        2 <-> 0, 3, 4
        3 <-> 2, 4
        4 <-> 2, 3, 6
        5 <-> 6
        6 <-> 4, 5
    """
    manager = ProgramMgr(pipes.strip().split('\n'))
    print(manager.GetNumProgramContainingId(id=0))