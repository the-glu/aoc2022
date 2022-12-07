
root = {"dirs": {}, "files": {}, "papa": None}


with open("input") as f:

    cdir = root

    for x in f.readlines():
        x = x.strip()

        if x == "$ cd /":
            continue
        elif x.startswith("$ ls"):
            continue
        elif x.startswith("$ cd"):
            xx = x.split(" ")
            if xx[2] == "..":
                cdir = cdir["papa"]
            else:
                cdir = cdir["dirs"][xx[2]]
        else:
            xx = x.split(" ")
            if xx[0] == "dir":
                cdir["dirs"][xx[1]] = {"dirs": {}, "files": {}, "papa": cdir}
            else:
                cdir["files"][xx[1]] = int(xx[0])

print(root)

def comp_size(d):
    tt = 0
    for sdir in d["dirs"].values():
        comp_size(sdir)
        tt += sdir["size"]
    for f in d["files"].values():
        tt += f
    d["size"] = tt

comp_size(root)
print(root)

def fs(d):
    tt = 0
    for sdir in d["dirs"].values():
        tt += fs(sdir)

    if d["size"] < 100000:
        tt += d["size"]
    return tt


print(fs(root))


cused = 70000000 - root["size"]
need_to_delete = 30000000 - cused

best_rm = None
best_rm_size = 99999999

def fs2(k, d):
    global best_rm, best_rm_size
    for k, sdir in d["dirs"].items():
        fs2(k, sdir)

    if d["size"] > need_to_delete:
        if d["size"] < best_rm_size:
            best_rm_size = d["size"]
            best_rm = k

print(need_to_delete)
fs2("/", root)
print(best_rm, best_rm_size)

