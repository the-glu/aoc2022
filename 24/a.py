
m = {}
ypos = 0

sx, sy = 0, 0
ex, ey = 0, 0

with open("input") as f:
    for i in f.readlines():
        i = i.strip()
        if i:
            for xpos, v in enumerate(i):
                m[(xpos, ypos)] = v
                if v == "S":
                    sx, sy = xpos, ypos
                if v == "E":
                    ex, ey = xpos, ypos
            ypos += 1

print(m)

x1 = 1
x2 = 6
y1 = 1
y2 = 4

# x1 = 1
# x2 = 120
# y1 = 1
# y2 = 25

B = []

for (x, y), v in m.items():
    if v in [">", "v", "^", "<"]:
        B.append((v, (x, y)))

def do_b(bb):
    nb = []
    for b, (x, y) in bb:
        if b == ">":
            x += 1
        elif b == "v":
            y += 1
        elif b == "^":
            y -= 1
        elif b == "<":
            x -= 1

        if x < x1:
            x = x2
        if x > x2:
            x = x1
        if y < y1:
            y = y2
        if y > y2:
            y = y1

        nb.append((b, (x, y)))

    return nb

BB = []
BB.append(B)

cycle = 1

b = do_b(B)

while b != B:
    BB.append(b)
    cycle += 1
    b = do_b(b)

print(cycle)

import networkx as nx

G = nx.DiGraph()

ocup = []

for step, b in enumerate(BB):
    m = []

    for _, (x, y) in b:
        m.append((x, y))

    ocup.append(m)

for step, b in enumerate(BB):
    G.add_node((step, sx, sy))
    G.add_node((step, ex, ey))
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            G.add_node((step, x, y))

print(sx, sy)
print(ex, ey)
for step, b in enumerate(BB):

    next_step = step + 1
    if next_step == len(BB):
        next_step = 0

    print("Building", step, next_step)

    G.add_edge((step, sx, sy), (next_step, sx, sy))
    G.add_edge((step, ex, ey), (next_step, ex, ey))

    if (sx, sy + 1) not in ocup[next_step]:
        G.add_edge((step, sx, sy), (next_step, sx, sy + 1))

    G.add_edge((step, sx, sy + 1), (next_step, sx, sy))

    G.add_edge((step, ex, ey - 1), (next_step, ex, ey))

    if (ex, ey - 1) not in ocup[next_step]:
        G.add_edge((step, ex, ey), (next_step, ex, ey - 1))

    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if (x, y) not in ocup[step]:
                for dx, dy in [(0, 0), (1, 0), (0, 1), (-1, 0), (0, -1)]:
                    if x1 <= (x + dx) <= x2 and y1 <= (y + dy) <= y2:
                        if (x + dx, y + dy) not in ocup[next_step]:
                            if x + dx == 6 and y + dy == 5:
                                print("!!!")
                            G.add_edge((step, x, y), (next_step, x + dx, y + dy))

tt = 0
mx = 1900000
mmp1dest = 0
for xx in range(len(BB)):
    try:
        # print("Checking", xx)
        l = len(nx.shortest_path(G, (0, sx, sy), (xx, ex, ey)))
        if l < mx:
            print(l, xx, nx.shortest_path(G, (0, sx, sy), (xx, ex, ey)))
            mx = l
            mmp1dest = xx

    except Exception as e:
        print(e)

print(mx - 1)
tt += mx - 1

mx = 1900000
mmp2dest = 0
for xx in range(len(BB)):
    try:
        # print("Checking2", xx)
        l = len(nx.shortest_path(G, (mmp1dest, ex, ey), (xx, sx, sy)))
        if l < mx:
            print(l, xx, nx.shortest_path(G, (mmp1dest, ex, ey), (xx, sx, sy)))
            mx = l
            mmp2dest = xx

    except Exception as e:
        print(e)

print(mx - 1)
tt += mx - 1

mx = 1900000
for xx in range(len(BB)):
    try:
        # print("Checking3", xx)
        l = len(nx.shortest_path(G, (mmp2dest, sx, sy), (xx, ex, ey)))
        if l < mx:
            print(l, xx, nx.shortest_path(G, (mmp2dest, sx, sy), (xx, ex, ey)))
            mx = l

    except Exception as e:
        print(e)

print(mx - 1)
print(tt + mx - 1)
