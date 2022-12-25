
V = {}
todo = []

with open("input") as f:
    for i in f.readlines():
        i = i.strip()
        if i:
            v, ins = i.split(": ")

            try:
                ins = int(ins)
                V[v] = ins
            except ValueError:
                V[v] = ins.split(" ")
                todo.append(v)

while todo:
    ntodo = []

    for v in todo:
        print(V[v])
        v1, ops, v2 = V[v]
        if v1 in todo or v2 in todo:
            ntodo.append(v)
        else:
            if ops == "+":
                V[v] = V[v1] + V[v2]
            elif ops == "-":
                V[v] = V[v1] - V[v2]
            elif ops == "*":
                V[v] = V[v1] * V[v2]
            elif ops == "/":
                V[v] = V[v1] / V[v2]

    todo = ntodo

print(V, todo)
print(V["root"])


import z3
s = z3.Solver()

ints = {}

todo = []

with open("input") as f:
    for i in f.readlines():
        i = i.strip()
        if i:
            v, ins = i.split(": ")

            ints[v] = z3.Real(v)

            if v == "humn":
                continue

            try:
                ins = int(ins)
                s.add(ints[v] == ins)
            except ValueError:
                todo.append((v, ins.split(" ")))

for v, (v1, ops, v2) in todo:
    if v == "root":
        s.add(ints[v1] == ints[v2])
    elif ops == "+":
        s.add(ints[v] == ints[v1] + ints[v2])
    elif ops == "-":
        s.add(ints[v] == ints[v1] - ints[v2])
    elif ops == "*":
        s.add(ints[v] == ints[v1] * ints[v2])
    elif ops == "/":
        s.add(ints[v] == ints[v1] / ints[v2])


s.check()
print(s.model())
print(s.model().evaluate(ints["humn"]))
