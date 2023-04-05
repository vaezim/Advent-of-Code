
def draw_line(point1, point2, vent_map):
    x1, y1, x2, y2 = point1[0], point1[1], point2[0], point2[1]
    if x1 == x2:
        x = x1
        for j in range(min(y1,y2),\
                       max(y1,y2)+1):
            vent_map[x][j] += 1
        return True
    elif y1 == y2:
        y = y1
        for i in range(min(x1,x2),\
                       max(x1,x2)+1):
            vent_map[i][y] += 1
        return True
    else:
        return False

def draw_diagonal(point1, point2, vent_map):
    x1, y1, x2, y2 = point1[0], point1[1], point2[0], point2[1]
    if x1 == x2 or y1 == y2:
        return False
    direction = [round((x2-x1)/abs(x2-x1)),\
                 round((y2-y1)/abs(y2-y1))]
    for i in range(abs(y2-y1)+1):
        vent_map[x1+i*direction[0]][y1+i*direction[1]] += 1
    return True
