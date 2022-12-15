
sx, sy = 0, 0
ex, ey = 0, 0
m = {}

with open("input") as f:

    y = 0

    for i in f.readlines():
        i = i.strip()
        if i:

            for x, v in enumerate(i):
                if v == "S":
                    sx, sy = x, y
                    v = "a"
                elif v == "E":
                    ex, ey = x, y
                    v = "z"

                m[(x, y)] = ord(v) - 97

            y += 1

print(m, sx, sy, ex, ey)


dist = {}
prev = {}
Q = [(sx, sy)]
dist[(sx, sy)] = 0

for (x, y), e in m.items():
    if e == 0:
        Q.append((x, y))
        dist[(x, y)] = 0

while Q:
    cx, cy = Q.pop(0)

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        tx, ty = cx + dx, cy + dy
        if (tx, ty) in m and m[(tx, ty)] == m[(tx, ty)] <= m[(cx, cy)] + 1:
            if (tx, ty) not in dist or dist[(tx, ty)] > dist[(cx, cy)] + 1:

                dist[(tx, ty)] = dist[(cx, cy)] + 1
                if (tx, ty) not in Q:
                    Q.append((tx, ty))

                if (tx, ty) == (ex, ey):
                    print(dist[(tx, ty)])
                    a = 1 / 0
    # print(Q, dist)
