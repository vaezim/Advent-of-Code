##### Bottom-Up Approach #####
from queue import deque

class Path():
    def __init__(self, _map, init_pos, final_pos):
        self.map = _map
        self.init_pos = init_pos
        self.final_pos = final_pos

        self.discovered = [[float('inf')]*len(_map[0]) for _ in range(len(_map))]
        self.discovered[final_pos[0]][final_pos[1]] = 0

        self.visited = set()

        self.explore_queue = deque()
        self.explore_queue.append(final_pos)
        self.in_queue = set()
        self.in_queue.add(tuple(final_pos))

    def explore(self):
        while len(self.explore_queue):
            node = self.explore_queue.popleft()
            x1, y1 = node[0], node[1]
            self.in_queue.remove(tuple(node))

            self.visited.add(tuple(node))

            # Top
            if (x1-1,y1) not in self.visited and (x1-1,y1) not in self.in_queue and self.canGo([x1-1,y1], node):
                self.localShortestPath([x1-1,y1])
                self.explore_queue.append([x1-1,y1])
                self.in_queue.add((x1-1,y1))
            # Bottom
            if (x1+1,y1) not in self.visited and (x1+1,y1) not in self.in_queue and self.canGo([x1+1,y1], node):
                self.localShortestPath([x1+1,y1])
                self.explore_queue.append([x1+1,y1])
                self.in_queue.add((x1+1,y1))
            # Left
            if (x1,y1-1) not in self.visited and (x1,y1-1) not in self.in_queue and self.canGo([x1,y1-1], node):
                self.localShortestPath([x1,y1-1])
                self.explore_queue.append([x1,y1-1])
                self.in_queue.add((x1,y1-1))
            # Right
            if (x1,y1+1) not in self.visited and (x1,y1+1) not in self.in_queue and self.canGo([x1,y1+1], node):
                self.localShortestPath([x1,y1+1])
                self.explore_queue.append([x1,y1+1])
                self.in_queue.add((x1,y1+1))

    def localShortestPath(self, node):
        x1, y1 = node[0], node[1]
        neighbor_path_len = []
        
        # Top
        if self.canGo(node, [x1-1,y1]):
            neighbor_path_len.append(self.discovered[x1-1][y1])
        # Bottom
        if self.canGo(node, [x1+1,y1]):
            neighbor_path_len.append(self.discovered[x1+1][y1])
        # Left
        if self.canGo(node, [x1,y1-1]):
            neighbor_path_len.append(self.discovered[x1][y1-1])
        # Right
        if self.canGo(node, [x1,y1+1]):
            neighbor_path_len.append(self.discovered[x1][y1+1])

        self.discovered[x1][y1] = min(self.discovered[x1][y1], min(neighbor_path_len)+1)

    def globalShortestPath(self):
        self.explore()
        x1, y1 = self.init_pos[0], self.init_pos[1]
        return self.discovered[x1][y1]

    def canGo(self, loc1, loc2): # is loc2 climbable from loc1
        x1, y1 = loc1[0], loc1[1]
        x2, y2 = loc2[0], loc2[1]
        if x1 < 0 or y1 < 0 or x1 >= len(self.map) or y1 >= len(self.map[0]):
            return False
        if x2 < 0 or y2 < 0 or x2 >= len(self.map) or y2 >= len(self.map[0]):
            return False
        h1, h2 = self.map[x1][y1], self.map[x2][y2]
        return ord(h2) - ord(h1) <= 1
        