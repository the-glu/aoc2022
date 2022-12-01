elfs = []

ct = 0

with open("input") as f:
    for x in f.readlines():
        if not x.strip():
            elfs.append(ct)
            ct = 0
        else:
            ct += int(x)

    elfs.append(ct)

print(elfs)
ttt = 0
for x in range(3):
    tt = max(elfs)
    ttt += tt
    print(ttt, tt)
    elfs.remove(tt)

