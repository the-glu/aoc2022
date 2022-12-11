
ins = []

with open("input") as f:
    for x in f.readlines():
        x = x.strip()
        if x:
            ins.append(x.split(" "))

x = 1
cycle = 0
tt = 0

def c():
    global x, cycle, tt
    z = (cycle - 1) % 40
    if z == x  + 1 or z == x - 1 or z == x:
        print("#", end="")
    else:
        print(" ", end="")

    if cycle in [20, 60, 100, 140, 180, 220]:
        tt += cycle * x
    if (cycle - 1) % 40 == 39:
        print("")

for i in ins:
    if i[0] == "noop":
        cycle += 1
        c()
    else:
        cycle += 1
        c()
        cycle += 1
        c()
        x += int(i[1])
print(x, cycle, tt)


