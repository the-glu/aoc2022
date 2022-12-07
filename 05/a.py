N = 9

buckets = []

for x in range(N):
    buckets.append([])

moves = []
mmode = False

with open("input") as f:
    for x in f.readlines():

        # x = x.strip()

        if not x.strip():
            mmode = True
            continue

        if mmode:
            trucs = x.split(" ")
            moves.append((int(trucs[1]), int(trucs[3]), int(trucs[5][:-1])))
        else:
            if x[1] == "1":
                continue
            for pos in range(N):
                elem = x[1 + pos * 4]
                print(pos, elem)
                if elem and elem != " ":
                    buckets[pos].append(elem)


print(buckets, moves)

for qty, fr, to in moves:
    xxx = []
    for _ in range(int(qty)):
        xxx.insert(0, buckets[fr - 1].pop(0))
    for xx in xxx:
        buckets[to - 1].insert(0, xx)

print(buckets)


for b in buckets:
    print(b[0])

