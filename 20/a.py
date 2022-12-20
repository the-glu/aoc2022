import copy

I = []

p = 0

with open("input") as f:
    for i in f.readlines():
        i = i.strip()
        if i:
            I.append((int(i) * 811589153, p))
            p += 1

print(I)
base = copy.deepcopy(I)

linked_list = {}

FIRST = I[0]
PREVIOUS = None

for i in I:
    linked_list[i] = [PREVIOUS, None]

    if PREVIOUS is not None:
        linked_list[PREVIOUS][1] = i

    PREVIOUS = i

linked_list[FIRST][0] = i  # Last
linked_list[i][1] = FIRST

print(linked_list)

def mover(i):
    cp, cn = linked_list[i]

    linked_list[cp][1] = cn


    linked_list[cn][0] = cp

    pn = linked_list[cn][1]

    linked_list[i][0] = cn
    linked_list[i][1] = pn
    linked_list[cn][1] = i
    linked_list[pn][0] = i


def moveb(i):
    cp, cn = linked_list[i]

    linked_list[cn][0] = cp
    linked_list[cp][1] = cn

    pp = linked_list[cp][0]

    linked_list[i][0] = pp
    linked_list[i][1] = cp
    linked_list[pp][1] = i
    linked_list[cp][0] = i

# mover(-3)
print(linked_list)

for x in range(10):
    print(x)
    for pouest in base:
        ins, __ = pouest
        # ins //= 811589153
        if ins > 0:
            for _ in range(ins % (len(base) - 1)):
                mover(pouest)
        else:
            for _ in range((-ins) % (len(base) - 1)):
                moveb(pouest)

def at(b, d):

    for bb, bbb in linked_list.keys():
        if bb == b:
            cpos = bb, bbb
            break

    while d > 0:
        d -= 1
        cpos = linked_list[cpos][1]
    return cpos[0]

print(at(0, 1000))
print(at(0, 2000))
print(at(0, 3000))

print(at(0, 1000) + at(0, 2000) + at(0, 3000))

