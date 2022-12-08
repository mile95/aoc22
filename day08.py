import math

with open("input.txt") as f:
    input = f.read().splitlines()


c = 0
for x in range(0, len(input)):
    for y in range(0, len(input[x])):
        val = input[x][y]
        if x == 0 or y == 0 or x == (len(input) - 1) or y == (len(input[x]) - 1):
            c += 1
        else:
            lr = input[x]
            lc = [x[y] for x in input]
            if all(a < val for a in lr[:y]) or all(a < val for a in lr[y + 1 :]):
                c += 1
            elif all(a < val for a in lc[:x]) or all(a < val for a in lc[x + 1 :]):
                c += 1

print(c)


def find_trees(val, items):
    c = 0
    for item in items:
        c += 1
        if val <= item:
            return c
    return c


m = 0
for x in range(0, len(input)):
    for y in range(0, len(input[x])):
        val = input[x][y]
        lr = input[x]
        lc = "".join([x[y] for x in input])

        up = lc[:x][::-1]
        left = lr[:y][::-1]
        down = lc[x + 1 :]
        right = lr[y + 1 :]

        m = max(
            m,
            math.prod(
                [
                    find_trees(val, up),
                    find_trees(val, left),
                    find_trees(val, down),
                    find_trees(val, right),
                ]
            ),
        )

print(m)
