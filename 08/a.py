
m = {}

with open("input") as f:

    px = 0

    for x in f.readlines():
        x = x.strip()
        if not x:
            continue

        for y, xx in enumerate(x):
            m[(px, y)] = xx

        px += 1

visi = 0

for (bx, by), bv in m.items():
    # v1 = True
    # v2 = True
    # v3 = True
    # v4 = True
    #
    # tx, ty = bx, by
    #
    # while True:
    #     tx -= 1
    #
    #     if (tx, ty) not in m:
    #         break
    #     if m[(tx, ty)] >= bv:
    #         v1 = False
    #         break
    #
    # tx, ty = bx, by
    #
    # while True:
    #     tx += 1
    #
    #     if (tx, ty) not in m:
    #         break
    #     if m[(tx, ty)] >= bv:
    #         v2 = False
    #         break
    #
    # tx, ty = bx, by
    #
    # while True:
    #     ty -= 1
    #
    #     if (tx, ty) not in m:
    #         break
    #     if m[(tx, ty)] >= bv:
    #         v3 = False
    #         break
    #
    # tx, ty = bx, by
    #
    # while True:
    #     ty += 1
    #
    #     if (tx, ty) not in m:
    #         break
    #     if m[(tx, ty)] >= bv:
    #         v4 = False
    #         break
    #
    # if v1 or v2 or v3 or v4:
    #     visi += 1


    v1 = 0
    v2 = 0
    v3 = 0
    v4 = 0

    tx, ty = bx, by

    while True:
        tx -= 1

        if (tx, ty) not in m:
            break
        if m[(tx, ty)] < bv:
            v1 += 1
        else:
            v1 += 1
            break

    tx, ty = bx, by

    while True:
        tx += 1

        if (tx, ty) not in m:
            break
        if m[(tx, ty)] < bv:
            v2 += 1
        else:
            v2 += 1
            break

    tx, ty = bx, by

    while True:
        ty -= 1

        if (tx, ty) not in m:
            break
        if m[(tx, ty)] < bv:
            v3 += 1
        else:
            v3 += 1
            break

    tx, ty = bx, by

    while True:
        ty += 1

        if (tx, ty) not in m:
            break
        if m[(tx, ty)] < bv:
            v4 += 1
        else:
            v4 += 1
            break

    s = v1 * v2 * v3 * v4
    if s > visi:
        visi = s

print(visi)

