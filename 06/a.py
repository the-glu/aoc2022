
with open("input") as f:
    for x in f.readlines():
        x = x.strip()
        last_x = []
        index = 0
        for xx in x:
            index += 1
            last_x.append(xx)
            if len(last_x) > 14:
                last_x.pop(0)
                ok = True
                for xp, xxx in enumerate(last_x):
                    if last_x.index(xxx) != xp:
                        ok = False
                if ok:
                    print(last_x, index)
                    break

