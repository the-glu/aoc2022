
moves = []
with open("input") as f:
    for x in f.readlines():
        x = x.strip()
        if x:
            moves.append(x.split(" "))

print(moves)

hx = 0
hy = 0
tx = 0
ty = 0

visited = []

def check():
    global hx, hy, tx, ty
    # print(hx, hy, tx, ty)
    if ty + 2 == hy and tx == hx:
        ty += 1
    elif ty - 2 == hy and tx == hx:
        ty -= 1
    elif tx + 2 == hx and ty == hy:
        tx += 1
    elif tx - 2 == hx and ty == hy:
        tx -= 1
    elif ty + 2 == hy and tx + 1 == hx:
        ty += 1
        tx += 1
    elif ty - 2 == hy and tx + 1 == hx:
        ty -= 1
        tx += 1
    elif tx + 2 == hx and ty + 1 == hy:
        tx += 1
        ty += 1
    elif tx - 2 == hx and ty + 1 == hy:
        tx -= 1
        ty += 1
    elif ty + 2 == hy and tx - 1 == hx:
        ty += 1
        tx -= 1
    elif ty - 2 == hy and tx - 1 == hx:
        ty -= 1
        tx -= 1
    elif tx + 2 == hx and ty - 1 == hy:
        tx += 1
        ty -= 1
    elif tx - 2 == hx and ty - 1 == hy:
        tx -= 1
        ty -= 1

    elif ty + 2 == hy and tx - 2 == hx:
        ty += 1
        tx -= 1
    elif ty - 2 == hy and tx - 2 == hx:
        ty -= 1
        tx -= 1
    elif tx + 2 == hx and ty - 2 == hy:
        tx += 1
        ty -= 1
    elif tx + 2 == hx and ty + 2 == hy:
        tx += 1
        ty += 1
    # print(hx, hy, tx, ty)


pos = []

for x in range(10):
    pos.append((0, 0))

for d, c in moves:
    for __ in range(int(c)):
        hx, hy = pos[0]
        if d == "R":
            hx += 1
        elif d == "L":
            hx -= 1
        elif d == "U":
            hy += 1
        elif d == "D":
            hy -= 1
        pos[0] = (hx, hy)
        for x in range(9):
            hx, hy = pos[x]
            tx, ty = pos[x + 1]
            check()
            pos[x + 1] = tx, ty
        print(pos)

        if (tx, ty) not in visited:
            visited.append((tx, ty))

print(len(visited))
