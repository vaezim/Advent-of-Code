
def ApplyLights1(instruct: str, grid):
    words = instruct.strip().split()
    x2,y2 = map(lambda x: int(x), words[-1].split(','))
    turn_modes = {"off": 0, "on": 1}
    
    if words[0] == "toggle":
        x1,y1 = map(lambda x: int(x), words[1].split(','))
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                grid[i][j] = int(not grid[i][j])
    else:
        x1,y1 = map(lambda x: int(x), words[2].split(','))
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                grid[i][j] = turn_modes[words[1]]

def ApplyLights2(instruct: str, grid):
    words = instruct.strip().split()
    x2,y2 = map(lambda x: int(x), words[-1].split(','))
    turn_modes = {"off": -1, "on": 1}
    
    if words[0] == "toggle":
        x1,y1 = map(lambda x: int(x), words[1].split(','))
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                grid[i][j] += 2
    else:
        x1,y1 = map(lambda x: int(x), words[2].split(','))
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                grid[i][j] += turn_modes[words[1]]
                grid[i][j] = max(0, grid[i][j])
