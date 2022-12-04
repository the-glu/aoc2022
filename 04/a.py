
l = []

with open("input") as f:
    for x in f.readlines():
        x = x.strip()
        p1, p2 = x.split(",")
        x1, x2 = p1.split("-")
        x3, x4 = p2.split("-")
        l.append((list(range(int(x1), int(x2) + 1)), list(range(int(x3), int(x4) + 1))))


tt = 0

for r1, r2 in l:
    # print(r1, r2)
    # ok = True
    # for r in r1:
    #     if r not in r2:
    #         ok = False
    #
    # print(ok)
    # if ok:
    #     tt += 1
    # else:
    #
    #     ok = True
    #     for r in r2:
    #         if r not in r1:
    #             ok = False
    #     print(ok)
    #     if ok:
    #         tt += 1

    ok = False
    for r in r1:
        if r in r2:
            ok = True

    if ok:
        tt += 1
    else:

        ok = False
        for r in r2:
            if r in r1:
                ok = True
        print(ok)
        if ok:
            tt += 1

print(tt)

