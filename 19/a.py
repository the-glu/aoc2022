
import copy
BLUEPRINTS = {}

with open("input") as f:
    for i in f.readlines():
        i = i.strip()
        if i:
            x = i.split(" ")
            BLUEPRINTS[int(x[1][:-1])] = {"ore": [("ore", int(x[6]))], "clay": [("ore", int(x[12]))], "obsi": [("ore", int(x[18])), ("clay", int(x[21]))], "geode": [("ore", int(x[27])), ("obsi", int(x[30]))]}

optimizator = {}

def do_step(b, robots, resou, mr):

    def cpm():
        claym = b["clay"][0][1]
        obsim = b["obsi"][0][1] + b["obsi"][1][1] * claym
        geom = b["geode"][0][1] + b["geode"][1][1] * obsim

        return robots["ore"] + robots["clay"] * claym + robots["obsi"] * obsim + robots["geode"] * geom

    global optimizator

    kok = f"{mr}-{resou}"

    if kok in optimizator:
        if optimizator[kok][1] >= cpm():
            return optimizator[kok][0]

    if mr == 0:
        return resou["geode"]

    robots_possible = []

    for r, rr in b.items():
        ok = True
        for x, q in rr:
            if resou[x] < q:
                ok = False

        if ok:
            robots_possible.append(r)

    nresou = copy.deepcopy(resou)

    for k, i in robots.items():
        nresou[k] += i

    cmax = 0

    robots_possible.append(None)

    # Prio
    if "geode" in robots_possible:
        robots_possible = ["geode"]
    elif "obsi" in robots_possible:
        robots_possible = ["obsi"]

    for choice in robots_possible:
        nrobots = copy.deepcopy(robots)
        n2resou = copy.deepcopy(nresou)

        if choice:
            for x, q in b[choice]:
                n2resou[x] -= q
            nrobots[choice] += 1

        cmax = max(cmax, do_step(b, nrobots, n2resou, mr - 1))

    optimizator[kok] = (cmax, cpm())

    return cmax


tt = 0
for bid, b in BLUEPRINTS.items():

    robots = {
        "ore": 1,
        "clay": 0,
        "obsi": 0,
        "geode": 0,
    }

    resou = {
        "ore": 0,
        "clay": 0,
        "obsi": 0,
        "geode": 0,
    }

    optimizator = {}
    x = do_step(b, robots, resou, 32)
    tt += bid * x
    print(bid, x, bid * x, tt)
