
def compare(l, r): # Part 1
    if l == r:
        return -1

    for i in range(max(len(l),len(r))):
        if i == len(l) and i < len(r):
            return True
        if i == len(r) and i < len(l):
            return False

        if type(l[i]) == int and type(r[i]) == int:
            if l[i] == r[i]:
                continue
            return l[i] < r[i]

        elif type(l[i]) == int:
            res = compare([l[i]], r[i])
            if res != -1:
                return res

        elif type(r[i]) == int:
            res = compare(l[i], [r[i]])
            if res != -1:
                return res

        else: # both are of type <list>
            res = compare(l[i], r[i])
            if res != -1:
                return res

    return -1

def comparator(l, r): # Part 2
    if l == r:
        return 0
    if not len(l):
        return 1
    if not len(r):
        return -1

    for i in range(max(len(l),len(r))):
        if i == len(l) and i < len(r):
            return 1
        if i == len(r) and i < len(l):
            return -1

        if type(l[i]) == int and type(r[i]) == int:
            if l[i] == r[i]:
                continue
            return 1 if l[i] < r[i] else -1

        elif type(l[i]) == int:
            res = comparator([l[i]], r[i])
            if res != 0:
                return res

        elif type(r[i]) == int:
            res = comparator(l[i], [r[i]])
            if res != 0:
                return res

        else: # both are of type <list>
            res = comparator(l[i], r[i])
            if res != 0:
                return res

    return 0
    