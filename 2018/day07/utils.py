import threading
from time import sleep
from string import ascii_uppercase
from collections import defaultdict


class Steps:
    def __init__(self, text):
        self.roots = []
        self.parent2child = defaultdict(list)  # parent => children
        self.child2parent = defaultdict(list)  # child => parents
        self._Process(text)

    def RunTwoWorkers(self):
        pass

    def _Work(self):
        pass

    def GetStepSequence(self):
        seq = ""
        visited = set()
        path_options = self.roots.copy()
        while len(path_options):
            if path_options[-1] in visited:
                path_options.pop()
                continue
            path_options.sort()
            path = path_options.pop(self._GetNextStep(path_options, visited))
            seq += path
            visited.add(path)
            for child in self.parent2child[path]:
                if child not in visited:
                    path_options.append(child)
        return seq

    def _GetNextStep(self, path_options, visited):
        for i in range(len(path_options)):
            if path_options[i] in visited:
                continue
            all_parents_visited = True
            for parent in self.child2parent[path_options[i]]:
                if parent not in visited:
                    all_parents_visited = False
                    break
            if all_parents_visited:
                return i
        return None

    def _Process(self, text):
        parents = set()
        children = set()
        for line in text:
            parent, child = line.split()[1], line.split()[7]
            self.parent2child[parent].append(child)
            self.child2parent[child].append(parent)
            parents.add(parent)
            children.add(child)
        for child in children:
            if child in parents:
                parents.remove(child)
        self.roots = list(parents)