mx1, mx2 = 1000, -1000
my1, my2 = 1000, -1000
mz1, mz2 = 1000, -1000
cubes = []
with open("input") as f:
    for i in f.readlines():
        i = i.strip()
        if i:
            x, y, z = i.split(",")
            cubes.append((int(x), int(y), int(z)))
            mx1 = min(mx1, int(x))
            mx2 = max(mx2, int(x))
            my1 = min(my1, int(y))
            my2 = max(my2, int(y))
            mz1 = min(mz1, int(z))
            mz2 = max(mz2, int(z))

print(mx1, mx2, my2, my2, mz1, mz2)

print(cubes)

surfs = 0

WATER = []

wtodo = [(mx1 - 1, my1 - 1, mz1 - 1)]

while wtodo:
    wx, wy, wz = wtodo.pop()

    if mx1 - 2 < wx < mx2 + 2:
        if my1 - 2 < wy < my2 + 2:
            if mz1 - 2 < wz < mz2 + 2:

                WATER.append((wx, wy, wz))

                if (wx - 1, wy, wz) not in cubes and (wx - 1, wy, wz) not in WATER:
                    wtodo.append((wx - 1, wy, wz))
                if (wx + 1, wy, wz) not in cubes and (wx + 1, wy, wz) not in WATER:
                    wtodo.append((wx + 1, wy, wz))
                if (wx, wy - 1, wz) not in cubes and (wx, wy - 1, wz) not in WATER:
                    wtodo.append((wx, wy - 1 , wz))
                if (wx, wy + 1, wz) not in cubes and (wx, wy + 1, wz) not in WATER:
                    wtodo.append((wx, wy + 1, wz))
                if (wx, wy, wz - 1) not in cubes and (wx, wy, wz - 1) not in WATER:
                    wtodo.append((wx, wy, wz - 1))
                if (wx, wy, wz + 1) not in cubes and (wx, wy, wz + 1) not in WATER:
                    wtodo.append((wx, wy, wz + 1))

print(WATER)

for x, y, z in cubes:

    if (x + 1, y, z) in WATER:
        surfs += 1
    if (x - 1, y, z) in WATER:
        surfs += 1
    if (x, y + 1, z) in WATER:
        surfs += 1
    if (x, y - 1, z) in WATER:
        surfs += 1
    if (x, y, z + 1) in WATER:
        surfs += 1
    if (x, y, z - 1) in WATER:
        surfs += 1
print(surfs)

