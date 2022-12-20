
m = {}

sensors = []

with open("input") as f:
    for i in f.readlines():
        i = i.strip()
        if i:
            spart, bpart = i.split(":")
            print(spart, bpart)
            x = spart.split("x=")[1]
            x, y = x.split(", y=")
            bx = bpart.split("x=")[1]
            bx, by = bx.split(", y=")

            sensors.append((int(x), int(y), int(bx), int(by)))

print(sensors)

def mana(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)

# for sx, sy, bx, by in sensors:
#     m[(sx, sy)] = "S"
#     m[(bx, by)] = "B"
#
#     rx = abs(sx - bx) * 4
#     ry = abs(sy - by) * 4
#     rx, ry = max(rx, ry), max(rx, ry)
#     bm = mana(sx, sy, bx, by)
#
#     print(sx, sy)
#
#
#     for dx in range(-rx - 1, rx + 2):
#         # for dy in range(-ry - 1, ry + 2):
#         #     if dy != 2000000:
#         #         continue
#         tx, ty = sx + dx, 2000000
#         if mana(sx, sy, tx, ty) <= bm:
#             if (tx, ty) not in m:
#                 m[(tx, ty)] = "#"
#
# for y in range(-5, 25):
#     for x in range(-10, 30):
#         print(m.get((x, y), " "), end="")
#     print("")
#
# tt = 0
#
# for (x, y), v in m.items():
#     if y == 2000000 and v == "#":
#         tt += 1
#
# print(tt)
#

possible_locs = []

b1 = True

# for sx, sy, bx, by in sensors:
#
#     m[(sx, sy)] = "S"
#     m[(bx, by)] = "B"
#     print(sx, sy)
#
#     cx, cy = bx, by
#     todo = []
#     done = []
#     bm = mana(sx, sy, bx, by) + 1
#
#     todo.append((bx, by))
#
#     while todo:
#         cx, cy = todo.pop(0)
#         done.append((cx, cy))
#         # print(len(done))
#
#         for dx in [-1, 0, 1]:
#             for dy in [-1, 0, 1]:
#                 tx, ty = cx + dx, cy + dy
#                 if (tx, ty) not in done and (tx, ty) not in todo:
#                     if mana(sx, sy, tx, ty) == bm:
#                         todo.append((tx, ty))
#     if b1:
#         for px, py in done:
#             if (px, py) != (bx, by) and px > 0 and px < 4000000 and py > 0 and py < 4000000 and (px, py) not in possible_locs:
#                 possible_locs.append((px, py))
#         b1 = True
#         break
#     else:
#         new_pos = []
#         for pos in possible_locs:
#             if pos in done:
#                 new_pos.append(pos)
#         possible_locs = new_pos


for sx, sy, bx, by in sensors:
    m[(sx, sy)] = "S"
    m[(bx, by)] = "B"

    bm = mana(sx, sy, bx, by)

    new_possible_pos = []

    for px, py in possible_locs:
        if mana(sx, sy, px, py) > bm:
            new_possible_pos.append((px, py))
    possible_locs = new_possible_pos

print(possible_locs)

import z3

def t():

    s = z3.Solver()

    x = z3.Int("x")
    y = z3.Int("y")

    s.add(x > 0, x < 4000000, y > 0, y < 4000000)

    def aabs(x):
        return z3.If(x >= 0, x, -x)

    for sx, sy, bx, by in sensors:

        ma = mana(sx, sy, bx, by)

        s.add(aabs(sx - x) + aabs(sy - y) > ma)

    s.check()
    print(s.model())

import timeit
print(timeit.timeit('t()', globals=globals(), number=20) / 20)
