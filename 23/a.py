
m = {}
ypos = 0

with open("input") as f:
    for i in f.readlines():
        i = i.strip()
        if i:
            for xpos, v in enumerate(i):
                m[(xpos, ypos)] = v
            ypos += 1

print(m)

POSD = [
    ((0, -1), [(0, -1), (-1, -1), (1, -1)]),
    ((0, 1), [(0, 1), (-1, 1), (1, 1)]),
    ((-1, 0), [(-1, 0), (-1, 1), (-1, -1)]),
    ((1, 0), [(1, 0), (1, 1), (1, -1)]),
]


def dispm():
    global m

    mmx, mpx, mmy, mpy = 10000000000, -100000000, 1000000000, -1000000

    for x, y in m.keys():
        mmx = min(mmx, x)
        mmy = min(mmy, y)
        mpx = max(mpx, x)
        mpy = max(mpy, y)

    print("")
    tt = 0

    for y in range(mmy, mpy + 1):
        for x in range(mmx, mpx + 1):
            print(m.get((x, y), "."), end="")
        print("")
    print("")

dispm()

for _ in range(100000000):

    wanted_targets = []
    wanted_moves = []

    nm = {}
    moved = False

    for (x, y), v in m.items():
        if v == "#":
            should_move = False
            cannotmove = True

            for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, 0), (1, -1), (1, 1)]:
                if m.get((x + dx, y + dy)) == "#":
                    should_move = True

            if should_move:
                for dx, dtests in POSD:
                    moveok = True
                    for dtest in dtests:
                        if m.get((x + dtest[0], y + dtest[1])) == "#":
                            moveok = False
                            break

                    if moveok:
                        wanted_moves.append(((x, y), (x + dx[0], y + dx[1])))
                        wanted_targets.append((x + dx[0], y + dx[1]))
                        cannotmove = False
                        break

            if cannotmove:
                nm[(x, y)] = "#"
                # wanted_targets.append((x, y))
            else:
                moved = True

    if not moved:
        print(_ + 1)
        a = 1 / 0

    for ps, pd in wanted_moves:
        if wanted_targets.count(pd) == 1:
            nm[pd] = "#"
        else:
            nm[ps] = "#"

    m = nm
    # dispm()

    dx, dtests = POSD.pop(0)
    POSD.append((dx, dtests))

print(m)

mmx, mpx, mmy, mpy = 10000000000, -100000000, 1000000000, -1000000

for x, y in m.keys():
    mmx = min(mmx, x)
    mmy = min(mmy, y)
    mpx = max(mpx, x)
    mpy = max(mpy, y)

print(mmx, mpx, mmy, mpy)

tt = 0

for x in range(mmx, mpx + 1):
    for y in range(mmy, mpy + 1):
        if (x, y) not in m:
            tt += 1

print(tt)
