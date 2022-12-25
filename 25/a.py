
l = []

with open("input") as f:
    for i in f.readlines():
        i = i.strip()
        if i:
            l.append(i)

print(l)

def stoi(l):
    p = 0
    t = 0

    for d in l[::-1]:
        if d == "-":
            d = -1
        elif d == "=":
            d = -2
        else:
            d = int(d)

        t += d * (5 ** p)
        p += 1

    return t





tt = 0
for x in l:
    print(x, stoi(x))
    tt += stoi(x)

print(tt)

print(30332970236150)
print(stoi("2=0--0---11--01=-100"))
