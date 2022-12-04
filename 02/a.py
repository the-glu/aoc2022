rounds = []

with open("input") as f:
    for x in f.readlines():
        x = x.strip()
        if x:
            rounds.append(x.split(" "))
    print(rounds)

s = 0

for b, a in rounds:
    # if a == "X":
    #     s += 1
    #     if b == "A":
    #         s += 3
    #     elif b == "B":
    #         s += 0
    #     elif b == "C":
    #         s += 6
    # elif a == "Y":
    #     s += 2
    #     if b == "A":
    #         s += 6
    #     elif b == "B":
    #         s += 3
    #     elif b == "C":
    #         s += 0
    # elif a == "Z":
    #     s += 3
    #     if b == "A":
    #         s += 0
    #     elif b == "B":
    #         s += 6
    #     elif b == "C":
    #         s += 3
    if a == "X":
        s += 0
        if b == "A":
            s += 3
        elif b == "B":
            s += 1
        elif b == "C":
            s += 2
    elif a == "Y":
        s += 3
        if b == "A":
            s += 1
        elif b == "B":
            s += 2
        elif b == "C":
            s += 3
    elif a == "Z":
        s += 6
        if b == "A":
            s += 2
        elif b == "B":
            s += 3
        elif b == "C":
            s += 1
print(s)

