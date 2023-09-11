
def GetStringAndMemoryDiff(line: str) -> int:
    diff = 2 # two double-quotes at the beggining and at the end
    line = line[1:-1]
    i = 0
    while i < len(line):
        c = line[i]
        if c != "\\":           # normal ascii char
            i += 1
            continue
        if line[i+1] != 'x':    # \"
            i += 2
            diff += 1
            continue
        diff += 3               # \xcd
        i += 4
    return diff

def GetStringAndEncodedDiff(line: str) -> int:
    diff = 2 # two double-quotes at the beggining and at the end
    for c in line:
        diff += c == '\\'
        diff += c == '"'
    return diff
