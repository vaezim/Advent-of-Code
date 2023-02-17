
def isHorVer(vent):
    head, tail = vent[0], vent[1]
    if head[0] == tail[0]:
        return 'V'
    if head[1] == tail[1]:
        return 'H'
    return False
    