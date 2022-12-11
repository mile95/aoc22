with open("input.txt") as f:
    input = f.read().splitlines()
    input = [i for i in input if i]


class Monkey:
    count = 0
    items = []
    op = ""
    test = ""
    t = ""
    f = ""

    def __init__(self, number, starting_items, op, test, t, f):
        self.number = number
        self.items = starting_items
        self.op = op
        self.test = test
        self.t = t
        self.f = f


def create_monkeys(input):
    modolus = 1
    monkeys = []
    for i in range(0, len(input), 6):
        items = [int(x) for x in input[i + 1].split(":")[1].split(",")]
        op = input[i + 2].split(":")[1].split("=")[1]
        test = int(input[i + 3].split()[::-1][0])
        modolus *= test
        t = int(input[i + 4].split()[::-1][0])
        f = int(input[i + 5].split()[::-1][0])
        monkeys.append(Monkey(i, items, op, test, t, f))
    return monkeys, modolus


def solve(q, monkeys, modolus):
    w = 0
    for r in range(q):
        for m in monkeys:
            for item in m.items:
                m.count += 1
                if "*" in m.op:
                    o1, o2 = m.op.split("*")[0], m.op.split("*")[1]
                    try:
                        o1 = int(o1)
                    except Exception:
                        o1 = item
                    try:
                        o2 = int(o2)
                    except Exception:
                        o2 = item
                    w = o1 * o2

                if "+" in m.op:
                    o1, o2 = m.op.split("+")[0], m.op.split("+")[1]
                    try:
                        o1 = int(o1)
                    except Exception:
                        o1 = item
                    try:
                        o2 = int(o2)
                    except Exception:
                        o2 = item
                    w = o1 + o2

                if q == 20:
                    w = w // 3

                if w % m.test == 0:
                    monkeys[m.t].items.append(w) if q == 20 else monkeys[
                        m.t
                    ].items.append(w % modolus)
                else:
                    monkeys[m.f].items.append(w) if q == 20 else monkeys[
                        m.f
                    ].items.append(w % modolus)

                m.items = m.items[1:]

    counts = [m.count for m in monkeys]
    counts.sort()
    counts.reverse()
    mb = counts[0] * counts[1]
    return mb


monkeys, modolus = create_monkeys(input)
print(solve(20, monkeys, modolus))
monkeys, modolus = create_monkeys(input)
print(solve(10000, monkeys, modolus))
