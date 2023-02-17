from itertools import product
from BellmanFord import Graph


class Valve():
    def __init__(self, valve_map, valveName2idx_dict, valveIdx2name_dict, valve_flow):
        self.map = valve_map
        self.name2idx = valveName2idx_dict
        self.idx2name = valveIdx2name_dict
        self.flow = valve_flow
        self.start = 'AA'
        self.time = None

        # Memoization
        self.visited_states = {}

        # Find shortest paths among all vertice pairs
        # <vertice_pair_SP>: [[0,4,2,8], [4,0,7,3], [...], ...]
        self.vertice_pair_SP = self.buildGraph()

    def buildGraph(self):
        g = Graph(len(self.map))
        spList = []
        for s, edge_list in enumerate(self.map):
            for t in edge_list:
                g.add_edge(s, self.name2idx[t], 1)
                g.add_edge(self.name2idx[t], s, 1)

        for v, flow in enumerate(self.flow):
            spList.append(g.bellman_ford(v))
        return spList

    def findLargestFlow(self, start, time_left, players_left, opened_valves): # opened_valves: set()
        # Base cases
        if time_left <= 1:
            if players_left == 0:
                return 0
            else:
                return self.findLargestFlow(self.start, self.time, 
                                            players_left-1, opened_valves)

        # Memoization
        hov = self.getHashableObj(opened_valves)
        if (start,time_left,players_left,hov) in self.visited_states:
            return self.visited_states.get((start,time_left,players_left,hov))

        start_idx = self.name2idx[start]
        subProblems = []

        # if current valve is not opened and has non-zero flow
        if start not in opened_valves and self.flow[start_idx] > 0:
            opened_valves.add(start)
            res = (time_left-1)*self.flow[start_idx] +\
                    self.findLargestFlow(start, time_left-1, players_left, opened_valves)
            subProblems.append(res)
            opened_valves.remove(start)

        # go to all other non-zero vertices
        for v, flow in enumerate(self.flow):
            if flow > 0 and v != start_idx:
                distance = self.vertice_pair_SP[start_idx][v]
                res = self.findLargestFlow(self.idx2name[v], time_left-distance, 
                                            players_left, opened_valves)
                subProblems.append(res)

        self.visited_states[(start,time_left,players_left,hov)] = max(subProblems)
        return max(subProblems)

    def reset(self):
        self.visited_states.clear()

    def getHashableObj(self, obj): # returns a hashable object from a set
        ret = list(obj)
        ret.sort()
        return tuple(ret)
