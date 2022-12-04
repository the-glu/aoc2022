
sacks =  []

with open("input") as f:
    for x in f.readlines():
        x = x.strip()
        mid = len(x) // 2
        sacks.append((x[:mid], x[mid:]))

print(sacks)

tt = 0

for s1, s2 in sacks:
    for s in s1:
        if s in s2 and s not in ad:
            print(s)
            sco = ord(s) - 96
            if sco < 0:
                sco += 32 + 26
            tt += sco
            print(sco)
            break

print(tt)


g1, g2, g3 = "", "", ""
tt = 0
print("")
print("")

with open("input") as f:
    for x in f.readlines():
        x = x.strip()
        if x:
            if not g1:
                g1 = x
            elif not g2:
                g2 = x
            elif not g3:
                g3 = x
                print(g1, g2, g3)

                for xx in g1:
                    if xx not in g2 or xx not in g3:
                        continue

                    print(xx)

                    sco = ord(xx) - 96
                    if sco < 0:
                        sco += 32 + 26
                    tt += sco
                    print(sco)
                    break

                g1, g2, g3 = "", "", ""
print(tt)
