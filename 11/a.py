MONKEYS = {
    0: {
        "items": [79, 98],
        "op": lambda x: x * 19,
        "test": lambda x: x % 23 == 0,
        "l": 23,
        "t": 2,
        "f": 3,
        "nb": 0,
    },
    1: {
        "items": [54, 65, 75, 74],
        "op": lambda x: x + 6,
        "test": lambda x: x % 19 == 0,
        "l": 19,
        "t": 2,
        "f": 0,
        "nb": 0,
    },
    2: {
        "items": [79, 60, 97],
        "op": lambda x: x * x,
        "test": lambda x: x % 13 == 0,
        "l": 13,
        "t": 1,
        "f": 3,
        "nb": 0,
    },
    3: {
        "items": [74],
        "op": lambda x: x + 3,
        "test": lambda x: x % 17 == 0,
        "l": 17,
        "t": 0,
        "f": 1,
        "nb": 0,
    },
}



MONKEYS = {
    0: {
        "items": [54, 82, 90, 88, 86, 54],
        "op": lambda x: x * 7,
        "test": lambda x: x % 11 == 0,
        "t": 2,
        "f": 6,
        "nb": 0,
    },
    1: {
        "items": [91, 65],
        "op": lambda x: x * 13,
        "test": lambda x: x % 5 == 0,
        "t": 7,
        "f": 4,
        "nb": 0,
    },
    2: {
        "items": [62, 54, 57, 92, 83, 63, 63],
        "op": lambda x: x + 1,
        "test": lambda x: x % 7 == 0,
        "t": 1,
        "f": 7,
        "nb": 0,
    },
    3: {
        "items": [67, 72, 68],
        "op": lambda x: x * x,
        "test": lambda x: x % 2 == 0,
        "t": 0,
        "f": 6,
        "nb": 0,
    },
    4: {
        "items": [68, 89, 90, 86, 84, 57, 72, 84],
        "op": lambda x: x + 7,
        "test": lambda x: x % 17 == 0,
        "t": 3,
        "f": 5,
        "nb": 0,
    },
    5: {
        "items": [79, 83, 64, 58],
        "op": lambda x: x + 6 ,
        "test": lambda x: x % 13 == 0,
        "t": 3,
        "f": 0,
        "nb": 0,
    },
    6: {
        "items": [96, 72, 89, 70, 88],
        "op": lambda x: x + 4,
        "test": lambda x: x % 3 == 0,
        "t": 1,
        "f": 2,
        "nb": 0,
    },
    7: {
        "items": [79],
        "op": lambda x: x + 8,
        "test": lambda x: x % 19 == 0,
        "t": 4,
        "f": 5,
        "nb": 0,
    },
}


for r in range(10000):
    print(r)

    for k, v in MONKEYS.items():
        for i in v["items"]:
            v["nb"] += 1
            i = v["op"](i)
            # i = i // 3
            if v["test"](i):
                MONKEYS[v["t"]]["items"].append(i % 9699690)
            else:
                MONKEYS[v["f"]]["items"].append(i % 9699690)
        v["items"] = []


nbs = [v["nb"] for v in MONKEYS.values()]

print(nbs)
nbs = sorted(nbs)
print(nbs)
