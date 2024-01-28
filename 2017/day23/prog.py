a, b, c, d, e, f, g, h = 1, 0, 0, 0, 0, 0, 0, 0
b = 79
c = b

if a != 0:
    b *= 100
    b += 100_000
    c = b
    c += 17000

while True:

    print("1", g, h)

    f = 1
    d = 2
    e = 2
    g = d
    g *= e
    g -= b

    # Line 15
    if g == 0:
        f = 0
    e += 1
    g = e
    g -= b

    # Line 20
    while g != 0:
        g = d
        g *= e
        g -= b
        if g == 0:
            f = 0
        e += 1
        g = e
        g -= b

    # Line 21
    d += 1
    g = d
    g -= b

    # Line 24
    while g != 0:
        e = 2

        ################
        """
        # Line 20
        while g != 0:
            g = d
            g *= e
            g -= b
            if g == 0:
                f = 0
            e += 1
            g = e
            g -= b
        """
        e = b
        if d*(e-1) - b == 0:
            f = 0
        g = 0
        ################

        d += 1
        g = d
        g -= b

    # Line 25
    if f == 0:
        h += 1
    g = b
    g -= c

    if g == 0:
        print(f"Value in the <h> register = {h}")
        break

    b += 17
