import networkx as nx
import copy


VA = {}


with open("input") as f:
    for i in f.readlines():
        i = i.strip()
        if i:
            a, b = i.split(";")
            a = a.split(" ")
            paths = b.split("to ")[1].split(", ")
            if paths:
                paths[0] = paths[0].split(" ")[1]
            VA[a[1]] = [int(a[4].split("=")[1]), False, paths]

print(VA)

max_score = 0
opti = {}


def gen_pos(cpos, V, mreming, score):
    global max_score, opti
    if mreming == 0:
        if score > max_score:
            max_score = score
            print(score)
        return []

    if (cpos, mreming) in opti:
        if opti[(cpos, mreming)] >= score:
            return

    opti[(cpos, mreming)] = score

    posbilies = []

    if not V[cpos][1] and V[cpos][0]:
        posbilies.append("!!")

    move_ok = False
    for s, o, _ in V.values():
        if s and not o:
            move_ok = True
            break

    if move_ok:
        for dest in V[cpos][2]:
            posbilies.append(dest)

    if not posbilies:
        posbilies.append("--")

    fpos = []

    nscore = score
    ds = 0
    for s, o, _ in V.values():
        if o:
            ds += s

    nscore += ds

    if posbilies[0] == "--":
        while mreming > 0:
            nscore += ds
            mreming -= 1

        if nscore > max_score:
            max_score = nscore
        return []

    for pos in posbilies:
        if pos != "--" and pos != "!!":
            tpos = pos
        else:
            tpos = cpos
        if pos == "!!":
            V2 = copy.deepcopy(V)
            V2[cpos][1] = True
        else:
            V2 = V
        gen_pos(tpos, V2, mreming - 1, nscore)

# x = gen_pos("AA", VA, 30, 0)
# print("Done")
# print(max_score)
# print(max_score)

def gen_pos_v2(cpos, cpos2, mreming, score):
    global max_score, opti
    if mreming == 0:
        if score > max_score:
            max_score = score
            print(max_score)
        return

    if (cpos, cpos2, mreming) in opti:
        if opti[(cpos, cpos2, mreming)] >= score:
            return

    opti[(cpos, cpos2, mreming)] = score

    move_ok = False
    ds = 0
    for s, o, _ in VA.values():
        if s and not o:
            move_ok = True
        elif o:
            ds += s

    if not move_ok:  # Quick end
        gen_pos_v2(cpos, cpos2, mreming - 1, score + ds)
        return

    if not VA[cpos][1] and VA[cpos][0]:  # Openable

        # Try to open
        VA[cpos][1] = True
        ds += VA[cpos][0]

        # ELOPEN
        if not VA[cpos2][1] and VA[cpos2][0]:  # Openable
            VA[cpos2][1] = True
            ds += VA[cpos2][0]

            gen_pos_v2(cpos, cpos2, mreming - 1, score + ds)

            VA[cpos2][1] = False
            ds -= VA[cpos2][0]

        for dest in VA[cpos2][2]:  # Move E
            gen_pos_v2(cpos, dest, mreming - 1, score + ds)
        VA[cpos][1] = False
        ds -= VA[cpos][0]

    # Just move
    for dest in VA[cpos][2]:

        # ELOPEN
        if not VA[cpos2][1] and VA[cpos2][0]:  # Openable
            VA[cpos2][1] = True
            ds += VA[cpos2][0]

            gen_pos_v2(dest, cpos2, mreming - 1, score + ds)

            VA[cpos2][1] = False
            ds -= VA[cpos2][0]


        for dest2 in VA[cpos2][2]:  # Move E
            gen_pos_v2(dest, dest2, mreming - 1, score + ds)

gen_pos_v2("AA", "AA", 25, 0)
print("Done")
print(max_score)
