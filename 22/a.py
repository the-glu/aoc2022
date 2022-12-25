

m = {}
ins = []

ypos = 0
ii = False
mx, my = 0, 0
pos = None

with open("input") as f:
    for i in f.readlines():
        i = i[:-1]
        if i:
            if ii:
                ins = i
            else:
                for xpos, v in enumerate(i):
                    if v != " ":
                        m[(xpos, ypos)] = v
                        if not pos:
                            pos = (xpos, ypos)
                    mx = max(mx, xpos)
                ypos += 1
                my = max(my, ypos)
        else:
            ii = True

print(m, ins, mx, my, pos)

DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]

d = DIRS[0]
dpos = 0

def get_next_input():
    global ins

    if not ins:
        return

    if ins[0] in ["R", "L"]:
        i = ins[0]
        ins = ins[1:]
        return i

    cins = ""

    while ins and ins[0] not in ["R", "L"]:
        cins = cins + ins[0]
        ins = ins[1:]
    return int(cins)

# i = get_next_input()
# while i:
#
#     print(i)
#     if i == "R":
#         dpos += 1
#         dpos = dpos % 4
#         d = DIRS[dpos]
#     elif i == "L":
#         dpos -= 1
#         dpos = dpos % 4
#         d = DIRS[dpos]
#     else:
#
#         for _ in range(i):
#             npos = ((pos[0] + d[0]) % mx, (pos[1] + d[1]) % my)
#
#             while npos not in m:
#                 npos = ((npos[0] + d[0]) % mx, (npos[1] + d[1]) % my)
#
#             print(npos, d)
#
#             if m[npos] == "#":
#                 npos = pos
#
#             pos = npos
#
#     i = get_next_input()



def wrap(pos, dpos):
    if dpos == 0:
        if pos[0] == 149:
            return (99, 149 - pos[1]), 2  # OK
        if pos[0] == 99:
            if 49 < pos[1] < 100:
                return (100 + (pos[1] - 50), 49), 3  # OK
            if 99 < pos[1] < 150:
                return (149, 50 - (pos[1] - 99)), 2  # OK
        if pos[0] == 49:
            return (50 + (pos[1] - 150), 149), 3  # OK
    elif dpos == 1:
        if pos[1] == 49:
            return (99, pos[0] - 100 + 50), 2
        if pos[1] == 149:
            return (49, pos[0] - 50 + 150), 2
        if pos[1] == 199:
            return (pos[0] + 100, 0), 1
    elif dpos == 3:
        if pos[1] == 0:
            if 49 < pos[0] < 100:
                return (0, pos[0] - 50 + 150), 0
            if 49 < pos[0] < 150:
                return (pos[0] - 100, 199), 3
        if pos[1] == 100:
            return (50, pos[0] + 50), 0
    elif dpos == 2:
        if pos[0] == 50:
            if 0 <= pos[1] < 50:
                return (0, 149 - pos[1]), 0
            if 49 < pos[1] < 100:
                return (pos[1] - 50, 100), 1
        if pos[0] == 0:
            if 99 < pos[1] < 150:
                return (50, (149 - pos[1])), 0
            if 149 < pos[1] < 200:
                return (pos[1] - 149 + 49, 0), 1

    print(pos, dpos)
    a = 1 / 0


i = get_next_input()
while i:

    print(i)
    if i == "R":
        dpos += 1
        dpos = dpos % 4
        d = DIRS[dpos]
    elif i == "L":
        dpos -= 1
        dpos = dpos % 4
        d = DIRS[dpos]
    else:

        for _ in range(i):
            npos = ((pos[0] + d[0]), (pos[1] + d[1]))

            if npos not in m:
                npos, ndpos = wrap(pos, dpos)

                if npos not in m:
                    print(pos, dpos, npos)
                    a = 2 / 0

                if m[npos] == "#":
                    npos = pos
                else:
                    dpos = ndpos
                    d = DIRS[dpos]

            if m[npos] == "#":
                npos = pos

            pos = npos

    i = get_next_input()

print(pos, dpos, (pos[0] + 1) * 4 + (pos[1] + 1) * 1000 + dpos % 4)
