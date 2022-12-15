m = {}


maxy = 0
with open("input") as f:
    for i in f.readlines():
        i = i.strip()
        if i:
            cords = i.split(" -> ")
            print(cords)
            cx, cy = cords[0].split(",")
            cx, cy = int(cx), int(cy)
            cords.pop(0)
            if cy > maxy:
                maxy = cy

            while cords:
                nx, ny = cords[0].split(",")
                nx, ny = int(nx), int(ny)
                nnx, nny = nx, ny
                cords.pop(0)
                print(cx, cy, nx, ny)
                if cy > maxy:
                    maxy = cy

                if cx == nx:
                    if cy > ny:
                        ny, cy = cy, ny
                    print("Y", cy, ny, cx)
                    for y in range(cy, ny + 1):
                        m[(cx, y)] = "#"
                else:

                    if cx > nx:
                        nx, cx = cx, nx
                    print("X", cx, nx, cy)
                    for x in range(cx, nx + 1):
                        m[(x, cy)] = "#"

                cx, cy = nnx, nny
            print("_")

maxy += 2

# m[(500, 0)] = "+"
print(maxy)


mx, my = 0, 0

def doonestep():
    global m, mx, my
    # for ((x, y), v) in m.items():
    x, y = mx, my
    v = m[(x, y)]
    if v != "o":
        raise Exception("WAT")
    if y + 1 == maxy:
        return False
    if (x, y + 1) not in m:
        m[(x, y + 1)] = "o"
        my += 1
        del m[(x, y)]
        return True
    if (x - 1, y + 1) not in m:
        m[(x - 1, y + 1)] = "o"
        mx -= 1
        my += 1
        del m[(x, y)]
        return True
    if (x + 1, y + 1) not in m:
        m[(x + 1, y + 1)] = "o"
        mx += 1
        my += 1
        del m[(x, y)]
        return True
    return False

def pm():
    global m
    for y in range(0, 10 + 4):
        for x in range(494 - 5, 504 + 5):
            print(m.get((x, y), "."), end="")
        print("")
    print("")


pm()
nbs = 0
genok = True
while genok:
    genok = False

    # for ((x, y), v) in m.items():
    x, y = 500, -1
    if (x, y + 1) not in m:
        genok = True
        m[(x, y + 1)] = "o"
        mx, my = x, y + 1
        nbs += 1

        print(nbs)
        while doonestep():
            pass
        # pm()
    # break


print(nbs)
