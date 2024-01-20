class Ray:
    def __init__(self, layout, starting_position, direction):
        self.Layout = layout
        self.Layout.AddRay(self)
        self.grid = layout.GetGrid()
        self.pos = starting_position    # [x, y]
        self.dir = direction            # ['N','W','E','S']
        self.visited = set()            # (x,y,dir)
        self.turn_map = {
            ".": {
                "N": "N", "W": "W", "E": "E", "S": "S"
            },
            "/": {
                "W": "S", "S": "W", "E": "N", "N": "E"
            },
            "\\": {
                "W": "N", "N": "W", "E": "S", "S": "E"
            },
            "-": {
                "E": "E", "W": "W", "N": "EW", "S": "EW"
            },
            "|": {
                "N": "N", "S": "S", "W": "NS", "E": "NS"
            }
        }
        self._Run()

    def _Run(self):
        x, y = self.pos[0],self.pos[1]
        # DP
        state = (x,y,self.dir)
        if state in self.visited:
            return
        self.visited.add(state)
        self.Layout.grid_energy_level[x][y] += 1
        # Turns
        rock_type = self.grid[x][y]
        turns = self.turn_map[rock_type][self.dir]
        initial_pos = self.pos.copy()
        turn = turns[0]
        self.dir = turn
        if turn == "N" and x > 0:
            self.pos[0] -= 1
        elif turn == "S" and x < len(self.grid)-1:
            self.pos[0] += 1
        elif turn == "W" and y > 0:
            self.pos[1] -= 1
        elif turn == "E" and y < len(self.grid[0])-1:
            self.pos[1] += 1
        # If Ray is split, Create another Ray
        if len(turns) == 2:
            Ray(self.Layout, initial_pos, turns[1])
        # Continue is position is changed
        if self.pos != initial_pos:
            return self._Run()
        
class Layout:
    def __init__(self, grid):
        self.grid = grid
        self.grid_energy_level = [[0]*len(self.grid[0]) for _ in range(len(self.grid))]
        self.rays = []

    def CastRay(self):
        ray = Ray(self, [0,0], "E")
        self.rays.append(ray)

    def AddRay(self, ray):
        self.rays.append(ray)

    def GetGrid(self):
        return self.grid